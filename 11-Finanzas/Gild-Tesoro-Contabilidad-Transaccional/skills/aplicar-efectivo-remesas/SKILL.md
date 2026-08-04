---
name: aplicar-efectivo-remesas
description: Aplica cobros/remesas a facturas u obligaciones (cash application 1:1, 1:N, N:1) con tolerancias y cola unapplied. Úsala cuando haya que casar pagos recibidos con open items o billing de APIs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Aplicar efectivo y remesas

## Propósito

Maximizar aplicación automática de efectivo con remesa estructurada y dejar unapplied/parciales con dueño, sin inventar facturas ni precios.

## Entradas

- Cobros / avisos de crédito (camt.054, extracto, pasarela).
- Open items (facturas, notas, obligations).
- Remesa estructurada (invoice IDs, montos, fechas) si existe.
- Tolerancias (monto, FX, descuentos).
- Contexto de monetización API (si aplica; datos de Du-Feld).

## Procedimiento

1. Inventaría cobros del periodo y open items elegibles.
2. Prioriza match por referencia de factura / end-to-end ID / remesa estructurada.
3. Aplica reglas 1:1, luego 1:N (un pago varias facturas) y N:1 (varios pagos una factura) solo con evidencia.
4. Documenta partial, overpayment y short-pay con diferencia explícita.
5. Envía unapplied a cola con aging y dueño (cliente, ops, Du-Feld).
6. Si el cobro es de API billing, no recalcules precio; usa tarifa/factura de Du-Feld o marca gap.
7. Propón asientos de aplicación vía skill de asientos; no postees en core.

## Salida

```md
## Universo de cobros / open items
## Matches (tipo 1:1 / 1:N / N:1)
## Partials / over / short
## Unapplied (aging + dueño)
## Tolerancias usadas
## Handoff Du-Feld / ops
## Riesgos / pendientes
```

## Casos límite

- Remesa libre / no estructurada → matching asistido; no auto-cierre masivo.
- Cliente con varias razones sociales → no mezcles open items sin confirmación.
- Descuento no autorizado → break comercial, no force apply.

## Validación

- Cada apply cita cobro + open item(s) + montos.
- Tolerancias documentadas.
- Unapplied no oculto.

## Criterios de terminado

- Caja aplicada reproducible; unapplied con aging.
- Gaps de pricing tienen dueño Du-Feld.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Pago = suma 3 facturas + refs | Apply 1:N completo |
| Ambiguo | Pago sin remesa | Cola unapplied + candidatos |
| Límite | Overpay + tarifa API disputada | Partial apply + handoff Du-Feld |

## Fuentes

- Zanders — structured remittance / cash application — https://zandersgroup.com/en/insights/blog/iso-20022-xml-an-opportunity-to-accelerate-and-elevate-receivables-reconciliation (2026-08-04).
- ReconArt — ISO 20022 reconciliation efficiencies — https://www.reconart.com/blog/iso-20022-adoption-transform-reconciliation-enhance-payments-unlock-efficiencies/ (2026-08-04).
