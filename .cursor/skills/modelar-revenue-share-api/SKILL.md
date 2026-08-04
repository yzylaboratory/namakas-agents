---
name: modelar-revenue-share-api
description: Modela revenue share y liquidación comercial de partnerships de APIs (splits, floors, MGs). Úsala en alianzas con reparto de ingresos; no para pricing list retail simple sin partner.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar revenue share de APIs

## Propósito

Diseñar la economía de partnership (quién cobra, quién liquida, splits y mínimos) alineada a packaging Sabo y aprobable por Denjiro/Legal.

## Entradas

- Tipo de partner (TPP, ISV, marketplace, white-label).
- Modelo de pricing al usuario final o al partner.
- Costos y margen objetivo.
- Restricciones legales conocidas.
- Handoff Sabo de etapas partnership.

## Procedimiento

1. Clarifica roles: seller of record, merchant of record, bill-to party.
2. Propón estructura: % revenue share, fee fijo, híbrido, mínimo garantizado (MG), floors/ceilings.
3. Define base de cálculo (gross vs net, refunds, taxes, chargebacks).
4. Define calendario de liquidación y evidencia (reportes de uso + facturas).
5. Alinea con tiers light de Sabo; no rediseñes el journey DX.
6. Lista cláusulas que requieren Legal (audit rights, exclusivity, most-favored, SLA penalties).
7. Simula 2–3 escenarios de volumen (bajo/medio/alto) con margen.
8. Entrega RACI: Du-Feld (modelo), Denjiro (aprobación), Legal (contrato), Gild (asientos), Sabo (producto).

## Salida

```md
## Roles comerciales
## Estructura de share / MG / floors
## Base de cálculo y exclusiones
## Liquidación y evidencia
## Escenarios de margen
## Cláusulas → Legal
## RACI
```

## Casos límite

- Partner estratégico con MG que destruye margen → BLOCKED / DECISIONS_REQUIRED Denjiro.
- Cobro al end-user por el partner (MoR externo) → define reportes y audit trail.
- API regulatoria no cobrable en el medio → share solo sobre value-added.

## Validación

- Base de cálculo inequívoca.
- Escenarios de margen presentes.
- Legal gaps explícitos.
- Alineado a packaging Sabo.

## Criterios de terminado

- Modelo usable para negociación / term sheet interno.
- Aprobaciones abiertas listadas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | ISV rev-share 70/30 net | Modelo + liquidación mensual + RACI |
| Ambiguo | “Partimos ingresos” | Opciones de estructura + preguntas bloqueantes |
| Límite | MG alto + volumen incierto | Escenarios + recomendación no firmar sin floor de uso |

## Fuentes

- APIScout API Monetization 2026 (enterprise/contracts) — https://apiscout.dev/guides/api-monetization-models-guide-2026 (2026-08-04).
- Sabo — `definir-partnership-monetizacion-light` (nakamas, 2026-08-04) — frontera light vs comercial profunda.
