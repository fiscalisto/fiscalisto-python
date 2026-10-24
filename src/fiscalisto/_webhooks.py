"""Verificar que un webhook lo mandó Fiscalisto (Standard Webhooks): la firma HMAC-SHA256 de
`webhook-id.webhook-timestamp.cuerpo` con el secreto whsec_ del endpoint."""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import time
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from .types import Event


class FiscalistoWebhookError(Exception):
    """El webhook no es de Fiscalisto: falta un encabezado, la hora o la firma no cuadran."""


def _header(headers: Mapping[str, Any], name: str) -> str | None:
    # Flask's, Django's and requests' headers ignore case; a plain dict or WSGI environ doesn't.
    for key in (name, name.title(), "HTTP_" + name.upper().replace("-", "_")):
        try:
            value = headers[key]
        except (KeyError, TypeError):
            continue
        if isinstance(value, (list, tuple)):
            value = value[0] if value else None
        if value is not None:
            return str(value)
    for key, value in headers.items():
        if isinstance(key, str) and key.lower() == name:
            return str(value[0] if isinstance(value, (list, tuple)) else value)
    return None


def verify_webhook(
    payload: bytes | str,
    headers: Mapping[str, Any],
    secret: str,
    *,
    tolerance: int = 300,
    now: float | None = None,
) -> Event:
    """Revisa la firma y la hora de un webhook y le devuelve el evento. Pase el cuerpo
    exactamente como llegó (bytes o texto), no el JSON ya interpretado: un espacio de diferencia
    cambia la firma. Lanza FiscalistoWebhookError si no es de Fiscalisto."""
    if isinstance(payload, (bytearray, memoryview)):
        payload = bytes(payload)
    if not isinstance(payload, (bytes, str)):
        raise FiscalistoWebhookError(
            "Pase el cuerpo del webhook tal como llegó (bytes o texto), no el JSON ya interpretado."
        )
    body = payload if isinstance(payload, bytes) else payload.encode("utf-8")
    msg_id = _header(headers, "webhook-id")
    timestamp = _header(headers, "webhook-timestamp")
    signatures = _header(headers, "webhook-signature")
    if not msg_id or not timestamp or not signatures:
        raise FiscalistoWebhookError(
            "Faltan los encabezados webhook-id, webhook-timestamp o webhook-signature."
        )
    current = time.time() if now is None else now
    if not timestamp.isdigit() or abs(current - int(timestamp)) > tolerance:
        raise FiscalistoWebhookError(
            "La hora del webhook está fuera de tolerancia: puede ser una repetición."
        )
    if not secret.startswith("whsec_"):
        raise FiscalistoWebhookError("El secreto del endpoint empieza con whsec_.")
    try:
        key = base64.b64decode(secret[len("whsec_") :], validate=True)
    except (binascii.Error, ValueError) as error:
        raise FiscalistoWebhookError("El secreto del endpoint no es válido.") from error
    expected = hmac.new(key, f"{msg_id}.{timestamp}.".encode() + body, hashlib.sha256).digest()
    # Several during a secret change, separated by spaces: any one valid is enough.
    for part in signatures.split(" "):
        version, _, signature = part.partition(",")
        if version != "v1" or not signature:
            continue
        try:
            given = base64.b64decode(signature, validate=True)
        except (binascii.Error, ValueError):
            continue
        if hmac.compare_digest(given, expected):
            return cast("Event", json.loads(body))
    raise FiscalistoWebhookError("La firma del webhook no coincide con el secreto.")


class Webhooks:
    """fiscalisto.webhooks: verificar lo que llega a su endpoint."""

    def verify(
        self,
        payload: bytes | str,
        headers: Mapping[str, Any],
        secret: str,
        *,
        tolerance: int = 300,
        now: float | None = None,
    ) -> Event:
        """Igual que verify_webhook."""
        return verify_webhook(payload, headers, secret, tolerance=tolerance, now=now)
