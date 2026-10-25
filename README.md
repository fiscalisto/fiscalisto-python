# fiscalisto

El SDK de la [API de facturación de Fiscalisto](https://fiscalisto.com/docs/api): timbre CFDI 4.0 (facturas, pagos, notas de crédito, nómina, retenciones y lotes) desde Python.

- Tipos (`TypedDict`) para cada campo, con su descripción y su nombre en el XML del SAT; `mypy` y su editor los revisan.
- `Idempotency-Key` automática en cada `POST`: un reintento nunca timbra, crea ni manda nada dos veces.
- Reintentos solo de lo que es seguro repetir.
- Listas que se recorren solas con `for`.
- Webhooks verificados en una línea.
- Sin dependencias: Python 3.10 o más reciente.

```bash
pip install fiscalisto
```

```python
from fiscalisto import Fiscalisto

fiscalisto = Fiscalisto()  # la llave viene de FISCALISTO_API_KEY

invoice = fiscalisto.invoices.create(
    {
        "customer": {"tax_id": "ICV060329BY0", "legal_name": "INMOBILIARIA CVA", "tax_system": "601", "zip": "33826"},
        "payment_form": "03",
        "items": [{"description": "Mensualidad", "product_key": "86121700", "quantity": 2, "unit_price": 2500}],
    },
    idempotency_key="pedido-A-1042",
)

print(invoice["uuid"], invoice["total"])
```

La guía completa está en [fiscalisto.com/docs/api/sdk](https://fiscalisto.com/docs/api/sdk) y cada página de la [referencia](https://fiscalisto.com/docs/api) trae su ejemplo con el SDK.

## Desarrollo

`src/fiscalisto/types.py` y `src/fiscalisto/_resources.py` se generan desde la especificación OpenAPI con `bun run openapi` en la raíz del repositorio; no los edite. Lo demás se escribe a mano.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
mypy --strict src && ruff check src tests
```
