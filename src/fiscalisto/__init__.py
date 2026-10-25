"""El SDK de la API de facturación de Fiscalisto.

    from fiscalisto import Fiscalisto

    fiscalisto = Fiscalisto()  # la llave viene de FISCALISTO_API_KEY
    factura = fiscalisto.invoices.create({
        "customer": {"tax_id": "ICV060329BY0", "legal_name": "INMOBILIARIA CVA", "tax_system": "601", "zip": "33826"},
        "payment_form": "03",
        "items": [{"description": "Consultoría", "product_key": "80101500", "unit_price": 1000}],
    })

https://fiscalisto.com/docs/api
"""

from __future__ import annotations

from functools import cached_property

from ._core import (
    API_VERSION,
    VERSION,
    ErrorType,
    FiscalistoError,
    HttpRequest,
    HttpResponse,
    ListObject,
    Transport,
    urllib_transport,
)
from ._resources import FiscalistoApi
from ._webhooks import FiscalistoWebhookError, Webhooks, verify_webhook
from .error_codes import ErrorCode, ErrorCodeValue

__version__ = VERSION


class Fiscalisto(FiscalistoApi):
    """El cliente de la API: Fiscalisto("fk_test_…") o, sin llave, FISCALISTO_API_KEY.

    Opciones: base_url, max_retries (2), timeout (80 s), transport (otro cliente HTTP) y
    api_version (la de la API, por omisión API_VERSION; None usa la de su cuenta)."""

    @cached_property
    def webhooks(self) -> Webhooks:
        """Verificar lo que llega a su endpoint."""
        return Webhooks()


__all__ = [
    "API_VERSION",
    "VERSION",
    "ErrorCode",
    "ErrorCodeValue",
    "ErrorType",
    "Fiscalisto",
    "FiscalistoError",
    "FiscalistoWebhookError",
    "HttpRequest",
    "HttpResponse",
    "ListObject",
    "Transport",
    "urllib_transport",
    "verify_webhook",
]
