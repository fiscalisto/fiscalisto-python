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
        BankImport,
        BankTransaction,
        CancelInvoiceParams,
        CancelRetentionParams,
        CheckSatListsParams,
        ClassifyBankTransactionParams,
        CreateAdvanceParams,
        CreateBankTransactionsParams,
        CreateCreditNoteParams,
        CreateCustomerDataRequestParams,
        CreateCustomerParams,
        CreateEmployeeParams,
        CreateInvoiceBatchParams,
        CreateIssuerOnboardingLinkParams,
        CreateIssuerParams,
        CreatePaymentParams,
        CreatePayrollReceiptParams,
        CreateProductParams,
        CreateQuoteParams,
        CreateRecurringInvoiceParams,
        CreateRetentionParams,
        CreateSandboxParams,
        CreateSatDownloadParams,
        CreateStoreConnectionParams,
        CreateTicketParams,
        CreateWebhookEndpointParams,
        Customer,
        CustomerDataRequest,
        Deleted,
        Diot,
        Employee,
        Event,
        GetDiotFileParams,
        GetDiotParams,
        GetElectronicAccountingParams,
        GetInvoiceParams,
        GetInvoicePdfParams,
        GetInvoiceXmlParams,
        GetRetentionParams,
        GetRetentionPdfParams,
        GetRetentionXmlParams,
        GetSatCatalogParams,
        GetTrialBalanceParams,
        ImportStoreOrdersParams,
        Invoice,
        InvoiceBatch,
        InvoiceCreate,
        Issuer,
        IssuerOnboardingLink,
        JournalEntry,
        LedgerAccountList,
        ListAdvancesParams,
        ListBankTransactionsParams,
        ListCustomerDataRequestsParams,
        ListCustomersParams,
        ListEmployeesParams,
        ListEventsParams,
        ListInvoiceBatchesParams,
        ListInvoicesParams,
        ListIssuersParams,
        ListJournalEntriesParams,
        ListLedgerAccountsParams,
        ListProductsParams,
        ListQuotesParams,
        ListReceivablesParams,
        ListRecurringInvoicesParams,
        ListRetentionsParams,
        ListSatDownloadsParams,
        ListSatInvoicesParams,
        ListStoreConnectionsParams,
        ListTicketsParams,
        ListWebhookEndpointsParams,
        MatchBankTransactionParams,
        PayrollReceiptPreview,
        PreviewPayrollReceiptParams,
        Product,
        Quote,
        Receivable,
        RecurringInvoice,
        ResetTestDataParams,
        Retention,
        RollWebhookSecretParams,
        Sandbox,
        SandboxList,
        SatCatalogEntryList,
        SatDownload,
        SatInvoice,
        SatListCheck,
        SatListCheckList,
        SelfInvoicing,
        SendInvoiceParams,
        SendQuoteParams,
        SendRetentionParams,
        SignEfirmaParams,
        StoreConnection,
        StoreImport,
        TaxIdValidation,
        TestDataReset,
        TestWebhookEndpointParams,
        Ticket,
        TrialBalance,
        UpdateCustomerParams,
        UpdateEmployeeParams,
        UpdateIssuerParams,
        UpdateProductParams,
        UpdateQuoteParams,
        UpdateRecurringInvoiceParams,
        UpdateSelfInvoicingParams,
        UpdateStoreConnectionParams,
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


class TestDataResource:
    """Cuenta: fiscalisto.test_data."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def reset(
        self,
        params: ResetTestDataParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> TestDataReset:
        """Reiniciar los datos de prueba

        Deja el modo de pruebas como nuevo: cada emisor de pruebas conserva su RFC y su CSD de pruebas pero pierde sus facturas, clientes, productos, lotes, ligas y descargas, y se borran los eventos y el registro de solicitudes de pruebas. Las llaves y los webhooks se quedan. Con seed (por omisión) deja 3 clientes y 3 productos de ejemplo. Solo con una llave fk_test_; producción nunca se toca.

        POST /v1/test_data/reset
        https://fiscalisto.com/docs/api/referencia/cuenta/reset-test-data
        """
        result: TestDataReset = self._client.request(
            "POST", "/v1/test_data/reset", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class SandboxesResource:
    """Entornos de prueba: fiscalisto.sandboxes."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateSandboxParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Sandbox:
        """Crear un entorno de prueba

        Un modo de pruebas propio para una persona o un proyecto: nace con el emisor de pruebas del SAT y una llave fk_test_ (key.secret, una sola vez) que solo ve los emisores, webhooks y eventos del entorno, y que reinicia solo los suyos. Se crea con una llave de pruebas de la cuenta (no de otro entorno ni limitada a emisores). Hasta 25 por cuenta.

        POST /v1/sandboxes
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/create-sandbox
        """
        result: Sandbox = self._client.request(
            "POST", "/v1/sandboxes", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SandboxList:
        """Listar entornos de prueba

        GET /v1/sandboxes
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/list-sandboxes
        """
        result: SandboxList = self._client.request(
            "GET", "/v1/sandboxes", timeout=timeout, max_retries=max_retries
        )
        return result

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Sandbox:
        """Ver un entorno de prueba

        GET /v1/sandboxes/{id}
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/get-sandbox
        """
        result: Sandbox = self._client.request(
            "GET", f"/v1/sandboxes/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Deleted:
        """Borrar un entorno de prueba

        Sus llaves dejan de funcionar al momento, sus emisores se archivan y sus webhooks se borran. No toca nada de la cuenta ni de otros entornos.

        DELETE /v1/sandboxes/{id}
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/delete-sandbox
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/sandboxes/{_path(id)}", timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Crear un emisor

        Agrega un RFC que va a timbrar. Después suba su CSD (POST /v1/issuers/{id}/certificates) y, solo en producción, firme una vez el contrato con el PAC con su e.firma (POST /v1/issuers/{id}/efirma).

        POST /v1/issuers
        https://fiscalisto.com/docs/api/referencia/emisores/create-issuer
        """
        result: Issuer = self._client.request(
            "POST", "/v1/issuers", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Actualizar un emisor

        Solo cambia lo que mande. El RFC no cambia: cree otro emisor.

        POST /v1/issuers/{id}
        https://fiscalisto.com/docs/api/referencia/emisores/update-issuer
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Subir el CSD

        El certificado de sello digital (.cer y .key en base64) y la contraseña de la llave. Se guarda cifrado y solo se usa para sellar. En pruebas se revisa pero se timbra con el CSD de pruebas del SAT.

        POST /v1/issuers/{id}/certificates
        https://fiscalisto.com/docs/api/referencia/emisores/upload-certificate
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/certificates", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def sign_efirma(
        self,
        id: str,
        params: SignEfirmaParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Firmar el contrato con el PAC

        Una sola vez por RFC antes de timbrar en producción: firma el contrato de servicio del PAC (Finkok) con la e.firma del emisor. La e.firma se usa en memoria para esa firma y no se guarda, salvo que mande keep_for_downloads: true para pedirle al SAT las facturas del emisor (POST /v1/sat_downloads); entonces se guarda cifrada y puede borrarla con DELETE.

        POST /v1/issuers/{id}/efirma
        https://fiscalisto.com/docs/api/referencia/emisores/sign-efirma
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/efirma", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete_efirma(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Issuer:
        """Borrar la e.firma guardada

        Borra la e.firma que guardó con keep_for_downloads. El emisor sigue timbrando; ya no puede pedir descargas al SAT hasta que la mande de nuevo.

        DELETE /v1/issuers/{id}/efirma
        https://fiscalisto.com/docs/api/referencia/emisores/delete-efirma
        """
        result: Issuer = self._client.request(
            "DELETE", f"/v1/issuers/{_path(id)}/efirma", timeout=timeout, max_retries=max_retries
        )
        return result

    def create_onboarding_link(
        self,
        id: str,
        params: CreateIssuerOnboardingLinkParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> IssuerOnboardingLink:
        """Crear una liga de alta

        Una página en fiscalisto.com donde el dueño del emisor sube su CSD y firma el contrato con el PAC con su e.firma, sin que esos archivos ni sus contraseñas pasen por su plataforma. Mande a su cliente a url; al terminar vuelve a return_url y llega issuer.ready. Cada liga sirve para un emisor, hasta que vence.

        POST /v1/issuers/{id}/onboarding_links
        https://fiscalisto.com/docs/api/referencia/emisores/create-issuer-onboarding-link
        """
        result: IssuerOnboardingLink = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/onboarding_links", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def get_self_invoicing(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SelfInvoicing:
        """Ver el portal de autofactura de un emisor

        GET /v1/issuers/{id}/self_invoicing
        https://fiscalisto.com/docs/api/referencia/autofactura/get-self-invoicing
        """
        result: SelfInvoicing = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}/self_invoicing", timeout=timeout, max_retries=max_retries
        )
        return result

    def update_self_invoicing(
        self,
        id: str,
        params: UpdateSelfInvoicingParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SelfInvoicing:
        """Cambiar las reglas de autofactura

        Hasta cuándo se puede facturar un ticket y cada cuánto se timbra la factura global.

        POST /v1/issuers/{id}/self_invoicing
        https://fiscalisto.com/docs/api/referencia/autofactura/update-self-invoicing
        """
        result: SelfInvoicing = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/self_invoicing", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Cancelar una factura

        Pide la cancelación al SAT. Si el cliente debe aceptarla queda en pending (escuche invoice.canceled o invoice.cancellation_rejected). Usa un timbre la primera vez que el SAT acepta la solicitud; repetirla, o pedirla otra vez después de un rechazo, no. Nunca se niega por falta de timbres.

        POST /v1/invoices/{id}/cancel
        https://fiscalisto.com/docs/api/referencia/facturas/cancel-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/cancel", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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

    def mark_paid(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Marcar pagada

        Una factura PUE timbrada con paid_later (o marcada por cobrar) ya se pagó: queda paid y llega invoice.paid. Una PPD se paga con su complemento de pago (POST /v1/payments).

        POST /v1/invoices/{id}/mark_paid
        https://fiscalisto.com/docs/api/referencia/cuentas-por-cobrar/mark-invoice-paid
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/mark_paid", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def mark_unpaid(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Marcar por cobrar

        Una factura PUE que el cliente aún no paga (le paga este mes): queda unpaid hasta POST /v1/invoices/{id}/mark_paid. Si el mes termina sin pago, la ley pide sustituirla por una PPD (regla 2.7.1.39 de la RMF).

        POST /v1/invoices/{id}/mark_unpaid
        https://fiscalisto.com/docs/api/referencia/cuentas-por-cobrar/mark-invoice-unpaid
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/mark_unpaid", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class ReceivablesResource:
    """Cuentas por cobrar: fiscalisto.receivables."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def list(
        self,
        params: ListReceivablesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Receivable]:
        """Ver lo que le deben

        Lo que debe cada cliente, por moneda, de sus facturas abiertas (PPD con saldo y PUE por cobrar), ordenado por RFC. Las facturas de cada uno: GET /v1/invoices?customer=RFC&payment_status=open.

        GET /v1/receivables
        https://fiscalisto.com/docs/api/referencia/cuentas-por-cobrar/list-receivables
        """
        return self._client.list("/v1/receivables", params, timeout=timeout, max_retries=max_retries)


class BankTransactionsResource:
    """Conciliación bancaria: fiscalisto.bank_transactions."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateBankTransactionsParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> BankImport:
        """Mandar depósitos

        Los depósitos de la cuenta del emisor (de la API de su banco o de un estado de cuenta), hasta 1,000 por solicitud. Uno que ya mandó (mismo día, monto, referencia y concepto) se omite, así que puede mandar periodos que se enciman. Cada uno trae suggested_match: las facturas que parece pagar.

        POST /v1/bank_transactions
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/create-bank-transactions
        """
        result: BankImport = self._client.request(
            "POST", "/v1/bank_transactions", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListBankTransactionsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[BankTransaction]:
        """Listar depósitos

        Los más recientes primero; los abiertos con su suggested_match.

        GET /v1/bank_transactions
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/list-bank-transactions
        """
        return self._client.list("/v1/bank_transactions", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> BankTransaction:
        """Ver un depósito

        GET /v1/bank_transactions/{id}
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/get-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "GET", f"/v1/bank_transactions/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def match(
        self,
        id: str,
        params: MatchBankTransactionParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> BankTransaction:
        """Conciliar un depósito

        El depósito pagó estas facturas (de un mismo cliente), o sin invoices, las de suggested_match. Sus facturas PUE por cobrar quedan pagadas (invoice.paid). No timbra: para pagar una PPD con este depósito, POST /v1/payments con bank_transaction.

        POST /v1/bank_transactions/{id}/match
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/match-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "POST", f"/v1/bank_transactions/{_path(id)}/match", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def classify(
        self,
        id: str,
        params: ClassifyBankTransactionParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> BankTransaction:
        """Explicar un depósito sin factura

        Un depósito que ninguna factura explica: venta (aún sin facturar), prestamo, traspaso o devolucion. El SAT puede presumir ingreso un depósito sin explicar (CFF art. 59 fr. III).

        POST /v1/bank_transactions/{id}/classify
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/classify-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "POST", f"/v1/bank_transactions/{_path(id)}/classify", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def reopen(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> BankTransaction:
        """Deshacer la conciliación

        Vuelve a open, y sus facturas vuelven a deber. Si se pagó con un complemento vigente, cancélelo antes.

        POST /v1/bank_transactions/{id}/reopen
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/reopen-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "POST", f"/v1/bank_transactions/{_path(id)}/reopen", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Retention:
        """Enviar por correo

        POST /v1/retentions/{id}/send
        https://fiscalisto.com/docs/api/referencia/retenciones/send-retention
        """
        result: Retention = self._client.request(
            "POST", f"/v1/retentions/{_path(id)}/send", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def cancel(
        self,
        id: str,
        params: CancelRetentionParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Retention:
        """Cancelar una constancia

        Se cancela en el momento (no espera aceptación). Usa un timbre.

        POST /v1/retentions/{id}/cancel
        https://fiscalisto.com/docs/api/referencia/retenciones/cancel-retention
        """
        result: Retention = self._client.request(
            "POST", f"/v1/retentions/{_path(id)}/cancel", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Employee:
        """Crear un empleado

        POST /v1/employees
        https://fiscalisto.com/docs/api/referencia/nomina/create-employee
        """
        result: Employee = self._client.request(
            "POST", "/v1/employees", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Employee:
        """Actualizar un empleado

        POST /v1/employees/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/update-employee
        """
        result: Employee = self._client.request(
            "POST", f"/v1/employees/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> PayrollReceiptPreview:
        """Calcular un recibo sin timbrar

        POST /v1/payroll_receipts/preview
        https://fiscalisto.com/docs/api/referencia/nomina/preview-payroll-receipt
        """
        result: PayrollReceiptPreview = self._client.request(
            "POST", "/v1/payroll_receipts/preview", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> TaxIdValidation:
        """Validar los datos fiscales de un cliente

        Antes de timbrar: si el RFC, el nombre, el régimen, el código postal y el uso van a pasar. Sin cif_id revisa lo que se puede revisar sin el SAT (formato, régimen para ese tipo de persona, código postal en el catálogo, uso para el régimen, nombre sin «S.A. de C.V.») y las listas del SAT. Con el idCIF de la constancia lee el registro del SAT y compara nombre, código postal y régimen, como hará el PAC. No usa timbres.

        POST /v1/tax_ids/validate
        https://fiscalisto.com/docs/api/referencia/clientes/validate-tax-id
        """
        result: TaxIdValidation = self._client.request(
            "POST", "/v1/tax_ids/validate", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Customer:
        """Crear un cliente

        POST /v1/customers
        https://fiscalisto.com/docs/api/referencia/clientes/create-customer
        """
        result: Customer = self._client.request(
            "POST", "/v1/customers", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Customer:
        """Actualizar un cliente

        POST /v1/customers/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/update-customer
        """
        result: Customer = self._client.request(
            "POST", f"/v1/customers/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> CustomerDataRequest:
        """Pedirle sus datos fiscales a un cliente

        Una liga (url) que usted le manda a su cliente: la abre en fiscalisto.com y da su RFC, nombre, régimen, código postal y uso, escritos o leídos de su constancia, revisados antes de aceptarlos. Al mandarlos llega customer_data_request.completed. Un cliente nuevo queda en el catálogo del emisor; si ya existía con otros datos, los nuevos vienen en submission para que usted los aplique.

        POST /v1/customer_data_requests
        https://fiscalisto.com/docs/api/referencia/clientes/create-customer-data-request
        """
        result: CustomerDataRequest = self._client.request(
            "POST", "/v1/customer_data_requests", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Product:
        """Crear un producto

        POST /v1/products
        https://fiscalisto.com/docs/api/referencia/productos/create-product
        """
        result: Product = self._client.request(
            "POST", "/v1/products", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Product:
        """Actualizar un producto

        POST /v1/products/{id}
        https://fiscalisto.com/docs/api/referencia/productos/update-product
        """
        result: Product = self._client.request(
            "POST", f"/v1/products/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SatListCheckList:
        """Revisar varios RFC en las listas del SAT

        Hasta 1,000 RFC en una solicitud, en el mismo orden en que los mandó (sin repetidos). No usa timbres.

        POST /v1/sat_lists/check
        https://fiscalisto.com/docs/api/referencia/listas-del-sat/check-sat-lists
        """
        result: SatListCheckList = self._client.request(
            "POST", "/v1/sat_lists/check", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class SatDownloadsResource:
    """Descargas del SAT: fiscalisto.sat_downloads."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateSatDownloadParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SatDownload:
        """Pedirle al SAT las facturas de un emisor

        La descarga masiva del SAT: las facturas que el emisor recibió (o emitió) en un periodo de hasta un año, con su XML. Contesta 202 de inmediato; el SAT tarda de minutos a horas y al terminar llega sat_download.completed (o sat_download.failed) y las facturas quedan en GET /v1/sat_invoices. En producción necesita la e.firma guardada del emisor; en pruebas no se le pregunta al SAT: la descarga trae facturas de ejemplo al instante. No usa timbres.

        POST /v1/sat_downloads
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/create-sat-download
        """
        result: SatDownload = self._client.request(
            "POST", "/v1/sat_downloads", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListSatDownloadsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[SatDownload]:
        """Listar descargas del SAT

        GET /v1/sat_downloads
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/list-sat-downloads
        """
        return self._client.list("/v1/sat_downloads", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SatDownload:
        """Ver una descarga del SAT

        GET /v1/sat_downloads/{id}
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/get-sat-download
        """
        result: SatDownload = self._client.request(
            "GET", f"/v1/sat_downloads/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class SatInvoicesResource:
    """Descargas del SAT: fiscalisto.sat_invoices."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def list(
        self,
        params: ListSatInvoicesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[SatInvoice]:
        """Listar facturas del SAT

        Las facturas que trajeron sus descargas (y las demás que Fiscalisto tenga del emisor), de la más reciente a la más antigua por fecha.

        GET /v1/sat_invoices
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/list-sat-invoices
        """
        return self._client.list("/v1/sat_invoices", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> SatInvoice:
        """Ver una factura del SAT

        GET /v1/sat_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/get-sat-invoice
        """
        result: SatInvoice = self._client.request(
            "GET", f"/v1/sat_invoices/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def xml(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> str:
        """Descargar el XML de una factura del SAT

        El CFDI tal como lo entregó el SAT.

        GET /v1/sat_invoices/{id}/xml
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/get-sat-invoice-xml
        """
        result: str = self._client.request(
            "GET", f"/v1/sat_invoices/{_path(id)}/xml", result="text", timeout=timeout, max_retries=max_retries
        )
        return result


class TicketsResource:
    """Autofactura: fiscalisto.tickets."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateTicketParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Ticket:
        """Registrar un ticket

        Una venta que su comprador factura él mismo: con el código (code) y el total en el portal del emisor (url, que puede incrustar en su página con fiscalisto.js), da sus datos fiscales y la factura se timbra al momento con los timbres de su cuenta. Lo que nadie factura entra solo en la factura global del periodo. Registrar otra vez el mismo folio con el mismo total contesta el ticket que ya existe (los reintentos son seguros); con otro total, 409.

        POST /v1/tickets
        https://fiscalisto.com/docs/api/referencia/autofactura/create-ticket
        """
        result: Ticket = self._client.request(
            "POST", "/v1/tickets", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListTicketsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Ticket]:
        """Listar tickets

        Del más reciente al más antiguo por fecha de venta.

        GET /v1/tickets
        https://fiscalisto.com/docs/api/referencia/autofactura/list-tickets
        """
        return self._client.list("/v1/tickets", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Ticket:
        """Ver un ticket

        GET /v1/tickets/{id}
        https://fiscalisto.com/docs/api/referencia/autofactura/get-ticket
        """
        result: Ticket = self._client.request(
            "GET", f"/v1/tickets/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def cancel(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Ticket:
        """Cancelar un ticket

        Una venta que no se hizo (devolución, error): ya no se puede facturar ni entra en la factura global. Solo mientras esté pendiente.

        DELETE /v1/tickets/{id}
        https://fiscalisto.com/docs/api/referencia/autofactura/cancel-ticket
        """
        result: Ticket = self._client.request(
            "DELETE", f"/v1/tickets/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result


class AccountingResource:
    """Contabilidad: fiscalisto.accounting."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def journal_entries(
        self,
        params: ListJournalEntriesParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[JournalEntry]:
        """Listar las pólizas de un mes

        Una póliza de diario por cada CFDI de ingreso o egreso vigente del mes, emitido o recibido (los recibidos con la categoría de su gasto), con sus cuentas y código agrupador del SAT. En pesos; un CFDI en otra moneda sin tipo de cambio no se registra. Es un punto de partida para su contador: no incluye bancos, nómina ni depreciaciones.

        GET /v1/accounting/journal_entries
        https://fiscalisto.com/docs/api/referencia/contabilidad/list-journal-entries
        """
        return self._client.list("/v1/accounting/journal_entries", params, timeout=timeout, max_retries=max_retries)

    def trial_balance(
        self,
        params: GetTrialBalanceParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> TrialBalance:
        """Ver la balanza de comprobación

        Saldo inicial, cargos, abonos y saldo final de cada cuenta en el mes. Los saldos iniciales se acumulan desde el primer CFDI (las de resultados, desde enero), y los resultados de cada año anterior se cierran a capital.

        GET /v1/accounting/trial_balance
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-trial-balance
        """
        result: TrialBalance = self._client.request(
            "GET", "/v1/accounting/trial_balance", query=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def accounts(
        self,
        params: ListLedgerAccountsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> LedgerAccountList:
        """Ver el catálogo de cuentas

        Las cuentas que usan las pólizas, con su código agrupador del SAT.

        GET /v1/accounting/accounts
        https://fiscalisto.com/docs/api/referencia/contabilidad/list-ledger-accounts
        """
        result: LedgerAccountList = self._client.request(
            "GET", "/v1/accounting/accounts", query=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def electronic_accounting(
        self,
        params: GetElectronicAccountingParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> str:
        """Descargar la contabilidad electrónica

        El ZIP del mes para el Buzón Tributario: el catálogo (CT) y la balanza (BN, o BC si es complementaria), cada uno en su ZIP con el nombre que espera el SAT, en el formato 1.3 del Anexo 24. Con journal_request, también las pólizas (PL), que se entregan cuando el SAT las pide.

        GET /v1/accounting/electronic_accounting
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-electronic-accounting
        """
        result: str = self._client.request(
            "GET", "/v1/accounting/electronic_accounting", query=params, result="text", timeout=timeout, max_retries=max_retries
        )
        return result

    def diot(
        self,
        params: GetDiotParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Diot:
        """Ver la DIOT de un mes

        Lo efectivamente pagado a cada proveedor en el mes (facturas PUE y complementos de pago recibidos), con sus notas de crédito como devoluciones, por tipo de operación. Sale de las facturas recibidas que trajo de las descargas del SAT. Desde enero de 2025 (formato 2025).

        GET /v1/accounting/diot
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-diot
        """
        result: Diot = self._client.request(
            "GET", "/v1/accounting/diot", query=params, timeout=timeout, max_retries=max_retries
        )
        return result

    def diot_file(
        self,
        params: GetDiotFileParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> str:
        """Descargar la DIOT para el SAT

        El TXT de carga masiva de la DIOT 2025: 54 campos separados por |, pesos enteros. Con group_small_suppliers=true junta en una línea global a los proveedores chicos (regla 4.5.2 RMF). Un mes sin pagos a proveedores responde diot_empty: esa se presenta sin operaciones en el portal del SAT.

        GET /v1/accounting/diot/file
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-diot-file
        """
        result: str = self._client.request(
            "GET", "/v1/accounting/diot/file", query=params, result="text", timeout=timeout, max_retries=max_retries
        )
        return result


class StoreConnectionsResource:
    """Tiendas en línea: fiscalisto.store_connections."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateStoreConnectionParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> StoreConnection:
        """Conectar una tienda

        Shopify: con el dominio y las llaves de la app de la tienda (Dev Dashboard, permisos read_orders y write_orders) registra los webhooks y queda active. Mercado Libre: queda pending hasta que el vendedor autorice en authorize_url. Desde entonces cada pedido pagado es un ticket (folio SHOP-1001 o ML-…), que su comprador factura en el portal o entra en la factura global; un pedido cancelado o reembolsado completo cancela su ticket.

        POST /v1/store_connections
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/create-store-connection
        """
        result: StoreConnection = self._client.request(
            "POST", "/v1/store_connections", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListStoreConnectionsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[StoreConnection]:
        """Listar tiendas

        Las más recientes primero, también las desconectadas.

        GET /v1/store_connections
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/list-store-connections
        """
        return self._client.list("/v1/store_connections", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> StoreConnection:
        """Ver una tienda

        GET /v1/store_connections/{id}
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/get-store-connection
        """
        result: StoreConnection = self._client.request(
            "GET", f"/v1/store_connections/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateStoreConnectionParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> StoreConnection:
        """Cambiar cómo se vuelven tickets sus pedidos

        Cuenta para los pedidos que lleguen; los tickets ya hechos no cambian.

        POST /v1/store_connections/{id}
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/update-store-connection
        """
        result: StoreConnection = self._client.request(
            "POST", f"/v1/store_connections/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> StoreConnection:
        """Desconectar una tienda

        Sus pedidos dejan de llegar y se borran sus llaves y webhooks. Los tickets que ya hizo siguen.

        DELETE /v1/store_connections/{id}
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/delete-store-connection
        """
        result: StoreConnection = self._client.request(
            "DELETE", f"/v1/store_connections/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def import_orders(
        self,
        id: str,
        params: ImportStoreOrdersParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> StoreImport:
        """Traer pedidos pagados

        Los pedidos pagados desde una fecha (hasta 31 días, 200 a la vez) que no llegaron por webhook: la tienda se conectó después o estuvo caída. Un pedido que ya es ticket no se repite.

        POST /v1/store_connections/{id}/import_orders
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/import-store-orders
        """
        result: StoreImport = self._client.request(
            "POST", f"/v1/store_connections/{_path(id)}/import_orders", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class RecurringInvoicesResource:
    """Facturas recurrentes: fiscalisto.recurring_invoices."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateRecurringInvoiceParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> RecurringInvoice:
        """Crear una factura recurrente

        Una factura que el emisor timbra solo en cada fecha (cada interval meses en day_of_month, o cada interval semanas o días), a la hora que elija, con los timbres de su cuenta, y la manda al cliente si send_email. Cada una es una factura normal (invoice.stamped, con recurring_invoice) y nunca se timbra dos veces el mismo periodo. invoice es el cuerpo de POST /v1/invoices: se revisa ahora, con las mismas reglas.

        POST /v1/recurring_invoices
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/create-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "POST", "/v1/recurring_invoices", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListRecurringInvoicesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[RecurringInvoice]:
        """Listar facturas recurrentes

        Las más recientes primero.

        GET /v1/recurring_invoices
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/list-recurring-invoices
        """
        return self._client.list("/v1/recurring_invoices", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> RecurringInvoice:
        """Ver una factura recurrente

        GET /v1/recurring_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/get-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "GET", f"/v1/recurring_invoices/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateRecurringInvoiceParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> RecurringInvoice:
        """Cambiar o pausar una factura recurrente

        Solo lo que mande cambia. invoice reemplaza la factura completa desde la siguiente vez. active: false la pausa; active: true la reanuda desde hoy, sin timbrar las fechas que pasaron en pausa. schedule.start_date mueve la siguiente fecha.

        POST /v1/recurring_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/update-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "POST", f"/v1/recurring_invoices/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Deleted:
        """Borrar una factura recurrente

        Ya no timbra más; las facturas que timbró se quedan.

        DELETE /v1/recurring_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/delete-recurring-invoice
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/recurring_invoices/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def skip(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> RecurringInvoice:
        """Saltar la siguiente factura

        La siguiente fecha pasa a la que sigue, sin timbrar nada.

        POST /v1/recurring_invoices/{id}/skip
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/skip-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "POST", f"/v1/recurring_invoices/{_path(id)}/skip", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def run(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Timbrar ahora la que toca

        Timbra el periodo que ya toca (next_invoice_on es hoy o antes) sin esperar su hora. Si no toca aún, 409 recurring_not_due. Si la hora llega mientras tanto, no se timbra dos veces: es el mismo periodo.

        POST /v1/recurring_invoices/{id}/run
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/run-recurring-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/recurring_invoices/{_path(id)}/run", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result


class QuotesResource:
    """Cotizaciones: fiscalisto.quotes."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateQuoteParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Quote:
        """Crear una cotización

        Una cotización en borrador, con los conceptos y las condiciones de pago de una factura (se revisan con las mismas reglas, así que siempre se puede facturar). customer es un cliente de su catálogo, uno con sus datos fiscales (se agrega a sus clientes) o solo name y email si aún no los tiene. Se manda con POST /v1/quotes/{id}/send.

        POST /v1/quotes
        https://fiscalisto.com/docs/api/referencia/cotizaciones/create-quote
        """
        result: Quote = self._client.request(
            "POST", "/v1/quotes", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def list(
        self,
        params: ListQuotesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> ListObject[Quote]:
        """Listar cotizaciones

        Las más recientes primero, cada una en su última versión.

        GET /v1/quotes
        https://fiscalisto.com/docs/api/referencia/cotizaciones/list-quotes
        """
        return self._client.list("/v1/quotes", params, timeout=timeout, max_retries=max_retries)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Quote:
        """Ver una cotización

        Su última versión.

        GET /v1/quotes/{id}
        https://fiscalisto.com/docs/api/referencia/cotizaciones/get-quote
        """
        result: Quote = self._client.request(
            "GET", f"/v1/quotes/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateQuoteParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Quote:
        """Cambiar una cotización

        Solo lo que mande cambia. Un borrador cambia ahí mismo; una que ya se envió se vuelve una versión nueva en borrador (mismo número, version + 1) que el cliente ve al mandarla; mientras, su liga muestra la anterior. Una aceptada, rechazada o facturada ya no cambia.

        POST /v1/quotes/{id}
        https://fiscalisto.com/docs/api/referencia/cotizaciones/update-quote
        """
        result: Quote = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Deleted:
        """Borrar una cotización

        Solo una que nunca se envió; si no, 400 quote_not_draft.

        DELETE /v1/quotes/{id}
        https://fiscalisto.com/docs/api/referencia/cotizaciones/delete-quote
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/quotes/{_path(id)}", timeout=timeout, max_retries=max_retries
        )
        return result

    def send(
        self,
        id: str,
        params: SendQuoteParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Quote:
        """Mandar una cotización

        La manda por correo con su PDF y la liga donde el cliente la ve, la acepta, pide cambios o la rechaza. Con send_email: false solo se marca enviada y contesta url, para que usted la mande por WhatsApp o su propio correo.

        POST /v1/quotes/{id}/send
        https://fiscalisto.com/docs/api/referencia/cotizaciones/send-quote
        """
        result: Quote = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}/send", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def accept(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Quote:
        """Marcar aceptada

        El cliente le dijo que sí por teléfono, en persona… Llega quote.accepted. No timbra: para eso, POST /v1/quotes/{id}/invoice.

        POST /v1/quotes/{id}/accept
        https://fiscalisto.com/docs/api/referencia/cotizaciones/accept-quote
        """
        result: Quote = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}/accept", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def invoice(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> Invoice:
        """Facturar una cotización

        Timbra la factura con los conceptos de la cotización y los datos fiscales del cliente, y la deja facturada (invoice). Si no estaba aceptada, la marca aceptada. Una en otra moneda va al tipo de cambio de hoy. Sin los datos fiscales del cliente, 400 quote_customer_missing; rechazada o vencida, 400 quote_not_invoiceable. Si ya se facturó, contesta esa factura.

        POST /v1/quotes/{id}/invoice
        https://fiscalisto.com/docs/api/referencia/cotizaciones/invoice-quote
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}/invoice", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def pdf(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> bytes:
        """Descargar el PDF

        El PDF de su última versión, con el diseño de PDF del emisor.

        GET /v1/quotes/{id}/pdf
        https://fiscalisto.com/docs/api/referencia/cotizaciones/get-quote-pdf
        """
        result: bytes = self._client.request(
            "GET", f"/v1/quotes/{_path(id)}/pdf", result="bytes", timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Crear un webhook

        La respuesta trae el secreto de firma (secret) una sola vez.

        POST /v1/webhook_endpoints
        https://fiscalisto.com/docs/api/referencia/webhooks/create-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "POST", "/v1/webhook_endpoints", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Actualizar un webhook

        POST /v1/webhook_endpoints/{id}
        https://fiscalisto.com/docs/api/referencia/webhooks/update-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookEndpoint:
        """Cambiar el secreto

        Un secreto nuevo, que la respuesta trae una sola vez. El anterior sigue firmando (una segunda firma en webhook-signature) el tiempo que elija, 24 horas por omisión, para que cambie su servidor sin rechazar eventos. Si se filtró, mande previous_secret_expires_in: 0.

        POST /v1/webhook_endpoints/{id}/roll_secret
        https://fiscalisto.com/docs/api/referencia/webhooks/roll-webhook-secret
        """
        result: WebhookEndpoint = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}/roll_secret", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
        )
        return result

    def test(
        self,
        id: str,
        params: TestWebhookEndpointParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> WebhookTest:
        """Mandar un evento de prueba

        Manda ahora, una sola vez y sin reintentos, un evento del tipo que elija con un objeto de ejemplo (sus id no existen), firmado como los reales, aunque el webhook no escuche ese tipo. La respuesta trae lo que contestó su servidor. El evento no sale en GET /v1/events, pero sí en las entregas del webhook.

        POST /v1/webhook_endpoints/{id}/test
        https://fiscalisto.com/docs/api/referencia/webhooks/test-webhook-endpoint
        """
        result: WebhookTest = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}/test", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries
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
    def test_data(self) -> TestDataResource:
        """Cuenta."""
        return TestDataResource(self)

    @cached_property
    def sandboxes(self) -> SandboxesResource:
        """Entornos de prueba."""
        return SandboxesResource(self)

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
    def receivables(self) -> ReceivablesResource:
        """Cuentas por cobrar."""
        return ReceivablesResource(self)

    @cached_property
    def bank_transactions(self) -> BankTransactionsResource:
        """Conciliación bancaria."""
        return BankTransactionsResource(self)

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
    def sat_downloads(self) -> SatDownloadsResource:
        """Descargas del SAT."""
        return SatDownloadsResource(self)

    @cached_property
    def sat_invoices(self) -> SatInvoicesResource:
        """Descargas del SAT."""
        return SatInvoicesResource(self)

    @cached_property
    def tickets(self) -> TicketsResource:
        """Autofactura."""
        return TicketsResource(self)

    @cached_property
    def accounting(self) -> AccountingResource:
        """Contabilidad."""
        return AccountingResource(self)

    @cached_property
    def store_connections(self) -> StoreConnectionsResource:
        """Tiendas en línea."""
        return StoreConnectionsResource(self)

    @cached_property
    def recurring_invoices(self) -> RecurringInvoicesResource:
        """Facturas recurrentes."""
        return RecurringInvoicesResource(self)

    @cached_property
    def quotes(self) -> QuotesResource:
        """Cotizaciones."""
        return QuotesResource(self)

    @cached_property
    def webhook_endpoints(self) -> WebhookEndpointsResource:
        """Webhooks."""
        return WebhookEndpointsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """Eventos."""
        return EventsResource(self)
