# Generado por `bun run openapi` desde la especificación OpenAPI de la API: no lo edite.
"""Cada recurso de la API y sus llamadas."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING
from urllib.parse import quote

from ._core import Core, ListObject

if TYPE_CHECKING:
    from .types import (
        Account,
        AdvanceList,
        ApplyAdvanceParams,
        Balance,
        CancelInvoiceParams,
        CancelRetentionParams,
        CheckSatListsParams,
        CreateAdvanceParams,
        CreateCreditNoteParams,
        CreateCustomerDataRequestParams,
        CreateCustomerParams,
        CreateEmployeeParams,
        CreateInvoiceBatchParams,
        CreateIssuerParams,
        CreatePaymentParams,
        CreatePayrollReceiptParams,
        CreateProductParams,
        CreateRetentionParams,
        CreateWebhookEndpointParams,
        Customer,
        CustomerDataRequest,
        Deleted,
        Employee,
        Event,
        GetInvoiceParams,
        GetInvoicePdfParams,
        GetInvoiceXmlParams,
        GetRetentionParams,
        GetRetentionPdfParams,
        GetRetentionXmlParams,
        GetSatCatalogParams,
        Invoice,
        InvoiceBatch,
        InvoiceCreate,
        Issuer,
        ListAdvancesParams,
        ListCustomerDataRequestsParams,
        ListCustomersParams,
        ListEmployeesParams,
        ListEventsParams,
        ListInvoiceBatchesParams,
        ListInvoicesParams,
        ListIssuersParams,
        ListProductsParams,
        ListRetentionsParams,
        ListWebhookEndpointsParams,
        PayrollReceiptPreview,
        PreviewPayrollReceiptParams,
        Product,
        Retention,
        RollWebhookSecretParams,
        SatCatalogEntryList,
        SatListCheck,
        SatListCheckList,
        SendInvoiceParams,
        SendRetentionParams,
        SignEfirmaParams,
        TaxIdValidation,
        TestWebhookEndpointParams,
        UpdateCustomerParams,
        UpdateEmployeeParams,
        UpdateIssuerParams,
        UpdateProductParams,
        UpdateWebhookEndpointParams,
        UploadCertificateParams,
        ValidateTaxIdParams,
        WebhookEndpoint,
        WebhookTest,
    )


def _path(value: str) -> str:
    return quote(str(value), safe="")


class AccountResource:
    """Cuenta: fiscalisto.account."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Account:
        """Ver la cuenta

        La cuenta API y la llave con que se hizo la solicitud. Útil para probar la llave.

        GET /v1/account
        https://fiscalisto.com/docs/api/referencia/cuenta/get-account
        """
        result: Account = self._client.request(
            "GET", "/v1/account", timeout=timeout, max_retries=max_retries
        )
        return result


class BalanceResource:
    """Cuenta: fiscalisto.balance."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Balance:
        """Ver los timbres

        Los timbres de producción que le quedan, por paquete. En pruebas se timbra gratis.

        GET /v1/balance
        https://fiscalisto.com/docs/api/referencia/cuenta/get-balance
        """
        result: Balance = self._client.request(
            "GET", "/v1/balance", timeout=timeout, max_retries=max_retries
        )
        return result


class IssuersResource:
    """Emisores: fiscalisto.issuers."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateIssuerParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Crear un emisor

        Agrega un RFC que va a timbrar. Después suba su CSD (POST /v1/issuers/{id}/certificates) y, solo en producción, firme una vez el contrato con el PAC con su e.firma (POST /v1/issuers/{id}/efirma).

        POST /v1/issuers
        https://fiscalisto.com/docs/api/referencia/emisores/create-issuer
        """
        result: Issuer = self._client.request(
            "POST", "/v1/issuers", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListIssuersParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Issuer]:
        """Listar emisores

        GET /v1/issuers
        https://fiscalisto.com/docs/api/referencia/emisores/list-issuers
        """
        return self._client.list("/v1/issuers", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Ver un emisor

        GET /v1/issuers/{id}
        https://fiscalisto.com/docs/api/referencia/emisores/get-issuer
        """
        result: Issuer = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateIssuerParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Actualizar un emisor

        Solo cambia lo que mande. El RFC no cambia: cree otro emisor.

        POST /v1/issuers/{id}
        https://fiscalisto.com/docs/api/referencia/emisores/update-issuer
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def archive(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Archivar un emisor

        Deja de timbrar; sus comprobantes se quedan.

        DELETE /v1/issuers/{id}
        https://fiscalisto.com/docs/api/referencia/emisores/archive-issuer
        """
        result: Issuer = self._client.request(
            "DELETE", f"/v1/issuers/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def upload_certificate(
        self,
        id: str,
        params: UploadCertificateParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Subir el CSD

        El certificado de sello digital (.cer y .key en base64) y la contraseña de la llave. Se guarda cifrado y solo se usa para sellar. En pruebas se revisa pero se timbra con el CSD de pruebas del SAT.

        POST /v1/issuers/{id}/certificates
        https://fiscalisto.com/docs/api/referencia/emisores/upload-certificate
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/certificates", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def sign_efirma(
        self,
        id: str,
        params: SignEfirmaParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Firmar el contrato con el PAC

        Una sola vez por RFC antes de timbrar en producción: firma el contrato de servicio del PAC (Finkok) con la e.firma del emisor. La e.firma se usa en memoria para esa firma y nunca se guarda.

        POST /v1/issuers/{id}/efirma
        https://fiscalisto.com/docs/api/referencia/emisores/sign-efirma
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/efirma", body=params, timeout=timeout, max_retries=max_retries
        )
        return result


class InvoicesResource:
    """Facturas: fiscalisto.invoices."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: InvoiceCreate,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Timbrar una factura

        Revisa la factura con las reglas del SAT, la sella y la timbra en una sola llamada. Responde con la factura timbrada (status valid) o, si el PAC tarda, en processing (escuche invoice.stamped). Lo que puede omitir tiene el valor usual: PUE, MXN, uso G03 (S01 con régimen 616), objeto de impuesto 02, IVA 16%, cantidad 1, unidad E48.

        POST /v1/invoices
        https://fiscalisto.com/docs/api/referencia/facturas/create-invoice
        """
        result: Invoice = self._client.request(
            "POST", "/v1/invoices", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListInvoicesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Invoice]:
        """Listar facturas

        Las más recientes primero.

        GET /v1/invoices
        https://fiscalisto.com/docs/api/referencia/facturas/list-invoices
        """
        return self._client.list("/v1/invoices", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        params: GetInvoiceParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Ver una factura

        Por su id (inv_…) o por su folio fiscal (UUID).

        GET /v1/invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas/get-invoice
        """
        result: Invoice = self._client.request(
            "GET", f"/v1/invoices/{_path(id)}", query=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def pdf(
        self,
        id: str,
        params: GetInvoicePdfParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> bytes:
        """Descargar el PDF

        GET /v1/invoices/{id}/pdf
        https://fiscalisto.com/docs/api/referencia/facturas/get-invoice-pdf
        """
        result: bytes = self._client.request(
            "GET", f"/v1/invoices/{_path(id)}/pdf", query=params, result="bytes", timeout=timeout, max_retries=max_retries
        )
        return result

    def xml(
        self,
        id: str,
        params: GetInvoiceXmlParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> str:
        """Descargar el XML

        El CFDI timbrado, tal como lo tiene el SAT.

        GET /v1/invoices/{id}/xml
        https://fiscalisto.com/docs/api/referencia/facturas/get-invoice-xml
        """
        result: str = self._client.request(
            "GET", f"/v1/invoices/{_path(id)}/xml", query=params, result="text", timeout=timeout, max_retries=max_retries
        )
        return result

    def send(
        self,
        id: str,
        params: SendInvoiceParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Enviar por correo

        Manda el PDF y el XML con el diseño de Fiscalisto. Sin `to`, al correo del cliente. Con la misma Idempotency-Key no se manda dos veces.

        POST /v1/invoices/{id}/send
        https://fiscalisto.com/docs/api/referencia/facturas/send-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/send", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def cancel(
        self,
        id: str,
        params: CancelInvoiceParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Cancelar una factura

        Pide la cancelación al SAT. Si el cliente debe aceptarla queda en pending (escuche invoice.canceled o invoice.cancellation_rejected). Usa un timbre la primera vez que el SAT acepta la solicitud; repetirla, o pedirla otra vez después de un rechazo, no. Nunca se niega por falta de timbres.

        POST /v1/invoices/{id}/cancel
        https://fiscalisto.com/docs/api/referencia/facturas/cancel-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/cancel", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def substitute(
        self,
        id: str,
        params: InvoiceCreate,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Sustituir una factura

        Timbra la factura corregida (el mismo cuerpo que POST /v1/invoices, relacionada 04) y cancela la anterior con motivo 01.

        POST /v1/invoices/{id}/substitute
        https://fiscalisto.com/docs/api/referencia/facturas/substitute-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/substitute", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class PaymentsResource:
    """Pagos y notas de crédito: fiscalisto.payments."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreatePaymentParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Timbrar un complemento de pago

        El recibo de pago (CFDI tipo P, Pagos 2.0) de facturas PPD: parcialidad, saldo anterior e insoluto e impuestos de cada una los calcula Fiscalisto.

        POST /v1/payments
        https://fiscalisto.com/docs/api/referencia/pagos-y-notas-de-credito/create-payment
        """
        result: Invoice = self._client.request(
            "POST", "/v1/payments", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class CreditNotesResource:
    """Pagos y notas de crédito: fiscalisto.credit_notes."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateCreditNoteParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Timbrar una nota de crédito

        Un egreso (tipo E) relacionado 01 (o 03, devolución) a una factura, con su IVA y retenciones en la misma proporción. amount es antes de impuestos.

        POST /v1/credit_notes
        https://fiscalisto.com/docs/api/referencia/pagos-y-notas-de-credito/create-credit-note
        """
        result: Invoice = self._client.request(
            "POST", "/v1/credit_notes", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class AdvancesResource:
    """Anticipos: fiscalisto.advances."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateAdvanceParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Timbrar un anticipo

        La factura del anticipo: un concepto «Anticipo del bien o servicio» (84111506, ACT). amount es lo que pagó el cliente con IVA.

        POST /v1/advances
        https://fiscalisto.com/docs/api/referencia/anticipos/create-advance
        """
        result: Invoice = self._client.request(
            "POST", "/v1/advances", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListAdvancesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> AdvanceList:
        """Listar anticipos sin aplicar

        GET /v1/advances
        https://fiscalisto.com/docs/api/referencia/anticipos/list-advances
        """
        result: AdvanceList = self._client.request(
            "GET", "/v1/advances", query=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def apply(
        self,
        id: str,
        params: ApplyAdvanceParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Aplicar un anticipo

        Timbra la factura de lo vendido (el cuerpo de POST /v1/invoices) relacionada 07 al anticipo. Con method egreso, también la nota de aplicación. La misma Idempotency-Key continúa donde se quedó.

        POST /v1/advances/{id}/apply
        https://fiscalisto.com/docs/api/referencia/anticipos/apply-advance
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/advances/{_path(id)}/apply", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class RetentionsResource:
    """Retenciones: fiscalisto.retentions."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateRetentionParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Retention:
        """Timbrar una constancia de retenciones

        POST /v1/retentions
        https://fiscalisto.com/docs/api/referencia/retenciones/create-retention
        """
        result: Retention = self._client.request(
            "POST", "/v1/retentions", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListRetentionsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Retention]:
        """Listar constancias

        GET /v1/retentions
        https://fiscalisto.com/docs/api/referencia/retenciones/list-retentions
        """
        return self._client.list("/v1/retentions", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        params: GetRetentionParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Retention:
        """Ver una constancia

        GET /v1/retentions/{id}
        https://fiscalisto.com/docs/api/referencia/retenciones/get-retention
        """
        result: Retention = self._client.request(
            "GET", f"/v1/retentions/{_path(id)}", query=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def pdf(
        self,
        id: str,
        params: GetRetentionPdfParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> bytes:
        """Descargar el PDF

        GET /v1/retentions/{id}/pdf
        https://fiscalisto.com/docs/api/referencia/retenciones/get-retention-pdf
        """
        result: bytes = self._client.request(
            "GET", f"/v1/retentions/{_path(id)}/pdf", query=params, result="bytes", timeout=timeout, max_retries=max_retries
        )
        return result

    def xml(
        self,
        id: str,
        params: GetRetentionXmlParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> str:
        """Descargar el XML

        GET /v1/retentions/{id}/xml
        https://fiscalisto.com/docs/api/referencia/retenciones/get-retention-xml
        """
        result: str = self._client.request(
            "GET", f"/v1/retentions/{_path(id)}/xml", query=params, result="text", timeout=timeout, max_retries=max_retries
        )
        return result

    def send(
        self,
        id: str,
        params: SendRetentionParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Retention:
        """Enviar por correo

        POST /v1/retentions/{id}/send
        https://fiscalisto.com/docs/api/referencia/retenciones/send-retention
        """
        result: Retention = self._client.request(
            "POST", f"/v1/retentions/{_path(id)}/send", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def cancel(
        self,
        id: str,
        params: CancelRetentionParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Retention:
        """Cancelar una constancia

        Se cancela en el momento (no espera aceptación). Usa un timbre.

        POST /v1/retentions/{id}/cancel
        https://fiscalisto.com/docs/api/referencia/retenciones/cancel-retention
        """
        result: Retention = self._client.request(
            "POST", f"/v1/retentions/{_path(id)}/cancel", body=params, timeout=timeout, max_retries=max_retries
        )
        return result


class EmployeesResource:
    """Nómina: fiscalisto.employees."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateEmployeeParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Employee:
        """Crear un empleado

        POST /v1/employees
        https://fiscalisto.com/docs/api/referencia/nomina/create-employee
        """
        result: Employee = self._client.request(
            "POST", "/v1/employees", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListEmployeesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Employee]:
        """Listar empleados

        GET /v1/employees
        https://fiscalisto.com/docs/api/referencia/nomina/list-employees
        """
        return self._client.list("/v1/employees", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Employee:
        """Ver un empleado

        GET /v1/employees/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/get-employee
        """
        result: Employee = self._client.request(
            "GET", f"/v1/employees/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateEmployeeParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Employee:
        """Actualizar un empleado

        POST /v1/employees/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/update-employee
        """
        result: Employee = self._client.request(
            "POST", f"/v1/employees/{_path(id)}", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Deleted:
        """Borrar un empleado

        Sus recibos timbrados se quedan.

        DELETE /v1/employees/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/delete-employee
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/employees/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class PayrollReceiptsResource:
    """Nómina: fiscalisto.payroll_receipts."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreatePayrollReceiptParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Timbrar un recibo de nómina

        Nómina ordinaria (Nómina 1.2): Fiscalisto calcula sueldo, ISR con subsidio al empleo e IMSS del empleado y el periodo, como la app. Queda como factura tipo N (GET /v1/invoices/{id}). El emisor necesita employer_registration.

        POST /v1/payroll_receipts
        https://fiscalisto.com/docs/api/referencia/nomina/create-payroll-receipt
        """
        result: Invoice = self._client.request(
            "POST", "/v1/payroll_receipts", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def preview(
        self,
        params: PreviewPayrollReceiptParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> PayrollReceiptPreview:
        """Calcular un recibo sin timbrar

        POST /v1/payroll_receipts/preview
        https://fiscalisto.com/docs/api/referencia/nomina/preview-payroll-receipt
        """
        result: PayrollReceiptPreview = self._client.request(
            "POST", "/v1/payroll_receipts/preview", body=params, timeout=timeout, max_retries=max_retries
        )
        return result


class InvoiceBatchesResource:
    """Lotes: fiscalisto.invoice_batches."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateInvoiceBatchParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> InvoiceBatch:
        """Timbrar un lote de facturas

        Hasta 1,000 facturas de ingreso de un emisor, timbradas en segundo plano. Se revisan todas antes de empezar: si una no pasa, no se timbra ninguna. Responde 202; escuche invoice_batch.completed o consulte el lote.

        POST /v1/invoice_batches
        https://fiscalisto.com/docs/api/referencia/lotes/create-invoice-batch
        """
        result: InvoiceBatch = self._client.request(
            "POST", "/v1/invoice_batches", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListInvoiceBatchesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[InvoiceBatch]:
        """Listar lotes

        GET /v1/invoice_batches
        https://fiscalisto.com/docs/api/referencia/lotes/list-invoice-batches
        """
        return self._client.list("/v1/invoice_batches", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> InvoiceBatch:
        """Ver un lote

        Con cada factura: su estado, su id y su error.

        GET /v1/invoice_batches/{id}
        https://fiscalisto.com/docs/api/referencia/lotes/get-invoice-batch
        """
        result: InvoiceBatch = self._client.request(
            "GET", f"/v1/invoice_batches/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class TaxIdsResource:
    """Clientes: fiscalisto.tax_ids."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def validate(
        self,
        params: ValidateTaxIdParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> TaxIdValidation:
        """Validar los datos fiscales de un cliente

        Antes de timbrar: si el RFC, el nombre, el régimen, el código postal y el uso van a pasar. Sin cif_id revisa lo que se puede revisar sin el SAT (formato, régimen para ese tipo de persona, código postal en el catálogo, uso para el régimen, nombre sin «S.A. de C.V.») y las listas del SAT. Con el idCIF de la constancia lee el registro del SAT y compara nombre, código postal y régimen, como hará el PAC. No usa timbres.

        POST /v1/tax_ids/validate
        https://fiscalisto.com/docs/api/referencia/clientes/validate-tax-id
        """
        result: TaxIdValidation = self._client.request(
            "POST", "/v1/tax_ids/validate", body=params, timeout=timeout, max_retries=max_retries
        )
        return result


class CustomersResource:
    """Clientes: fiscalisto.customers."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateCustomerParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Customer:
        """Crear un cliente

        POST /v1/customers
        https://fiscalisto.com/docs/api/referencia/clientes/create-customer
        """
        result: Customer = self._client.request(
            "POST", "/v1/customers", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListCustomersParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Customer]:
        """Listar clientes

        GET /v1/customers
        https://fiscalisto.com/docs/api/referencia/clientes/list-customers
        """
        return self._client.list("/v1/customers", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Customer:
        """Ver un cliente

        GET /v1/customers/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/get-customer
        """
        result: Customer = self._client.request(
            "GET", f"/v1/customers/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateCustomerParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Customer:
        """Actualizar un cliente

        POST /v1/customers/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/update-customer
        """
        result: Customer = self._client.request(
            "POST", f"/v1/customers/{_path(id)}", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Deleted:
        """Borrar un cliente

        DELETE /v1/customers/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/delete-customer
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/customers/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class CustomerDataRequestsResource:
    """Clientes: fiscalisto.customer_data_requests."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateCustomerDataRequestParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> CustomerDataRequest:
        """Pedirle sus datos fiscales a un cliente

        Una liga (url) que usted le manda a su cliente: la abre en fiscalisto.com y da su RFC, nombre, régimen, código postal y uso, escritos o leídos de su constancia, revisados antes de aceptarlos. Al mandarlos llega customer_data_request.completed. Un cliente nuevo queda en el catálogo del emisor; si ya existía con otros datos, los nuevos vienen en submission para que usted los aplique.

        POST /v1/customer_data_requests
        https://fiscalisto.com/docs/api/referencia/clientes/create-customer-data-request
        """
        result: CustomerDataRequest = self._client.request(
            "POST", "/v1/customer_data_requests", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListCustomerDataRequestsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[CustomerDataRequest]:
        """Listar solicitudes de datos

        GET /v1/customer_data_requests
        https://fiscalisto.com/docs/api/referencia/clientes/list-customer-data-requests
        """
        return self._client.list("/v1/customer_data_requests", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> CustomerDataRequest:
        """Ver una solicitud de datos

        GET /v1/customer_data_requests/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/get-customer-data-request
        """
        result: CustomerDataRequest = self._client.request(
            "GET", f"/v1/customer_data_requests/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def cancel(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> CustomerDataRequest:
        """Cancelar una solicitud de datos

        La liga deja de funcionar. Una que el cliente ya contestó no se cancela.

        DELETE /v1/customer_data_requests/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/cancel-customer-data-request
        """
        result: CustomerDataRequest = self._client.request(
            "DELETE", f"/v1/customer_data_requests/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class ProductsResource:
    """Productos: fiscalisto.products."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateProductParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Product:
        """Crear un producto

        POST /v1/products
        https://fiscalisto.com/docs/api/referencia/productos/create-product
        """
        result: Product = self._client.request(
            "POST", "/v1/products", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListProductsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Product]:
        """Listar productos

        GET /v1/products
        https://fiscalisto.com/docs/api/referencia/productos/list-products
        """
        return self._client.list("/v1/products", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Product:
        """Ver un producto

        GET /v1/products/{id}
        https://fiscalisto.com/docs/api/referencia/productos/get-product
        """
        result: Product = self._client.request(
            "GET", f"/v1/products/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateProductParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Product:
        """Actualizar un producto

        POST /v1/products/{id}
        https://fiscalisto.com/docs/api/referencia/productos/update-product
        """
        result: Product = self._client.request(
            "POST", f"/v1/products/{_path(id)}", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Deleted:
        """Borrar un producto

        DELETE /v1/products/{id}
        https://fiscalisto.com/docs/api/referencia/productos/delete-product
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/products/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class SatCatalogsResource:
    """Catálogos del SAT: fiscalisto.sat_catalogs."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def get(
        self,
        name: str,
        params: GetSatCatalogParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SatCatalogEntryList:
        """Consultar un catálogo del SAT

        product_keys y unit_keys se buscan con q (texto o clave). Los demás vienen completos: tax_systems, cfdi_uses, payment_forms, payment_methods, relationship_types, cancellation_motives, export_types, tax_objects, retention_codes.

        GET /v1/sat_catalogs/{name}
        https://fiscalisto.com/docs/api/referencia/catalogos-del-sat/get-sat-catalog
        """
        result: SatCatalogEntryList = self._client.request(
            "GET", f"/v1/sat_catalogs/{_path(name)}", query=params, timeout=timeout, max_retries=max_retries
        )
        return result


class SatListsResource:
    """Listas del SAT: fiscalisto.sat_lists."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def get(
        self,
        tax_id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SatListCheck:
        """Revisar un RFC en las listas del SAT

        Si el RFC aparece en la lista 69-B (operaciones simuladas), 69-B Bis o del art. 69 (no localizados, créditos firmes, exigibles, cancelados, sentencias, CSD sin efectos). Las listas se actualizan cada día con los archivos del SAT. No usa timbres.

        GET /v1/sat_lists/{tax_id}
        https://fiscalisto.com/docs/api/referencia/listas-del-sat/get-sat-list-check
        """
        result: SatListCheck = self._client.request(
            "GET", f"/v1/sat_lists/{_path(tax_id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def check(
        self,
        params: CheckSatListsParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SatListCheckList:
        """Revisar varios RFC en las listas del SAT

        Hasta 1,000 RFC en una solicitud, en el mismo orden en que los mandó (sin repetidos). No usa timbres.

        POST /v1/sat_lists/check
        https://fiscalisto.com/docs/api/referencia/listas-del-sat/check-sat-lists
        """
        result: SatListCheckList = self._client.request(
            "POST", "/v1/sat_lists/check", body=params, timeout=timeout, max_retries=max_retries
        )
        return result


class WebhookEndpointsResource:
    """Webhooks: fiscalisto.webhook_endpoints."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateWebhookEndpointParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Crear un webhook

        La respuesta trae el secreto de firma (secret) una sola vez.

        POST /v1/webhook_endpoints
        https://fiscalisto.com/docs/api/referencia/webhooks/create-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "POST", "/v1/webhook_endpoints", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListWebhookEndpointsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[WebhookEndpoint]:
        """Listar webhooks

        GET /v1/webhook_endpoints
        https://fiscalisto.com/docs/api/referencia/webhooks/list-webhook-endpoints
        """
        return self._client.list("/v1/webhook_endpoints", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Ver un webhook

        GET /v1/webhook_endpoints/{id}
        https://fiscalisto.com/docs/api/referencia/webhooks/get-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "GET", f"/v1/webhook_endpoints/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateWebhookEndpointParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Actualizar un webhook

        POST /v1/webhook_endpoints/{id}
        https://fiscalisto.com/docs/api/referencia/webhooks/update-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Deleted:
        """Borrar un webhook

        DELETE /v1/webhook_endpoints/{id}
        https://fiscalisto.com/docs/api/referencia/webhooks/delete-webhook-endpoint
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/webhook_endpoints/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def roll_secret(
        self,
        id: str,
        params: RollWebhookSecretParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Cambiar el secreto

        Un secreto nuevo, que la respuesta trae una sola vez. El anterior sigue firmando (una segunda firma en webhook-signature) el tiempo que elija, 24 horas por omisión, para que cambie su servidor sin rechazar eventos. Si se filtró, mande previous_secret_expires_in: 0.

        POST /v1/webhook_endpoints/{id}/roll_secret
        https://fiscalisto.com/docs/api/referencia/webhooks/roll-webhook-secret
        """
        result: WebhookEndpoint = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}/roll_secret", body=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def test(
        self,
        id: str,
        params: TestWebhookEndpointParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookTest:
        """Mandar un evento de prueba

        Manda ahora, una sola vez y sin reintentos, un evento del tipo que elija con un objeto de ejemplo (sus id no existen), firmado como los reales, aunque el webhook no escuche ese tipo. La respuesta trae lo que contestó su servidor. El evento no sale en GET /v1/events, pero sí en las entregas del webhook.

        POST /v1/webhook_endpoints/{id}/test
        https://fiscalisto.com/docs/api/referencia/webhooks/test-webhook-endpoint
        """
        result: WebhookTest = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}/test", body=params, timeout=timeout, max_retries=max_retries
        )
        return result


class EventsResource:
    """Eventos: fiscalisto.events."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def list(
        self,
        params: ListEventsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Event]:
        """Listar eventos

        Los de los últimos 30 días, los más recientes primero.

        GET /v1/events
        https://fiscalisto.com/docs/api/referencia/eventos/list-events
        """
        return self._client.list("/v1/events", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Event:
        """Ver un evento

        GET /v1/events/{id}
        https://fiscalisto.com/docs/api/referencia/eventos/get-event
        """
        result: Event = self._client.request(
            "GET", f"/v1/events/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class FiscalistoApi(Core):
    """Cada recurso de la API. Úselo por medio de Fiscalisto."""

    @cached_property
    def account(self) -> AccountResource:
        """Cuenta."""
        return AccountResource(self)

    @cached_property
    def balance(self) -> BalanceResource:
        """Cuenta."""
        return BalanceResource(self)

    @cached_property
    def issuers(self) -> IssuersResource:
        """Emisores."""
        return IssuersResource(self)

    @cached_property
    def invoices(self) -> InvoicesResource:
        """Facturas."""
        return InvoicesResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        """Pagos y notas de crédito."""
        return PaymentsResource(self)

    @cached_property
    def credit_notes(self) -> CreditNotesResource:
        """Pagos y notas de crédito."""
        return CreditNotesResource(self)

    @cached_property
    def advances(self) -> AdvancesResource:
        """Anticipos."""
        return AdvancesResource(self)

    @cached_property
    def retentions(self) -> RetentionsResource:
        """Retenciones."""
        return RetentionsResource(self)

    @cached_property
    def employees(self) -> EmployeesResource:
        """Nómina."""
        return EmployeesResource(self)

    @cached_property
    def payroll_receipts(self) -> PayrollReceiptsResource:
        """Nómina."""
        return PayrollReceiptsResource(self)

    @cached_property
    def invoice_batches(self) -> InvoiceBatchesResource:
        """Lotes."""
        return InvoiceBatchesResource(self)

    @cached_property
    def tax_ids(self) -> TaxIdsResource:
        """Clientes."""
        return TaxIdsResource(self)

    @cached_property
    def customers(self) -> CustomersResource:
        """Clientes."""
        return CustomersResource(self)

    @cached_property
    def customer_data_requests(self) -> CustomerDataRequestsResource:
        """Clientes."""
        return CustomerDataRequestsResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        """Productos."""
        return ProductsResource(self)

    @cached_property
    def sat_catalogs(self) -> SatCatalogsResource:
        """Catálogos del SAT."""
        return SatCatalogsResource(self)

    @cached_property
    def sat_lists(self) -> SatListsResource:
        """Listas del SAT."""
        return SatListsResource(self)

    @cached_property
    def webhook_endpoints(self) -> WebhookEndpointsResource:
        """Webhooks."""
        return WebhookEndpointsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """Eventos."""
        return EventsResource(self)
