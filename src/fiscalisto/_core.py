"""Lo que hace cada llamada del SDK: la llave, la Idempotency-Key, los reintentos seguros, los
errores y las listas que se recorren solas. Los recursos (_resources.py) solo dicen qué ruta
llamar."""

from __future__ import annotations

import json
import os
import random
import re
import time
import uuid
from collections.abc import Callable, Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, Generic, Literal, TypeVar
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request as _UrllibRequest
from urllib.request import urlopen

VERSION = "0.1.11"
# La versión de la API para la que se hizo este SDK: va en cada solicitud (Fiscalisto-Version).
API_VERSION = "2026-10-24"
DEFAULT_BASE_URL = "https://api.fiscalisto.com"

ErrorType = Literal[
    "invalid_request_error",
    "authentication_error",
    "permission_error",
    "not_found_error",
    "idempotency_error",
    "rate_limit_error",
    "invoice_error",
    "balance_error",
    "api_error",
    "connection_error",
]


class FiscalistoError(Exception):
    """Un error de la API (o de la conexión, con type connection_error). code es estable:
    decida con él; el mensaje es para mostrarlo a una persona."""

    type: ErrorType
    code: str
    message: str
    #: El campo que hay que corregir (items.0.unit_price).
    param: str | None
    #: El código del SAT o del PAC cuando ellos lo rechazaron (CFDI40145).
    sat_code: str | None
    #: El comprobante rechazado (inv_…), cuando lo hay.
    invoice: str | None
    doc_url: str | None
    #: Búsquelo en Desarrolladores › Solicitudes o mándelo a soporte.
    request_id: str | None
    #: El código HTTP (sin él, la solicitud no llegó).
    status: int | None
    #: El objeto error tal como llegó.
    raw: dict[str, Any]

    def __init__(
        self, raw: Mapping[str, Any], status: int | None = None, request_id: str | None = None
    ) -> None:
        def text(k: str) -> str | None:
            v = raw.get(k)
            return v if isinstance(v, str) else None

        self.raw = dict(raw)
        self.message = text("message") or "Error de la API de Fiscalisto"
        self.type = text("type") or "api_error"  # type: ignore[assignment]
        self.code = text("code") or "unknown"
        self.param = text("param")
        self.sat_code = text("sat_code")
        self.invoice = text("invoice")
        self.doc_url = text("doc_url")
        self.request_id = text("request_id") or request_id
        self.status = status
        super().__init__(self.message)

    def __repr__(self) -> str:
        return (
            f"FiscalistoError(code={self.code!r}, status={self.status!r}, message={self.message!r})"
        )


@dataclass
class HttpRequest:
    """Lo que el SDK manda (para un transport propio)."""

    method: str
    url: str
    headers: dict[str, str]
    body: bytes | None
    timeout: float


@dataclass
class HttpResponse:
    """Lo que el transport contesta: headers con nombres en minúsculas."""

    status: int
    headers: dict[str, str] = field(default_factory=dict)
    body: bytes = b""


Transport = Callable[[HttpRequest], HttpResponse]
"""Otro cliente HTTP (pruebas, proxies). Lanza OSError (o TimeoutError) si no hubo respuesta."""


def urllib_transport(request: HttpRequest) -> HttpResponse:
    """El transport de siempre: urllib de la biblioteca estándar."""
    req = _UrllibRequest(
        request.url, data=request.body, headers=request.headers, method=request.method
    )
    try:
        with urlopen(req, timeout=request.timeout) as res:
            return HttpResponse(
                res.status, {k.lower(): v for k, v in res.headers.items()}, res.read()
            )
    except HTTPError as error:
        with error:
            return HttpResponse(
                error.code,
                {k.lower(): v for k, v in (error.headers or {}).items()},
                error.read(),
            )


T = TypeVar("T")


class ListObject(Generic[T]):
    """Una lista: data y has_more son la primera página; recorrerla con for da todos los
    objetos, página por página."""

    def __init__(self, page: Callable[[str | None], dict[str, Any]]) -> None:
        self._page = page
        self._first: dict[str, Any] | None = None

    def first_page(self) -> dict[str, Any]:
        """La primera página, como la contesta la API (object, data, has_more, url)."""
        if self._first is None:
            self._first = self._page(None)
        return self._first

    @property
    def data(self) -> list[T]:
        return self.first_page()["data"]  # type: ignore[no-any-return]

    @property
    def has_more(self) -> bool:
        return bool(self.first_page()["has_more"])

    def __iter__(self) -> Iterator[T]:
        page = self.first_page()
        while True:
            items = page["data"]
            yield from items
            if not page["has_more"] or not items:
                return
            page = self._page(items[-1]["id"])

    def to_list(self, max: int = 10_000) -> list[T]:
        """Todos los objetos en una lista, hasta max (por omisión 10,000)."""
        out: list[T] = []
        for item in self:
            if len(out) >= max:
                break
            out.append(item)
        return out


def _invalid_response(status: int, body: bytes, request_id: str | None) -> FiscalistoError:
    """A success that isn't the API's JSON: a proxy's or a network portal's page answered instead."""
    text = " ".join(body.decode("utf-8", "replace").split())[:80] or "vacía"
    return FiscalistoError(
        {
            "type": "api_error",
            "code": "invalid_response",
            "message": f"La respuesta ({status}) no es de la API: {text}. ¿Hay un proxy o un portal de por medio?",
        },
        status,
        request_id,
    )


def _backoff(attempt: int) -> float:
    """0.5 s, 1 s, 2 s… hasta 8 s, con algo de azar para no llegar todos juntos."""
    return min(8.0, 0.5 * 2.0**attempt) * (0.75 + random.random() / 2)


def _query_value(value: Any) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)


_KEY = re.compile(r"^fk_(live|test)_")


class Core:
    """El cliente: la llave, la dirección de la API, los reintentos y el transport."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        max_retries: int = 2,
        timeout: float = 80.0,
        transport: Transport | None = None,
        sleep: Callable[[float], None] | None = None,
        api_version: str | None = API_VERSION,
        language: Literal["es", "en"] | None = None,
    ) -> None:
        """api_key: su llave fk_test_… o fk_live_…; sin ella, la variable FISCALISTO_API_KEY.
        timeout: segundos para cada respuesta (80 por omisión: el PAC puede tardar).
        api_version: la versión de la API (Fiscalisto-Version); None usa la de su cuenta.
        language: "en" para los mensajes de error en inglés (Accept-Language)."""
        key = api_key if api_key is not None else os.environ.get("FISCALISTO_API_KEY")
        if not key:
            raise ValueError(
                'Falta la llave de la API: Fiscalisto("fk_test_…") o la variable '
                "FISCALISTO_API_KEY. Créela en Desarrolladores › Llaves."
            )
        if not _KEY.match(key):
            raise ValueError(
                "La llave de la API empieza con fk_live_ o fk_test_. (Un secreto whsec_ es "
                "para verificar webhooks.)"
            )
        self._key = key
        # A proxy's path stays: https://proxy.example.com/fiscalisto + /v1/invoices.
        self._base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")
        self._max_retries = max_retries
        self._timeout = timeout
        self._transport = transport or urllib_transport
        self._sleep = sleep or time.sleep
        self._api_version = api_version
        self._language = language

    @property
    def livemode(self) -> bool:
        """True con una llave fk_live_ (producción), False con fk_test_ (pruebas)."""
        return self._key.startswith("fk_live_")

    def request(
        self,
        method: str,
        path: str,
        *,
        body: Any = None,
        query: Mapping[str, Any] | None = None,
        idempotent: bool = False,
        result: Literal["json", "bytes", "text"] = "json",
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Any:
        url = self._base_url + path
        pairs = [(k, _query_value(v)) for k, v in (query or {}).items() if v is not None]
        # Ids as their objects in the same answer: expand=["issuer", "data.recurring_invoice"].
        pairs += [("expand[]", e) for e in expand or []]
        if pairs:
            url = f"{url}?{urlencode(pairs)}"
        headers = {
            "authorization": f"Bearer {self._key}",
            "user-agent": f"fiscalisto-python/{VERSION}",
            "accept": "application/json",
        }
        if self._api_version:
            headers["fiscalisto-version"] = self._api_version
        if self._language:
            headers["accept-language"] = self._language
        key = (idempotency_key or str(uuid.uuid4())) if idempotent else None
        if key:
            headers["idempotency-key"] = key
        data: bytes | None = None
        if method == "POST":
            headers["content-type"] = "application/json"
            data = json.dumps(body if body is not None else {}, ensure_ascii=False).encode()
        # Only what can't do something twice is repeated after a failure we can't see through:
        # reads, deletes and requests with an Idempotency-Key. A 429 was never processed.
        safe = method in ("GET", "DELETE") or key is not None
        retries = self._max_retries if max_retries is None else max_retries
        wait = self._timeout if timeout is None else timeout

        attempt = 0
        while True:
            try:
                res = self._transport(HttpRequest(method, url, dict(headers), data, wait))
            except OSError as error:
                if safe and attempt < retries:
                    self._sleep(_backoff(attempt))
                    attempt += 1
                    continue
                timed_out = isinstance(error, TimeoutError) or "timed out" in str(error)
                hint = (
                    f" Repita con la misma Idempotency-Key ({key}) para saber si se timbró."
                    if key
                    else ""
                )
                raise FiscalistoError(
                    {
                        "type": "connection_error",
                        "code": "timeout" if timed_out else "connection_failed",
                        "message": f"La API no contestó en {wait:g} s.{hint}"
                        if timed_out
                        else f"No se pudo conectar con la API: {error}",
                        "idempotency_key": key,
                    }
                ) from error
            request_id = res.headers.get("request-id")
            if 200 <= res.status < 300:
                if result == "bytes":
                    return res.body
                if result == "text":
                    return res.body.decode("utf-8")
                try:
                    return json.loads(res.body)
                except ValueError:
                    raise _invalid_response(res.status, res.body, request_id) from None
            try:
                parsed = json.loads(res.body)
                raw = parsed.get("error") if isinstance(parsed, dict) else None
            except ValueError:
                raw = None
            raw = raw if isinstance(raw, dict) else {}
            try:
                retry_after = float(res.headers.get("retry-after", ""))
            except ValueError:
                retry_after = 0.0
            retryable = (
                res.status == 429
                or raw.get("code") == "request_in_progress"
                or (safe and res.status >= 500)
            )
            if retryable and attempt < retries and not retry_after > 60:
                self._sleep(retry_after if retry_after > 0 else _backoff(attempt))
                attempt += 1
                continue
            raise FiscalistoError(raw, res.status, request_id)

    def list(
        self,
        path: str,
        query: Mapping[str, Any] | None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Any]:
        def page(starting_after: str | None) -> dict[str, Any]:
            q = dict(query or {})
            if starting_after:
                q["starting_after"] = starting_after
            return self.request(  # type: ignore[no-any-return]
                "GET", path, query=q, timeout=timeout, max_retries=max_retries, expand=expand
            )

        return ListObject(page)
