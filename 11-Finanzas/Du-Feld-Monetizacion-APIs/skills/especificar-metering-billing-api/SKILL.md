---
name: especificar-metering-billing-api
description: Especifica metering y billing billing-grade (eventos, idempotencia, ingest async, SoT de factura, alertas). Úsala antes de cobrar; no para pricing estratégico abstracto sin telemetría.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar metering y billing de API

## Propósito

Definir la infraestructura lógica de medición y facturación para que el cobro sea correcto, auditable y no degrade el runtime del API.

## Entradas

- Value metric y reglas de conteo.
- Modelo de planes (base, metered, overage).
- Stack candidato (Stripe Meters/Metronome, Lago, Orb, interno).
- SLAs de latencia del API path.

## Procedimiento

1. Modela el evento de uso: campos mínimos (tenant, metric, quantity, timestamp, idempotency_key, resource_id).
2. Exige idempotencia en retries; documenta dedupe window.
3. Separa enforcement (gateway quotas) de billing SoT (plataforma de facturación).
4. Prefiere ingest asíncrono (cola) para no añadir latencia al request path.
5. Define agregación de período, overages, prorrateo, créditos y dunning a alto nivel.
6. Elige enfoque de plataforma: Billing Meters legacy vs Metronome (Stripe docs: Metronome preferido en integraciones nuevas) u open-source Lago — justifica.
7. Define alertas de cuota/spend y export hacia portal (Koala) sin diseñar UI.
8. Define job de reconciliación pre-invoice y ownership (ops + Du-Feld + Gild).
9. Lista anti-patrones: lógica de precio en plugin de gateway; meter sync en hot path; doble cobro.

## Salida

```md
## Event schema + idempotency
## Flujo ingest (async) y enforcement
## Plataforma de billing (decisión + razones)
## Ciclo de factura / overages / créditos
## Alertas y datos hacia portal
## Reconciliación pre-cierre
## Riesgos y anti-patrones evitados
```

## Casos límite

- Alto QPS → no uses sync HTTP a billing en cada request.
- Multi-meter + contratos enterprise custom → señala salto a Metronome/Orb/Lago.
- Disputas → retención de raw events con retención legal acordada (escala Legal).

## Validación

- Idempotencia definida.
- Gateway ≠ invoice SoT.
- Path caliente sin dependencia síncrona de billing.
- Reconciliación con dueño.

## Criterios de terminado

- Spec implementable por engineering/ops.
- Criterios “listo para cobrar” de metering cumplidos o gaps dueñados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 1 métrica, mid volume | Event schema + async ingest + Stripe/Metronome path |
| Ambiguo | “Conecta Stripe” | Requisitos + comparación Meters vs Metronome |
| Límite | 5 meters + precios por contrato | Recomendación plataforma contract-aware + risks |

## Fuentes

- Stripe — Record usage for billing — https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage (2026-08-04).
- Stripe — Usage-based billing / Metronome — https://docs.stripe.com/billing/usage-based (2026-08-04).
- Adam Arant — Usage metering patterns — https://adamarant.com/en/blog/usage-based-pricing-for-saas-the-metering-and-billing-patterns-that-work (2026-08-04).
- APIScout API Monetization 2026 — https://apiscout.dev/guides/api-monetization-models-guide-2026 (2026-08-04).
