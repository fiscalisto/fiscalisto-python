"""El SDK sin red: un transport falso contesta como la API."""

from __future__ import annotations

import json
import os
import unittest
from pathlib import Path
from typing import Any

from fiscalisto import (
    Fiscalisto,
    FiscalistoError,
    FiscalistoWebhookError,
    HttpRequest,
    HttpResponse,
    verify_webhook,
)

VECTOR = json.loads((Path(__file__).parents[2] / "fixtures" / "webhook.json").read_text())


def answer(status: int, body: Any, **headers: str) -> HttpResponse:
    data = body if isinstance(body, bytes) else json.dumps(body).encode()
    return HttpResponse(status, {k.replace("_", "-"): v for k, v in headers.items()}, data)


class Fake:
    """Contesta en orden; una excepción en la lista se lanza (red caída)."""

    def __init__(self, *answers: HttpResponse | Exception) -> None:
        self.answers = list(answers)
        self.requests: list[HttpRequest] = []

    def __call__(self, request: HttpRequest) -> HttpResponse:
        self.requests.append(request)
        a = self.answers.pop(0)
        if isinstance(a, Exception):
            raise a
        return a


def client(fake: Fake, **options: Any) -> tuple[Fiscalisto, list[float]]:
    waits: list[float] = []
    return Fiscalisto("fk_test_abc", transport=fake, sleep=waits.append, **options), waits


ERROR = {
    "error": {
        "type": "invoice_error",
        "code": "invoice_rejected",
        "message": "El SAT no la aceptó.",
        "param": "customer",
        "sat_code": "CFDI40147",
        "invoice": "inv_1",
        "doc_url": "https://fiscalisto.com/docs/api/errores#invoice_rejected",
        "request_id": "req_1",
    }
}


class KeyTest(unittest.TestCase):
    def test_requires_a_key(self) -> None:
        old = os.environ.pop("FISCALISTO_API_KEY", None)
        try:
            with self.assertRaisesRegex(ValueError, "FISCALISTO_API_KEY"):
                Fiscalisto()
            with self.assertRaisesRegex(ValueError, "fk_live_"):
                Fiscalisto("whsec_x")
            os.environ["FISCALISTO_API_KEY"] = "fk_live_x"
            self.assertTrue(Fiscalisto().livemode)
            self.assertFalse(Fiscalisto("fk_test_x").livemode)
        finally:
            os.environ.pop("FISCALISTO_API_KEY", None)
            if old is not None:
                os.environ["FISCALISTO_API_KEY"] = old


class RequestTest(unittest.TestCase):
    def test_sends_the_key_and_json(self) -> None:
        fake = Fake(answer(200, {"id": "cus_1"}))
        f, _ = client(fake, base_url="http://api.localhost:3000")
        f.customers.create({"tax_id": "ICV060329BY0", "legal_name": "INMOBILIARIA CVA"})
        r = fake.requests[0]
        self.assertEqual(r.method, "POST")
        self.assertEqual(r.url, "http://api.localhost:3000/v1/customers")
        self.assertEqual(r.headers["authorization"], "Bearer fk_test_abc")
        self.assertEqual(r.headers["content-type"], "application/json")
        self.assertTrue(r.headers["user-agent"].startswith("fiscalisto-python/"))
        self.assertNotIn("idempotency-key", r.headers)
        self.assertEqual(json.loads(r.body or b"")["legal_name"], "INMOBILIARIA CVA")

    def test_stamping_gets_an_idempotency_key_reused_on_retries(self) -> None:
        fake = Fake(
            answer(503, {"error": {"type": "api_error", "code": "internal_error"}}),
            OSError("connection reset"),
            answer(201, {"id": "inv_1"}),
        )
        f, waits = client(fake)
        self.assertEqual(f.invoices.create({"items": []})["id"], "inv_1")  # type: ignore[typeddict-item]
        keys = {r.headers["idempotency-key"] for r in fake.requests}
        self.assertEqual(len(fake.requests), 3)
        self.assertEqual(len(keys), 1)
        self.assertEqual(len(waits), 2)

    def test_takes_your_idempotency_key(self) -> None:
        fake = Fake(answer(201, {"id": "inv_1"}))
        f, _ = client(fake)
        f.invoices.substitute("inv_1/x", {"items": []}, idempotency_key="pedido-1042")  # type: ignore[typeddict-item]
        self.assertEqual(fake.requests[0].headers["idempotency-key"], "pedido-1042")
        self.assertEqual(
            fake.requests[0].url, "https://api.fiscalisto.com/v1/invoices/inv_1%2Fx/substitute"
        )

    def test_never_repeats_what_could_do_something_twice(self) -> None:
        fake = Fake(answer(500, {"error": {"type": "api_error", "code": "internal_error"}}))
        f, _ = client(fake)
        with self.assertRaises(FiscalistoError) as caught:
            f.customers.create({"tax_id": "ICV060329BY0", "legal_name": "X"})
        self.assertEqual((caught.exception.status, len(fake.requests)), (500, 1))
        fake = Fake(OSError("down"))
        f, _ = client(fake)
        with self.assertRaises(FiscalistoError) as caught:
            f.customers.create({"tax_id": "ICV060329BY0", "legal_name": "X"})
        self.assertEqual(caught.exception.type, "connection_error")
        self.assertEqual(caught.exception.code, "connection_failed")

    def test_waits_what_retry_after_says(self) -> None:
        busy = {"error": {"type": "rate_limit_error", "code": "rate_limit"}}
        fake = Fake(answer(429, busy, retry_after="7"), answer(200, {"object": "balance"}))
        f, waits = client(fake)
        f.balance.get()
        self.assertEqual(waits, [7.0])
        # Longer than a minute: the error, so your code decides.
        fake = Fake(answer(429, busy, retry_after="3600"))
        f, waits = client(fake)
        with self.assertRaises(FiscalistoError) as caught:
            f.balance.get()
        self.assertEqual((caught.exception.code, waits), ("rate_limit", []))

    def test_waits_for_a_stamp_in_progress(self) -> None:
        fake = Fake(
            answer(409, {"error": {"type": "idempotency_error", "code": "request_in_progress"}}),
            answer(201, {"id": "inv_1"}),
        )
        f, _ = client(fake)
        f.invoices.create({"items": []})  # type: ignore[typeddict-item]
        self.assertEqual(len(fake.requests), 2)

    def test_gives_up_after_max_retries(self) -> None:
        down = answer(503, {"error": {"type": "api_error", "code": "internal_error"}})
        fake = Fake(down, down)
        f, _ = client(fake, max_retries=1)
        with self.assertRaises(FiscalistoError):
            f.invoices.get("inv_1")
        self.assertEqual(len(fake.requests), 2)
        fake = Fake(TimeoutError("timed out"))
        f, _ = client(fake)
        with self.assertRaises(FiscalistoError) as caught:
            f.invoices.create({"items": []}, max_retries=0)  # type: ignore[typeddict-item]
        self.assertEqual(caught.exception.code, "timeout")
        self.assertIn("Idempotency-Key", str(caught.exception))

    def test_errors_carry_what_to_fix(self) -> None:
        fake = Fake(answer(422, ERROR, request_id="req_header"))
        f, _ = client(fake)
        with self.assertRaises(FiscalistoError) as caught:
            f.invoices.create({"items": []})  # type: ignore[typeddict-item]
        e = caught.exception
        self.assertEqual(
            (e.type, e.code, e.param, e.sat_code, e.invoice, e.request_id, e.status),
            ("invoice_error", "invoice_rejected", "customer", "CFDI40147", "inv_1", "req_1", 422),
        )
        self.assertEqual(str(e), "El SAT no la aceptó.")
        fake = Fake(answer(502, b"<html>bad gateway</html>", request_id="req_2"))
        f, _ = client(fake, max_retries=0)
        with self.assertRaises(FiscalistoError) as caught:
            f.account.get()
        self.assertEqual((caught.exception.code, caught.exception.request_id), ("unknown", "req_2"))

    def test_files_and_query(self) -> None:
        fake = Fake(answer(200, b"%PDF-1.7"), answer(200, b"<cfdi:Comprobante/>"))
        f, _ = client(fake)
        self.assertEqual(f.invoices.pdf("inv_1"), b"%PDF-1.7")
        self.assertEqual(f.invoices.xml("inv_1"), "<cfdi:Comprobante/>")
        fake = Fake(answer(200, {"object": "list", "data": [], "has_more": False}))
        f, _ = client(fake)
        list(f.issuers.list({"include_archived": True, "limit": 5}))
        self.assertTrue(fake.requests[0].url.endswith("?include_archived=true&limit=5"))

    def test_lists_walk_every_page(self) -> None:
        page = lambda ids, more: answer(  # noqa: E731
            200, {"object": "list", "data": [{"id": i} for i in ids], "has_more": more}
        )
        fake = Fake(page(["cus_1", "cus_2"], True), page(["cus_3"], False))
        f, _ = client(fake)
        listing = f.customers.list({"limit": 2})
        self.assertEqual([c["id"] for c in listing.data], ["cus_1", "cus_2"])
        self.assertEqual([c["id"] for c in listing], ["cus_1", "cus_2", "cus_3"])
        self.assertTrue(fake.requests[1].url.endswith("limit=2&starting_after=cus_2"))
        fake = Fake(page(["cus_1", "cus_2"], True))
        f, _ = client(fake)
        self.assertEqual(len(f.customers.list().to_list(max=1)), 1)


class RoutesTest(unittest.TestCase):
    def test_every_route_has_a_method(self) -> None:
        calls = json.loads((Path(__file__).parents[2] / "fixtures" / "calls.json").read_text())
        f = Fiscalisto("fk_test_x")
        for route, call in calls.items():
            resource, method = call["python"].split(".")
            self.assertTrue(callable(getattr(getattr(f, resource), method, None)), route)


class WebhookTest(unittest.TestCase):
    def test_verifies_standard_webhooks(self) -> None:
        h = VECTOR["headers"]
        at = VECTOR["timestamp"]
        event = verify_webhook(VECTOR["body"], h, VECTOR["secret"], now=at)
        self.assertEqual(event["type"], "invoice.stamped")
        f = Fiscalisto("fk_test_x")
        self.assertEqual(
            f.webhooks.verify(VECTOR["body"].encode(), h, VECTOR["secret"], now=at)["id"],
            h["webhook-id"],
        )
        # While a secret changes, two signatures: either one is enough.
        both = {**h, "webhook-signature": VECTOR["overlap_signature"]}
        verify_webhook(VECTOR["body"], both, VECTOR["secret"], now=at)
        # Header names in any case, a WSGI environ, lists of values.
        verify_webhook(
            VECTOR["body"], {k.title(): v for k, v in h.items()}, VECTOR["secret"], now=at
        )
        environ = {"HTTP_" + k.upper().replace("-", "_"): v for k, v in h.items()}
        verify_webhook(VECTOR["body"], environ, VECTOR["secret"], now=at)
        verify_webhook(VECTOR["body"], {k: [v] for k, v in h.items()}, VECTOR["secret"], now=at)

    def test_refuses_what_isnt_from_fiscalisto(self) -> None:
        h = VECTOR["headers"]
        at = VECTOR["timestamp"]
        cases: list[tuple[Any, dict[str, Any], str, float]] = [
            (
                VECTOR["body"],
                {**h, "webhook-signature": VECTOR["wrong_signature"]},
                VECTOR["secret"],
                at,
            ),
            (VECTOR["body"] + " ", h, VECTOR["secret"], at),
            (VECTOR["body"], h, VECTOR["secret"], at + 301),
            (VECTOR["body"], {"webhook-id": h["webhook-id"]}, VECTOR["secret"], at),
            (VECTOR["body"], h, "fk_test_x", at),
            (json.loads(VECTOR["body"]), h, VECTOR["secret"], at),
        ]
        for payload, headers, secret, now in cases:
            with self.assertRaises(FiscalistoWebhookError):
                verify_webhook(payload, headers, secret, now=now)


if __name__ == "__main__":
    unittest.main()
