# Generado por `bun run openapi` desde la especificación OpenAPI de la API: no lo edite.
"""Los tipos de la API: cada objeto y cada cuerpo, como diccionarios (TypedDict)."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Literal, TypedDict, Union

# Only type checkers read NotRequired before 3.11: the annotations are never evaluated.
if sys.version_info >= (3, 11):
    from typing import NotRequired
elif TYPE_CHECKING:  # pragma: no cover
    from typing_extensions import NotRequired

__all__ = [
    "Account",
    "AccountKey",
    "Advance",
    "AdvanceCustomer",
    "AdvanceList",
    "ApiError",
    "ApiErrorError",
    "ApplyAdvanceParams",
    "ApplyAdvanceParamsRemainder",
    "Balance",
    "BalanceAutoRecharge",
    "BalanceLowEvent",
    "BalancePacksItem",
    "CancelInvoiceParams",
    "CancelRetentionParams",
    "CheckSatListsParams",
    "CreateAdvanceParams",
    "CreateAdvanceParamsCustomer",
    "CreateAdvanceParamsCustomerForeign",
    "CreateCreditNoteParams",
    "CreateCustomerDataRequestParams",
    "CreateCustomerParams",
    "CreateCustomerParamsForeign",
    "CreateEmployeeParams",
    "CreateInvoiceBatchParams",
    "CreateInvoiceBatchParamsInvoicesItem",
    "CreateIssuerOnboardingLinkParams",
    "CreateIssuerParams",
    "CreatePaymentParams",
    "CreatePaymentParamsDocumentsItem",
    "CreatePayrollReceiptParams",
    "CreatePayrollReceiptParamsPeriod",
    "CreateProductParams",
    "CreateRetentionParams",
    "CreateRetentionParamsDividends",
    "CreateRetentionParamsForeignPayment",
    "CreateRetentionParamsInterest",
    "CreateRetentionParamsPeriod",
    "CreateRetentionParamsRecipient",
    "CreateRetentionParamsTaxesItem",
    "CreateRetentionParamsTotals",
    "CreateSatDownloadParams",
    "CreateTicketParams",
    "CreateWebhookEndpointParams",
    "Customer",
    "CustomerDataRequest",
    "CustomerDataRequestCompletedEvent",
    "CustomerDataRequestList",
    "CustomerDataRequestSubmission",
    "CustomerForeign",
    "CustomerList",
    "Deleted",
    "Employee",
    "EmployeeList",
    "Event",
    "EventList",
    "EventType",
    "GetInvoiceParams",
    "GetInvoicePdfParams",
    "GetInvoiceXmlParams",
    "GetRetentionParams",
    "GetRetentionPdfParams",
    "GetRetentionXmlParams",
    "GetSatCatalogParams",
    "Invoice",
    "InvoiceAdvanceApplication",
    "InvoiceBatch",
    "InvoiceBatchCompletedEvent",
    "InvoiceBatchInvoicesItem",
    "InvoiceBatchList",
    "InvoiceCanceledEvent",
    "InvoiceCancellation",
    "InvoiceCancellationPendingEvent",
    "InvoiceCancellationRejectedEvent",
    "InvoiceCreate",
    "InvoiceCreateAddenda",
    "InvoiceCreateCartaPorte",
    "InvoiceCreateCartaPorteAir",
    "InvoiceCreateCartaPorteAirShipper",
    "InvoiceCreateCartaPorteAirShipperForeign",
    "InvoiceCreateCartaPorteDestinationsItem",
    "InvoiceCreateCartaPorteDestinationsItemAddress",
    "InvoiceCreateCartaPorteDestinationsItemForeign",
    "InvoiceCreateCartaPorteDestinationsItemStation",
    "InvoiceCreateCartaPorteDriversItem",
    "InvoiceCreateCartaPorteDriversItemForeign",
    "InvoiceCreateCartaPorteFiguresItem",
    "InvoiceCreateCartaPorteFiguresItemAddress",
    "InvoiceCreateCartaPorteFiguresItemForeign",
    "InvoiceCreateCartaPorteGoodsItem",
    "InvoiceCreateCartaPorteGoodsItemCofepris",
    "InvoiceCreateCartaPorteGoodsItemCustomsDocsItem",
    "InvoiceCreateCartaPorteGoodsItemDetail",
    "InvoiceCreateCartaPorteGoodsItemGuidesItem",
    "InvoiceCreateCartaPorteGoodsItemHazmat",
    "InvoiceCreateCartaPorteGoodsItemMaterial",
    "InvoiceCreateCartaPorteGoodsItemQuantitiesItem",
    "InvoiceCreateCartaPorteInternational",
    "InvoiceCreateCartaPorteIstmo",
    "InvoiceCreateCartaPorteOrigin",
    "InvoiceCreateCartaPorteOriginAddress",
    "InvoiceCreateCartaPorteOriginForeign",
    "InvoiceCreateCartaPorteOriginStation",
    "InvoiceCreateCartaPorteRail",
    "InvoiceCreateCartaPorteRailCarsItem",
    "InvoiceCreateCartaPorteRailCarsItemContainersItem",
    "InvoiceCreateCartaPorteRailRightsItem",
    "InvoiceCreateCartaPorteSea",
    "InvoiceCreateCartaPorteSeaContainersItem",
    "InvoiceCreateCartaPorteSeaContainersItemTrailersItem",
    "InvoiceCreateCartaPorteVehicle",
    "InvoiceCreateCartaPorteVehicleTrailersItem",
    "InvoiceCreateComercioExterior",
    "InvoiceCreateComercioExteriorGoodsItem",
    "InvoiceCreateComercioExteriorIssuerAddress",
    "InvoiceCreateComercioExteriorOwnersItem",
    "InvoiceCreateComercioExteriorReceiverAddress",
    "InvoiceCreateComercioExteriorRecipient",
    "InvoiceCreateComercioExteriorRecipientAddress",
    "InvoiceCreateCustomer",
    "InvoiceCreateCustomerForeign",
    "InvoiceCreateDonation",
    "InvoiceCreateGlobal",
    "InvoiceCreateIne",
    "InvoiceCreateIneEntitiesItem",
    "InvoiceCreateItemsItem",
    "InvoiceCreateItemsItemIedu",
    "InvoiceCreateItemsItemThirdParty",
    "InvoiceCreateItemsItemUsedVehicle",
    "InvoiceCreateItemsItemUsedVehicleCustomsItem",
    "InvoiceCreateLeyendasItem",
    "InvoiceCreateLocalTaxesItem",
    "InvoiceCreateRelated",
    "InvoiceCustomer",
    "InvoiceEmail",
    "InvoiceError",
    "InvoiceFailedEvent",
    "InvoiceItem",
    "InvoiceList",
    "InvoicePayment",
    "InvoicePaymentDocumentsItem",
    "InvoicePayroll",
    "InvoicePayrollDeductionsItem",
    "InvoicePayrollEmployee",
    "InvoicePayrollEmployer",
    "InvoicePayrollOtherPaymentsItem",
    "InvoicePayrollPerceptionsItem",
    "InvoicePayrollPeriod",
    "InvoiceStampedEvent",
    "InvoiceSubstitutes",
    "InvoiceTaxes",
    "Issuer",
    "IssuerCertificate",
    "IssuerList",
    "IssuerOnboardingLink",
    "IssuerReadyEvent",
    "IssuerSatDownloads",
    "ListAdvancesParams",
    "ListCustomerDataRequestsParams",
    "ListCustomersParams",
    "ListEmployeesParams",
    "ListEventsParams",
    "ListInvoiceBatchesParams",
    "ListInvoicesParams",
    "ListIssuersParams",
    "ListProductsParams",
    "ListRetentionsParams",
    "ListSatDownloadsParams",
    "ListSatInvoicesParams",
    "ListTicketsParams",
    "ListWebhookEndpointsParams",
    "PayrollReceiptPreview",
    "PayrollReceiptPreviewDeductionsItem",
    "PayrollReceiptPreviewIsr",
    "PayrollReceiptPreviewIsrAdjustment",
    "PayrollReceiptPreviewOtherPaymentsItem",
    "PayrollReceiptPreviewPerceptionsItem",
    "PayrollReceiptPreviewPeriod",
    "PayrollReceiptPreviewTotals",
    "PreviewPayrollReceiptParams",
    "PreviewPayrollReceiptParamsPeriod",
    "Product",
    "ProductList",
    "ResetTestDataParams",
    "Retention",
    "RetentionCanceledEvent",
    "RetentionCancellation",
    "RetentionEmail",
    "RetentionError",
    "RetentionFailedEvent",
    "RetentionList",
    "RetentionPeriod",
    "RetentionRecipient",
    "RetentionStampedEvent",
    "RetentionTaxesItem",
    "RetentionTotals",
    "RollWebhookSecretParams",
    "SatCatalogEntry",
    "SatCatalogEntryList",
    "SatDownload",
    "SatDownloadCompletedEvent",
    "SatDownloadFailedEvent",
    "SatDownloadList",
    "SatInvoice",
    "SatInvoiceIssuedBy",
    "SatInvoiceIssuedTo",
    "SatInvoiceList",
    "SatInvoiceTaxes",
    "SatListCheck",
    "SatListCheckList",
    "SatListCheckListsItem",
    "SelfInvoicing",
    "SendInvoiceParams",
    "SendRetentionParams",
    "SignEfirmaParams",
    "TaxIdValidation",
    "TaxIdValidationErrorsItem",
    "TaxIdValidationSatRecord",
    "TaxIdValidationWarningsItem",
    "TestDataReset",
    "TestWebhookEndpointParams",
    "Ticket",
    "TicketCustomer",
    "TicketIncludedInGlobalEvent",
    "TicketInvoicedEvent",
    "TicketList",
    "UpdateCustomerParams",
    "UpdateCustomerParamsForeign",
    "UpdateEmployeeParams",
    "UpdateIssuerParams",
    "UpdateProductParams",
    "UpdateSelfInvoicingParams",
    "UpdateWebhookEndpointParams",
    "UploadCertificateParams",
    "ValidateTaxIdParams",
    "WebhookEndpoint",
    "WebhookEndpointList",
    "WebhookTest",
    "WebhookTestDelivery",
]


class AccountKey(TypedDict):
    """La llave con que se hizo la solicitud: id, nombre y emisores a los que se limita."""
    id: str
    """Id de la llave."""
    name: str
    """Nombre de la llave."""
    issuers: list[str] | None
    """Emisores a los que se limita la llave; null si puede usar todos."""
    read_only: bool
    """true si la llave solo consulta (key_read_only en lo demás)."""
    expires_at: str | None
    """Cuándo deja de funcionar: la vigencia elegida al crearla, o el fin del traslape al cambiarla. null si no vence."""


class Account(TypedDict):
    """La cuenta API de la llave que hizo la solicitud."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["account"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    name: str
    """El nombre de la cuenta API."""
    key: AccountKey
    """La llave con que se hizo la solicitud: id, nombre y emisores a los que se limita."""


class BalanceAutoRecharge(TypedDict):
    timbres: int
    """Timbres del paquete que se compra."""
    at: int
    """Se compra con esta cantidad o menos."""
    max_per_month: int
    """Como máximo tantas compras al mes."""


class BalancePacksItem(TypedDict):
    timbres: int
    """Timbres del paquete."""
    remaining: int
    """Los que le quedan."""
    purchased_at: str | None
    """Cuándo se compró."""
    expires_at: str | None
    """Cuándo vencen; null si no vencen."""


class Balance(TypedDict):
    """Timbres de producción de la cuenta, por paquete, el que vence antes primero."""
    object: Literal["balance"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    available: int
    """Timbres disponibles en total."""
    unlimited: bool
    """true si la cuenta timbra sin usar timbres."""
    low_balance_at: int
    """Con esta cantidad o menos llega balance.low (y otra vez al acabarse). Se elige en Desarrolladores › Timbres."""
    auto_recharge: BalanceAutoRecharge | None
    """La recarga automática con la tarjeta guardada, o null si está apagada."""
    packs: list[BalancePacksItem]
    """Los paquetes con timbres, el que vence antes primero (en ese orden se usan)."""


class IssuerCertificate(TypedDict):
    serial_number: str | None
    """Número de serie (NoCertificado)."""
    expires_at: str | None
    """Cuándo vence."""


class IssuerSatDownloads(TypedDict):
    """Si puede pedirle al SAT sus facturas (POST /v1/sat_downloads): available es true en pruebas, y en producción mientras su e.firma guardada esté vigente (efirma_expires_at)."""
    available: bool
    """true si puede pedir descargas al SAT ahora: siempre en pruebas; en producción con su e.firma guardada y vigente."""
    efirma_expires_at: str | None
    """Cuándo vence la e.firma guardada para las descargas, o null si no hay una."""


class Issuer(TypedDict):
    """Un emisor: un RFC que timbra desde su cuenta API."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["issuer"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str | None
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str | None
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    status: Literal["active", "needs_certificate", "certificate_expired", "needs_efirma", "archived"]
    """active: puede timbrar. needs_certificate: falta su CSD. needs_efirma: falta firmar una vez el contrato con el PAC con su e.firma (solo en producción). certificate_expired: su CSD venció. archived: archivado."""
    requirement: str | None
    """Qué le falta al emisor para timbrar, y cómo dárselo."""
    certificate: IssuerCertificate | None
    """El sello digital (CSD) cargado: número de serie y vencimiento."""
    sat_downloads: IssuerSatDownloads
    """Si puede pedirle al SAT sus facturas (POST /v1/sat_downloads): available es true en pruebas, y en producción mientras su e.firma guardada esté vigente (efirma_expires_at)."""
    employer_registration: str | None
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: str | None
    """CURP, 18 caracteres."""
    stamps_as: str
    """RFC con el que se timbra: el del emisor en producción y el de pruebas del SAT (EKU9003173C9) en pruebas."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    archived_at: str | None
    """Cuándo se archivó (ya no timbra), o null."""
    metadata: dict[str, str]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class InvoiceItem(TypedDict):
    """Un concepto, con los mismos campos con que se mandó."""
    pass


class InvoiceCustomer(TypedDict):
    """Cliente (Receptor): el id de uno de su catálogo (cus_…) o sus datos en un objeto."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: NotRequired[str]
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    foreign: NotRequired[dict[str, Any]]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""


class InvoiceTaxes(TypedDict):
    iva: float | None
    """IVA trasladado."""
    ieps: float | None
    """IEPS trasladado."""
    iva_withheld: float | None
    """IVA retenido."""
    isr_withheld: float | None
    """ISR retenido."""
    local_transferred: float | None
    """Impuestos locales trasladados."""
    local_withheld: float | None
    """Impuestos locales retenidos."""


class InvoicePaymentDocumentsItem(TypedDict):
    uuid: str
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    series: str | None
    """Serie de la factura pagada."""
    folio: str | None
    """Folio de la factura pagada."""
    currency: str
    """Moneda de la factura pagada (MonedaDR)."""
    partiality: int
    """Número de parcialidad (NumParcialidad)."""
    previous_balance: float
    """Saldo anterior de la factura (ImpSaldoAnt)."""
    amount: float
    """Lo que se paga de esa factura (ImpPagado), en la moneda de la factura."""
    remaining: float
    """Saldo insoluto después de este pago (ImpSaldoInsoluto)."""


class InvoicePayment(TypedDict):
    date: str | None
    """Fecha del pago (FechaPago)."""
    payment_form: str | None
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    currency: str
    """Moneda del pago (MonedaP)."""
    exchange_rate: float | None
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    amount: float
    """Monto del pago (Monto)."""
    operation_number: str | None
    """Número de operación del pago (NumOperacion), como el rastreo SPEI."""
    documents: list[InvoicePaymentDocumentsItem]
    """Las facturas que paga (DoctoRelacionado)."""


class InvoicePayrollPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: str
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class InvoicePayrollEmployer(TypedDict):
    """El patrón (Emisor del complemento): registro patronal y CURP si es persona física."""
    employer_registration: str | None
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: str | None
    """CURP, 18 caracteres."""


class InvoicePayrollEmployee(TypedDict):
    """El empleado (emp_…)."""
    id: str | None
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    number: str
    """Número de empleado (NumEmpleado)."""
    curp: str
    """CURP, 18 caracteres."""
    social_security_number: str | None
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    start_date: str
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    contract_type: str
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    unionized: bool
    """true si es sindicalizado (Sindicalizado)."""
    workday_type: str
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    regime_type: str
    """Tipo de régimen (TipoRegimen): 02 sueldos y salarios."""
    department: NotRequired[str | None]
    """Departamento (Departamento)."""
    position: NotRequired[str | None]
    """Puesto (Puesto)."""
    risk_class: str | None
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    contribution_base_salary: float | None
    """Salario base de cotización (SalarioBaseCotApor)."""
    integrated_daily_salary: float | None
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    state: str
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""


class InvoicePayrollPerceptionsItem(TypedDict):
    type: str
    """Tipo de percepción (TipoPercepcion), c_TipoPercepcion: 001 sueldos…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    taxed: float
    """Importe gravado (ImporteGravado)."""
    exempt: float
    """Importe exento (ImporteExento)."""


class InvoicePayrollDeductionsItem(TypedDict):
    type: str
    """Tipo de deducción (TipoDeduccion), c_TipoDeduccion: 001 IMSS, 002 ISR…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe (Importe)."""


class InvoicePayrollOtherPaymentsItem(TypedDict):
    type: str
    """Tipo de otro pago (TipoOtroPago), c_TipoOtroPago: 002 subsidio para el empleo."""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe pagado (Importe)."""
    subsidy_caused: NotRequired[float]
    """Subsidio causado (SubsidioCausado)."""
    subsidy_applied: NotRequired[float]
    """Del subsidio causado, el ISR que evitó (no va en el XML)."""


class InvoicePayroll(TypedDict):
    """Solo en un recibo de nómina (type N)."""
    periodicity: str
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    period: InvoicePayrollPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    days: float
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    employer: InvoicePayrollEmployer
    """El patrón (Emisor del complemento): registro patronal y CURP si es persona física."""
    employee: InvoicePayrollEmployee
    """El empleado (emp_…)."""
    perceptions: list[InvoicePayrollPerceptionsItem]
    """Percepciones (Percepcion): sueldo y demás, gravado y exento."""
    deductions: list[InvoicePayrollDeductionsItem]
    """Deducciones (Deduccion): ISR, cuotas IMSS y demás."""
    other_payments: list[InvoicePayrollOtherPaymentsItem]
    """Otros pagos (OtroPago): subsidio para el empleo."""


class InvoiceCancellation(TypedDict):
    status: str | None
    """pending (espera la respuesta del cliente), accepted (cancelada), rejected (el cliente la rechazó) o lapsed (venció; puede pedirla otra vez)."""
    motive: str | None
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 nominativa en una global."""
    substitution: str | None
    """El comprobante que sustituye a este (su id o su UUID), con el motivo 01."""
    canceled_at: str | None
    """Cuándo se canceló."""


class InvoiceEmail(TypedDict):
    to: str | None
    """A quién (correos separados por comas)."""
    cc: str | None
    """Con copia (correos separados por comas)."""
    sent_at: str | None
    """Cuándo se envió."""


class InvoiceError(TypedDict):
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""
    sat_code: str | None
    """Código del SAT o del PAC (CFDI40xxx)."""
    raw: str
    """El texto original del PAC."""


class InvoiceSubstitutes(TypedDict):
    """La factura que esta sustituyó y si quedó cancelada."""
    invoice: str
    """La factura sustituida (inv_…)."""
    canceled: bool
    """true si la sustituida ya quedó cancelada."""
    cancel_error: NotRequired[str]
    """Por qué no se pudo cancelar la sustituida (cancélela con POST /v1/invoices/{id}/cancel)."""


class InvoiceAdvanceApplication(TypedDict):
    """La aplicación del anticipo: método, nota de aplicación y su estado."""
    advance: str | None
    """El anticipo, como factura (inv_…)."""
    advance_uuid: str
    """El folio fiscal del anticipo."""
    method: Literal["egreso", "remanente"]
    """egreso (la factura completa y después una nota de crédito por el anticipo, opción A) o remanente (la factura solo por lo que falta, opción B)."""
    status: Literal["done", "credit_note_pending"]
    """done (listo) o credit_note_pending (falta timbrar la nota de aplicación: repita la solicitud con la misma Idempotency-Key)."""
    credit_note: str | None
    """La nota de aplicación del anticipo (inv_…), con method egreso."""
    credit_note_error: NotRequired[str]
    """Por qué no se timbró la nota de aplicación (repita con la misma Idempotency-Key)."""


# Un CFDI 4.0 emitido: factura de ingreso o global, traslado, nota de crédito (E), complemento de pago (P) o recibo de nómina (N).
Invoice = TypedDict(
    "Invoice",
    {
        "id": "str",
        "livemode": "bool",
        "object": "Literal[\"invoice\"]",
        "issuer": "str",
        "type": "Literal[\"I\", \"E\", \"P\", \"T\", \"N\"]",
        "status": "Literal[\"processing\", \"pending\", \"valid\", \"rejected\", \"canceled\"]",
        "uuid": "str | None",
        "series": "str | None",
        "folio": "str | None",
        "date": "str | None",
        "customer": "InvoiceCustomer",
        "use": "str | None",
        "payment_form": "str | None",
        "payment_method": "str | None",
        "currency": "str",
        "exchange_rate": "float | None",
        "items": "list[InvoiceItem]",
        "subtotal": "float | None",
        "discount": "float | None",
        "taxes": "InvoiceTaxes | None",
        "total": "float | None",
        "related": "dict[str, Any] | None",
        "payment": "NotRequired[InvoicePayment | None]",
        "payroll": "NotRequired[InvoicePayroll]",
        "global": "NotRequired[dict[str, Any]]",
        "cancellation": "InvoiceCancellation | None",
        "email": "InvoiceEmail | None",
        "error": "InvoiceError | None",
        "created_at": "str | None",
        "metadata": "dict[str, str]",
        "warnings": "NotRequired[list[str]]",
        "email_error": "NotRequired[str]",
        "substitutes": "NotRequired[InvoiceSubstitutes]",
        "advance_application": "NotRequired[InvoiceAdvanceApplication]",
    },
)


class RetentionRecipient(TypedDict):
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    foreign: bool
    """true si el receptor es extranjero (sin RFC)."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""


class RetentionPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    year: int
    """Año (Ejercicio)."""
    from_month: int
    """Mes inicial (MesIni), 1 a 12."""
    to_month: int
    """Mes final (MesFin), 1 a 12, del mismo año."""


class RetentionTotals(TypedDict):
    """Totales (Totales)."""
    operation: float | None
    """Monto total de la operación (MontoTotOperacion)."""
    taxed: float | None
    """Monto gravado (MontoTotGrav). Por omisión, operation menos exempt."""
    exempt: float | None
    """Monto exento (MontoTotExent). Por omisión 0."""
    withheld: float | None
    """Total retenido (MontoTotRet)."""


class RetentionTaxesItem(TypedDict):
    tax: str
    """Impuesto: isr, iva o ieps (ImpuestoRet 001, 002, 003)."""
    base: float
    """Base del impuesto retenido (BaseRet)."""
    amount: float
    """Monto retenido (MontoRet)."""
    payment_type: str
    """Tipo de pago de la retención (TipoPagoRet): 01 definitivo IVA, 02 definitivo IEPS, 03 definitivo ISR, 04 provisional ISR. Por omisión el usual de cada impuesto."""


class RetentionCancellation(TypedDict):
    status: str
    """pending (espera la respuesta del cliente), accepted (cancelada), rejected (el cliente la rechazó) o lapsed (venció; puede pedirla otra vez)."""
    motive: str | None
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 nominativa en una global."""
    canceled_at: str | None
    """Cuándo se canceló."""


class RetentionEmail(TypedDict):
    to: str | None
    """A quién (correos separados por comas)."""
    sent_at: str | None
    """Cuándo se envió."""


class RetentionError(TypedDict):
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""
    sat_code: str | None
    """Código del SAT o del PAC (CFDI40xxx)."""
    raw: str
    """El texto original del PAC."""


class Retention(TypedDict):
    """Una constancia de retenciones e información de pagos (CFDI de retenciones 2.0)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["retention"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    status: Literal["processing", "valid", "rejected", "canceled"]
    """processing: el PAC no ha contestado. valid: timbrada. rejected: el SAT o el PAC no la aceptaron (ver error). canceled: cancelada."""
    uuid: str | None
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    folio: int | None
    """Folio (Folio). Fiscalisto asigna el siguiente de la serie; mande uno solo si debe ser ese."""
    internal_folio: str | None
    """Folio interno (FolioInt): RET1, RET2…"""
    date: str | None
    """Fecha de emisión (Fecha), hora de la Ciudad de México."""
    code: str
    """Clave de la retención (CveRetenc), c_CveRetenc: 01 servicios profesionales, 05 arrendamiento, 14 dividendos, 16 intereses, 18 pagos al extranjero…"""
    description: str | None
    """Descripción de la retención (DescRetenc)."""
    recipient: RetentionRecipient
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    period: RetentionPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    totals: RetentionTotals
    """Totales (Totales)."""
    taxes: list[RetentionTaxesItem]
    """Impuestos del comprobante, por tipo."""
    dividends: NotRequired[dict[str, Any]]
    """Complemento de dividendos."""
    interest: NotRequired[dict[str, Any]]
    """Complemento de intereses."""
    foreign_payment: NotRequired[dict[str, Any]]
    """Complemento de pagos a extranjeros."""
    cancellation: RetentionCancellation | None
    """La cancelación, si se pidió: estado, motivo, sustituto y cuándo."""
    email: RetentionEmail | None
    """El envío por correo: a quién, con copia a quién y cuándo (null si no se ha enviado)."""
    error: RetentionError | None
    """Por qué el SAT o el PAC no lo aceptaron: mensaje, código del SAT y texto original."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    metadata: dict[str, str]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""
    warnings: NotRequired[list[str]]
    """Avisos que no impidieron timbrar (por ejemplo, el XML se guardará después)."""
    email_error: NotRequired[str]
    """Por qué no se pudo mandar el correo; el comprobante sí se timbró."""


class CustomerForeign(TypedDict):
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str | None
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class Customer(TypedDict):
    """Un cliente del catálogo de un emisor."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["customer"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: str | None
    """Correo del cliente (varios separados por comas), a donde van sus facturas."""
    use: str | None
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    foreign: CustomerForeign | None
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: bool
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""
    updated_at: str | None
    """Cuándo cambió por última vez, ISO 8601 (-06:00)."""


class Product(TypedDict):
    """Un producto o servicio del catálogo de un emisor."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["product"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str | None
    """Nombre corto para encontrarlo, solo para usted."""
    description: str
    """Descripción que va en el CFDI (Descripcion)."""
    product_key: str
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: str
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: str | None
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: str | None
    """Número de identificación o SKU (NoIdentificacion)."""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""
    taxability: str
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: str
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: float | None
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: str | None
    """Tasa o Cuota (TipoFactor del IEPS)."""
    iva_retention: float
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: float
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    updated_at: str | None
    """Cuándo cambió por última vez, ISO 8601 (-06:00)."""


class Employee(TypedDict):
    """Un empleado de un emisor, para sus recibos de nómina."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["employee"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre completo del empleado."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    curp: str
    """CURP, 18 caracteres."""
    social_security_number: str
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: str | None
    """Correo del empleado, a donde van sus recibos."""
    start_date: str
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    end_date: str | None
    """Último día trabajado si ya no trabaja ahí, AAAA-MM-DD."""
    daily_salary: float
    """Salario diario."""
    integrated_daily_salary: float
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    contract_type: str
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    workday_type: str
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    regime_type: str
    """Tipo de régimen (TipoRegimen): 02 sueldos y salarios."""
    periodicity: str
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    risk_class: str
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    state: str
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""
    border_zone: bool
    """true si trabaja en la zona libre de la frontera norte (salario mínimo de frontera)."""
    unionized: bool
    """true si es sindicalizado (Sindicalizado)."""
    department: str | None
    """Departamento (Departamento)."""
    position: str | None
    """Puesto (Puesto)."""
    warnings: list[str]
    """Lo que el SAT podría observar de sus datos, antes de timbrar."""


class PayrollReceiptPreviewPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: str
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class PayrollReceiptPreviewPerceptionsItem(TypedDict):
    type: str
    """Tipo de percepción (TipoPercepcion), c_TipoPercepcion: 001 sueldos…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    taxed: float
    """Importe gravado (ImporteGravado)."""
    exempt: float
    """Importe exento (ImporteExento)."""


class PayrollReceiptPreviewDeductionsItem(TypedDict):
    type: str
    """Tipo de deducción (TipoDeduccion), c_TipoDeduccion: 001 IMSS, 002 ISR…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe (Importe)."""


class PayrollReceiptPreviewOtherPaymentsItem(TypedDict):
    type: str
    """Tipo de otro pago (TipoOtroPago), c_TipoOtroPago: 002 subsidio para el empleo."""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe pagado (Importe)."""
    subsidy_caused: NotRequired[float]
    """Subsidio causado (SubsidioCausado)."""
    subsidy_applied: NotRequired[float]
    """Del subsidio causado, el ISR que evitó (no va en el XML)."""


class PayrollReceiptPreviewIsrAdjustment(TypedDict):
    """El ajuste de fin de mes: subsidio revertido y el ISR que retiene."""
    reversed: float
    """Subsidio causado antes en el mes que se revierte."""
    isr: float
    """El cálculo del ISR del periodo: base, tarifa, subsidio y resultado."""


class PayrollReceiptPreviewIsr(TypedDict):
    """El cálculo del ISR del periodo: base, tarifa, subsidio y resultado."""
    tariff: float
    """ISR según la tarifa del periodo."""
    subsidy: float
    """Subsidio para el empleo causado."""
    withheld: float
    """ISR retenido (tarifa menos subsidio, no menos de 0)."""
    exempt_minimum: bool
    """true si gana el salario mínimo: no se le retiene ISR."""
    adjustment: NotRequired[PayrollReceiptPreviewIsrAdjustment]
    """El ajuste de fin de mes: subsidio revertido y el ISR que retiene."""


class PayrollReceiptPreviewTotals(TypedDict):
    """Totales: percepciones, deducciones, otros pagos y el neto a pagar."""
    salaries: float
    """Total de sueldos, salarios y asimilados (TotalSueldos)."""
    taxed: float
    """Total gravado (TotalGravado)."""
    exempt: float
    """Total exento (TotalExento)."""
    perceptions: float
    """Total de percepciones (TotalPercepciones)."""
    other_deductions: float
    """Otras deducciones (TotalOtrasDeducciones)."""
    taxes_withheld: float
    """Impuestos retenidos (TotalImpuestosRetenidos)."""
    deductions: float
    """Total de deducciones (TotalDeducciones)."""
    other_payments: float
    """Total de otros pagos (TotalOtrosPagos)."""
    subtotal: float
    """Subtotal del comprobante: percepciones más otros pagos."""
    net: float
    """Neto a pagar al empleado."""


class PayrollReceiptPreview(TypedDict):
    """El recibo como se timbraría: percepciones, deducciones (ISR, IMSS), otros pagos (subsidio) y el neto."""
    object: Literal["payroll_receipt_preview"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    employee: str
    """El empleado (emp_…)."""
    periodicity: str
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    period: PayrollReceiptPreviewPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    days: float
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    contribution_base_salary: float
    """Salario base de cotización (SalarioBaseCotApor)."""
    perceptions: list[PayrollReceiptPreviewPerceptionsItem]
    """Percepciones (Percepcion): sueldo y demás, gravado y exento."""
    deductions: list[PayrollReceiptPreviewDeductionsItem]
    """Deducciones (Deduccion): ISR, cuotas IMSS y demás."""
    other_payments: list[PayrollReceiptPreviewOtherPaymentsItem]
    """Otros pagos (OtroPago): subsidio para el empleo."""
    isr: PayrollReceiptPreviewIsr
    """El cálculo del ISR del periodo: base, tarifa, subsidio y resultado."""
    totals: PayrollReceiptPreviewTotals
    """Totales: percepciones, deducciones, otros pagos y el neto a pagar."""


class AdvanceCustomer(TypedDict):
    """Cliente (Receptor): el id de uno de su catálogo (cus_…) o sus datos en un objeto."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class Advance(TypedDict):
    """Un anticipo timbrado que aún no se aplica."""
    object: Literal["advance"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    uuid: str
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    date: str
    """Fecha de emisión (Fecha), hora de la Ciudad de México."""
    series: str | None
    """Serie (Serie), hasta 25 caracteres. Cada serie lleva sus propios folios."""
    folio: str | None
    """Folio (Folio). Fiscalisto asigna el siguiente de la serie; mande uno solo si debe ser ese."""
    customer: AdvanceCustomer
    """Cliente (Receptor): el id de uno de su catálogo (cus_…) o sus datos en un objeto."""
    amount: float
    """El anticipo antes de impuestos."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    iva: str
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    currency: str
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""


class InvoiceBatchInvoicesItem(TypedDict):
    index: int
    """Su posición en invoices, desde 0."""
    reference: str | None
    """Su identificador de esta factura (su número de pedido), hasta 100 caracteres."""
    status: Literal["processing", "valid", "failed"]
    """processing, valid (timbrada) o failed (no se timbró; ver error)."""
    invoice: str | None
    """La factura timbrada (inv_…)."""
    uuid: str | None
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    error: str | None
    """Por qué no se timbró."""


class InvoiceBatch(TypedDict):
    """Un lote de hasta 1,000 facturas timbradas en segundo plano."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["invoice_batch"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str
    """Nombre del lote, para usted."""
    status: Literal["processing", "completed"]
    """processing: timbrando. completed: ya no queda ninguna por timbrar."""
    total: int
    """Cuántas facturas tiene el lote."""
    stamped: int
    """Cuántas se timbraron."""
    failed: int
    """Cuántas no se timbraron (quedan con su motivo)."""
    processing: NotRequired[int]
    """Cuántas siguen en proceso."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    completed_at: str | None
    """Cuándo terminó."""
    invoices: NotRequired[list[InvoiceBatchInvoicesItem]]
    """Cada factura del lote (no viene en listas ni en eventos)."""


class SatCatalogEntry(TypedDict):
    """Una clave de un catálogo del SAT."""
    code: str
    """La clave en el catálogo del SAT."""
    description: str
    """Su descripción en el catálogo."""


class SatListCheckListsItem(TypedDict):
    list: Literal["69", "69b", "69b_bis"]
    """69b: art. 69-B (operaciones simuladas). 69b_bis: art. 69-B Bis (pérdidas fiscales). 69: art. 69 (no localizados, adeudos, cancelados)."""
    source: str
    """El archivo del SAT de donde viene (clave)."""
    source_name: str
    """El nombre del archivo del SAT, para mostrarlo."""
    situation: str | None
    """Su situación según el SAT: Presunto, Definitivo, Desvirtuado, Sentencia favorable; en el art. 69, el supuesto (null si el archivo no la trae)."""
    published_on: str | None
    """Fecha de publicación en el SAT o en el DOF (null si no la trae)."""
    details: dict[str, str] | None
    """Lo demás que publica el SAT para ese RFC (oficios, fechas, montos), tal cual; null si nada."""


class SatListCheck(TypedDict):
    """Si un RFC aparece en las listas del SAT (69-B, 69-B Bis y art. 69)."""
    object: Literal["sat_list_check"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    tax_id: str
    """El RFC revisado."""
    name: str | None
    """El nombre con que aparece en las listas del SAT (null si no aparece)."""
    listed: bool
    """true si el RFC aparece en alguna lista, aunque haya desvirtuado."""
    risk: Literal["high", "medium", "none"]
    """high: 69-B o 69-B Bis como presunto o definitivo (el SAT dice que simula operaciones; sus facturas no se pueden deducir). medium: una lista del art. 69 (no localizado, créditos firmes o exigibles, cancelados, sentencias, CSD sin efectos). none: no aparece, o ya desvirtuó o tiene sentencia favorable."""
    lists: list[SatListCheckListsItem]
    """Cada lista en que aparece; vacía si no aparece en ninguna."""
    lists_updated_at: str | None
    """Cuándo se actualizaron las listas por última vez (cada día a las 00:00 de la Ciudad de México)."""


class TaxIdValidationErrorsItem(TypedDict):
    param: str
    """El campo: tax_id, legal_name, tax_system, zip, use o cif_id."""
    code: str
    """Qué falló, para su código: tax_id_format, tax_id_date, legal_name_capital_regime, legal_name_mismatch, tax_system_person, tax_system_mismatch, zip_unknown, zip_mismatch, use_tax_system, cif_id_not_found…"""
    message: str
    """La explicación, para mostrarla a su usuario."""
    suggestion: str | None
    """El valor correcto cuando se sabe (el del SAT con cif_id, o el nombre sin régimen de capital); null si no."""


class TaxIdValidationWarningsItem(TypedDict):
    param: str
    """El campo."""
    code: str
    """tax_id_check_digit, legal_name_format, tax_id_listed_69b o tax_id_listed_69."""
    message: str
    """La explicación."""
    suggestion: str | None
    """El valor sugerido, o null."""


class TaxIdValidationSatRecord(TypedDict):
    legal_name: str | None
    """El nombre o razón social, como lo tiene el SAT."""
    zip: str | None
    """El código postal de su domicilio fiscal."""
    tax_systems: list[str]
    """Sus regímenes vigentes (c_RegimenFiscal)."""


class TaxIdValidation(TypedDict):
    """Si los datos fiscales de un cliente van a pasar el SAT."""
    object: Literal["tax_id_validation"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    tax_id: str
    """El RFC revisado."""
    kind: Literal["company", "person", "generic"]
    """company (persona moral, 12 caracteres), person (persona física, 13) o generic (XAXX010101000, XEXX010101000)."""
    valid: bool
    """true si no hay errores: con lo que mandó, el SAT no debería rechazar la factura por los datos del cliente."""
    checked_with_sat: bool
    """true si se comparó con el registro del SAT (mandó cif_id y el SAT contestó)."""
    errors: list[TaxIdValidationErrorsItem]
    """Lo que haría que el SAT rechace la factura. Cada uno con el campo (param), un código, la explicación y, si se puede, el valor correcto (suggestion)."""
    warnings: list[TaxIdValidationWarningsItem]
    """Lo que no impide timbrar pero conviene revisar: el dígito verificador, mayúsculas, si el RFC está en las listas del SAT."""
    sat_record: TaxIdValidationSatRecord | None
    """Lo que tiene el SAT en la constancia (con cif_id): nombre, código postal y regímenes vigentes. null sin cif_id."""
    sat_error: str | None
    """Si el SAT no contestó a tiempo (con cif_id): reintente en unos minutos. null si contestó o no se consultó."""
    sat_lists: SatListCheck | None
    """Si el RFC aparece en las listas del SAT. null con un RFC genérico o mal escrito."""


class CustomerDataRequestSubmission(TypedDict):
    tax_id: str
    """Su RFC."""
    legal_name: str
    """Su nombre o razón social, como en su constancia."""
    tax_system: str
    """Su régimen fiscal (c_RegimenFiscal)."""
    zip: str
    """El código postal de su domicilio fiscal."""
    use: str
    """El uso del CFDI que eligió (c_UsoCFDI)."""
    email: str | None
    """Su correo para recibir facturas, si lo dio."""
    source: Literal["constancia", "manual"]
    """constancia (leído de su constancia o del SAT con su idCIF) o manual (escrito)."""
    customer: str | None
    """El cliente (cus_…) en el catálogo del emisor: el nuevo, o el que ya existía con ese RFC."""
    applied: bool
    """true si quedó en el catálogo. false si el cliente ya existía con otros datos: aplíquelos con POST /v1/customers/{id} si son correctos."""
    submitted_at: str | None
    """Cuándo los mandó."""


class CustomerDataRequest(TypedDict):
    """Una liga para que un cliente dé sus datos fiscales."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["customer_data_request"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor que le va a facturar."""
    status: Literal["open", "completed", "expired", "canceled"]
    """open (la liga espera), completed (el cliente mandó sus datos), expired (venció) o canceled."""
    url: str | None
    """La liga para su cliente, en fiscalisto.com. null cuando ya no está abierta."""
    reference: str | None
    """Su id para este cliente o pedido."""
    description: str | None
    """Lo que el cliente ve arriba del formulario."""
    expires_at: str | None
    """Cuándo deja de servir la liga."""
    created_at: str | None
    """Cuándo se creó."""
    submission: CustomerDataRequestSubmission | None
    """Lo que mandó el cliente (el último envío: puede corregirlo en las 24 horas siguientes). null mientras no conteste."""


class TestDataReset(TypedDict):
    """Lo que se borró (y se creó) al reiniciar los datos de prueba."""
    object: Literal["test_data_reset"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: Literal[False]
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuers: int
    """Cuántos emisores de pruebas se vaciaron (archivados incluidos)."""
    deleted_rows: int
    """Cuántos registros se borraron: facturas, clientes, productos, lotes, ligas, descargas…"""
    deleted_events: int
    """Cuántos eventos de pruebas se borraron (con sus entregas)."""
    customers_created: int
    """Clientes de ejemplo creados (con seed)."""
    products_created: int
    """Productos de ejemplo creados (con seed)."""


# Una solicitud al SAT de las facturas emitidas o recibidas de un emisor en un periodo.
SatDownload = TypedDict(
    "SatDownload",
    {
        "id": "str",
        "livemode": "bool",
        "object": "Literal[\"sat_download\"]",
        "issuer": "str",
        "direction": "Literal[\"received\", \"issued\"]",
        "from": "str | None",
        "to": "str | None",
        "type": "Literal[\"I\", \"E\", \"P\", \"T\", \"N\"] | None",
        "counterparty_tax_id": "str | None",
        "uuid": "str | None",
        "status": "Literal[\"processing\", \"completed\", \"failed\"]",
        "new_invoices": "int | None",
        "error": "str | None",
        "created_at": "str | None",
        "completed_at": "str | None",
    },
)


class SatInvoiceIssuedBy(TypedDict):
    """Quien la emitió (Emisor)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class SatInvoiceIssuedTo(TypedDict):
    """A quien se la emitieron (Receptor)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class SatInvoiceTaxes(TypedDict):
    """Impuestos del comprobante: trasladados (iva, ieps), retenidos (iva_withheld, isr_withheld, ieps_withheld) y locales."""
    iva: float
    """IVA trasladado."""
    ieps: float
    """IEPS trasladado."""
    iva_withheld: float
    """IVA retenido."""
    isr_withheld: float
    """ISR retenido."""
    ieps_withheld: float
    """IEPS retenido."""
    local_transferred: float
    """Impuestos locales trasladados (ISH y similares)."""
    local_withheld: float
    """Impuestos locales retenidos."""


class SatInvoice(TypedDict):
    """Una factura que el SAT tiene del emisor, emitida o recibida, traída con una descarga."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sat_invoice"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor de su cuenta (iss_…) a quien pertenece esta factura."""
    uuid: str
    """El folio fiscal (UUID del timbre)."""
    direction: Literal["received", "issued"]
    """received (se la hicieron al emisor) o issued (la emitió)."""
    type: Literal["I", "E", "P", "T", "N"] | None
    """Tipo de comprobante (TipoDeComprobante): I ingreso, E egreso, P pago, T traslado, N nómina."""
    date: str
    """La fecha del comprobante (Fecha), en la hora local con que se emitió."""
    series: str | None
    """Serie (Serie), o null."""
    folio: str | None
    """Folio (Folio), o null."""
    issued_by: SatInvoiceIssuedBy
    """Quien la emitió (Emisor)."""
    issued_to: SatInvoiceIssuedTo
    """A quien se la emitieron (Receptor)."""
    currency: str | None
    """Moneda (Moneda): MXN, USD…"""
    exchange_rate: float | None
    """Tipo de cambio (TipoCambio), o null en pesos."""
    payment_method: str | None
    """Método de pago (MetodoPago): PUE o PPD."""
    payment_form: str | None
    """Forma de pago (FormaPago), clave de c_FormaPago."""
    use: str | None
    """Uso del CFDI (UsoCFDI)."""
    subtotal: float | None
    """Subtotal (SubTotal)."""
    total: float | None
    """Total (Total)."""
    taxes: SatInvoiceTaxes
    """Impuestos del comprobante: trasladados (iva, ieps), retenidos (iva_withheld, isr_withheld, ieps_withheld) y locales."""
    sat_status: Literal["active", "canceled"] | None
    """Su estado en el SAT cuando se revisó: active (vigente) o canceled. null si aún no se revisa."""
    sat_download: str | None
    """La descarga (sdl_…) que la trajo, o null."""
    downloaded_at: str | None
    """Cuándo llegó."""


class TicketCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class Ticket(TypedDict):
    """Una venta que su comprador puede facturar él mismo en el portal del emisor (autofactura)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["ticket"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor que vendió."""
    folio: str
    """El folio de la venta en su sistema."""
    code: str
    """Lo que su comprador escribe en el portal junto con el total: el folio y 4 caracteres al azar (A123-K7QX). Imprímalo en el ticket o mándelo con la compra."""
    status: Literal["pending", "invoiced", "global", "cancelled"]
    """pending (se puede facturar), invoiced (su comprador lo facturó: la factura en invoice), global (entró en la factura global del periodo) o cancelled."""
    url: str | None
    """La página del portal con el código ya escrito: el comprador pone el total y sus datos. Puede incrustarla con fiscalisto.js. null si ya no está pendiente."""
    total: float
    """Lo que se cobró, impuestos incluidos y sin propina."""
    tip: float
    """La propina (no va en la factura)."""
    payment_form: str
    """c_FormaPago de la venta."""
    description: str
    """El concepto de la factura."""
    product_key: str
    """c_ClaveProdServ del concepto."""
    sold_at: str
    """Cuándo se vendió."""
    invoiceable_until: str
    """El último día (AAAA-MM-DD) en que el comprador puede facturarlo; después entra en la factura global."""
    invoice: str | None
    """La factura (inv_…) que hizo su comprador, o null."""
    global_invoice: str | None
    """La factura global (inv_…) en que entró, o null."""
    customer: TicketCustomer | None
    """A quién se facturó, o null."""
    created_at: str | None
    """Cuándo se registró."""


class SelfInvoicing(TypedDict):
    """El portal de autofactura de un emisor y sus reglas."""
    object: Literal["self_invoicing"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    portal_url: str
    """El portal permanente del emisor: ahí cualquier comprador factura con su código y su total."""
    window: Literal["month", "days"]
    """month: se factura hasta el fin del mes de la venta. days: hasta window_days días después."""
    window_days: int
    """Días para facturar con window: days."""
    global_periodicity: Literal["01", "02", "03", "04"]
    """Cada cuánto se timbra sola la factura global con lo que nadie facturó: 01 diaria, 02 semanal, 03 quincenal, 04 mensual."""


class IssuerOnboardingLink(TypedDict):
    """Una liga para que el dueño de un emisor suba su CSD y firme con su e.firma."""
    object: Literal["issuer_onboarding_link"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor que se da de alta."""
    url: str
    """La página para el dueño del emisor, en fiscalisto.com. Ábrala en el navegador de su cliente; no la incruste en un iframe."""
    return_url: str | None
    """A dónde regresa al terminar."""
    expires_at: str | None
    """Cuándo deja de servir la liga. Pida otra cuando quiera."""
    created_at: str | None
    """Cuándo se creó."""


class WebhookEndpoint(TypedDict):
    """Una dirección de su servidor que recibe eventos."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["webhook_endpoint"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    url: str
    """Dirección https de su servidor que recibe los avisos."""
    description: str | None
    """Para qué es, para usted."""
    events: list[str]
    """Eventos que quiere recibir, o ["*"] para todos (por omisión). Ver la lista en Webhooks."""
    status: Literal["enabled", "failing", "disabled"]
    """enabled: entregando. failing: sus entregas fallan (se apaga tras 5 días así). disabled: apagado."""
    disabled_reason: NotRequired[str | None]
    """Por qué se apagó (sus entregas fallaron 5 días seguidos, o usted lo apagó)."""
    failing_since: NotRequired[str | None]
    """Desde cuándo fallan las entregas, o null."""
    previous_secret_expires_at: str | None
    """Hasta cuándo el secreto anterior también firma (después de cambiarlo), o null."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    secret: NotRequired[str]
    """Secreto de firma (whsec_…). Solo viene al crearlo o al cambiarlo: guárdelo para verificar las firmas."""


class WebhookTestDelivery(TypedDict):
    """Cómo le fue: ok si contestó 2xx, el código, el error y el inicio de su respuesta."""
    ok: bool
    """true si su servidor contestó 2xx."""
    status: int | None
    """El código HTTP que contestó; null si no se pudo conectar."""
    error: str | None
    """Qué falló (sin respuesta, no se pudo conectar, otro código), o null."""
    response_body: str | None
    """El inicio de lo que contestó su servidor (hasta 2,000 caracteres)."""
    duration_ms: int
    """Cuánto tardó su servidor, en milisegundos."""


class WebhookTest(TypedDict):
    """Un evento de prueba que se mandó a su webhook, y lo que respondió su servidor."""
    object: Literal["webhook_test"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    event: Event
    """El evento que se mandó, como lo recibió su servidor."""
    delivery: WebhookTestDelivery
    """Cómo le fue: ok si contestó 2xx, el código, el error y el inicio de su respuesta."""


EventType = Literal["invoice.stamped", "invoice.failed", "invoice.canceled", "invoice.cancellation_pending", "invoice.cancellation_rejected", "retention.stamped", "retention.failed", "retention.canceled", "invoice_batch.completed", "customer_data_request.completed", "sat_download.completed", "sat_download.failed", "ticket.invoiced", "ticket.included_in_global", "issuer.ready", "balance.low"]
"""Lo que puede pasar: el tipo de cada evento."""


class InvoiceEventData(TypedDict):
    object: Invoice
    """El objeto como quedó: el comprobante completo, como lo contesta su GET."""


class RetentionEventData(TypedDict):
    object: Retention
    """El objeto como quedó: la constancia completo, como lo contesta su GET."""


class InvoiceBatchEventData(TypedDict):
    object: InvoiceBatch
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class CustomerDataRequestEventData(TypedDict):
    object: CustomerDataRequest
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class SatDownloadEventData(TypedDict):
    object: SatDownload
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class TicketEventData(TypedDict):
    object: Ticket
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class IssuerEventData(TypedDict):
    object: Issuer
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class BalanceEventData(TypedDict):
    object: Balance
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class InvoiceStampedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.stamped"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceFailedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.failed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceCanceledEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.canceled"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceCancellationPendingEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.cancellation_pending"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceCancellationRejectedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.cancellation_rejected"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class RetentionStampedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["retention.stamped"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: RetentionEventData


class RetentionFailedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["retention.failed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: RetentionEventData


class RetentionCanceledEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["retention.canceled"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: RetentionEventData


class InvoiceBatchCompletedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice_batch.completed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceBatchEventData


class CustomerDataRequestCompletedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["customer_data_request.completed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: CustomerDataRequestEventData


class SatDownloadCompletedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sat_download.completed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SatDownloadEventData


class SatDownloadFailedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sat_download.failed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SatDownloadEventData


class TicketInvoicedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["ticket.invoiced"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: TicketEventData


class TicketIncludedInGlobalEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["ticket.included_in_global"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: TicketEventData


class IssuerReadyEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["issuer.ready"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: IssuerEventData


class BalanceLowEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["balance.low"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, ticket.invoiced, ticket.included_in_global, issuer.ready o balance.low."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: BalanceEventData


Event = Union[
    InvoiceStampedEvent,
    InvoiceFailedEvent,
    InvoiceCanceledEvent,
    InvoiceCancellationPendingEvent,
    InvoiceCancellationRejectedEvent,
    RetentionStampedEvent,
    RetentionFailedEvent,
    RetentionCanceledEvent,
    InvoiceBatchCompletedEvent,
    CustomerDataRequestCompletedEvent,
    SatDownloadCompletedEvent,
    SatDownloadFailedEvent,
    TicketInvoicedEvent,
    TicketIncludedInGlobalEvent,
    IssuerReadyEvent,
    BalanceLowEvent,
]
"""Un evento: según su type, data.object es la factura, la constancia o el lote."""


class Deleted(TypedDict):
    """Confirmación de que se borró."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, evt_, whe_)."""
    object: str
    """Qué tipo de objeto es («invoice», «customer»…)."""
    deleted: Literal[True]
    """Siempre true."""


class ApiErrorError(TypedDict):
    """Por qué el SAT o el PAC no lo aceptaron: mensaje, código del SAT y texto original."""
    type: Literal["invalid_request_error", "authentication_error", "permission_error", "not_found_error", "idempotency_error", "rate_limit_error", "invoice_error", "balance_error", "api_error"]
    """La familia del error: invalid_request_error, authentication_error, permission_error, not_found_error, idempotency_error, rate_limit_error, invoice_error, balance_error o api_error."""
    code: str
    """La razón precisa, estable (ver Errores)."""
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""
    param: NotRequired[str]
    """El campo con el problema (items.0.unit_price)."""
    sat_code: NotRequired[str]
    """Código del SAT o del PAC (CFDI40xxx)."""
    doc_url: str
    """La explicación de este código en la documentación."""
    request_id: str
    """El id de la solicitud (req_…). Inclúyalo si nos escribe."""


class ApiError(TypedDict):
    """Todos los errores tienen esta forma."""
    error: ApiErrorError
    """Por qué el SAT o el PAC no lo aceptaron: mensaje, código del SAT y texto original."""


class IssuerList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Issuer]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class InvoiceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Invoice]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class AdvanceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Advance]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class RetentionList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Retention]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class EmployeeList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Employee]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class InvoiceBatchList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[InvoiceBatch]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class CustomerList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Customer]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class CustomerDataRequestList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[CustomerDataRequest]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class ProductList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Product]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatCatalogEntryList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatCatalogEntry]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatListCheckList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatListCheck]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatDownloadList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatDownload]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatInvoiceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatInvoice]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class TicketList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Ticket]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class WebhookEndpointList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[WebhookEndpoint]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class EventList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Event]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class InvoiceCreateCustomerForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class InvoiceCreateCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[InvoiceCreateCustomerForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class InvoiceCreateItemsItemThirdParty(TypedDict):
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    tax_id: str
    """RFC de a cuenta de quién (RfcACuentaTerceros)."""
    name: str
    """Nombre (NombreACuentaTerceros)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscalACuentaTerceros), c_RegimenFiscal."""
    zip: str
    """Código postal de su domicilio fiscal (DomicilioFiscalACuentaTerceros)."""


class InvoiceCreateItemsItemIedu(TypedDict):
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    student_name: str
    """Nombre del alumno (nombreAlumno)."""
    curp: str
    """CURP, 18 caracteres."""
    level: Literal["Preescolar", "Primaria", "Secundaria", "Profesional técnico", "Bachillerato o su equivalente"]
    """Nivel educativo (nivelEducativo)."""
    rvoe: str
    """Reconocimiento de validez oficial de estudios (autRVOE)."""
    payer_tax_id: NotRequired[str | None]
    """RFC de quien paga, si no es el receptor (rfcPago)."""


class InvoiceCreateItemsItemUsedVehicleCustomsItem(TypedDict):
    number: str
    """Número del documento de importación (numero)."""
    date: str
    """Fecha del documento (fecha), AAAA-MM-DD."""
    office: NotRequired[str]
    """Aduana (aduana)."""


class InvoiceCreateItemsItemUsedVehicle(TypedDict):
    """Complemento de vehículo usado."""
    purchase_amount: float
    """Monto de adquisición (montoAdquisicion)."""
    sale_amount: float
    """Monto de enajenación (montoEnajenacion)."""
    vehicle_key: str
    """Clave vehicular (claveVehicular)."""
    make: str
    """Marca (marca)."""
    type: str
    """Tipo o versión (tipo)."""
    model: str
    """Año del modelo (modelo), 4 dígitos."""
    engine_number: NotRequired[str]
    """Número de motor (numeroMotor)."""
    serial_number: NotRequired[str]
    """Número de serie (numeroSerie)."""
    niv: NotRequired[str]
    """Número de identificación vehicular (NIV)."""
    guide_value: float
    """Valor según la guía EBC o Libro Azul (valor)."""
    customs: NotRequired[list[InvoiceCreateItemsItemUsedVehicleCustomsItem]]
    """Información aduanera de la importación del vehículo (InformacionAduanera)."""


class InvoiceCreateItemsItem(TypedDict):
    """Un concepto. description, product_key y unit_price son obligatorios, salvo que mande product (prd_…): entonces vienen de su catálogo y lo que mande encima gana."""
    product: NotRequired[str]
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    description: NotRequired[str]
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount: NotRequired[float]
    """Descuento (Descuento)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    ieps_units: NotRequired[float]
    """Unidades de IEPS a cuota (litros, cigarros…), si no son la cantidad."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    predial: NotRequired[list[str]]
    """Números de cuenta predial (CuentaPredial) en arrendamiento."""
    pedimentos: NotRequired[list[str]]
    """Números de pedimento (InformacionAduanera) de mercancía importada."""
    third_party: NotRequired[InvoiceCreateItemsItemThirdParty]
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    iedu: NotRequired[InvoiceCreateItemsItemIedu]
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    used_vehicle: NotRequired[InvoiceCreateItemsItemUsedVehicle]
    """Complemento de vehículo usado."""
    addenda: NotRequired[dict[str, str]]
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""


class InvoiceCreateCartaPorteInternational(TypedDict):
    """Transporte internacional (TranspInternac Sí): entrada o salida, país, vía y regímenes aduaneros."""
    direction: Literal["Entrada", "Salida"]
    """EntradaSalidaMerc: Entrada o Salida."""
    country: str
    """País de origen o destino (PaisOrigenDestino), c_Pais."""
    via: str
    """Vía de entrada o salida (ViaEntradaSalida), c_CveTransporte (05 ducto incluido)."""
    regimes: list[str]
    """Regímenes aduaneros (RegimenAduanero), c_RegimenAduanero."""


class InvoiceCreateCartaPorteIstmo(TypedDict):
    """Corredor Interoceánico del Istmo de Tehuantepec: polos de origen y destino (c_RegistroISTMO)."""
    origin: str
    """Polo de origen (UbicacionPoloOrigen)."""
    destination: str
    """Polo de destino (UbicacionPoloDestino)."""


class InvoiceCreateCartaPorteOriginForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteOriginStation(TypedDict):
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    type: NotRequired[str]
    """Tipo de estación (TipoEstacion): 01 origen, 02 intermedia, 03 destino final."""
    number: NotRequired[str]
    """Clave de la estación, puerto o aeropuerto (NumEstacion), c_Estaciones."""
    name: NotRequired[str]
    """Nombre de la estación (NombreEstacion)."""
    foreign: NotRequired[bool]
    """true si la estación está en el extranjero (va sin TipoEstacion)."""


class InvoiceCreateCartaPorteOriginAddress(TypedDict):
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""
    street: NotRequired[str]
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""
    country: NotRequired[str]
    """País (Pais), c_Pais. Por omisión MEX."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""


class InvoiceCreateCartaPorteOrigin(TypedDict):
    """Ubicación de origen (Ubicacion TipoUbicacion Origen): remitente, fecha y hora de salida y domicilio."""
    tax_id: str
    """RFC del remitente (RFCRemitenteDestinatario); XEXX010101000 si es extranjero."""
    name: NotRequired[str]
    """Nombre del remitente (NombreRemitenteDestinatario)."""
    foreign: NotRequired[InvoiceCreateCartaPorteOriginForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    date_time: str
    """Fecha y hora de salida (origen) o llegada (destino), AAAA-MM-DDTHH:MM, hora local."""
    distance_km: NotRequired[float]
    """Distancia recorrida desde la ubicación anterior, en km (DistanciaRecorrida). Autotransporte y ferroviario."""
    station: NotRequired[InvoiceCreateCartaPorteOriginStation]
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    navigation: NotRequired[Literal["Altura", "Cabotaje"]]
    """Marítimo: tipo de tráfico (NavegacionTrafico), Altura o Cabotaje."""
    address: InvoiceCreateCartaPorteOriginAddress
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""


class InvoiceCreateCartaPorteDestinationsItemForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteDestinationsItemStation(TypedDict):
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    type: NotRequired[str]
    """Tipo de estación (TipoEstacion): 01 origen, 02 intermedia, 03 destino final."""
    number: NotRequired[str]
    """Clave de la estación, puerto o aeropuerto (NumEstacion), c_Estaciones."""
    name: NotRequired[str]
    """Nombre de la estación (NombreEstacion)."""
    foreign: NotRequired[bool]
    """true si la estación está en el extranjero (va sin TipoEstacion)."""


class InvoiceCreateCartaPorteDestinationsItemAddress(TypedDict):
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""
    street: NotRequired[str]
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""
    country: NotRequired[str]
    """País (Pais), c_Pais. Por omisión MEX."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""


class InvoiceCreateCartaPorteDestinationsItem(TypedDict):
    tax_id: str
    """RFC del destinatario (RFCRemitenteDestinatario); XEXX010101000 si es extranjero."""
    name: NotRequired[str]
    """Nombre del destinatario (NombreRemitenteDestinatario)."""
    foreign: NotRequired[InvoiceCreateCartaPorteDestinationsItemForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    date_time: str
    """Fecha y hora de salida (origen) o llegada (destino), AAAA-MM-DDTHH:MM, hora local."""
    distance_km: NotRequired[float]
    """Distancia recorrida desde la ubicación anterior, en km (DistanciaRecorrida). Autotransporte y ferroviario."""
    station: NotRequired[InvoiceCreateCartaPorteDestinationsItemStation]
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    navigation: NotRequired[Literal["Altura", "Cabotaje"]]
    """Marítimo: tipo de tráfico (NavegacionTrafico), Altura o Cabotaje."""
    address: InvoiceCreateCartaPorteDestinationsItemAddress
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""


class InvoiceCreateCartaPorteGoodsItemHazmat(TypedDict):
    """Material peligroso (MaterialPeligroso Sí): clave UN y embalaje."""
    key: str
    """Clave del material peligroso (CveMaterialPeligroso), c_MaterialPeligroso (número UN)."""
    packaging: str
    """Tipo de embalaje (Embalaje), c_TipoEmbalaje."""
    packaging_description: NotRequired[str]
    """Descripción del embalaje (DescripEmbalaje)."""


class InvoiceCreateCartaPorteGoodsItemCofepris(TypedDict):
    """Datos COFEPRIS de la mercancía: sector y lo que pide cada uno (medicamentos, precursores, psicotrópicos, sustancias tóxicas, plaguicidas)."""
    sector: str
    """Sector COFEPRIS (SectorCOFEPRIS): 01 medicamento, 02 precursores y químicos de uso dual, 03 psicotrópicos y estupefacientes, 04 sustancias tóxicas, 05 plaguicidas y fertilizantes."""
    active_ingredient: NotRequired[str]
    """Nombre del ingrediente activo (NombreIngredienteActivo)."""
    chemical_name: NotRequired[str]
    """Nombre químico (NomQuimico)."""
    generic_name: NotRequired[str]
    """Denominación genérica del producto (DenominacionGenericaProd)."""
    brand_name: NotRequired[str]
    """Denominación distintiva o marca (DenominacionDistintivaProd)."""
    manufacturer: NotRequired[str]
    """Fabricante (Fabricante)."""
    expiry: NotRequired[str]
    """Fecha de caducidad (FechaCaducidad), AAAA-MM-DD."""
    lot: NotRequired[str]
    """Lote del medicamento (LoteMedicamento)."""
    form: NotRequired[str]
    """Forma farmacéutica (FormaFarmaceutica), c_FormaFarmaceutica."""
    conditions: NotRequired[str]
    """Condiciones especiales de transporte (CondicionesEspTransp), c_CondicionesEspeciales."""
    sanitary_registry: NotRequired[str]
    """Registro sanitario o folio de autorización (RegistroSanitarioFolioAutorizacion)."""
    import_permit: NotRequired[str]
    """Permiso de importación (PermisoImportacion)."""
    vucem_folio: NotRequired[str]
    """Folio de importación VUCEM (FolioImpoVUCEM)."""
    cas: NotRequired[str]
    """Número CAS de la sustancia (NumCAS)."""
    importer: NotRequired[str]
    """Razón social de la empresa importadora (RazonSocialEmpImp)."""
    pesticide_registry: NotRequired[str]
    """Registro sanitario de plaguicidas COFEPRIS (NumRegSanPlagCOFEPRIS)."""
    manufacturer_data: NotRequired[str]
    """Datos del fabricante (DatosFabricante)."""
    formulator_data: NotRequired[str]
    """Datos del formulador (DatosFormulador)."""
    maquilador_data: NotRequired[str]
    """Datos del maquilador (DatosMaquilador)."""
    authorized_use: NotRequired[str]
    """Uso autorizado (UsoAutorizado)."""


class InvoiceCreateCartaPorteGoodsItemMaterial(TypedDict):
    """Tipo de materia (TipoMateria, c_TipoMateria) y su descripción si es «otra»."""
    type: str
    """Tipo de materia (TipoMateria), c_TipoMateria."""
    description: NotRequired[str]
    """Descripción de la materia (DescripcionMateria), con el tipo 05 otra."""


class InvoiceCreateCartaPorteGoodsItemCustomsDocsItem(TypedDict):
    type: str
    """Tipo de documento (TipoDocumento), c_DocumentoAduanero: 01 pedimento…"""
    pedimento: NotRequired[str]
    """Número de pedimento (NumPedimento), con el formato «NN  NN  NNNN  NNNNNNN». Solo con el tipo 01."""
    doc_id: NotRequired[str]
    """Identificador del documento aduanero (IdentDocAduanero), con un tipo distinto de 01."""
    importer_tax_id: NotRequired[str]
    """RFC del importador (RFCImpo), con un pedimento."""


class InvoiceCreateCartaPorteGoodsItemGuidesItem(TypedDict):
    number: str
    """Número de guía (NumeroGuiaIdentificacion)."""
    description: str
    """Descripción del contenido (DescripGuiaIdentificacion)."""
    weight_kg: float
    """Peso en kilogramos (PesoEnKg)."""


class InvoiceCreateCartaPorteGoodsItemQuantitiesItem(TypedDict):
    quantity: float
    """Cantidad que va a ese destino."""
    destination: int
    """El destino, por su posición en destinations (desde 0)."""
    mode: NotRequired[Literal["01", "02", "03", "04"]]
    """Medio en que va esa cantidad (CvesTransporte), c_CveTransporte."""


class InvoiceCreateCartaPorteGoodsItemDetail(TypedDict):
    """Marítimo: detalle de la mercancía (DetalleMercancia): kilos netos, tara y piezas."""
    net_kg: float
    """Peso neto en kg (PesoNeto)."""
    tare_kg: float
    """Tara en kg (PesoTara)."""
    pieces: NotRequired[int]
    """Número de piezas (NumPiezas)."""


class InvoiceCreateCartaPorteGoodsItem(TypedDict):
    product_key: str
    """Clave del bien transportado (BienesTransp), c_ClaveProdServCP."""
    description: str
    """Descripción de la mercancía (Descripcion)."""
    quantity: float
    """Cantidad (Cantidad)."""
    unit_key: str
    """Clave de unidad (ClaveUnidad), c_ClaveUnidad."""
    weight_kg: float
    """Peso en kilogramos (PesoEnKg)."""
    dimensions: NotRequired[str]
    """Dimensiones (Dimensiones), como 30/40/30cm o en plg."""
    hazmat: NotRequired[InvoiceCreateCartaPorteGoodsItemHazmat]
    """Material peligroso (MaterialPeligroso Sí): clave UN y embalaje."""
    cofepris: NotRequired[InvoiceCreateCartaPorteGoodsItemCofepris]
    """Datos COFEPRIS de la mercancía: sector y lo que pide cada uno (medicamentos, precursores, psicotrópicos, sustancias tóxicas, plaguicidas)."""
    value: NotRequired[float]
    """Valor de la mercancía (ValorMercancia); obligatorio en transporte aéreo."""
    currency: NotRequired[str]
    """Moneda del valor de la mercancía (Moneda), c_Moneda."""
    tariff: NotRequired[str]
    """Fracción arancelaria (FraccionArancelaria), 10 dígitos. Transporte internacional."""
    cce_uuid: NotRequired[str]
    """UUID del CFDI con complemento de comercio exterior (UUIDComercioExt)."""
    material: NotRequired[InvoiceCreateCartaPorteGoodsItemMaterial]
    """Tipo de materia (TipoMateria, c_TipoMateria) y su descripción si es «otra»."""
    customs_docs: NotRequired[list[InvoiceCreateCartaPorteGoodsItemCustomsDocsItem]]
    """Documentación aduanera (DocumentacionAduanera) de la mercancía en transporte internacional."""
    guides: NotRequired[list[InvoiceCreateCartaPorteGoodsItemGuidesItem]]
    """Paquetería: guías de los paquetes o tarimas (GuiasIdentificacion)."""
    quantities: NotRequired[list[InvoiceCreateCartaPorteGoodsItemQuantitiesItem]]
    """Cuánto va a cada destino (CantidadTransporta), por destino."""
    detail: NotRequired[InvoiceCreateCartaPorteGoodsItemDetail]
    """Marítimo: detalle de la mercancía (DetalleMercancia): kilos netos, tara y piezas."""
    stcc: NotRequired[str]
    """Ferroviario: clave STCC (ClaveSTCC)."""


class InvoiceCreateCartaPorteVehicleTrailersItem(TypedDict):
    type: str
    """Subtipo de remolque (SubTipoRem), c_SubTipoRem."""
    plate: str
    """Placa del remolque (Placa)."""


class InvoiceCreateCartaPorteVehicle(TypedDict):
    """Autotransporte (Autotransporte): vehículo, permiso SCT, seguros y remolques."""
    config: str
    """Configuración vehicular (ConfigVehicular), c_ConfigAutotransporte: C2, T3S2…"""
    plate: str
    """Placa (PlacaVM), sin guiones ni espacios."""
    year: int
    """Año del modelo (AnioModeloVM)."""
    gross_weight: float
    """Peso bruto vehicular en toneladas (PesoBrutoVehicular)."""
    permit_type: str
    """Tipo de permiso SCT (PermSCT), c_TipoPermiso."""
    permit_number: str
    """Número de permiso SCT (NumPermisoSCT)."""
    insurer: str
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: str
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    env_insurer: NotRequired[str]
    """Aseguradora de daños al medio ambiente (AseguraMedAmbiente); obligatoria con material peligroso."""
    env_policy: NotRequired[str]
    """Póliza de daños al medio ambiente (PolizaMedAmbiente)."""
    cargo_insurer: NotRequired[str]
    """Aseguradora de la carga (AseguraCarga)."""
    cargo_policy: NotRequired[str]
    """Póliza de la carga (PolizaCarga)."""
    premium: NotRequired[float]
    """Prima del seguro (PrimaSeguro)."""
    trailers: NotRequired[list[InvoiceCreateCartaPorteVehicleTrailersItem]]
    """Remolques o semirremolques (Remolque): tipo (c_SubTipoRem) y placa."""


class InvoiceCreateCartaPorteSeaContainersItemTrailersItem(TypedDict):
    type: str
    """Subtipo de remolque (SubTipoRem), c_SubTipoRem."""
    plate: str
    """Placa del remolque (Placa)."""


class InvoiceCreateCartaPorteSeaContainersItem(TypedDict):
    type: str
    """Tipo de contenedor (TipoContenedor), c_ContenedorMaritimo o c_Contenedor en ferroviario."""
    registration: NotRequired[str]
    """Matrícula (Matricula)."""
    seal: NotRequired[str]
    """Número de precinto (NumPrecinto)."""
    related_id_ccp: NotRequired[str]
    """Ferri: el IdCCP de la Carta Porte del autotransporte a bordo (IdCCPRelacionado)."""
    truck_plate: NotRequired[str]
    """Ferri: placa del vehículo a bordo (PlacaVMCCP)."""
    certified_at: NotRequired[str]
    """Ferri: fecha de certificación de la Carta Porte del vehículo (FechaCertificacionCCP)."""
    trailers: NotRequired[list[InvoiceCreateCartaPorteSeaContainersItemTrailersItem]]
    """Remolques o semirremolques (Remolque): tipo (c_SubTipoRem) y placa."""


class InvoiceCreateCartaPorteSea(TypedDict):
    """Transporte marítimo (TransporteMaritimo): embarcación, naviero y contenedores."""
    permit_type: NotRequired[str]
    """Tipo de permiso SCT (PermSCT), c_TipoPermiso."""
    permit_number: NotRequired[str]
    """Número de permiso SCT (NumPermisoSCT)."""
    insurer: NotRequired[str]
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: NotRequired[str]
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    vessel_type: str
    """Tipo de embarcación (TipoEmbarcacion), c_ConfigMaritima."""
    registration: str
    """Matrícula (Matricula)."""
    imo: str
    """Número IMO (NumeroOMI): IMO y 7 dígitos."""
    year: NotRequired[int]
    """Año de la embarcación (AnioEmbarcacion)."""
    vessel_name: NotRequired[str]
    """Nombre de la embarcación (NombreEmbarc)."""
    flag: str
    """Nacionalidad de la embarcación (NacionalidadEmbarc), c_Pais."""
    gross_tonnage: float
    """Unidades de arqueo bruto (UnidadesDeArqBruto)."""
    cargo_type: str
    """Tipo de carga (TipoCarga), c_ClaveTipoCarga."""
    length: NotRequired[float]
    """Eslora en metros (Eslora)."""
    beam: NotRequired[float]
    """Manga en metros (Manga)."""
    draft: NotRequired[float]
    """Calado en metros (Calado)."""
    depth: NotRequired[float]
    """Puntal en metros (Puntal)."""
    line: NotRequired[str]
    """Línea naviera (LineaNaviera)."""
    agent_name: str
    """Nombre del agente naviero consignatario (NombreAgenteNaviero)."""
    agent_authorization: str
    """Autorización del agente naviero (NumAutorizacionNaviero), c_NumAutorizacionNaviero."""
    voyage: NotRequired[str]
    """Número de viaje (NumViaje)."""
    bill_of_lading: NotRequired[str]
    """Número de conocimiento de embarque (NumConocEmbarc)."""
    temp_permit: NotRequired[str]
    """Permiso temporal de navegación (PermisoTempNavegacion), para una embarcación extranjera."""
    containers: NotRequired[list[InvoiceCreateCartaPorteSeaContainersItem]]
    """Contenedores (Contenedor)."""


class InvoiceCreateCartaPorteAirShipperForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteAirShipper(TypedDict):
    """Embarcador (RFCEmbarcador o NumRegIdTribEmbarc y ResidenciaFiscalEmbarc, NombreEmbarcador)."""
    tax_id: NotRequired[str]
    """RFC del embarcador (RFCEmbarcador)."""
    foreign: NotRequired[InvoiceCreateCartaPorteAirShipperForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    name: NotRequired[str]
    """Nombre del embarcador (NombreEmbarcador)."""


class InvoiceCreateCartaPorteAir(TypedDict):
    """Transporte aéreo (TransporteAereo): permiso, guía y transportista."""
    permit_type: str
    """Tipo de permiso SCT (PermSCT), c_TipoPermiso."""
    permit_number: str
    """Número de permiso SCT (NumPermisoSCT)."""
    aircraft: NotRequired[str]
    """Matrícula de la aeronave (MatriculaAeronave)."""
    insurer: NotRequired[str]
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: NotRequired[str]
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    waybill: str
    """Número de guía aérea (NumeroGuia), de 12 a 15 caracteres."""
    contract_place: NotRequired[str]
    """Lugar del contrato (LugarContrato)."""
    carrier: str
    """Código del transportista (CodigoTransportista), c_CodigoTransporteAereo."""
    shipper: NotRequired[InvoiceCreateCartaPorteAirShipper]
    """Embarcador (RFCEmbarcador o NumRegIdTribEmbarc y ResidenciaFiscalEmbarc, NombreEmbarcador)."""
    rate_charge: NotRequired[float]
    """Cargo por tasación (CargoPorTasacion)."""


class InvoiceCreateCartaPorteRailRightsItem(TypedDict):
    type: str
    """Tipo de derecho de paso (TipoDerechoDePaso), c_DerechosDePaso."""
    km: float
    """Kilometraje pagado (KilometrajePagado)."""


class InvoiceCreateCartaPorteRailCarsItemContainersItem(TypedDict):
    type: str
    """Tipo de contenedor (TipoContenedor), c_ContenedorMaritimo o c_Contenedor en ferroviario."""
    empty_kg: float
    """Peso del contenedor vacío en kg (PesoContenedorVacio)."""
    net_kg: float
    """Peso neto en kg (PesoNeto)."""


class InvoiceCreateCartaPorteRailCarsItem(TypedDict):
    type: str
    """Tipo de carro (TipoCarro), c_TipoCarro."""
    registration: str
    """Matrícula (Matricula)."""
    guide: str
    """Guía del carro (GuiaCarro)."""
    net_tons: float
    """Toneladas netas del carro (ToneladasNetasCarro)."""
    containers: NotRequired[list[InvoiceCreateCartaPorteRailCarsItemContainersItem]]
    """Contenedores (Contenedor)."""


class InvoiceCreateCartaPorteRail(TypedDict):
    """Transporte ferroviario (TransporteFerroviario): servicio, tráfico, derechos de paso y carros."""
    service: str
    """Tipo de servicio (TipoDeServicio), c_TipoDeServicio."""
    traffic: str
    """Tipo de tráfico (TipoDeTrafico), c_TipoDeTrafico."""
    insurer: NotRequired[str]
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: NotRequired[str]
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    rights: NotRequired[list[InvoiceCreateCartaPorteRailRightsItem]]
    """Derechos de paso (DerechosDePaso): tipo y kilómetros."""
    cars: list[InvoiceCreateCartaPorteRailCarsItem]
    """Carros (Carro)."""


class InvoiceCreateCartaPorteDriversItemForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteDriversItem(TypedDict):
    tax_id: str | Literal[""]
    """RFC del operador (RFCFigura); vacío si es extranjero (con foreign)."""
    license: str
    """Número de licencia (NumLicencia)."""
    name: str
    """Nombre del operador (NombreFigura)."""
    foreign: NotRequired[InvoiceCreateCartaPorteDriversItemForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""


class InvoiceCreateCartaPorteFiguresItemForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteFiguresItemAddress(TypedDict):
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""
    street: NotRequired[str]
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""
    country: NotRequired[str]
    """País (Pais), c_Pais. Por omisión MEX."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""


class InvoiceCreateCartaPorteFiguresItem(TypedDict):
    type: Literal["02", "03", "04", "05"]
    """Tipo de figura (TipoFigura): 02 propietario, 03 arrendador, 04 notificado, 05 integrante."""
    tax_id: NotRequired[str]
    """RFC de la figura (RFCFigura)."""
    foreign: NotRequired[InvoiceCreateCartaPorteFiguresItemForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    name: str
    """Nombre de la figura (NombreFigura)."""
    parts: NotRequired[list[str]]
    """Partes del transporte que posee o arrienda (ParteTransporte), c_ParteTransporte."""
    address: NotRequired[InvoiceCreateCartaPorteFiguresItemAddress]
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""


class InvoiceCreateCartaPorte(TypedDict):
    """Complemento Carta Porte 3.1 (traslado de mercancías)."""
    modes: NotRequired[list[Literal["01", "02", "03", "04"]]]
    """Cómo viajan las mercancías (c_CveTransporte): 01 autotransporte, 02 marítimo, 03 aéreo, 04 ferroviario; varios si es intermodal. Por omisión 01."""
    international: NotRequired[InvoiceCreateCartaPorteInternational]
    """Transporte internacional (TranspInternac Sí): entrada o salida, país, vía y regímenes aduaneros."""
    istmo: NotRequired[InvoiceCreateCartaPorteIstmo]
    """Corredor Interoceánico del Istmo de Tehuantepec: polos de origen y destino (c_RegistroISTMO)."""
    reverse_logistics: NotRequired[bool]
    """Autotransporte: true si es logística inversa, recolección o devolución."""
    origin: InvoiceCreateCartaPorteOrigin
    """Ubicación de origen (Ubicacion TipoUbicacion Origen): remitente, fecha y hora de salida y domicilio."""
    destinations: list[InvoiceCreateCartaPorteDestinationsItem]
    """Ubicaciones de destino (TipoUbicacion Destino), en orden: destinatario, llegada, distancia y domicilio."""
    goods: list[InvoiceCreateCartaPorteGoodsItem]
    """Mercancías (Mercancia) que se transportan."""
    vehicle: NotRequired[InvoiceCreateCartaPorteVehicle]
    """Autotransporte (Autotransporte): vehículo, permiso SCT, seguros y remolques."""
    sea: NotRequired[InvoiceCreateCartaPorteSea]
    """Transporte marítimo (TransporteMaritimo): embarcación, naviero y contenedores."""
    air: NotRequired[InvoiceCreateCartaPorteAir]
    """Transporte aéreo (TransporteAereo): permiso, guía y transportista."""
    rail: NotRequired[InvoiceCreateCartaPorteRail]
    """Transporte ferroviario (TransporteFerroviario): servicio, tráfico, derechos de paso y carros."""
    drivers: list[InvoiceCreateCartaPorteDriversItem]
    """Operadores (FiguraTransporte tipo 01): RFC, licencia y nombre."""
    figures: NotRequired[list[InvoiceCreateCartaPorteFiguresItem]]
    """Otras figuras de transporte: 02 propietario, 03 arrendador, 04 notificado, 05 integrante de coordinados."""


class InvoiceCreateIneEntitiesItem(TypedDict):
    key: str
    """Clave de la entidad (ClaveEntidad), 3 letras."""
    scope: NotRequired[Literal["Local", "Federal"]]
    """Ámbito (Ambito): Local o Federal."""
    accounting_ids: NotRequired[list[str]]
    """Claves de contabilidad (IdContabilidad)."""


class InvoiceCreateIne(TypedDict):
    """Complemento INE (procesos electorales)."""
    process: Literal["Ordinario", "Precampaña", "Campaña"]
    """Tipo de proceso (TipoProceso): Ordinario, Precampaña o Campaña."""
    committee: NotRequired[Literal["Ejecutivo Nacional", "Ejecutivo Estatal", "Directivo Estatal"]]
    """Tipo de comité (TipoComite), con el proceso Ordinario."""
    accounting_id: NotRequired[str]
    """Clave de contabilidad (IdContabilidad), hasta 6 dígitos."""
    entities: NotRequired[list[InvoiceCreateIneEntitiesItem]]
    """Entidades (Entidad): clave del estado, ámbito y claves de contabilidad."""


class InvoiceCreateLeyendasItem(TypedDict):
    text: str
    """Texto de la leyenda (textoLeyenda)."""
    disposition: NotRequired[str]
    """Disposición fiscal (disposicionFiscal), por ejemplo LISR."""
    norm: NotRequired[str]
    """Norma o artículo (norma)."""


class InvoiceCreateDonation(TypedDict):
    """Complemento de donatarias."""
    in_kind: NotRequired[bool]
    """true si el donativo es en especie (va sin forma de pago en efectivo)."""
    deducted: NotRequired[bool]
    """true si el donativo es deducible para quien lo da."""


class InvoiceCreateLocalTaxesItem(TypedDict):
    retention: bool
    """true si es una retención local; false si es un traslado."""
    name: str
    """Nombre del impuesto local (ImpLocTrasladado o ImpLocRetenido), como ISH."""
    rate: float
    """Tasa en por ciento (TasadeTraslado o TasadeRetencion)."""
    amount: float
    """Importe del impuesto local."""


class InvoiceCreateComercioExteriorOwnersItem(TypedDict):
    tax_id: str
    """Número de registro tributario del propietario (NumRegIdTrib)."""
    country: str
    """País de residencia del propietario (ResidenciaFiscal), c_Pais."""


class InvoiceCreateComercioExteriorIssuerAddress(TypedDict):
    """Domicilio del emisor (Emisor Domicilio): calle y números; lo demás sale de su código postal."""
    street: str
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: NotRequired[str]
    """Código postal del emisor (CodigoPostal)."""


class InvoiceCreateComercioExteriorReceiverAddress(TypedDict):
    """Domicilio del receptor en el extranjero (Receptor Domicilio)."""
    street: str
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    state: NotRequired[str]
    """Estado (Estado), c_Estado para USA y CAN."""
    country: str
    """País (Pais), c_Pais."""
    zip: str
    """Código postal en su país (CodigoPostal)."""


class InvoiceCreateComercioExteriorRecipientAddress(TypedDict):
    """Domicilio del destinatario (Domicilio)."""
    street: str
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    country: str
    """País (Pais), c_Pais. Por omisión MEX."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""


class InvoiceCreateComercioExteriorRecipient(TypedDict):
    """Destinatario, si no es el receptor (Destinatario)."""
    name: NotRequired[str]
    """Nombre del destinatario (Nombre)."""
    tax_id: NotRequired[str]
    """Número de registro tributario del destinatario (NumRegIdTrib)."""
    address: InvoiceCreateComercioExteriorRecipientAddress
    """Domicilio del destinatario (Domicilio)."""


class InvoiceCreateComercioExteriorGoodsItem(TypedDict):
    id: NotRequired[str]
    """Número de identificación de la mercancía (NoIdentificacion): el sku de su concepto."""
    tariff: NotRequired[str]
    """Fracción arancelaria (FraccionArancelaria), 10 dígitos. Transporte internacional."""
    unit: str
    """Unidad aduana (UnidadAduana), c_UnidadAduana."""
    quantity: NotRequired[float]
    """Cantidad en la unidad aduana (CantidadAduana)."""
    unit_value_usd: NotRequired[float]
    """Valor unitario en dólares (ValorUnitarioAduana)."""


class InvoiceCreateComercioExterior(TypedDict):
    """Complemento de comercio exterior 2.0."""
    motive: NotRequired[Literal["05"]]
    """Motivo de traslado (MotivoTraslado): 05 envío de mercancías propias."""
    owners: NotRequired[list[InvoiceCreateComercioExteriorOwnersItem]]
    """Propietarios de la mercancía si no es el emisor (Propietario), con motive 05."""
    incoterm: NotRequired[str]
    """Incoterm (Incoterm), c_INCOTERM: EXW, FOB, CIF, DAP, DDP…"""
    certificate: NotRequired[str]
    """Número de certificado de origen (NumCertificadoOrigen)."""
    usd_rate: float
    """Tipo de cambio a dólares (TipoCambioUSD)."""
    issuer_curp: NotRequired[str]
    """CURP del emisor persona física (Emisor Curp)."""
    issuer_address: NotRequired[InvoiceCreateComercioExteriorIssuerAddress]
    """Domicilio del emisor (Emisor Domicilio): calle y números; lo demás sale de su código postal."""
    receiver_address: NotRequired[InvoiceCreateComercioExteriorReceiverAddress]
    """Domicilio del receptor en el extranjero (Receptor Domicilio)."""
    recipient: NotRequired[InvoiceCreateComercioExteriorRecipient]
    """Destinatario, si no es el receptor (Destinatario)."""
    goods: list[InvoiceCreateComercioExteriorGoodsItem]
    """Mercancías (Mercancia), una por concepto exportado."""
    notes: NotRequired[str]
    """Observaciones del complemento (Observaciones)."""


class InvoiceCreateGlobal(TypedDict):
    """Factura global a público en general (InformacionGlobal): periodicidad, meses y año."""
    periodicity: str
    """Periodicidad (Periodicidad), c_Periodicidad: 01 diario, 02 semanal, 03 quincenal, 04 mensual, 05 bimestral."""
    months: str
    """Meses (Meses), c_Meses: 01 a 12, o 13 a 18 bimestres."""
    year: int
    """Año (Año)."""


class InvoiceCreateAddenda(TypedDict):
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""
    type: Literal["walmart", "soriana", "liverpool", "homedepot", "chedraui", "generic"]
    values: dict[str, str]
    customer: NotRequired[dict[str, str]]


class InvoiceCreateRelated(TypedDict):
    """CFDI relacionados (CfdiRelacionados): tipo de relación de c_TipoRelacion y los UUID."""
    relationship: str
    """Tipo de relación (TipoRelacion): 01 nota de crédito, 03 devolución, 04 sustitución, 07 anticipo…"""
    uuids: list[str]
    """Folios fiscales relacionados."""


# Una factura (CFDI 4.0). Un campo que no existe se rechaza con parameter_unknown, nunca se ignora.
InvoiceCreate = TypedDict(
    "InvoiceCreate",
    {
        "issuer": "NotRequired[str]",
        "customer": "str | InvoiceCreateCustomer",
        "items": "list[InvoiceCreateItemsItem]",
        "type": "NotRequired[Literal[\"I\", \"T\"]]",
        "carta_porte": "NotRequired[InvoiceCreateCartaPorte]",
        "ine": "NotRequired[InvoiceCreateIne]",
        "leyendas": "NotRequired[list[InvoiceCreateLeyendasItem]]",
        "donation": "NotRequired[InvoiceCreateDonation]",
        "local_taxes": "NotRequired[list[InvoiceCreateLocalTaxesItem]]",
        "export": "NotRequired[Literal[\"01\", \"02\", \"03\", \"04\"]]",
        "comercio_exterior": "NotRequired[InvoiceCreateComercioExterior]",
        "global": "NotRequired[InvoiceCreateGlobal]",
        "use": "NotRequired[str]",
        "payment_form": "NotRequired[str]",
        "payment_method": "NotRequired[Literal[\"PUE\", \"PPD\"]]",
        "paid_later": "NotRequired[bool]",
        "currency": "NotRequired[str]",
        "series": "NotRequired[str]",
        "notes": "NotRequired[str]",
        "pdf_language": "NotRequired[Literal[\"es\", \"en\", \"bi\"]]",
        "addenda": "NotRequired[InvoiceCreateAddenda]",
        "related": "NotRequired[InvoiceCreateRelated]",
        "exchange_rate": "NotRequired[float]",
        "folio": "NotRequired[int]",
        "continue_sequence": "NotRequired[bool]",
        "date": "NotRequired[str]",
        "send_email": "NotRequired[bool]",
        "email_cc": "NotRequired[str | None]",
        "metadata": "NotRequired[dict[str, str]]",
    },
)


class ResetTestDataParams(TypedDict):
    seed: NotRequired[bool]
    """true (por omisión) para dejarle a cada emisor de pruebas 3 clientes y 3 productos de ejemplo. false para dejarlo vacío."""


class CreateIssuerParams(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    employer_registration: NotRequired[str | None]
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class ListIssuersParams(TypedDict):
    """Los parámetros de GET /v1/issuers."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    tax_id: NotRequired[str]
    """Solo el de este RFC."""
    include_archived: NotRequired[bool]
    """true para incluir los archivados."""


class UpdateIssuerParams(TypedDict):
    legal_name: NotRequired[str]
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: NotRequired[str]
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    employer_registration: NotRequired[str | None]
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""
    metadata: NotRequired[dict[str, str] | None]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class UploadCertificateParams(TypedDict):
    cer: str
    """El archivo .cer en base64 (puede traer el prefijo data:)."""
    key: str
    """El archivo .key en base64 (puede traer el prefijo data:)."""
    password: str
    """La contraseña de la llave privada (.key). Se usa para abrirla y no se guarda en texto."""


class SignEfirmaParams(TypedDict):
    cer: str
    """El archivo .cer en base64 (puede traer el prefijo data:)."""
    key: str
    """El archivo .key en base64 (puede traer el prefijo data:)."""
    password: str
    """La contraseña de la llave privada (.key). Se usa para abrirla y no se guarda en texto."""
    keep_for_downloads: NotRequired[bool]
    """true para guardarla (cifrada) y poder pedir al SAT las facturas del emisor con POST /v1/sat_downloads. Sin esto solo firma el contrato con el PAC y no se guarda."""


class CreateIssuerOnboardingLinkParams(TypedDict):
    return_url: NotRequired[str]
    """A dónde regresa el botón al terminar, por ejemplo la página de su plataforma donde su cliente sigue. Sin ella, la página solo dice que ya terminó."""
    expires_in_hours: NotRequired[int]
    """Horas que la liga sirve, de 1 a 168 (7 días). Por omisión 24."""


class ListInvoicesParams(TypedDict):
    """Los parámetros de GET /v1/invoices."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["valid", "pending", "canceled", "rejected", "processing"]]
    """valid, pending, canceled, rejected o processing."""
    type: NotRequired[Literal["I", "E", "P", "T", "N"]]
    """I, E, P, T o N."""
    customer: NotRequired[str]
    """RFC del cliente."""
    created_gte: NotRequired[str]
    """Creadas desde, en ISO 8601. Un día solo (2026-10-01) cuenta desde su inicio en hora de la Ciudad de México."""
    created_lte: NotRequired[str]
    """Creadas hasta, en ISO 8601. Un día solo (2026-10-31) incluye el día completo en hora de la Ciudad de México."""


class GetInvoiceParams(TypedDict):
    """Los parámetros de GET /v1/invoices/{id}."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""
    refresh: NotRequired[bool]
    """true para preguntar su estado al SAT ahora (cancelaciones en espera)."""


class GetInvoicePdfParams(TypedDict):
    """Los parámetros de GET /v1/invoices/{id}/pdf."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class GetInvoiceXmlParams(TypedDict):
    """Los parámetros de GET /v1/invoices/{id}/xml."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class SendInvoiceParams(TypedDict):
    to: NotRequired[str]
    """A quién (correos separados por comas)."""
    cc: NotRequired[str | None]
    """Con copia (correos separados por comas)."""


class CancelInvoiceParams(TypedDict):
    motive: NotRequired[Literal["01", "02", "03", "04"]]
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 nominativa en una global."""
    substitution: NotRequired[str]
    """El comprobante que sustituye a este (su id o su UUID), con el motivo 01."""


class CreatePaymentParamsDocumentsItem(TypedDict):
    invoice: str
    """La factura (inv_… o su UUID)."""
    amount: float
    """Lo que se paga de esa factura (ImpPagado), en la moneda de la factura."""
    received: NotRequired[float | None]
    """Solo si la factura es de otra moneda que el pago: lo que recibió por ella en la moneda del pago. Fiscalisto calcula la equivalencia (EquivalenciaDR)."""


class CreatePaymentParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    date: NotRequired[str]
    """Fecha en que le pagaron (FechaPago), AAAA-MM-DD. Por omisión hoy."""
    payment_form: str
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    operation_number: NotRequired[str | None]
    """Número de operación del pago (NumOperacion), como el rastreo SPEI."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float | None]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    series: NotRequired[str]
    """Serie (Serie), hasta 25 caracteres. Cada serie lleva sus propios folios."""
    documents: list[CreatePaymentParamsDocumentsItem]
    """Las facturas que paga (DoctoRelacionado)."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email: NotRequired[str]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    email_cc: NotRequired[str | None]
    """Correos con copia, separados por comas."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class CreateCreditNoteParams(TypedDict):
    invoice: str
    """La factura (inv_… o su UUID)."""
    amount: float
    """Importe de la nota antes de impuestos: Fiscalisto agrega el IVA y las retenciones de la factura en la misma proporción."""
    description: NotRequired[str]
    """Descripción del concepto de la nota (Descripcion), como «Descuento por pronto pago»."""
    payment_form: str
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    relationship: NotRequired[Literal["01", "03"]]
    """Tipo de relación (TipoRelacion): 01 nota de crédito, 03 devolución, 04 sustitución, 07 anticipo…"""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email: NotRequired[str]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    email_cc: NotRequired[str | None]
    """Correos con copia, separados por comas."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class CreateAdvanceParamsCustomerForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class CreateAdvanceParamsCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[CreateAdvanceParamsCustomerForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class CreateAdvanceParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    customer: str | CreateAdvanceParamsCustomer
    """Cliente (Receptor): el id de uno de su catálogo (cus_…) o sus datos en un objeto."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    amount: float
    """Lo que pagó el cliente, con IVA incluido."""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    payment_form: str
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    series: NotRequired[str]
    """Serie (Serie), hasta 25 caracteres. Cada serie lleva sus propios folios."""
    notes: NotRequired[str]
    """Observaciones que aparecen en el PDF (no van en el XML)."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email_cc: NotRequired[str | None]
    """Correos con copia, separados por comas."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class ListAdvancesParams(TypedDict):
    """Los parámetros de GET /v1/advances."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    customer: NotRequired[str]
    """RFC del cliente."""


class ApplyAdvanceParamsRemainder(TypedDict):
    """Cómo se paga lo que falta del anticipo: ahora con su forma de pago, o después (PPD)."""
    paid_now: bool
    """true si lo que falta se paga ahora (PUE); false si después (PPD)."""
    payment_form: NotRequired[str]
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""


class CreateRetentionParamsRecipient(TypedDict):
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    foreign: NotRequired[bool]
    """true si el receptor es extranjero (sin RFC)."""
    tax_id: NotRequired[str | None]
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""


class CreateRetentionParamsPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    year: int
    """Año (Ejercicio)."""
    month: NotRequired[int]
    """Un solo mes, del 1 al 12 (MesIni y MesFin iguales)."""
    from_month: NotRequired[int]
    """Mes inicial (MesIni), 1 a 12."""
    to_month: NotRequired[int]
    """Mes final (MesFin), 1 a 12, del mismo año."""


class CreateRetentionParamsTotals(TypedDict):
    """Totales (Totales)."""
    operation: float
    """Monto total de la operación (MontoTotOperacion)."""
    taxed: NotRequired[float]
    """Monto gravado (MontoTotGrav). Por omisión, operation menos exempt."""
    exempt: NotRequired[float]
    """Monto exento (MontoTotExent). Por omisión 0."""


class CreateRetentionParamsTaxesItem(TypedDict):
    tax: str
    """Impuesto: isr, iva o ieps (ImpuestoRet 001, 002, 003)."""
    base: float
    """Base del impuesto retenido (BaseRet)."""
    amount: float
    """Monto retenido (MontoRet)."""
    payment_type: NotRequired[str]
    """Tipo de pago de la retención (TipoPagoRet): 01 definitivo IVA, 02 definitivo IEPS, 03 definitivo ISR, 04 provisional ISR. Por omisión el usual de cada impuesto."""


class CreateRetentionParamsDividends(TypedDict):
    """Complemento de dividendos."""
    type: Literal["01", "02", "03", "04", "05", "06"]
    """Tipo de dividendo o utilidad distribuida (CveTipDivOUtil), c_TipoDividendoOUtilidadDistribuida."""
    isr_mexico: float
    """ISR acreditable en México (MontISRAcredRetMexico)."""
    isr_foreign: float
    """ISR acreditable en el extranjero (MontISRAcredRetExtranjero)."""
    foreign_retention: NotRequired[float | None]
    """Retención en el extranjero sobre dividendos (MontRetExtDivExt)."""
    company: Literal["nacional", "extranjera"]
    """Tipo de sociedad que distribuye (TipoSocDistrDiv): nacional o extranjera."""
    national_credit: NotRequired[float | None]
    """ISR acreditable nacional (MontISRAcredNal)."""
    accumulated_national: NotRequired[float | None]
    """Dividendo acumulable nacional (MontDivAcumNal)."""
    accumulated_foreign: NotRequired[float | None]
    """Dividendo acumulable extranjero (MontDivAcumExt)."""


class CreateRetentionParamsInterest(TypedDict):
    """Complemento de intereses."""
    financial_system: bool
    """true si los intereses vienen del sistema financiero (SistFinanciero)."""
    retirement: bool
    """true si se retiraron los intereses en el periodo (RetiroAORESRetInt)."""
    derivatives: bool
    """true si son operaciones financieras derivadas (OperFinancDerivad)."""
    nominal: float
    """Interés nominal (MontIntNominal)."""
    real: float
    """Interés real (MontIntReal)."""
    loss: float
    """Pérdida (Perdida)."""


class CreateRetentionParamsForeignPayment(TypedDict):
    """Complemento de pagos a extranjeros."""
    beneficiary: bool
    """true si quien recibe es el beneficiario efectivo (EsBenefEfectDelCobro)."""
    country: NotRequired[str | None]
    """País de residencia del extranjero (PaisDeResidParaEfecFisc), 2 letras."""
    concept: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    """Concepto del pago (ConceptoPago), c_TipoContribuyenteSujetoRetencion."""
    description: str
    """Descripción del concepto (DescripcionConcepto)."""
    beneficiary_tax_id: NotRequired[str | None]
    """RFC del beneficiario, si no es quien recibe (RFC)."""
    beneficiary_curp: NotRequired[str | None]
    """CURP del beneficiario (CURP)."""
    beneficiary_name: NotRequired[str | None]
    """Nombre o razón social del beneficiario (NomDenRazSocB)."""


class CreateRetentionParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    code: str
    """Clave de la retención (CveRetenc), c_CveRetenc: 01 servicios profesionales, 05 arrendamiento, 14 dividendos, 16 intereses, 18 pagos al extranjero…"""
    description: NotRequired[str | None]
    """Descripción de la retención (DescRetenc); obligatoria con la clave 25 (otro tipo)."""
    recipient: CreateRetentionParamsRecipient
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    period: CreateRetentionParamsPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    totals: CreateRetentionParamsTotals
    """Totales (Totales)."""
    taxes: list[CreateRetentionParamsTaxesItem]
    """Impuestos del comprobante, por tipo."""
    dividends: NotRequired[CreateRetentionParamsDividends]
    """Complemento de dividendos."""
    interest: NotRequired[CreateRetentionParamsInterest]
    """Complemento de intereses."""
    foreign_payment: NotRequired[CreateRetentionParamsForeignPayment]
    """Complemento de pagos a extranjeros."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email: NotRequired[str]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class ListRetentionsParams(TypedDict):
    """Los parámetros de GET /v1/retentions."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["valid", "canceled", "rejected", "processing"]]
    """valid, canceled, rejected o processing."""
    recipient: NotRequired[str]
    """RFC del receptor."""
    year: NotRequired[str]
    """Ejercicio, 4 dígitos."""


class GetRetentionParams(TypedDict):
    """Los parámetros de GET /v1/retentions/{id}."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""
    refresh: NotRequired[bool]
    """true para preguntar su estado al SAT ahora (cancelaciones en espera)."""


class GetRetentionPdfParams(TypedDict):
    """Los parámetros de GET /v1/retentions/{id}/pdf."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class GetRetentionXmlParams(TypedDict):
    """Los parámetros de GET /v1/retentions/{id}/xml."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class SendRetentionParams(TypedDict):
    to: NotRequired[str]
    """A quién (correos separados por comas)."""


class CancelRetentionParams(TypedDict):
    motive: NotRequired[Literal["01", "02", "03", "04"]]
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 nominativa en una global."""
    substitution: NotRequired[str]
    """El comprobante que sustituye a este (su id o su UUID), con el motivo 01."""


class CreateEmployeeParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre completo del empleado, como en su constancia de situación fiscal."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    curp: str
    """CURP, 18 caracteres."""
    social_security_number: str
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del empleado, a donde van sus recibos con send_email."""
    start_date: str
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    end_date: NotRequired[str | None]
    """Último día trabajado si ya no trabaja ahí, AAAA-MM-DD."""
    daily_salary: float
    """Salario diario."""
    integrated_daily_salary: float
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    contract_type: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    workday_type: NotRequired[str]
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    periodicity: NotRequired[str]
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    risk_class: NotRequired[str]
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    state: str
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""
    border_zone: NotRequired[bool]
    """true si trabaja en la zona libre de la frontera norte (salario mínimo de frontera)."""
    unionized: NotRequired[bool]
    """true si es sindicalizado (Sindicalizado)."""
    department: NotRequired[str | None]
    """Departamento (Departamento)."""
    position: NotRequired[str | None]
    """Puesto (Puesto)."""


class ListEmployeesParams(TypedDict):
    """Los parámetros de GET /v1/employees."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class UpdateEmployeeParams(TypedDict):
    number: NotRequired[str]
    """Número de empleado (NumEmpleado)."""
    name: NotRequired[str]
    """Nombre completo del empleado, como en su constancia de situación fiscal."""
    tax_id: NotRequired[str]
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    curp: NotRequired[str]
    """CURP, 18 caracteres."""
    social_security_number: NotRequired[str]
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del empleado, a donde van sus recibos con send_email."""
    start_date: NotRequired[str]
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    end_date: NotRequired[str | None]
    """Último día trabajado si ya no trabaja ahí, AAAA-MM-DD."""
    daily_salary: NotRequired[float]
    """Salario diario."""
    integrated_daily_salary: NotRequired[float]
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    contract_type: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    workday_type: NotRequired[str]
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    periodicity: NotRequired[str]
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    risk_class: NotRequired[str]
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    state: NotRequired[str]
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""
    border_zone: NotRequired[bool]
    """true si trabaja en la zona libre de la frontera norte (salario mínimo de frontera)."""
    unionized: NotRequired[bool]
    """true si es sindicalizado (Sindicalizado)."""
    department: NotRequired[str | None]
    """Departamento (Departamento)."""
    position: NotRequired[str | None]
    """Puesto (Puesto)."""


class CreatePayrollReceiptParamsPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: NotRequired[str]
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class CreatePayrollReceiptParams(TypedDict):
    employee: str
    """El empleado (emp_…)."""
    period: CreatePayrollReceiptParamsPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    days: NotRequired[float]
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class PreviewPayrollReceiptParamsPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: NotRequired[str]
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class PreviewPayrollReceiptParams(TypedDict):
    employee: str
    """El empleado (emp_…)."""
    period: PreviewPayrollReceiptParamsPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    days: NotRequired[float]
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class CreateInvoiceBatchParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    name: NotRequired[str]
    """Nombre del lote, para usted."""
    invoices: list[CreateInvoiceBatchParamsInvoicesItem]
    """Las facturas, como el cuerpo de POST /v1/invoices, con reference opcional."""


class ListInvoiceBatchesParams(TypedDict):
    """Los parámetros de GET /v1/invoice_batches."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class ValidateTaxIdParams(TypedDict):
    tax_id: str
    """El RFC del cliente."""
    legal_name: NotRequired[str]
    """El nombre o razón social que va a poner en la factura."""
    tax_system: NotRequired[str]
    """Su régimen fiscal (c_RegimenFiscal), como 601 o 612."""
    zip: NotRequired[str]
    """El código postal de su domicilio fiscal."""
    use: NotRequired[str]
    """El uso del CFDI (c_UsoCFDI), como G03."""
    cif_id: NotRequired[str]
    """El idCIF de su constancia de situación fiscal (11 dígitos, arriba a la izquierda, junto al QR). Con él se compara todo con lo que tiene el SAT."""


class CreateCustomerParamsForeign(TypedDict):
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class CreateCustomerParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del cliente (varios separados por comas), a donde van sus facturas con send_email."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    foreign: NotRequired[CreateCustomerParamsForeign | None]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class ListCustomersParams(TypedDict):
    """Los parámetros de GET /v1/customers."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    tax_id: NotRequired[str]
    """Solo el de este RFC."""


class UpdateCustomerParamsForeign(TypedDict):
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class UpdateCustomerParams(TypedDict):
    tax_id: NotRequired[str]
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: NotRequired[str]
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: NotRequired[str]
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del cliente (varios separados por comas), a donde van sus facturas con send_email."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    foreign: NotRequired[UpdateCustomerParamsForeign | None]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class CreateCustomerDataRequestParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…) que va a facturarle. Por omisión, su único emisor."""
    reference: NotRequired[str]
    """Su id para este cliente o pedido, como «Pedido 1042». El cliente la ve arriba del formulario y viene de vuelta en el evento."""
    description: NotRequired[str]
    """Una línea que el cliente ve arriba del formulario: para qué son sus datos."""
    expires_in_days: NotRequired[int]
    """Días que la liga sirve, de 1 a 60. Por omisión 60."""


class ListCustomerDataRequestsParams(TypedDict):
    """Los parámetros de GET /v1/customer_data_requests."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class CreateProductParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    name: NotRequired[str | None]
    """Nombre corto para encontrarlo, solo para usted; en el CFDI va description."""
    description: str
    """Descripción."""
    product_key: str
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float | None]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""


class ListProductsParams(TypedDict):
    """Los parámetros de GET /v1/products."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    sku: NotRequired[str]
    """Solo el de este SKU."""
    product_key: NotRequired[str]
    """Solo los de esta clave del SAT."""


class UpdateProductParams(TypedDict):
    name: NotRequired[str | None]
    """Nombre corto para encontrarlo, solo para usted; en el CFDI va description."""
    description: NotRequired[str]
    """Descripción."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float | None]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""


class GetSatCatalogParams(TypedDict):
    """Los parámetros de GET /v1/sat_catalogs/{name}."""
    q: NotRequired[str]
    """Qué buscar: palabras («consultoría») o una clave."""
    limit: NotRequired[int]
    """Hasta cuántos, de 1 a 100 (búsquedas). Por omisión 20."""


class CheckSatListsParams(TypedDict):
    tax_ids: list[str]
    """Los RFC a revisar, hasta 1000."""


CreateSatDownloadParams = TypedDict(
    "CreateSatDownloadParams",
    {
        "issuer": "NotRequired[str]",
        "direction": "NotRequired[Literal[\"received\", \"issued\"]]",
        "from": "str",
        "to": "str",
        "type": "NotRequired[Literal[\"I\", \"E\", \"P\", \"T\", \"N\"]]",
        "counterparty_tax_id": "NotRequired[str]",
        "uuid": "NotRequired[str]",
    },
)


class ListSatDownloadsParams(TypedDict):
    """Los parámetros de GET /v1/sat_downloads."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class ListSatInvoicesParams(TypedDict):
    """Los parámetros de GET /v1/sat_invoices."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    direction: NotRequired[Literal["received", "issued"]]
    """received (por omisión) o issued."""
    type: NotRequired[Literal["I", "E", "P", "T", "N"]]
    """I, E, P, T o N."""
    counterparty_tax_id: NotRequired[str]
    """El RFC de quien la emitió (recibidas) o de quien la recibió (emitidas)."""
    date_gte: NotRequired[str]
    """Con fecha desde este día (AAAA-MM-DD)."""
    date_lte: NotRequired[str]
    """Con fecha hasta este día (AAAA-MM-DD), incluido."""


class CreateTicketParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…) que vendió. Por omisión, su único emisor."""
    folio: str
    """El folio de la venta en su sistema, único por emisor: letras, números, - _ / y punto. Registrar el mismo folio con el mismo total responde el ticket que ya existe."""
    total: float
    """Lo que se cobró, impuestos incluidos y sin propina."""
    tip: NotRequired[float]
    """Propina: no va en la factura. El cliente puede escribir el total con ella o sin ella."""
    payment_form: str
    """c_FormaPago de la venta: 01 efectivo, 04 tarjeta de crédito…"""
    sold_at: NotRequired[str]
    """Cuándo se vendió: ISO 8601 (2026-10-02T13:45:00-06:00) o la hora de la Ciudad de México sin zona. Por omisión, ahora."""
    product: NotRequired[str]
    """Un producto (prd_…) de su catálogo: el concepto de la factura."""
    description: NotRequired[str]
    """El concepto. Con `product`, reemplaza su descripción; sin él, va con `product_key`."""
    product_key: NotRequired[str]
    """c_ClaveProdServ (8 dígitos), si no usa `product`."""
    unit_key: NotRequired[str]
    """c_ClaveUnidad. Por omisión, la de la clave del producto."""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA incluida en el total. Por omisión 0.16."""


class ListTicketsParams(TypedDict):
    """Los parámetros de GET /v1/tickets."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["pending", "invoiced", "global", "cancelled"]]
    """pending, invoiced, global o cancelled."""
    sold_at_gte: NotRequired[str]
    """Vendidos desde (ISO 8601 o AAAA-MM-DD)."""
    sold_at_lte: NotRequired[str]
    """Vendidos hasta (ISO 8601 o AAAA-MM-DD, el día completo)."""


class UpdateSelfInvoicingParams(TypedDict):
    window: NotRequired[Literal["month", "days"]]
    """Hasta cuándo se puede facturar un ticket: `month`, hasta el fin del mes de la venta (lo usual ante el SAT); `days`, `window_days` días después."""
    window_days: NotRequired[int]
    """Días para facturar con `window: days`."""
    global_periodicity: NotRequired[Literal["01", "02", "03", "04"]]
    """c_Periodicidad de la factura global con los tickets que nadie facturó: 01 diaria, 02 semanal, 03 quincenal, 04 mensual."""


class CreateWebhookEndpointParams(TypedDict):
    url: str
    """Dirección https de su servidor que recibe los avisos."""
    events: NotRequired[list[str] | None]
    """Eventos que quiere recibir, o ["*"] para todos (por omisión). Ver la lista en Webhooks."""
    description: NotRequired[str | None]
    """Para qué es, para usted (no se manda en los eventos)."""


class ListWebhookEndpointsParams(TypedDict):
    """Los parámetros de GET /v1/webhook_endpoints."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""


class UpdateWebhookEndpointParams(TypedDict):
    url: NotRequired[str]
    """Dirección https de su servidor que recibe los avisos."""
    events: NotRequired[list[str] | None]
    """Eventos que quiere recibir, o ["*"] para todos (por omisión). Ver la lista en Webhooks."""
    description: NotRequired[str | None]
    """Para qué es, para usted (no se manda en los eventos)."""
    disabled: NotRequired[bool]
    """true para apagarlo sin borrarlo."""


class RollWebhookSecretParams(TypedDict):
    previous_secret_expires_in: NotRequired[int]
    """Segundos que el secreto anterior sigue firmando, de 0 (deja de firmar ya: úselo si se filtró) a 86400. Por omisión 86400 (24 horas)."""


class TestWebhookEndpointParams(TypedDict):
    type: NotRequired[Literal["invoice.stamped", "invoice.failed", "invoice.canceled", "invoice.cancellation_pending", "invoice.cancellation_rejected", "retention.stamped", "retention.failed", "retention.canceled", "invoice_batch.completed", "customer_data_request.completed", "sat_download.completed", "sat_download.failed", "ticket.invoiced", "ticket.included_in_global", "issuer.ready", "balance.low"]]
    """El evento a mandar. Por omisión invoice.stamped."""


class ListEventsParams(TypedDict):
    """Los parámetros de GET /v1/events."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    type: NotRequired[Literal["invoice.stamped", "invoice.failed", "invoice.canceled", "invoice.cancellation_pending", "invoice.cancellation_rejected", "retention.stamped", "retention.failed", "retention.canceled", "invoice_batch.completed", "customer_data_request.completed", "sat_download.completed", "sat_download.failed", "ticket.invoiced", "ticket.included_in_global", "issuer.ready", "balance.low"]]
    """Solo de este tipo."""
    object: NotRequired[str]
    """Solo los de este objeto (inv_…, ret_…, bat_…)."""


class ApplyAdvanceParams(InvoiceCreate):
    """El cuerpo de POST /v1/invoices (la factura de lo vendido) con method y remainder."""
    method: NotRequired[Literal["egreso", "remanente"]]
    """egreso (la factura completa y después una nota de crédito por el anticipo, opción A) o remanente (la factura solo por lo que falta, opción B)."""
    remainder: NotRequired[ApplyAdvanceParamsRemainder]
    """Cómo se paga lo que falta del anticipo: ahora con su forma de pago, o después (PPD)."""


class CreateInvoiceBatchParamsInvoicesItem(InvoiceCreate):
    """Una factura del lote: el cuerpo de POST /v1/invoices, sin issuer, type, global ni metadata (el lote es de un emisor y de facturas de ingreso), con su reference."""
    reference: NotRequired[str]
    """Su identificador de esta factura (su número de pedido), hasta 100 caracteres."""
