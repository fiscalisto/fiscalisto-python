# Generado por `bun run openapi` desde la especificación OpenAPI de la API: no lo edite.
"""Cada recurso de la API y sus llamadas."""

from __future__ import annotations

from collections.abc import Sequence
from functools import cached_property
from typing import TYPE_CHECKING
from urllib.parse import quote

from ._core import Core, ListObject

if TYPE_CHECKING:
    from .types import (
        Account,
        AdvanceList,
        AdvanceTestClockParams,
        ApplyAdvanceParams,
        Balance,
        BankImport,
        BankTransaction,
        Branch,
        CancelInvoiceParams,
        CancelRetentionParams,
        CheckSatListsParams,
        ClassifyBankTransactionParams,
        ComplianceOpinion,
        CreateAdvanceParams,
        CreateBankTransactionsParams,
        CreateBranchParams,
        CreateCreditNoteParams,
        CreateCustomerDataRequestParams,
        CreateCustomerParams,
        CreateEmployeeParams,
        CreateInvoiceBatchParams,
        CreateIssuerOnboardingLinkParams,
        CreateIssuerParams,
        CreatePaymentParams,
        CreatePayrollBatchParams,
        CreatePayrollReceiptParams,
        CreateProductParams,
        CreateQuoteParams,
        CreateRecurringInvoiceParams,
        CreateRetentionParams,
        CreateSandboxParams,
        CreateSatDownloadParams,
        CreateStockAdjustmentParams,
        CreateStoreConnectionParams,
        CreateTestClockParams,
        CreateTicketParams,
        CreateWebhookEndpointParams,
        CrossCheckCfdi,
        CrossChecks,
        Customer,
        CustomerDataRequest,
        Deleted,
        Diot,
        Employee,
        Event,
        ExternalPayrollReceiptCreate,
        ExternalPayrollReceiptPreview,
        FinancialStatements,
        GetCrossCheckCfdiParams,
        GetCrossChecksParams,
        GetDiotFileParams,
        GetDiotParams,
        GetElectronicAccountingParams,
        GetFinancialStatementsParams,
        GetInvoiceParams,
        GetInvoicePdfParams,
        GetInvoiceXmlParams,
        GetRetentionParams,
        GetRetentionPdfParams,
        GetRetentionXmlParams,
        GetSatCatalogParams,
        GetSatDeclarationCalendarParams,
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
        ListBranchesParams,
        ListCustomerDataRequestsParams,
        ListCustomersParams,
        ListEmployeesParams,
        ListEventsParams,
        ListInvoiceBatchesParams,
        ListInvoicesParams,
        ListIssuersParams,
        ListJournalEntriesParams,
        ListLedgerAccountsParams,
        ListPayrollBatchesParams,
        ListProductsParams,
        ListQuotesParams,
        ListReceivablesParams,
        ListRecurringInvoicesParams,
        ListRetentionsParams,
        ListSatDeclarationsParams,
        ListSatDownloadsParams,
        ListSatFindingsParams,
        ListSatInvoicesParams,
        ListSatMailboxMessagesParams,
        ListStockAdjustmentsParams,
        ListStockMovementsParams,
        ListStoreConnectionsParams,
        ListTicketsParams,
        ListWarehouseStockParams,
        ListWarehousesParams,
        ListWebhookEndpointsParams,
        MatchBankTransactionParams,
        PayrollBatch,
        PayrollReceiptPreview,
        PreviewPayrollReceiptParams,
        Product,
        Quote,
        Receivable,
        RecurringInvoice,
        RefreshSatDeclarationsParams,
        ResetTestDataParams,
        Retention,
        RollWebhookSecretParams,
        Sandbox,
        SandboxList,
        SatCatalogEntryList,
        SatDeclaration,
        SatDeclarationCalendar,
        SatDeclarationsRefresh,
        SatDownload,
        SatFindingList,
        SatInvoice,
        SatListCheck,
        SatListCheckList,
        SatMailboxMessage,
        SatRefresh,
        SelfInvoicing,
        SendInvoiceParams,
        SendQuoteParams,
        SendRetentionParams,
        SignEfirmaParams,
        StockAdjustment,
        StockLevel,
        StockLevelList,
        StockMovement,
        StoreConnection,
        StoreImport,
        TaxIdValidation,
        TaxStatusCertificate,
        TestClock,
        TestDataReset,
        TestWebhookEndpointParams,
        Ticket,
        TrialBalance,
        UpdateAccountParams,
        UpdateBranchParams,
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
        Warehouse,
        WarehouseList,
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
        expand: Sequence[str] | None = None,
    ) -> Account:
        """Ver la cuenta

        La cuenta API y la llave con que se hizo la solicitud. Útil para probar la llave.

        GET /v1/account
        https://fiscalisto.com/docs/api/referencia/cuenta/get-account
        """
        result: Account = self._client.request(
            "GET", "/v1/account", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def update(
        self,
        params: UpdateAccountParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Account:
        """Cambiar la versión de la API

        Mueve la versión de la API de la cuenta: la que reciben sus solicitudes sin el encabezado Fiscalisto-Version y sus webhooks sin api_version propio. Antes, pruebe la nueva mandando Fiscalisto-Version en sus solicitudes. Con una llave de la cuenta con todos los permisos (no de un entorno de prueba). Queda en Desarrolladores › Actividad.

        POST /v1/account
        https://fiscalisto.com/docs/api/referencia/cuenta/update-account
        """
        result: Account = self._client.request(
            "POST", "/v1/account", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> TestDataReset:
        """Reiniciar los datos de prueba

        Deja el modo de pruebas como nuevo: cada emisor de pruebas conserva su RFC y su CSD de pruebas pero pierde sus facturas, clientes, productos, lotes, ligas y descargas, y se borran los eventos y el registro de solicitudes de pruebas. Las llaves y los webhooks se quedan. Con seed (por omisión) deja 2 clientes y 3 productos de ejemplo. Solo con una llave fk_test_; producción nunca se toca.

        POST /v1/test_data/reset
        https://fiscalisto.com/docs/api/referencia/cuenta/reset-test-data
        """
        result: TestDataReset = self._client.request(
            "POST", "/v1/test_data/reset", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Sandbox:
        """Crear un entorno de prueba

        Un modo de pruebas propio para una persona o un proyecto: nace con el emisor de pruebas del SAT y una llave fk_test_ (key.secret, una sola vez) que solo ve los emisores, webhooks y eventos del entorno, y que reinicia solo los suyos. Se crea con una llave de pruebas de la cuenta (no de otro entorno ni limitada a emisores). Hasta 25 por cuenta.

        POST /v1/sandboxes
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/create-sandbox
        """
        result: Sandbox = self._client.request(
            "POST", "/v1/sandboxes", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SandboxList:
        """Listar entornos de prueba

        Los entornos de prueba de la cuenta, cada uno con su emisor de prueba y su llave fk_test_. Hasta 25 por cuenta.

        GET /v1/sandboxes
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/list-sandboxes
        """
        result: SandboxList = self._client.request(
            "GET", "/v1/sandboxes", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Sandbox:
        """Ver un entorno de prueba

        Un entorno de prueba: su nombre, su emisor y lo que lleva usado hoy de sus reinicios.

        GET /v1/sandboxes/{id}
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/get-sandbox
        """
        result: Sandbox = self._client.request(
            "GET", f"/v1/sandboxes/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar un entorno de prueba

        Sus llaves dejan de funcionar al momento, sus emisores se archivan y sus webhooks se borran. No toca nada de la cuenta ni de otros entornos.

        DELETE /v1/sandboxes/{id}
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/delete-sandbox
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/sandboxes/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result


class TestClocksResource:
    """Entornos de prueba: fiscalisto.test_clocks."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        id: str,
        params: CreateTestClockParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> TestClock:
        """Crear un reloj de prueba

        Le da a un emisor de pruebas su propia hora, congelada en frozen_time (ahora, si no la manda): sus facturas recurrentes, cotizaciones, cuentas por cobrar y tickets cuentan los días con ella, y nada de eso corre solo hasta que usted lo adelanta. Para ver en segundos lo que pasa en meses. Solo emisores de prueba; uno por emisor.

        POST /v1/issuers/{id}/test_clock
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/create-test-clock
        """
        result: TestClock = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/test_clock", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> TestClock:
        """Ver el reloj de prueba

        La hora que es «hoy» para un emisor de prueba y hasta dónde se ha adelantado. Solo emisores de prueba.

        GET /v1/issuers/{id}/test_clock
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/get-test-clock
        """
        result: TestClock = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}/test_clock", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> TestClock:
        """Borrar el reloj de prueba

        El emisor vuelve a la hora real; lo que el reloj dejó pendiente lo hacen los procesos diarios.

        DELETE /v1/issuers/{id}/test_clock
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/delete-test-clock
        """
        result: TestClock = self._client.request(
            "DELETE", f"/v1/issuers/{_path(id)}/test_clock", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def advance(
        self,
        id: str,
        params: AdvanceTestClockParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> TestClock:
        """Adelantar el reloj de prueba

        Mueve el reloj hasta frozen_time haciendo, día por día, lo que habría pasado: timbra las facturas recurrentes de cada periodo, vence las cotizaciones y hace las facturas globales de tickets, con sus eventos. Contesta cuando terminó, con lo que hizo en advanced, y llega test_clock.ready. Hasta 25 comprobantes por solicitud: si se detiene antes, stopped_early y otra llamada sigue. Los CFDI se timbran con la fecha real (el SAT solo acepta la de hoy); el periodo, los vencimientos y los eventos siguen al reloj.

        POST /v1/issuers/{id}/test_clock/advance
        https://fiscalisto.com/docs/api/referencia/entornos-de-prueba/advance-test-clock
        """
        result: TestClock = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/test_clock/advance", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Balance:
        """Ver los timbres

        Los timbres de producción que le quedan, por paquete. En pruebas se timbra gratis.

        GET /v1/balance
        https://fiscalisto.com/docs/api/referencia/cuenta/get-balance
        """
        result: Balance = self._client.request(
            "GET", "/v1/balance", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Issuer:
        """Crear un emisor

        Agrega un RFC que va a timbrar. Después suba su CSD (POST /v1/issuers/{id}/certificates) y, solo en producción, firme una vez el contrato con el PAC con su e.firma (POST /v1/issuers/{id}/efirma).

        POST /v1/issuers
        https://fiscalisto.com/docs/api/referencia/emisores/create-issuer
        """
        result: Issuer = self._client.request(
            "POST", "/v1/issuers", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListIssuersParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Issuer]:
        """Listar emisores

        Los emisores de la cuenta en el modo de la llave, los más recientes primero. Una llave limitada a algunos emisores solo ve los suyos.

        GET /v1/issuers
        https://fiscalisto.com/docs/api/referencia/emisores/list-issuers
        """
        return self._client.list("/v1/issuers", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Issuer:
        """Ver un emisor

        Un emisor: sus datos fiscales, si ya puede timbrar (status, CSD y contrato con el PAC) y su registro patronal.

        GET /v1/issuers/{id}
        https://fiscalisto.com/docs/api/referencia/emisores/get-issuer
        """
        result: Issuer = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Issuer:
        """Actualizar un emisor

        Solo cambia lo que mande. El RFC no cambia: cree otro emisor.

        POST /v1/issuers/{id}
        https://fiscalisto.com/docs/api/referencia/emisores/update-issuer
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def archive(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Issuer:
        """Archivar un emisor

        Deja de timbrar; sus comprobantes se quedan.

        DELETE /v1/issuers/{id}
        https://fiscalisto.com/docs/api/referencia/emisores/archive-issuer
        """
        result: Issuer = self._client.request(
            "DELETE", f"/v1/issuers/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Issuer:
        """Subir el CSD

        El certificado de sello digital (.cer y .key en base64) y la contraseña de la llave. Se guarda cifrado y solo se usa para sellar. En pruebas se revisa pero se timbra con el CSD de pruebas del SAT.

        POST /v1/issuers/{id}/certificates
        https://fiscalisto.com/docs/api/referencia/emisores/upload-certificate
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/certificates", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Issuer:
        """Firmar el contrato con el PAC

        Una sola vez por RFC antes de timbrar en producción: firma el contrato de servicio del PAC (Finkok) con la e.firma del emisor. La e.firma se usa en memoria para esa firma y no se guarda, salvo que mande keep_for_downloads: true para pedirle al SAT las facturas del emisor (POST /v1/sat_downloads); entonces se guarda cifrada y puede borrarla con DELETE.

        POST /v1/issuers/{id}/efirma
        https://fiscalisto.com/docs/api/referencia/emisores/sign-efirma
        """
        result: Issuer = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/efirma", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete_efirma(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Issuer:
        """Borrar la e.firma guardada

        Borra la e.firma que guardó con keep_for_downloads. El emisor sigue timbrando; ya no puede pedir descargas al SAT hasta que la mande de nuevo.

        DELETE /v1/issuers/{id}/efirma
        https://fiscalisto.com/docs/api/referencia/emisores/delete-efirma
        """
        result: Issuer = self._client.request(
            "DELETE", f"/v1/issuers/{_path(id)}/efirma", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> IssuerOnboardingLink:
        """Crear una liga de alta

        Una página en fiscalisto.com donde el dueño del emisor sube su CSD y firma el contrato con el PAC con su e.firma, sin que esos archivos ni sus contraseñas pasen por su plataforma. Mande a su cliente a url; al terminar vuelve a return_url y llega issuer.ready. Cada liga sirve para un emisor, hasta que vence.

        POST /v1/issuers/{id}/onboarding_links
        https://fiscalisto.com/docs/api/referencia/emisores/create-issuer-onboarding-link
        """
        result: IssuerOnboardingLink = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/onboarding_links", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def compliance_opinion(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ComplianceOpinion:
        """Ver la opinión de cumplimiento (32-D)

        La última opinión que trajo del SAT: positiva, negativa (con sus motivos), sin obligaciones o en suspensión. result es null hasta la primera consulta. No usa timbres.

        GET /v1/issuers/{id}/compliance_opinion
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/get-compliance-opinion
        """
        result: ComplianceOpinion = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}/compliance_opinion", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def refresh_compliance_opinion(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatRefresh:
        """Pedir la opinión de cumplimiento al SAT

        La pide al SAT ahora con la e.firma guardada del emisor (POST /v1/issuers/{id}/efirma con keep_for_downloads: true). 1 timbre en producción, una vez cada 10 minutos; regresa si el SAT no contesta. Si el SAT tarda, contesta status processing y el resultado llega a GET /v1/issuers/{id}/compliance_opinion. En pruebas da una positiva de ejemplo.

        POST /v1/issuers/{id}/compliance_opinion/refresh
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/refresh-compliance-opinion
        """
        result: SatRefresh = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/compliance_opinion/refresh", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def compliance_opinion_pdf(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> bytes:
        """Descargar el PDF de la opinión de cumplimiento

        El PDF de la última opinión, como lo da el SAT. No usa timbres.

        GET /v1/issuers/{id}/compliance_opinion/pdf
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/get-compliance-opinion-pdf
        """
        result: bytes = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}/compliance_opinion/pdf", result="bytes", timeout=timeout, max_retries=max_retries
        )
        return result

    def tax_status_certificate(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> TaxStatusCertificate:
        """Ver la constancia de situación fiscal

        Lo que dice la última constancia generada: razón social, regímenes, código postal, estatus en el padrón e idCIF. No usa timbres.

        GET /v1/issuers/{id}/tax_status_certificate
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/get-tax-status-certificate
        """
        result: TaxStatusCertificate = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}/tax_status_certificate", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def refresh_tax_status_certificate(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatRefresh:
        """Generar la constancia de situación fiscal en el SAT

        Genera una constancia nueva con la e.firma guardada del emisor. 1 timbre en producción, una vez cada 10 minutos; regresa si el SAT no contesta. En pruebas hace una con los datos del emisor.

        POST /v1/issuers/{id}/tax_status_certificate/refresh
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/refresh-tax-status-certificate
        """
        result: SatRefresh = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/tax_status_certificate/refresh", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def tax_status_certificate_pdf(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> bytes:
        """Descargar el PDF de la constancia

        El PDF de la última constancia, como lo da el SAT. No usa timbres.

        GET /v1/issuers/{id}/tax_status_certificate/pdf
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/get-tax-status-certificate-pdf
        """
        result: bytes = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}/tax_status_certificate/pdf", result="bytes", timeout=timeout, max_retries=max_retries
        )
        return result

    def refresh_sat_mailbox(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatRefresh:
        """Revisar el buzón tributario en el SAT

        Lee los avisos del buzón tributario del emisor ahora, con su e.firma guardada; nunca abre notificaciones (abrirlas firma el acuse y corren los plazos). 1 timbre en producción, una vez cada 10 minutos. En pruebas deja dos avisos de ejemplo.

        POST /v1/issuers/{id}/sat_mailbox/refresh
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/refresh-sat-mailbox
        """
        result: SatRefresh = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/sat_mailbox/refresh", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def get_self_invoicing(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SelfInvoicing:
        """Ver el portal de autofactura de un emisor

        El portal de autofactura del emisor: su dirección, hasta cuándo se puede facturar un ticket y cómo se arma la factura global.

        GET /v1/issuers/{id}/self_invoicing
        https://fiscalisto.com/docs/api/referencia/autofactura/get-self-invoicing
        """
        result: SelfInvoicing = self._client.request(
            "GET", f"/v1/issuers/{_path(id)}/self_invoicing", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> SelfInvoicing:
        """Cambiar las reglas de autofactura

        Hasta cuándo se puede facturar un ticket y cada cuánto se timbra la factura global.

        POST /v1/issuers/{id}/self_invoicing
        https://fiscalisto.com/docs/api/referencia/autofactura/update-self-invoicing
        """
        result: SelfInvoicing = self._client.request(
            "POST", f"/v1/issuers/{_path(id)}/self_invoicing", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Timbrar una factura

        Revisa la factura con las reglas del SAT, la sella y la timbra en una sola llamada. Responde con la factura timbrada (status valid) o, si el PAC tarda, en processing (escuche invoice.stamped). Lo que puede omitir tiene el valor usual: PUE, MXN, uso G03 (S01 con régimen 616), objeto de impuesto 02, IVA 16%, cantidad 1, unidad E48.

        POST /v1/invoices
        https://fiscalisto.com/docs/api/referencia/facturas/create-invoice
        """
        result: Invoice = self._client.request(
            "POST", "/v1/invoices", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListInvoicesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Invoice]:
        """Listar facturas

        Las más recientes primero.

        GET /v1/invoices
        https://fiscalisto.com/docs/api/referencia/facturas/list-invoices
        """
        return self._client.list("/v1/invoices", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        params: GetInvoiceParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Ver una factura

        Por su id (inv_…) o por su folio fiscal (UUID).

        GET /v1/invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas/get-invoice
        """
        result: Invoice = self._client.request(
            "GET", f"/v1/invoices/{_path(id)}", query=params, timeout=timeout, max_retries=max_retries, expand=expand
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

        La representación impresa del CFDI, como la recibe su cliente. En vez del id puede usar el UUID (con issuer si la cuenta tiene varios emisores).

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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Enviar por correo

        Manda el PDF y el XML con el diseño de Fiscalisto. Sin `to`, al correo del cliente. Con la misma Idempotency-Key no se manda dos veces.

        POST /v1/invoices/{id}/send
        https://fiscalisto.com/docs/api/referencia/facturas/send-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/send", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Cancelar una factura

        Pide la cancelación al SAT. Si el cliente debe aceptarla queda en pending (escuche invoice.canceled o invoice.cancellation_rejected). No usa timbres.

        POST /v1/invoices/{id}/cancel
        https://fiscalisto.com/docs/api/referencia/facturas/cancel-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/cancel", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Sustituir una factura

        Timbra la factura corregida (el mismo cuerpo que POST /v1/invoices, relacionada 04) y cancela la anterior con motivo 01.

        POST /v1/invoices/{id}/substitute
        https://fiscalisto.com/docs/api/referencia/facturas/substitute-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/substitute", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def mark_paid(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Marcar pagada

        Una factura PUE timbrada con paid_later (o marcada por cobrar) ya se pagó: queda paid y llega invoice.paid. Una PPD se paga con su complemento de pago (POST /v1/payments).

        POST /v1/invoices/{id}/mark_paid
        https://fiscalisto.com/docs/api/referencia/cuentas-por-cobrar/mark-invoice-paid
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/mark_paid", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def mark_unpaid(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Marcar por cobrar

        Una factura PUE que el cliente aún no paga (le paga este mes): queda unpaid hasta POST /v1/invoices/{id}/mark_paid. Si el mes termina sin pago, la ley pide sustituirla por una PPD (regla 2.7.1.39 de la RMF).

        POST /v1/invoices/{id}/mark_unpaid
        https://fiscalisto.com/docs/api/referencia/cuentas-por-cobrar/mark-invoice-unpaid
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/invoices/{_path(id)}/mark_unpaid", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> ListObject[Receivable]:
        """Ver lo que le deben

        Lo que debe cada cliente, por moneda, de sus facturas abiertas (PPD con saldo y PUE por cobrar), ordenado por RFC. Las facturas de cada uno: GET /v1/invoices?customer=RFC&payment_status=open.

        GET /v1/receivables
        https://fiscalisto.com/docs/api/referencia/cuentas-por-cobrar/list-receivables
        """
        return self._client.list("/v1/receivables", params, timeout=timeout, max_retries=max_retries, expand=expand)


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
        expand: Sequence[str] | None = None,
    ) -> BankImport:
        """Mandar depósitos

        Los depósitos de la cuenta del emisor (de la API de su banco o de un estado de cuenta), hasta 1,000 por solicitud. Uno que ya mandó (mismo día, monto, referencia y concepto) se omite, así que puede mandar periodos que se enciman. Cada uno trae suggested_match: las facturas que parece pagar.

        POST /v1/bank_transactions
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/create-bank-transactions
        """
        result: BankImport = self._client.request(
            "POST", "/v1/bank_transactions", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListBankTransactionsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[BankTransaction]:
        """Listar depósitos

        Los más recientes primero; los abiertos con su suggested_match.

        GET /v1/bank_transactions
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/list-bank-transactions
        """
        return self._client.list("/v1/bank_transactions", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> BankTransaction:
        """Ver un depósito

        Un depósito mandado a conciliación, con las facturas que se le encontraron o el pago que se registró con él.

        GET /v1/bank_transactions/{id}
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/get-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "GET", f"/v1/bank_transactions/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> BankTransaction:
        """Conciliar un depósito

        El depósito pagó estas facturas (de un mismo cliente), o sin invoices, las de suggested_match. Sus facturas PUE por cobrar quedan pagadas (invoice.paid). No timbra: para pagar una PPD con este depósito, POST /v1/payments con bank_transaction.

        POST /v1/bank_transactions/{id}/match
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/match-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "POST", f"/v1/bank_transactions/{_path(id)}/match", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> BankTransaction:
        """Explicar un depósito sin factura

        Un depósito que ninguna factura explica: venta (aún sin facturar), prestamo, traspaso o devolucion. El SAT puede presumir ingreso un depósito sin explicar (CFF art. 59 fr. III).

        POST /v1/bank_transactions/{id}/classify
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/classify-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "POST", f"/v1/bank_transactions/{_path(id)}/classify", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def reopen(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> BankTransaction:
        """Deshacer la conciliación

        Vuelve a open, y sus facturas vuelven a deber. Si se pagó con un complemento vigente, cancélelo antes.

        POST /v1/bank_transactions/{id}/reopen
        https://fiscalisto.com/docs/api/referencia/conciliacion-bancaria/reopen-bank-transaction
        """
        result: BankTransaction = self._client.request(
            "POST", f"/v1/bank_transactions/{_path(id)}/reopen", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Timbrar un complemento de pago

        El recibo de pago (CFDI tipo P, Pagos 2.0) de facturas PPD: parcialidad, saldo anterior e insoluto e impuestos de cada una los calcula Fiscalisto.

        POST /v1/payments
        https://fiscalisto.com/docs/api/referencia/pagos-y-notas-de-credito/create-payment
        """
        result: Invoice = self._client.request(
            "POST", "/v1/payments", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Timbrar una nota de crédito

        Un egreso (tipo E) relacionado 01 (o 03, devolución) a una factura, con su IVA y retenciones en la misma proporción. amount es antes de impuestos.

        POST /v1/credit_notes
        https://fiscalisto.com/docs/api/referencia/pagos-y-notas-de-credito/create-credit-note
        """
        result: Invoice = self._client.request(
            "POST", "/v1/credit_notes", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Timbrar un anticipo

        La factura del anticipo: un concepto «Anticipo del bien o servicio» (84111506, ACT). amount es lo que pagó el cliente con IVA.

        POST /v1/advances
        https://fiscalisto.com/docs/api/referencia/anticipos/create-advance
        """
        result: Invoice = self._client.request(
            "POST", "/v1/advances", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListAdvancesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> AdvanceList:
        """Listar anticipos sin aplicar

        Los anticipos timbrados que todavía no se aplican a una factura, con lo que queda de cada uno. Filtre por customer para los de un cliente.

        GET /v1/advances
        https://fiscalisto.com/docs/api/referencia/anticipos/list-advances
        """
        result: AdvanceList = self._client.request(
            "GET", "/v1/advances", query=params, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Aplicar un anticipo

        Timbra la factura de lo vendido (el cuerpo de POST /v1/invoices) relacionada 07 al anticipo. Con method egreso, también la nota de aplicación. La misma Idempotency-Key continúa donde se quedó.

        POST /v1/advances/{id}/apply
        https://fiscalisto.com/docs/api/referencia/anticipos/apply-advance
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/advances/{_path(id)}/apply", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Retention:
        """Timbrar una constancia de retenciones

        Timbra una constancia de retenciones e información de pagos (Retenciones 2.0) con los folios RET1, RET2… del emisor. Una vez por Idempotency-Key; con send_email y email la manda al receptor al timbrarla.

        POST /v1/retentions
        https://fiscalisto.com/docs/api/referencia/retenciones/create-retention
        """
        result: Retention = self._client.request(
            "POST", "/v1/retentions", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListRetentionsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Retention]:
        """Listar constancias

        Las constancias del emisor, las más recientes primero.

        GET /v1/retentions
        https://fiscalisto.com/docs/api/referencia/retenciones/list-retentions
        """
        return self._client.list("/v1/retentions", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        params: GetRetentionParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Retention:
        """Ver una constancia

        Una constancia de retenciones con su estado, sus impuestos retenidos y, si se mandó, a quién.

        GET /v1/retentions/{id}
        https://fiscalisto.com/docs/api/referencia/retenciones/get-retention
        """
        result: Retention = self._client.request(
            "GET", f"/v1/retentions/{_path(id)}", query=params, timeout=timeout, max_retries=max_retries, expand=expand
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

        La representación impresa de la constancia.

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

        El XML timbrado de la constancia, tal como lo tiene el SAT.

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
        expand: Sequence[str] | None = None,
    ) -> Retention:
        """Enviar por correo

        Manda el PDF y el XML de la constancia a los correos de to (o al que se dio al timbrarla). Dos envíos a la vez de la misma constancia: el segundo contesta email_failed.

        POST /v1/retentions/{id}/send
        https://fiscalisto.com/docs/api/referencia/retenciones/send-retention
        """
        result: Retention = self._client.request(
            "POST", f"/v1/retentions/{_path(id)}/send", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Retention:
        """Cancelar una constancia

        Se cancela en el momento (no espera aceptación). No usa timbres.

        POST /v1/retentions/{id}/cancel
        https://fiscalisto.com/docs/api/referencia/retenciones/cancel-retention
        """
        result: Retention = self._client.request(
            "POST", f"/v1/retentions/{_path(id)}/cancel", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Employee:
        """Crear un empleado

        Un empleado del emisor para sus recibos de nómina: RFC, CURP, NSS, salario diario, salario diario integrado y periodicidad. Lo que no mande tiene el valor usual (contrato indefinido, jornada diurna, quincenal, riesgo clase I). warnings dice lo que el SAT podría rechazar.

        POST /v1/employees
        https://fiscalisto.com/docs/api/referencia/nomina/create-employee
        """
        result: Employee = self._client.request(
            "POST", "/v1/employees", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListEmployeesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Employee]:
        """Listar empleados

        Los empleados del emisor, los más recientes primero.

        GET /v1/employees
        https://fiscalisto.com/docs/api/referencia/nomina/list-employees
        """
        return self._client.list("/v1/employees", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Employee:
        """Ver un empleado

        Un empleado con sus datos y lo que el SAT podría rechazar en warnings.

        GET /v1/employees/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/get-employee
        """
        result: Employee = self._client.request(
            "GET", f"/v1/employees/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Employee:
        """Actualizar un empleado

        Cambia solo los campos que manda; los recibos ya timbrados no cambian.

        POST /v1/employees/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/update-employee
        """
        result: Employee = self._client.request(
            "POST", f"/v1/employees/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar un empleado

        Sus recibos timbrados se quedan.

        DELETE /v1/employees/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/delete-employee
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/employees/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Timbrar un recibo de nómina

        Nómina ordinaria (Nómina 1.2): Fiscalisto calcula sueldo, ISR con subsidio al empleo e IMSS del empleado y el periodo, como la app, y nada más: aguinaldo, PTU, finiquitos, bonos, horas extra, Infonavit o préstamos los calcula su sistema y se timbran con POST /v1/payroll_receipts/external (pedirlos aquí contesta payroll_calculation_unsupported). Revise antes el recibo con POST /v1/payroll_receipts/preview y mande su confirmation_token: así solo se timbra el recibo que revisó (si cambió, 409 payroll_calculation_changed). Queda como factura tipo N (GET /v1/invoices/{id}). El emisor necesita employer_registration.

        POST /v1/payroll_receipts
        https://fiscalisto.com/docs/api/referencia/nomina/create-payroll-receipt
        """
        result: Invoice = self._client.request(
            "POST", "/v1/payroll_receipts", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def preview(
        self,
        params: PreviewPayrollReceiptParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> PayrollReceiptPreview:
        """Calcular un recibo sin timbrar

        El recibo como se timbraría (percepciones, ISR con el subsidio para el empleo, cuotas IMSS y el neto), sin timbrar ni usar timbres, con el confirmation_token que lo timbra tal cual y los avisos de lo que no incluye (un finiquito, valores del año que aún no se cargan).

        POST /v1/payroll_receipts/preview
        https://fiscalisto.com/docs/api/referencia/nomina/preview-payroll-receipt
        """
        result: PayrollReceiptPreview = self._client.request(
            "POST", "/v1/payroll_receipts/preview", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def create_external(
        self,
        params: ExternalPayrollReceiptCreate,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Timbrar un recibo calculado por su sistema

        Para un sistema de nómina que ya calculó el recibo: timbra exactamente sus percepciones (gravado y exento), deducciones, otros pagos, horas extra, incapacidades, separación o jubilación, ordinario (type O) o extraordinario (type E: aguinaldo, PTU, finiquito). Fiscalisto no recalcula ni redondea nada: revisa el XSD, los catálogos del SAT, la Matriz de errores y que sus totales cuadren, y si algo falla responde payroll_invalid con todos los problemas en errors[] (cada uno con su param). Un recibo ordinario por empleado (RFC) y periodo; uno extraordinario por empleado y payroll_run_id. Repetirlo con los mismos importes devuelve el mismo recibo; con otros importes, 409 payroll_receipt_exists (corríjalo con replaces). Queda como factura tipo N.

        POST /v1/payroll_receipts/external
        https://fiscalisto.com/docs/api/referencia/nomina/create-external-payroll-receipt
        """
        result: Invoice = self._client.request(
            "POST", "/v1/payroll_receipts/external", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def preview_external(
        self,
        params: ExternalPayrollReceiptCreate,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ExternalPayrollReceiptPreview:
        """Revisar un recibo calculado por su sistema, sin timbrar

        Las mismas revisiones que al timbrar, sin timbrar ni usar timbres: devuelve el recibo como se timbraría, los avisos y el XML sin sellar (unsigned_xml), con sus importes tal cual. Si algo falla, payroll_invalid con errors[].

        POST /v1/payroll_receipts/external/preview
        https://fiscalisto.com/docs/api/referencia/nomina/preview-external-payroll-receipt
        """
        result: ExternalPayrollReceiptPreview = self._client.request(
            "POST", "/v1/payroll_receipts/external/preview", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result


class PayrollBatchesResource:
    """Nómina: fiscalisto.payroll_batches."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreatePayrollBatchParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> PayrollBatch:
        """Timbrar una nómina completa (lote)

        Toda una corrida de nómina en una solicitud: hasta 1,000 recibos de un emisor, timbrados en segundo plano uno tras otro, sin el límite de timbres por segundo de una sola solicitud. De una de dos formas, nunca mezcladas: receipts (ids de empleado; Fiscalisto calcula cada recibo con el periodo del lote) o external_receipts (los recibos que calculó su sistema, como en POST /v1/payroll_receipts/external, con reference en lugar de metadata). Todo lo que se puede revisar antes se revisa antes: si algo falla, no se timbra ninguno y el error dice qué recibo (param receipts.3.employee). Lo que solo se sabe al timbrar (un periodo ya pagado, el SAT que rechaza un RFC) queda en ese recibo, con su error. Un recibo por empleado y periodo: mandar la corrida otra vez, aun con otra Idempotency-Key, devuelve los recibos que ya tiene. Responde 202; escuche payroll_batch.completed o consulte el lote.

        POST /v1/payroll_batches
        https://fiscalisto.com/docs/api/referencia/nomina/create-payroll-batch
        """
        result: PayrollBatch = self._client.request(
            "POST", "/v1/payroll_batches", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListPayrollBatchesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[PayrollBatch]:
        """Listar lotes de nómina

        Los lotes de nómina, los más recientes primero, con cuántos recibos se timbraron y cuántos no.

        GET /v1/payroll_batches
        https://fiscalisto.com/docs/api/referencia/nomina/list-payroll-batches
        """
        return self._client.list("/v1/payroll_batches", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> PayrollBatch:
        """Ver un lote de nómina

        Con el recibo de cada empleado: timbrado (su factura y UUID) o por qué no (error.code y error.message).

        GET /v1/payroll_batches/{id}
        https://fiscalisto.com/docs/api/referencia/nomina/get-payroll-batch
        """
        result: PayrollBatch = self._client.request(
            "GET", f"/v1/payroll_batches/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> InvoiceBatch:
        """Timbrar un lote de facturas

        Hasta 1,000 facturas de ingreso de un emisor, timbradas en segundo plano. Se revisan todas antes de empezar: si una no pasa, no se timbra ninguna. Responde 202; escuche invoice_batch.completed o consulte el lote.

        POST /v1/invoice_batches
        https://fiscalisto.com/docs/api/referencia/lotes/create-invoice-batch
        """
        result: InvoiceBatch = self._client.request(
            "POST", "/v1/invoice_batches", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListInvoiceBatchesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[InvoiceBatch]:
        """Listar lotes

        Los lotes de facturas, los más recientes primero, con cuántas se timbraron y cuántas fallaron.

        GET /v1/invoice_batches
        https://fiscalisto.com/docs/api/referencia/lotes/list-invoice-batches
        """
        return self._client.list("/v1/invoice_batches", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> InvoiceBatch:
        """Ver un lote

        Con cada factura: su estado, su id y su error.

        GET /v1/invoice_batches/{id}
        https://fiscalisto.com/docs/api/referencia/lotes/get-invoice-batch
        """
        result: InvoiceBatch = self._client.request(
            "GET", f"/v1/invoice_batches/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> TaxIdValidation:
        """Validar los datos fiscales de un cliente

        Antes de timbrar: si el RFC, el nombre, el régimen, el código postal y el uso van a pasar. Sin cif_id revisa lo que se puede revisar sin el SAT (formato, régimen para ese tipo de persona, código postal en el catálogo, uso para el régimen, nombre sin «S.A. de C.V.») y las listas del SAT. Con el idCIF de la constancia lee el registro del SAT y compara nombre, código postal y régimen, como hará el PAC. No usa timbres.

        POST /v1/tax_ids/validate
        https://fiscalisto.com/docs/api/referencia/clientes/validate-tax-id
        """
        result: TaxIdValidation = self._client.request(
            "POST", "/v1/tax_ids/validate", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result


class BranchesResource:
    """Sucursales: fiscalisto.branches."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateBranchParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Branch:
        """Crear una sucursal

        Otro lugar desde donde factura el emisor, con su propio código postal: sus facturas llevan ese CP en LugarExpedicion (y su zona horaria en la Fecha, y el IVA 8 % si es de la franja fronteriza), su dirección en el PDF y, si las da, sus propias series. Un CP que ya tiene otra sucursal contesta branch_exists; el del domicilio fiscal del emisor no es sucursal (es la Matriz). Hasta 200 por emisor.

        POST /v1/branches
        https://fiscalisto.com/docs/api/referencia/sucursales/create-branch
        """
        result: Branch = self._client.request(
            "POST", "/v1/branches", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListBranchesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Branch]:
        """Listar sucursales

        Las sucursales del emisor, las más recientes primero. Las archivadas solo con include_archived=true.

        GET /v1/branches
        https://fiscalisto.com/docs/api/referencia/sucursales/list-branches
        """
        return self._client.list("/v1/branches", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Branch:
        """Ver una sucursal

        Una sucursal del emisor.

        GET /v1/branches/{id}
        https://fiscalisto.com/docs/api/referencia/sucursales/get-branch
        """
        result: Branch = self._client.request(
            "GET", f"/v1/branches/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def update(
        self,
        id: str,
        params: UpdateBranchParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Branch:
        """Actualizar una sucursal

        Cambia solo los campos que manda; una serie en null vuelve a la del emisor. archived: true la archiva (ya no se factura desde ella y sus facturas la siguen nombrando), false la restaura. El código postal de una sucursal que ya facturó no cambia: si se mudó, archívela y cree otra.

        POST /v1/branches/{id}
        https://fiscalisto.com/docs/api/referencia/sucursales/update-branch
        """
        result: Branch = self._client.request(
            "POST", f"/v1/branches/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar una sucursal

        Solo una que nunca facturó; con facturas contesta branch_has_invoices: archívela con archived: true.

        DELETE /v1/branches/{id}
        https://fiscalisto.com/docs/api/referencia/sucursales/delete-branch
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/branches/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Customer:
        """Crear un cliente

        Un cliente del catálogo del emisor, con sus datos fiscales como vienen en su constancia. Un RFC que ya está en el catálogo contesta customer_exists.

        POST /v1/customers
        https://fiscalisto.com/docs/api/referencia/clientes/create-customer
        """
        result: Customer = self._client.request(
            "POST", "/v1/customers", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListCustomersParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Customer]:
        """Listar clientes

        Los clientes del emisor, los más recientes primero. Con tax_id, el de ese RFC.

        GET /v1/customers
        https://fiscalisto.com/docs/api/referencia/clientes/list-customers
        """
        return self._client.list("/v1/customers", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Customer:
        """Ver un cliente

        Un cliente del catálogo.

        GET /v1/customers/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/get-customer
        """
        result: Customer = self._client.request(
            "GET", f"/v1/customers/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Customer:
        """Actualizar un cliente

        Cambia solo los campos que manda. Las facturas ya timbradas no cambian.

        POST /v1/customers/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/update-customer
        """
        result: Customer = self._client.request(
            "POST", f"/v1/customers/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar un cliente

        Lo quita del catálogo. Sus facturas timbradas siguen igual.

        DELETE /v1/customers/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/delete-customer
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/customers/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> CustomerDataRequest:
        """Pedirle sus datos fiscales a un cliente

        Una liga (url) que usted le manda a su cliente: la abre en fiscalisto.com y da su RFC, nombre, régimen, código postal y uso, escritos o leídos de su constancia, revisados antes de aceptarlos. Al mandarlos llega customer_data_request.completed. Un cliente nuevo queda en el catálogo del emisor; si ya existía con otros datos, los nuevos vienen en submission para que usted los aplique.

        POST /v1/customer_data_requests
        https://fiscalisto.com/docs/api/referencia/clientes/create-customer-data-request
        """
        result: CustomerDataRequest = self._client.request(
            "POST", "/v1/customer_data_requests", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListCustomerDataRequestsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[CustomerDataRequest]:
        """Listar solicitudes de datos

        Las ligas para pedir datos fiscales, las más recientes primero, con su estado.

        GET /v1/customer_data_requests
        https://fiscalisto.com/docs/api/referencia/clientes/list-customer-data-requests
        """
        return self._client.list("/v1/customer_data_requests", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> CustomerDataRequest:
        """Ver una solicitud de datos

        Una solicitud de datos: su liga y, si el cliente ya contestó, sus datos fiscales y el cliente que se guardó.

        GET /v1/customer_data_requests/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/get-customer-data-request
        """
        result: CustomerDataRequest = self._client.request(
            "GET", f"/v1/customer_data_requests/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def cancel(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> CustomerDataRequest:
        """Cancelar una solicitud de datos

        La liga deja de funcionar. Una que el cliente ya contestó no se cancela.

        DELETE /v1/customer_data_requests/{id}
        https://fiscalisto.com/docs/api/referencia/clientes/cancel-customer-data-request
        """
        result: CustomerDataRequest = self._client.request(
            "DELETE", f"/v1/customer_data_requests/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Product:
        """Crear un producto

        Un producto o servicio del catálogo del emisor, con su clave del SAT, su unidad, su precio y sus impuestos, para usarlo en items con product.

        POST /v1/products
        https://fiscalisto.com/docs/api/referencia/productos/create-product
        """
        result: Product = self._client.request(
            "POST", "/v1/products", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListProductsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Product]:
        """Listar productos

        Los productos del emisor, los más recientes primero. Filtre por sku o product_key.

        GET /v1/products
        https://fiscalisto.com/docs/api/referencia/productos/list-products
        """
        return self._client.list("/v1/products", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Product:
        """Ver un producto

        Un producto del catálogo.

        GET /v1/products/{id}
        https://fiscalisto.com/docs/api/referencia/productos/get-product
        """
        result: Product = self._client.request(
            "GET", f"/v1/products/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Product:
        """Actualizar un producto

        Cambia solo los campos que manda. Las facturas ya timbradas no cambian.

        POST /v1/products/{id}
        https://fiscalisto.com/docs/api/referencia/productos/update-product
        """
        result: Product = self._client.request(
            "POST", f"/v1/products/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar un producto

        Lo quita del catálogo. Las facturas que lo usaron siguen igual.

        DELETE /v1/products/{id}
        https://fiscalisto.com/docs/api/referencia/productos/delete-product
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/products/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def stock(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> StockLevelList:
        """Ver las existencias de un producto

        Lo que hay del producto en cada almacén del emisor (también en 0), apartado por cotizaciones y disponible.

        GET /v1/products/{id}/stock
        https://fiscalisto.com/docs/api/referencia/inventario/get-product-stock
        """
        result: StockLevelList = self._client.request(
            "GET", f"/v1/products/{_path(id)}/stock", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result


class SatMailboxMessagesResource:
    """Cumplimiento SAT: fiscalisto.sat_mailbox_messages."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def list(
        self,
        params: ListSatMailboxMessagesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[SatMailboxMessage]:
        """Listar avisos del buzón tributario

        Los avisos que trajo del buzón del emisor, los más recientes primero. No usa timbres.

        GET /v1/sat_mailbox_messages
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/list-sat-mailbox-messages
        """
        return self._client.list("/v1/sat_mailbox_messages", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatMailboxMessage:
        """Ver un aviso del buzón tributario

        Un aviso del buzón, con su urgencia y si pide hacer algo.

        GET /v1/sat_mailbox_messages/{id}
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/get-sat-mailbox-message
        """
        result: SatMailboxMessage = self._client.request(
            "GET", f"/v1/sat_mailbox_messages/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result


class SatFindingsResource:
    """Cumplimiento SAT: fiscalisto.sat_findings."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def list(
        self,
        params: ListSatFindingsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatFindingList:
        """Listar hallazgos en los CFDI

        Lo que Fiscalisto encontró en los CFDI del emisor (los suyos y los descargados del SAT) y nadie ha revisado, por tipo y del más grave al más leve: proveedores en la lista 69-B, CFDI cancelados, pagos en efectivo de más de $2,000, errores de CFDI 4.0. Todos en una página. No usa timbres.

        GET /v1/sat_findings
        https://fiscalisto.com/docs/api/referencia/cumplimiento-sat/list-sat-findings
        """
        result: SatFindingList = self._client.request(
            "GET", "/v1/sat_findings", query=params, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result


class WarehousesResource:
    """Inventario: fiscalisto.warehouses."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def list(
        self,
        params: ListWarehousesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> WarehouseList:
        """Listar almacenes

        Los almacenes del emisor, los más recientes primero: el de la Matriz y uno por sucursal se crean solos. Todos en una página.

        GET /v1/warehouses
        https://fiscalisto.com/docs/api/referencia/inventario/list-warehouses
        """
        result: WarehouseList = self._client.request(
            "GET", "/v1/warehouses", query=params, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Warehouse:
        """Ver un almacén

        Un almacén del emisor.

        GET /v1/warehouses/{id}
        https://fiscalisto.com/docs/api/referencia/inventario/get-warehouse
        """
        result: Warehouse = self._client.request(
            "GET", f"/v1/warehouses/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def stock(
        self,
        id: str,
        params: ListWarehouseStockParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[StockLevel]:
        """Ver las existencias de un almacén

        Lo que hay de cada producto en el almacén, el producto más reciente primero. Solo los que tienen existencias, salvo con include_empty=true (todos los que llevan track_stock).

        GET /v1/warehouses/{id}/stock
        https://fiscalisto.com/docs/api/referencia/inventario/list-warehouse-stock
        """
        return self._client.list(f"/v1/warehouses/{_path(id)}/stock", params, timeout=timeout, max_retries=max_retries, expand=expand)


class StockMovementsResource:
    """Inventario: fiscalisto.stock_movements."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def list(
        self,
        params: ListStockMovementsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[StockMovement]:
        """Listar movimientos (kárdex)

        Cada entrada y salida de existencias, la más reciente primero: ventas (de sus facturas), compras, ajustes, traspasos y lo que deshizo una cancelación.

        GET /v1/stock_movements
        https://fiscalisto.com/docs/api/referencia/inventario/list-stock-movements
        """
        return self._client.list("/v1/stock_movements", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> StockMovement:
        """Ver un movimiento

        Una entrada o salida de existencias, con lo que la causó (source).

        GET /v1/stock_movements/{id}
        https://fiscalisto.com/docs/api/referencia/inventario/get-stock-movement
        """
        result: StockMovement = self._client.request(
            "GET", f"/v1/stock_movements/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result


class StockAdjustmentsResource:
    """Inventario: fiscalisto.stock_adjustments."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def create(
        self,
        params: CreateStockAdjustmentParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> StockAdjustment:
        """Ajustar existencias

        Mete o saca existencias de un almacén con su motivo: el inventario inicial, una merma, un robo, un sobrante. Las entradas valen su unit_cost (o el costo promedio), las salidas el costo del emisor (promedio o PEPS). Los productos deben llevar track_stock: true. Se aplica al momento (status applied).

        POST /v1/stock_adjustments
        https://fiscalisto.com/docs/api/referencia/inventario/create-stock-adjustment
        """
        result: StockAdjustment = self._client.request(
            "POST", "/v1/stock_adjustments", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListStockAdjustmentsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[StockAdjustment]:
        """Listar ajustes

        Los ajustes del emisor, los más recientes primero.

        GET /v1/stock_adjustments
        https://fiscalisto.com/docs/api/referencia/inventario/list-stock-adjustments
        """
        return self._client.list("/v1/stock_adjustments", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> StockAdjustment:
        """Ver un ajuste

        Un ajuste de existencias, con sus líneas.

        GET /v1/stock_adjustments/{id}
        https://fiscalisto.com/docs/api/referencia/inventario/get-stock-adjustment
        """
        result: StockAdjustment = self._client.request(
            "GET", f"/v1/stock_adjustments/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> SatCatalogEntryList:
        """Consultar un catálogo del SAT

        product_keys y unit_keys se buscan con q (texto o clave). Los demás vienen completos: tax_systems, cfdi_uses, payment_forms, payment_methods, relationship_types, cancellation_motives, export_types, tax_objects, retention_codes.

        GET /v1/sat_catalogs/{name}
        https://fiscalisto.com/docs/api/referencia/catalogos-del-sat/get-sat-catalog
        """
        result: SatCatalogEntryList = self._client.request(
            "GET", f"/v1/sat_catalogs/{_path(name)}", query=params, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> SatListCheck:
        """Revisar un RFC en las listas del SAT

        Si el RFC aparece en la lista 69-B (operaciones simuladas), 69-B Bis o del art. 69 (no localizados, créditos firmes, exigibles, cancelados, sentencias, CSD sin efectos). Las listas se actualizan cada día con los archivos del SAT. No usa timbres.

        GET /v1/sat_lists/{tax_id}
        https://fiscalisto.com/docs/api/referencia/listas-del-sat/get-sat-list-check
        """
        result: SatListCheck = self._client.request(
            "GET", f"/v1/sat_lists/{_path(tax_id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def check(
        self,
        params: CheckSatListsParams,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatListCheckList:
        """Revisar varios RFC en las listas del SAT

        Hasta 1,000 RFC en una solicitud, en el mismo orden en que los mandó (sin repetidos). No usa timbres.

        POST /v1/sat_lists/check
        https://fiscalisto.com/docs/api/referencia/listas-del-sat/check-sat-lists
        """
        result: SatListCheckList = self._client.request(
            "POST", "/v1/sat_lists/check", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> SatDownload:
        """Pedirle al SAT las facturas de un emisor

        La descarga masiva del SAT: las facturas que el emisor recibió (o emitió) en un periodo de hasta un año, con su XML. Contesta 202 de inmediato; el SAT tarda de minutos a horas y al terminar llega sat_download.completed (o sat_download.failed) y las facturas quedan en GET /v1/sat_invoices. En producción necesita la e.firma guardada del emisor; en pruebas no se le pregunta al SAT: la descarga trae facturas de ejemplo al instante. En producción usa 1 timbre por cada 100 CFDI que trae (al menos 1).

        POST /v1/sat_downloads
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/create-sat-download
        """
        result: SatDownload = self._client.request(
            "POST", "/v1/sat_downloads", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListSatDownloadsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[SatDownload]:
        """Listar descargas del SAT

        Las descargas pedidas al SAT, las más recientes primero, con su estado.

        GET /v1/sat_downloads
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/list-sat-downloads
        """
        return self._client.list("/v1/sat_downloads", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatDownload:
        """Ver una descarga del SAT

        Una descarga del SAT: su periodo, su estado y cuántos CFDI trajo. Al terminar llega sat_download.completed.

        GET /v1/sat_downloads/{id}
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/get-sat-download
        """
        result: SatDownload = self._client.request(
            "GET", f"/v1/sat_downloads/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> ListObject[SatInvoice]:
        """Listar facturas del SAT

        Las facturas que trajeron sus descargas (y las demás que Fiscalisto tenga del emisor), de la más reciente a la más antigua por fecha.

        GET /v1/sat_invoices
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/list-sat-invoices
        """
        return self._client.list("/v1/sat_invoices", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatInvoice:
        """Ver una factura del SAT

        Un CFDI que trajo una descarga del SAT, con sus importes y su estado ante el SAT.

        GET /v1/sat_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/descargas-del-sat/get-sat-invoice
        """
        result: SatInvoice = self._client.request(
            "GET", f"/v1/sat_invoices/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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


class SatDeclarationsResource:
    """Declaraciones del SAT: fiscalisto.sat_declarations."""

    def __init__(self, client: Core) -> None:
        self._client = client

    def refresh(
        self,
        params: RefreshSatDeclarationsParams | None = None,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatDeclarationsRefresh:
        """Consultar las declaraciones de un emisor en el SAT

        Entra al SAT con la e.firma guardada del emisor y trae las declaraciones que presentó: provisionales o definitivas (desde 2022), la anual de persona moral (desde 2019) y las del servicio anterior Declaraciones y pagos, con su PDF, su acuse y sus cifras. La primera consulta trae todos los años que el SAT conserva; las siguientes, este año y el anterior. Solo consulta: nunca presenta ni firma nada. En producción usa 1 timbre por consulta (regresa si el SAT no contesta) y se puede hacer una vez cada 10 minutos por emisor. Contesta en menos de un minuto; si queda algo por bajar (status processing), sigue solo en la siguiente hora sin otro timbre. En pruebas no se le pregunta al SAT: trae declaraciones de ejemplo al instante.

        POST /v1/sat_declarations/refresh
        https://fiscalisto.com/docs/api/referencia/declaraciones-del-sat/refresh-sat-declarations
        """
        result: SatDeclarationsRefresh = self._client.request(
            "POST", "/v1/sat_declarations/refresh", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListSatDeclarationsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[SatDeclaration]:
        """Listar declaraciones del SAT

        Las declaraciones que trajeron sus consultas, del ejercicio y mes más recientes a los más antiguos (la anual antes de los meses de su año). No usa timbres.

        GET /v1/sat_declarations
        https://fiscalisto.com/docs/api/referencia/declaraciones-del-sat/list-sat-declarations
        """
        return self._client.list("/v1/sat_declarations", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def calendar(
        self,
        params: GetSatDeclarationCalendarParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatDeclarationCalendar:
        """Ver el año mes por mes

        Cada mes del ejercicio con sus obligaciones: presentada (con sus declaraciones), falta (venció y no la encontramos) o por presentar, con el día en que vence (el 17 del mes siguiente, o el día hábil siguiente, más los días por el sexto dígito del RFC). Se arma con lo que trajeron sus consultas; no usa timbres.

        GET /v1/sat_declarations/calendar
        https://fiscalisto.com/docs/api/referencia/declaraciones-del-sat/get-sat-declaration-calendar
        """
        result: SatDeclarationCalendar = self._client.request(
            "GET", "/v1/sat_declarations/calendar", query=params, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> SatDeclaration:
        """Ver una declaración del SAT

        Una declaración presentada al SAT, con sus cifras en summary y si ya están su PDF y su acuse.

        GET /v1/sat_declarations/{id}
        https://fiscalisto.com/docs/api/referencia/declaraciones-del-sat/get-sat-declaration
        """
        result: SatDeclaration = self._client.request(
            "GET", f"/v1/sat_declarations/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def pdf(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> bytes:
        """Descargar el PDF de una declaración

        La declaración como la da el SAT. No usa timbres.

        GET /v1/sat_declarations/{id}/pdf
        https://fiscalisto.com/docs/api/referencia/declaraciones-del-sat/get-sat-declaration-pdf
        """
        result: bytes = self._client.request(
            "GET", f"/v1/sat_declarations/{_path(id)}/pdf", result="bytes", timeout=timeout, max_retries=max_retries
        )
        return result

    def receipt(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> bytes:
        """Descargar el acuse de una declaración

        El acuse de recibo, con la línea de captura si hay algo a pagar. No usa timbres.

        GET /v1/sat_declarations/{id}/receipt
        https://fiscalisto.com/docs/api/referencia/declaraciones-del-sat/get-sat-declaration-receipt
        """
        result: bytes = self._client.request(
            "GET", f"/v1/sat_declarations/{_path(id)}/receipt", result="bytes", timeout=timeout, max_retries=max_retries
        )
        return result

    def financial_statements(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> str:
        """Descargar los estados financieros de una anual

        El Excel de estados financieros de la anual de persona moral, como lo da el SAT. No usa timbres.

        GET /v1/sat_declarations/{id}/financial_statements
        https://fiscalisto.com/docs/api/referencia/declaraciones-del-sat/get-sat-declaration-financial-statements
        """
        result: str = self._client.request(
            "GET", f"/v1/sat_declarations/{_path(id)}/financial_statements", result="text", timeout=timeout, max_retries=max_retries
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
        expand: Sequence[str] | None = None,
    ) -> Ticket:
        """Registrar un ticket

        Una venta que su comprador factura él mismo: con el código (code) y el total en el portal del emisor (url, que puede incrustar en su página con fiscalisto.js), da sus datos fiscales y la factura se timbra al momento con los timbres de su cuenta. Lo que nadie factura entra solo en la factura global del periodo. Registrar otra vez el mismo folio con el mismo total contesta el ticket que ya existe (los reintentos son seguros); con otro total, 409. Una venta de varios conceptos (el folio de un hotel) va en lines, cada uno con su clave SAT, descripción, impuestos y monto.

        POST /v1/tickets
        https://fiscalisto.com/docs/api/referencia/autofactura/create-ticket
        """
        result: Ticket = self._client.request(
            "POST", "/v1/tickets", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListTicketsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Ticket]:
        """Listar tickets

        Del más reciente al más antiguo por fecha de venta.

        GET /v1/tickets
        https://fiscalisto.com/docs/api/referencia/autofactura/list-tickets
        """
        return self._client.list("/v1/tickets", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Ticket:
        """Ver un ticket

        Un ticket de autofactura: si ya se facturó (invoice) o entró en la factura global (global_invoice).

        GET /v1/tickets/{id}
        https://fiscalisto.com/docs/api/referencia/autofactura/get-ticket
        """
        result: Ticket = self._client.request(
            "GET", f"/v1/tickets/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def cancel(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Ticket:
        """Cancelar un ticket

        Una venta que no se hizo (devolución, error): ya no se puede facturar ni entra en la factura global. Solo mientras esté pendiente.

        DELETE /v1/tickets/{id}
        https://fiscalisto.com/docs/api/referencia/autofactura/cancel-ticket
        """
        result: Ticket = self._client.request(
            "DELETE", f"/v1/tickets/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> ListObject[JournalEntry]:
        """Listar las pólizas de un mes

        Las pólizas de diario del mes, con sus cuentas y código agrupador del SAT: una por cada CFDI de ingreso o egreso vigente, emitido o recibido (los recibidos con la categoría de su gasto); una por cada pago de un complemento; una por cada recibo de nómina, y una con la depreciación de los activos fijos. Un PUE se registra cobrado o pagado según su forma de pago. En pesos; un CFDI en otra moneda sin tipo de cambio no se registra. No incluye movimientos de banco sin CFDI ni provisiones.

        GET /v1/accounting/journal_entries
        https://fiscalisto.com/docs/api/referencia/contabilidad/list-journal-entries
        """
        return self._client.list("/v1/accounting/journal_entries", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def trial_balance(
        self,
        params: GetTrialBalanceParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> TrialBalance:
        """Ver la balanza de comprobación

        Saldo inicial, cargos, abonos y saldo final de cada cuenta en el mes. Los saldos iniciales se acumulan desde el primer CFDI, o desde los saldos iniciales capturados en la app (las de resultados, desde enero), y los resultados de cada año anterior se cierran a capital.

        GET /v1/accounting/trial_balance
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-trial-balance
        """
        result: TrialBalance = self._client.request(
            "GET", "/v1/accounting/trial_balance", query=params, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def financial_statements(
        self,
        params: GetFinancialStatementsParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> FinancialStatements:
        """Ver los estados financieros

        El estado de resultados (del mes y del año hasta ese mes) y el balance general al cierre del mes, leídos de la misma balanza, así que siempre suman las mismas pólizas.

        GET /v1/accounting/financial_statements
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-financial-statements
        """
        result: FinancialStatements = self._client.request(
            "GET", "/v1/accounting/financial_statements", query=params, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def cross_checks(
        self,
        params: GetCrossChecksParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> CrossChecks:
        """Cruzar lo declarado con lo facturado

        Cada mes ya vencido del año: el IVA trasladado, acreditable y retenido y los ingresos para ISR que el emisor declaró (de GET /v1/sat_declarations, después de POST /v1/sat_declarations/refresh) contra lo que dicen sus CFDI. Hasta $2 de diferencia es redondeo (las declaraciones van en pesos enteros). Una cifra que la declaración no trae en un renglón reconocible es unreadable con declared null, nunca 0. También el IVA a favor y el régimen con que factura. Gratis: no consulta al SAT.

        GET /v1/accounting/cross_checks
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-cross-checks
        """
        result: CrossChecks = self._client.request(
            "GET", "/v1/accounting/cross_checks", query=params, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def cross_check_cfdi(
        self,
        params: GetCrossCheckCfdiParams,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> CrossCheckCfdi:
        """Ver los CFDI de una cifra del cruce

        Los CFDI que forman lo facturado (invoiced) de una cifra del cruce de un mes, con los mismos cálculos de Impuestos: cada factura PUE o nota de crédito en su mes y cada factura PPD por lo que se pagó en el mes, con lo que aporta. La suma de cfdi más adjustment es invoiced. Sirve para ver por qué una cifra differs. Gratis: no consulta al SAT.

        GET /v1/accounting/cross_checks/cfdi
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-cross-check-cfdi
        """
        result: CrossCheckCfdi = self._client.request(
            "GET", "/v1/accounting/cross_checks/cfdi", query=params, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def accounts(
        self,
        params: ListLedgerAccountsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> LedgerAccountList:
        """Ver el catálogo de cuentas

        Las cuentas que usan las pólizas, con su código agrupador del SAT.

        GET /v1/accounting/accounts
        https://fiscalisto.com/docs/api/referencia/contabilidad/list-ledger-accounts
        """
        result: LedgerAccountList = self._client.request(
            "GET", "/v1/accounting/accounts", query=params, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Diot:
        """Ver la DIOT de un mes

        Lo efectivamente pagado a cada proveedor en el mes (facturas PUE y complementos de pago recibidos), con sus notas de crédito como devoluciones, por tipo de operación. Sale de las facturas recibidas que trajo de las descargas del SAT. Desde enero de 2025 (formato 2025).

        GET /v1/accounting/diot
        https://fiscalisto.com/docs/api/referencia/contabilidad/get-diot
        """
        result: Diot = self._client.request(
            "GET", "/v1/accounting/diot", query=params, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> StoreConnection:
        """Conectar una tienda

        Shopify: con el dominio y las llaves de la app de la tienda (Dev Dashboard, permisos read_orders y write_orders) registra los webhooks y queda active. Mercado Libre: queda pending hasta que el vendedor autorice en authorize_url. Desde entonces cada pedido pagado es un ticket (folio SHOP-1001 o ML-…), que su comprador factura en el portal o entra en la factura global; un pedido cancelado o reembolsado completo cancela su ticket.

        POST /v1/store_connections
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/create-store-connection
        """
        result: StoreConnection = self._client.request(
            "POST", "/v1/store_connections", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListStoreConnectionsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[StoreConnection]:
        """Listar tiendas

        Las más recientes primero, también las desconectadas.

        GET /v1/store_connections
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/list-store-connections
        """
        return self._client.list("/v1/store_connections", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> StoreConnection:
        """Ver una tienda

        Una tienda conectada (Shopify, Mercado Libre o WooCommerce), su estado y lo último que importó.

        GET /v1/store_connections/{id}
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/get-store-connection
        """
        result: StoreConnection = self._client.request(
            "GET", f"/v1/store_connections/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> StoreConnection:
        """Cambiar cómo se vuelven tickets sus pedidos

        Cuenta para los pedidos que lleguen; los tickets ya hechos no cambian.

        POST /v1/store_connections/{id}
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/update-store-connection
        """
        result: StoreConnection = self._client.request(
            "POST", f"/v1/store_connections/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> StoreConnection:
        """Desconectar una tienda

        Sus pedidos dejan de llegar y se borran sus llaves y webhooks. Los tickets que ya hizo siguen.

        DELETE /v1/store_connections/{id}
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/delete-store-connection
        """
        result: StoreConnection = self._client.request(
            "DELETE", f"/v1/store_connections/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> StoreImport:
        """Traer pedidos pagados

        Los pedidos pagados desde una fecha (hasta 31 días, 200 a la vez) que no llegaron por webhook: la tienda se conectó después o estuvo caída. Un pedido que ya es ticket no se repite.

        POST /v1/store_connections/{id}/import_orders
        https://fiscalisto.com/docs/api/referencia/tiendas-en-linea/import-store-orders
        """
        result: StoreImport = self._client.request(
            "POST", f"/v1/store_connections/{_path(id)}/import_orders", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> RecurringInvoice:
        """Crear una factura recurrente

        Una factura que el emisor timbra solo en cada fecha (cada interval meses en day_of_month, o cada interval semanas o días), a la hora que elija, con los timbres de su cuenta, y la manda al cliente si send_email. Cada una es una factura normal (invoice.stamped, con recurring_invoice) y nunca se timbra dos veces el mismo periodo. invoice es el cuerpo de POST /v1/invoices: se revisa ahora, con las mismas reglas.

        POST /v1/recurring_invoices
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/create-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "POST", "/v1/recurring_invoices", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListRecurringInvoicesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[RecurringInvoice]:
        """Listar facturas recurrentes

        Las más recientes primero.

        GET /v1/recurring_invoices
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/list-recurring-invoices
        """
        return self._client.list("/v1/recurring_invoices", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> RecurringInvoice:
        """Ver una factura recurrente

        Una factura recurrente: su calendario, la próxima fecha, la última factura que timbró y, si falló, por qué en last_error.

        GET /v1/recurring_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/get-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "GET", f"/v1/recurring_invoices/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> RecurringInvoice:
        """Cambiar o pausar una factura recurrente

        Solo lo que mande cambia. invoice reemplaza la factura completa desde la siguiente vez. active: false la pausa; active: true la reanuda desde hoy, sin timbrar las fechas que pasaron en pausa. schedule.start_date mueve la siguiente fecha.

        POST /v1/recurring_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/update-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "POST", f"/v1/recurring_invoices/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar una factura recurrente

        Ya no timbra más; las facturas que timbró se quedan.

        DELETE /v1/recurring_invoices/{id}
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/delete-recurring-invoice
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/recurring_invoices/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def skip(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> RecurringInvoice:
        """Saltar la siguiente factura

        La siguiente fecha pasa a la que sigue, sin timbrar nada.

        POST /v1/recurring_invoices/{id}/skip
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/skip-recurring-invoice
        """
        result: RecurringInvoice = self._client.request(
            "POST", f"/v1/recurring_invoices/{_path(id)}/skip", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def run(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Timbrar ahora la que toca

        Timbra el periodo que ya toca (next_invoice_on es hoy o antes) sin esperar su hora. Si no toca aún, 409 recurring_not_due. Si la hora llega mientras tanto, no se timbra dos veces: es el mismo periodo.

        POST /v1/recurring_invoices/{id}/run
        https://fiscalisto.com/docs/api/referencia/facturas-recurrentes/run-recurring-invoice
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/recurring_invoices/{_path(id)}/run", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Quote:
        """Crear una cotización

        Una cotización en borrador, con los conceptos y las condiciones de pago de una factura (se revisan con las mismas reglas, así que siempre se puede facturar). customer es un cliente de su catálogo, uno con sus datos fiscales (se agrega a sus clientes) o solo name y email si aún no los tiene. Se manda con POST /v1/quotes/{id}/send.

        POST /v1/quotes
        https://fiscalisto.com/docs/api/referencia/cotizaciones/create-quote
        """
        result: Quote = self._client.request(
            "POST", "/v1/quotes", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListQuotesParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[Quote]:
        """Listar cotizaciones

        Las más recientes primero, cada una en su última versión.

        GET /v1/quotes
        https://fiscalisto.com/docs/api/referencia/cotizaciones/list-quotes
        """
        return self._client.list("/v1/quotes", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Quote:
        """Ver una cotización

        Su última versión.

        GET /v1/quotes/{id}
        https://fiscalisto.com/docs/api/referencia/cotizaciones/get-quote
        """
        result: Quote = self._client.request(
            "GET", f"/v1/quotes/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Quote:
        """Cambiar una cotización

        Solo lo que mande cambia. Un borrador cambia ahí mismo; una que ya se envió se vuelve una versión nueva en borrador (mismo número, version + 1) que el cliente ve al mandarla; mientras, su liga muestra la anterior. Una aceptada, rechazada o facturada ya no cambia.

        POST /v1/quotes/{id}
        https://fiscalisto.com/docs/api/referencia/cotizaciones/update-quote
        """
        result: Quote = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar una cotización

        Solo una que nunca se envió; si no, 400 quote_not_draft.

        DELETE /v1/quotes/{id}
        https://fiscalisto.com/docs/api/referencia/cotizaciones/delete-quote
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/quotes/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> Quote:
        """Mandar una cotización

        La manda por correo con su PDF y la liga donde el cliente la ve, la acepta, pide cambios o la rechaza. Con send_email: false solo se marca enviada y contesta url, para que usted la mande por WhatsApp o su propio correo.

        POST /v1/quotes/{id}/send
        https://fiscalisto.com/docs/api/referencia/cotizaciones/send-quote
        """
        result: Quote = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}/send", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def accept(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Quote:
        """Marcar aceptada

        El cliente le dijo que sí por teléfono, en persona… Llega quote.accepted. No timbra: para eso, POST /v1/quotes/{id}/invoice.

        POST /v1/quotes/{id}/accept
        https://fiscalisto.com/docs/api/referencia/cotizaciones/accept-quote
        """
        result: Quote = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}/accept", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def invoice(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Invoice:
        """Facturar una cotización

        Timbra la factura con los conceptos de la cotización y los datos fiscales del cliente, y la deja facturada (invoice). Si no estaba aceptada, la marca aceptada. Una en otra moneda va al tipo de cambio de hoy. Sin los datos fiscales del cliente, 400 quote_customer_missing; rechazada o vencida, 400 quote_not_invoiceable. Si ya se facturó, contesta esa factura.

        POST /v1/quotes/{id}/invoice
        https://fiscalisto.com/docs/api/referencia/cotizaciones/invoice-quote
        """
        result: Invoice = self._client.request(
            "POST", f"/v1/quotes/{_path(id)}/invoice", idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> WebhookEndpoint:
        """Crear un webhook

        La respuesta trae el secreto de firma (secret) una sola vez.

        POST /v1/webhook_endpoints
        https://fiscalisto.com/docs/api/referencia/webhooks/create-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "POST", "/v1/webhook_endpoints", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def list(
        self,
        params: ListWebhookEndpointsParams | None = None,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> ListObject[WebhookEndpoint]:
        """Listar webhooks

        Los webhooks del modo de la llave. Hasta 16 por modo.

        GET /v1/webhook_endpoints
        https://fiscalisto.com/docs/api/referencia/webhooks/list-webhook-endpoints
        """
        return self._client.list("/v1/webhook_endpoints", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> WebhookEndpoint:
        """Ver un webhook

        Un webhook: su dirección, los eventos que recibe y si sus entregas fallan. El secreto solo viene al crearlo.

        GET /v1/webhook_endpoints/{id}
        https://fiscalisto.com/docs/api/referencia/webhooks/get-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "GET", f"/v1/webhook_endpoints/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> WebhookEndpoint:
        """Actualizar un webhook

        Cambia su dirección, sus eventos, su descripción o su versión de la API; con disabled: false vuelve a encender uno que se apagó.

        POST /v1/webhook_endpoints/{id}
        https://fiscalisto.com/docs/api/referencia/webhooks/update-webhook-endpoint
        """
        result: WebhookEndpoint = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
        )
        return result

    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Deleted:
        """Borrar un webhook

        Deja de mandar eventos a esa dirección. Los eventos siguen en GET /v1/events.

        DELETE /v1/webhook_endpoints/{id}
        https://fiscalisto.com/docs/api/referencia/webhooks/delete-webhook-endpoint
        """
        result: Deleted = self._client.request(
            "DELETE", f"/v1/webhook_endpoints/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> WebhookEndpoint:
        """Cambiar el secreto

        Un secreto nuevo, que la respuesta trae una sola vez. El anterior sigue firmando (una segunda firma en webhook-signature) el tiempo que elija, 24 horas por omisión, para que cambie su servidor sin rechazar eventos. Si se filtró, mande previous_secret_expires_in: 0.

        POST /v1/webhook_endpoints/{id}/roll_secret
        https://fiscalisto.com/docs/api/referencia/webhooks/roll-webhook-secret
        """
        result: WebhookEndpoint = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}/roll_secret", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> WebhookTest:
        """Mandar un evento de prueba

        Manda ahora, una sola vez y sin reintentos, un evento del tipo que elija con un objeto de ejemplo (sus id no existen), firmado como los reales, aunque el webhook no escuche ese tipo. La respuesta trae lo que contestó su servidor. El evento no sale en GET /v1/events, pero sí en las entregas del webhook.

        POST /v1/webhook_endpoints/{id}/test
        https://fiscalisto.com/docs/api/referencia/webhooks/test-webhook-endpoint
        """
        result: WebhookTest = self._client.request(
            "POST", f"/v1/webhook_endpoints/{_path(id)}/test", body=params, idempotent=True, idempotency_key=idempotency_key, timeout=timeout, max_retries=max_retries, expand=expand
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
        expand: Sequence[str] | None = None,
    ) -> ListObject[Event]:
        """Listar eventos

        Los de los últimos 30 días, los más recientes primero.

        GET /v1/events
        https://fiscalisto.com/docs/api/referencia/eventos/list-events
        """
        return self._client.list("/v1/events", params, timeout=timeout, max_retries=max_retries, expand=expand)

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        expand: Sequence[str] | None = None,
    ) -> Event:
        """Ver un evento

        Un evento de los últimos 30 días, con el objeto como estaba cuando pasó.

        GET /v1/events/{id}
        https://fiscalisto.com/docs/api/referencia/eventos/get-event
        """
        result: Event = self._client.request(
            "GET", f"/v1/events/{_path(id)}", timeout=timeout, max_retries=max_retries, expand=expand
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
    def test_clocks(self) -> TestClocksResource:
        """Entornos de prueba."""
        return TestClocksResource(self)

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
    def payroll_batches(self) -> PayrollBatchesResource:
        """Nómina."""
        return PayrollBatchesResource(self)

    @cached_property
    def invoice_batches(self) -> InvoiceBatchesResource:
        """Lotes."""
        return InvoiceBatchesResource(self)

    @cached_property
    def tax_ids(self) -> TaxIdsResource:
        """Clientes."""
        return TaxIdsResource(self)

    @cached_property
    def branches(self) -> BranchesResource:
        """Sucursales."""
        return BranchesResource(self)

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
    def sat_mailbox_messages(self) -> SatMailboxMessagesResource:
        """Cumplimiento SAT."""
        return SatMailboxMessagesResource(self)

    @cached_property
    def sat_findings(self) -> SatFindingsResource:
        """Cumplimiento SAT."""
        return SatFindingsResource(self)

    @cached_property
    def warehouses(self) -> WarehousesResource:
        """Inventario."""
        return WarehousesResource(self)

    @cached_property
    def stock_movements(self) -> StockMovementsResource:
        """Inventario."""
        return StockMovementsResource(self)

    @cached_property
    def stock_adjustments(self) -> StockAdjustmentsResource:
        """Inventario."""
        return StockAdjustmentsResource(self)

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
    def sat_declarations(self) -> SatDeclarationsResource:
        """Declaraciones del SAT."""
        return SatDeclarationsResource(self)

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
