---
name: reconciliar-uso-facturacion-api
description: Diseña reconciliación uso medido ↔ factura ↔ handoff contable (Gild). Úsala para cerrar períodos y disputes; no para inventar el modelo de pricing.
metadata:
  author: yzylabs
  version: "1.0"
---

# Reconciliar uso y facturación de API

## Propósito

Asegurar que lo medido, lo facturado y lo reconocible contablemente coinciden dentro de tolerancias — y que los gaps tienen dueño.

## Entradas

- Eventos/agregados de metering del período.
- Facturas o preview de invoice.
- Reglas de métrica y exclusiones.
- Política de créditos/ajustes.
- Contacto/proceso Gild Tesoro (si existe).

## Procedimiento

1. Define fuentes: raw events, agregados de billing, líneas de invoice, expectativas contables.
2. Cuadra totales por tenant/métrica/período; calcula delta y tolerancia.
3. Clasifica discrepancias: late events, dupes, exclusiones mal aplicadas, timezone, prorrateo.
4. Define playbook de dispute: evidencia, ventana, crédito, rebill.
5. Produce handoff a Gild: montos, moneda, período, partner, tipo de ingreso, excepciones.
6. Señala revenue leakage o overbilling material a Denjiro.
7. No inventes asientos; entrega datos para que Gild contabilice.
8. Registra controles preventivos (idempotency, cutoff, freeze de período).

## Salida

```md
## Período y alcance
## Cuadre (uso vs factura)
## Discrepancias y causa raíz
## Ajustes / créditos propuestos
## Handoff Gild Tesoro
## Controles preventivos
## Riesgos / leakage
```

## Casos límite

- Eventos llegados post-cutoff → política late-arrival explícita.
- Multi-currency / tax → escala Legal/tax; no inventes tasas.
- Partner niega uso → conserva raw evidence con retención acordada.

## Validación

- Totales trazables a eventos o agregados firmados.
- Handoff Gild completo o gap dueñado.
- Disputes con playbook.
- Sin asientos inventados por Du-Feld.

## Criterios de terminado

- Cuadre cerrado o discrepancias con dueño y next action.
- Paquete listo para Gild/Denjiro.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Agregados = invoice ±0.1% | Cuadre OK + handoff Gild |
| Ambiguo | “No cuadran los números” | Clasificación de causas + datos faltantes |
| Límite | Dupes por retry sin idempotency | Leakage cuantificado + fix preventivo |

## Fuentes

- Adam Arant — metering/billing reconciliation patterns — https://adamarant.com/en/blog/usage-based-pricing-for-saas-the-metering-and-billing-patterns-that-work (2026-08-04).
- Stripe usage recording (async summaries) — https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage (2026-08-04).
- APIScout — metering non-negotiable — https://apiscout.dev/guides/api-monetization-models-guide-2026 (2026-08-04).
