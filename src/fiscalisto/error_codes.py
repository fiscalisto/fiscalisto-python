# Generado por `bun run openapi` desde la lista de errores de la API: no lo edite.
"""Los códigos de error de la API, para comparar ``e.code`` sin escribir el texto."""

from __future__ import annotations

from typing import Final, Literal

__all__ = ["ErrorCode", "ErrorCodeValue"]


class ErrorCode:
    """``if e.code == ErrorCode.INVOICE_REJECTED: …`` Vea https://fiscalisto.com/docs/api/errores."""

    API_VERSION_INVALID: Final = "api_version_invalid"
    """No existe esa versión de la API (en Fiscalisto-Version o api_version). El mensaje dice cuáles hay; vea Versiones."""

    BANK_TRANSACTION_INVALID: Final = "bank_transaction_invalid"
    """El depósito no se puede conciliar, clasificar o reabrir así (ya está conciliado, las facturas son de otro cliente o una está cancelada…). El mensaje dice por qué."""

    BATCH_INVALID: Final = "batch_invalid"
    """Una factura del lote no pasa la revisión; param dice cuál (invoices.3.items.0.unit_price). Ninguna del lote se timbró."""

    BODY_TOO_LARGE: Final = "body_too_large"
    """El cuerpo pasa de 10 MB. Divida el trabajo en varios lotes."""

    BRANCH_EXISTS: Final = "branch_exists"
    """El emisor ya tiene una sucursal con ese código postal (cada una lleva el suyo); el mensaje dice cuál. Si está archivada, restáurela con archived: false."""

    BRANCH_HAS_INVOICES: Final = "branch_has_invoices"
    """La sucursal ya facturó, así que no se borra: archívela con archived: true y sus facturas la siguen nombrando."""

    BROWSER_NOT_SUPPORTED: Final = "browser_not_supported"
    """La API se llama desde su servidor, nunca desde el navegador: la llave secreta quedaría expuesta."""

    CALCULATION_MODE_AMBIGUOUS: Final = "calculation_mode_ambiguous"
    """Mezcló las dos formas de emitir un recibo de nómina: POST /v1/payroll_receipts calcula el recibo con los datos del empleado (emp_…); POST /v1/payroll_receipts/external timbra los importes que calculó su sistema. Use el endpoint que corresponde."""

    CANCELLATION_FAILED: Final = "cancellation_failed"
    """El SAT no aceptó la solicitud de cancelación; message dice por qué."""

    CATALOG_UNAVAILABLE: Final = "catalog_unavailable"
    """El catálogo del SAT no respondió (503). Reintente en unos segundos."""

    CERTIFICATE_INVALID: Final = "certificate_invalid"
    """El CSD no sirve: no es un certificado de sello (es una e.firma), está vencido, el .key no corresponde o la contraseña no abre la llave."""

    CERTIFICATE_REQUIRED: Final = "certificate_required"
    """Suba primero el CSD del emisor; después firme el contrato con su e.firma."""

    CONNECTION_FAILED: Final = "connection_failed"
    """No se pudo conectar con la API (connection_error)."""

    CUSTOMER_EXISTS: Final = "customer_exists"
    """Ya hay un cliente con ese RFC en el catálogo del emisor (o un producto con ese SKU)."""

    DAILY_LIMIT: Final = "daily_limit"
    """Llegó al tope del día de algo que no se paga con timbres: comprobantes en pruebas (1,000), RFC revisados en las listas del SAT o constancias consultadas. Retry-After dice cuántos segundos faltan para la medianoche de la Ciudad de México."""

    DATA_REQUEST_COMPLETED: Final = "data_request_completed"
    """El cliente ya mandó sus datos con esa liga: una solicitud completada no se cancela."""

    DIOT_EMPTY: Final = "diot_empty"
    """El mes no tiene pagos a proveedores: esa DIOT se presenta sin operaciones desde el portal del SAT."""

    EFIRMA_INVALID: Final = "efirma_invalid"
    """La e.firma no sirve: no es una e.firma (es un CSD), es de otro RFC, está vencida o la contraseña no abre la llave."""

    EFIRMA_REQUIRED: Final = "efirma_required"
    """Para pedirle al SAT las facturas de un emisor en producción, guarde antes su e.firma: POST /v1/issuers/{id}/efirma con keep_for_downloads: true. También si la guardada venció."""

    EMAIL_FAILED: Final = "email_failed"
    """No se pudo mandar el correo; lo demás sí se hizo: el comprobante está timbrado o la cotización quedó enviada (su url funciona). Repita el envío con su ruta /send."""

    ENDPOINT_EXISTS: Final = "endpoint_exists"
    """Ya hay un webhook con esa dirección en este modo; el mensaje dice cuál. Cámbielo en vez de crear otro."""

    ENDPOINT_LIMIT: Final = "endpoint_limit"
    """La cuenta llegó al máximo de webhooks en este modo."""

    EXPAND_INVALID: Final = "expand_invalid"
    """Un campo de expand[] no existe en la respuesta, no es el id de otro objeto, o se pidieron demasiados (hasta 10 campos, 4 niveles). Vea Expandir objetos."""

    IDEMPOTENCY_KEY_INVALID: Final = "idempotency_key_invalid"
    """Idempotency-Key es de 1 a 255 caracteres ASCII, sin acentos ni ñ: el id de su pedido o un UUID."""

    IDEMPOTENCY_KEY_MISSING: Final = "idempotency_key_missing"
    """Lo que timbra exige el encabezado Idempotency-Key (8 a 255 caracteres, uno nuevo por comprobante). Así un reintento nunca timbra dos veces."""

    IDEMPOTENCY_KEY_REUSED: Final = "idempotency_key_reused"
    """Esa Idempotency-Key ya se usó en las últimas 24 horas con otra solicitud (otra ruta u otro cuerpo). Use una nueva para cada operación distinta."""

    INSUFFICIENT_BALANCE: Final = "insufficient_balance"
    """La cuenta no tiene timbres de producción: para timbrar, revisar RFC en las listas, consultar constancias o pedir descargas al SAT. Compre un paquete en Desarrolladores › Timbres. En pruebas nunca pasa. Para enterarse antes, escuche balance.low o active la recarga automática."""

    INTERNAL_ERROR: Final = "internal_error"
    """Algo falló de nuestro lado. Repita la solicitud con la misma Idempotency-Key: nunca se timbra dos veces. Si sigue, escríbanos con el request_id."""

    INVALID_API_KEY: Final = "invalid_api_key"
    """La llave no existe, se revocó o expiró. Cree otra en Desarrolladores › Llaves."""

    INVALID_JSON: Final = "invalid_json"
    """El cuerpo no es un objeto JSON válido."""

    INVALID_RESPONSE: Final = "invalid_response"
    """La respuesta no se pudo leer (api_error): no es el JSON de la API, sino la página de un proxy o de un portal de la red. status dice qué contestó."""

    INVENTORY_REFUSED: Final = "inventory_refused"
    """Inventario no lo permite: el mensaje dice por qué (un lote que no es de ese producto, otro ajuste del mismo almacén en curso)."""

    INVOICE_INVALID: Final = "invoice_invalid"
    """La factura no cumple una regla del SAT que Fiscalisto revisa antes de mandarla al PAC (uso contra régimen, totales, complementos…). No se usó ningún timbre."""

    INVOICE_NOT_MARKABLE: Final = "invoice_not_markable"
    """Solo una factura de ingreso PUE vigente se marca pagada o por cobrar; una PPD se paga con su complemento de pago (type P)."""

    INVOICE_NOT_STAMPED: Final = "invoice_not_stamped"
    """La acción es para facturas timbradas (enviar, cancelar, sustituir)."""

    INVOICE_REJECTED: Final = "invoice_rejected"
    """El PAC o el SAT no la aceptaron. sat_code trae su código (CFDI40xxx) y message qué corregir. La factura queda como rejected; no se usó ningún timbre."""

    ISSUER_ARCHIVED: Final = "issuer_archived"
    """El emisor está archivado: ya no timbra. Sus comprobantes se pueden consultar y cancelar."""

    ISSUER_CREATION_LIMIT: Final = "issuer_creation_limit"
    """Se crearon 500 emisores en 24 horas. Escríbanos si necesita más."""

    ISSUER_EXISTS: Final = "issuer_exists"
    """Ese RFC ya es un emisor de la cuenta en este modo."""

    ISSUER_MISSING: Final = "issuer_missing"
    """No existe ese emisor en la cuenta (o es del otro modo)."""

    ISSUER_NOT_ALLOWED: Final = "issuer_not_allowed"
    """La llave no puede usar ese emisor."""

    ISSUER_REQUIRED: Final = "issuer_required"
    """La cuenta tiene varios emisores y la solicitud no dice cuál: mande issuer (iss_…)."""

    KEY_IN_SANDBOX: Final = "key_in_sandbox"
    """La llave es de un entorno de prueba y la solicitud es de toda la cuenta (como crear o borrar entornos): use una llave de pruebas de la cuenta."""

    KEY_READ_ONLY: Final = "key_read_only"
    """La llave es de solo lectura: puede hacer GET, validar RFC, revisar listas del SAT y calcular recibos de nómina, pero nada que timbre, cancele, envíe o cambie datos."""

    KEY_RESTRICTED: Final = "key_restricted"
    """La llave está limitada a algunos emisores y la solicitud toca otro (o crea uno nuevo, o usa algo de toda la cuenta como webhooks)."""

    LIVEMODE_MISMATCH: Final = "livemode_mismatch"
    """El objeto es del otro modo: una llave fk_test_ solo ve lo de pruebas y una fk_live_ lo de producción."""

    METHOD_NOT_ALLOWED: Final = "method_not_allowed"
    """La ruta existe pero no con ese método (por ejemplo, PUT: la API usa POST para actualizar)."""

    MISSING_API_KEY: Final = "missing_api_key"
    """Falta el encabezado Authorization: Bearer fk_test_… o fk_live_…."""

    PARAMETER_INVALID: Final = "parameter_invalid"
    """Un campo tiene un valor que no se acepta (formato, catálogo del SAT, rango). param dice cuál y message cómo corregirlo."""

    PARAMETER_MISSING: Final = "parameter_missing"
    """Falta un campo obligatorio. param dice cuál."""

    PARAMETER_UNKNOWN: Final = "parameter_unknown"
    """Mandó un campo o un parámetro de la URL que no existe (casi siempre un nombre mal escrito, como legalName en vez de legal_name, o ?statuss= en vez de ?status=). Nunca se ignora en silencio."""

    PAYROLL_INVALID: Final = "payroll_invalid"
    """El recibo de nómina no se puede calcular o timbrar con esos datos (periodo, días, registro patronal del emisor…). En un recibo calculado por su sistema (/v1/payroll_receipts/external), errors trae todos los problemas, cada uno con su param, code (missing, not_allowed, invalid, catalog, totals_mismatch, rule) y message. No se usó ningún timbre."""

    PAYROLL_PERIOD_OVERLAP: Final = "payroll_period_overlap"
    """El empleado ya tiene un recibo ordinario cuyo periodo se cruza con este (invoice). Un pago adicional del periodo va como recibo extraordinario (type E); para corregir aquel, use replaces."""

    PAYROLL_RECEIPT_EXISTS: Final = "payroll_receipt_exists"
    """El empleado ya tiene un recibo vigente de ese periodo (ordinario) o de esa corrida (payroll_run_id, extraordinario) con otros importes. invoice es ese recibo: corríjalo con replaces o cancélelo antes. Con los mismos importes se devuelve el mismo recibo, sin error."""

    PAYROLL_REPLACEMENT_INVALID: Final = "payroll_replacement_invalid"
    """replaces no es un recibo de nómina vigente del mismo emisor y del mismo empleado."""

    QUOTE_CUSTOMER_MISSING: Final = "quote_customer_missing"
    """La cotización no tiene los datos fiscales del cliente: agrégueselos con POST /v1/quotes/{id} (customer) o mándela con auto_invoice para que los dé al aceptarla."""

    QUOTE_INVALID: Final = "quote_invalid"
    """La cotización no se pudo guardar o ya no cambia (aceptada, rechazada o facturada), o no se puede mandar así. El mensaje dice por qué."""

    QUOTE_NOT_DRAFT: Final = "quote_not_draft"
    """Solo se borra una cotización que nunca se envió."""

    QUOTE_NOT_INVOICEABLE: Final = "quote_not_invoiceable"
    """La cotización se rechazó o venció: no se factura. Si venció, cámbiele valid_until (es una versión nueva)."""

    RATE_LIMIT: Final = "rate_limit"
    """Demasiadas solicitudes con la llave. Espere lo que dice Retry-After y reintente."""

    RECURRING_INVALID: Final = "recurring_invalid"
    """La factura recurrente no se pudo guardar: el día, la hora, la zona o la factura no son válidos. El mensaje dice cuál."""

    RECURRING_LIMIT: Final = "recurring_limit"
    """El emisor ya tiene el máximo de facturas recurrentes activas (25 en pruebas, 5,000 en producción). Pause o borre las que ya no use."""

    RECURRING_NOT_DUE: Final = "recurring_not_due"
    """Aún no toca timbrar la factura recurrente (409): su next_invoice_on es después de hoy. Para una factura antes de tiempo, use POST /v1/invoices."""

    RECURRING_PAUSED: Final = "recurring_paused"
    """La factura recurrente está en pausa: reanúdela con active: true para timbrarla."""

    REQUEST_IN_PROGRESS: Final = "request_in_progress"
    """Otra solicitud con la misma Idempotency-Key sigue en proceso, o otra solicitud está cambiando el mismo objeto (dos actualizaciones del mismo cliente a la vez esperan su turno hasta 15 segundos) (409, con Retry-After). Repítala en un momento con la misma llave: contestará lo mismo."""

    RESOURCE_MISSING: Final = "resource_missing"
    """No existe un objeto con ese id (o es de otro emisor o del otro modo)."""

    RETENTION_INVALID: Final = "retention_invalid"
    """La constancia de retenciones no cumple una regla del SAT. No se usó ningún timbre."""

    RETENTION_NOT_STAMPED: Final = "retention_not_stamped"
    """La acción es para constancias timbradas."""

    RETENTION_REJECTED: Final = "retention_rejected"
    """El PAC o el SAT no aceptaron la constancia; sat_code trae su código."""

    ROUTE_NOT_FOUND: Final = "route_not_found"
    """No existe esa ruta. Revise la dirección y la versión (/v1)."""

    SANDBOX_INVALID: Final = "sandbox_invalid"
    """No se pudo crear el entorno de prueba: falta su nombre o la cuenta ya tiene 25 (borre uno que ya no use)."""

    SAT_REFRESH_TOO_SOON: Final = "sat_refresh_too_soon"
    """Las declaraciones de ese emisor se consultaron en el SAT hace menos de 10 minutos (cada consulta entra al SAT con su e.firma). Retry-After dice cuántos segundos faltan; lo que ya trajo está en GET /v1/sat_declarations."""

    SAT_REQUEST_REJECTED: Final = "sat_request_rejected"
    """El SAT rechazó la solicitud de descarga. El mensaje trae su motivo, por ejemplo que ya se pidió el mismo periodo con los mismos filtros demasiadas veces (el SAT pone un límite de por vida)."""

    SAT_UNAVAILABLE: Final = "sat_unavailable"
    """El SAT no contestó o no dejó entrar con la e.firma del emisor. El mensaje trae lo que dijo; no se usó ningún timbre. Reintente en 10 minutos."""

    STAMP_RATE_LIMIT: Final = "stamp_rate_limit"
    """Demasiados timbres seguidos del mismo emisor. Espere lo que dice Retry-After; para muchas facturas use POST /v1/invoice_batches."""

    STORE_ALREADY_CONNECTED: Final = "store_already_connected"
    """Esa tienda ya está conectada a este emisor."""

    STORE_CONNECTION_FAILED: Final = "store_connection_failed"
    """La tienda no aceptó la conexión o no respondió como se esperaba (llaves equivocadas, permisos read_orders/write_orders que faltan, una tienda que no vende en pesos). El mensaje dice qué contestó."""

    STORE_DISCONNECTED: Final = "store_disconnected"
    """La tienda se desconectó: conéctela otra vez con POST /v1/store_connections."""

    STORE_NOT_AUTHORIZED: Final = "store_not_authorized"
    """El vendedor aún no autoriza la conexión en authorize_url."""

    STORE_PLATFORM_UNAVAILABLE: Final = "store_platform_unavailable"
    """Esa plataforma aún no está disponible en Fiscalisto."""

    SUBSTITUTION_UNSUPPORTED: Final = "substitution_unsupported"
    """Los complementos de pago y las notas de crédito no se sustituyen: se cancelan y se emite otro. Un recibo de nómina se sustituye con POST /v1/payroll_receipts/external y replaces."""

    TEST_CLOCK_ADVANCING: Final = "test_clock_advancing"
    """El reloj se está adelantando en otra solicitud (409, con Retry-After). Espere a test_clock.ready y repita."""

    TEST_CLOCK_EXISTS: Final = "test_clock_exists"
    """El emisor ya tiene un reloj de prueba: adelántelo, o bórrelo para volver a la hora real."""

    TEST_CLOCK_INVALID: Final = "test_clock_invalid"
    """frozen_time no sirve: no es una fecha y hora ISO 8601, es anterior a la hora del reloj (solo avanza) o va más de dos años adelante de la hora real."""

    TEST_CLOCK_MISSING: Final = "test_clock_missing"
    """El emisor no tiene reloj de prueba: créelo con POST /v1/issuers/{id}/test_clock."""

    TEST_CLOCK_UNSUPPORTED: Final = "test_clock_unsupported"
    """Los relojes de prueba son de emisores de prueba: use su llave fk_test_ y un emisor de pruebas."""

    TEST_MODE_ONLY: Final = "test_mode_only"
    """Esto solo existe en pruebas (como reiniciar los datos de prueba): use su llave fk_test_."""

    TICKET_FOLIO_TAKEN: Final = "ticket_folio_taken"
    """Ese folio ya está registrado para el emisor con otro total o con otra propina (409). Con el mismo total se contesta el ticket que ya existe."""

    TICKET_INVALID: Final = "ticket_invalid"
    """El ticket no se pudo registrar: el folio trae caracteres no válidos, la fecha de venta está en el futuro o es de hace más de un año, el producto ya no está en el catálogo… El mensaje dice cuál."""

    TICKET_NOT_PENDING: Final = "ticket_not_pending"
    """El ticket ya se facturó o entró en una factura global: no se puede cancelar."""

    TIMEOUT: Final = "timeout"
    """La API no contestó a tiempo (connection_error). Con lo que timbra, repita con la misma Idempotency-Key para saber si se timbró."""

    UNSUPPORTED_CONTENT_TYPE: Final = "unsupported_content_type"
    """Mande el cuerpo con Content-Type: application/json."""


ErrorCodeValue = Literal[
    "api_version_invalid",
    "bank_transaction_invalid",
    "batch_invalid",
    "body_too_large",
    "branch_exists",
    "branch_has_invoices",
    "browser_not_supported",
    "calculation_mode_ambiguous",
    "cancellation_failed",
    "catalog_unavailable",
    "certificate_invalid",
    "certificate_required",
    "connection_failed",
    "customer_exists",
    "daily_limit",
    "data_request_completed",
    "diot_empty",
    "efirma_invalid",
    "efirma_required",
    "email_failed",
    "endpoint_exists",
    "endpoint_limit",
    "expand_invalid",
    "idempotency_key_invalid",
    "idempotency_key_missing",
    "idempotency_key_reused",
    "insufficient_balance",
    "internal_error",
    "invalid_api_key",
    "invalid_json",
    "invalid_response",
    "inventory_refused",
    "invoice_invalid",
    "invoice_not_markable",
    "invoice_not_stamped",
    "invoice_rejected",
    "issuer_archived",
    "issuer_creation_limit",
    "issuer_exists",
    "issuer_missing",
    "issuer_not_allowed",
    "issuer_required",
    "key_in_sandbox",
    "key_read_only",
    "key_restricted",
    "livemode_mismatch",
    "method_not_allowed",
    "missing_api_key",
    "parameter_invalid",
    "parameter_missing",
    "parameter_unknown",
    "payroll_invalid",
    "payroll_period_overlap",
    "payroll_receipt_exists",
    "payroll_replacement_invalid",
    "quote_customer_missing",
    "quote_invalid",
    "quote_not_draft",
    "quote_not_invoiceable",
    "rate_limit",
    "recurring_invalid",
    "recurring_limit",
    "recurring_not_due",
    "recurring_paused",
    "request_in_progress",
    "resource_missing",
    "retention_invalid",
    "retention_not_stamped",
    "retention_rejected",
    "route_not_found",
    "sandbox_invalid",
    "sat_refresh_too_soon",
    "sat_request_rejected",
    "sat_unavailable",
    "stamp_rate_limit",
    "store_already_connected",
    "store_connection_failed",
    "store_disconnected",
    "store_not_authorized",
    "store_platform_unavailable",
    "substitution_unsupported",
    "test_clock_advancing",
    "test_clock_exists",
    "test_clock_invalid",
    "test_clock_missing",
    "test_clock_unsupported",
    "test_mode_only",
    "ticket_folio_taken",
    "ticket_invalid",
    "ticket_not_pending",
    "timeout",
    "unsupported_content_type",
]
"""Un código de error de la API."""
