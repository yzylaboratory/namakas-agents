---
name: definir-metricas-ttfv-partner
description: Define Time to First Value / Time to First Deal y el scorecard de métricas líderes y rezagadas del onboarding de partners. Úsala cuando se pidan KPIs de ramp, TTFV o dashboards de activación.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir métricas TTFV de partner

## Propósito

Fijar una definición operativa de TTFV y un scorecard que conecte actividad de onboarding con outcomes de revenue, evitando vanity metrics.

## Entradas

- Definición de “primer valor” por tier/modelo (deal, integración activada, primer caso resuelto, etc.).
- Fecha de firma / cohorte.
- Fuentes de datos (PRM, CRM, LMS, portal).
- Umbrales actuales del programa (si existen).

## Procedimiento

1. Escribe la fórmula TTFV: `fecha_outcome_verificado - fecha_firma` (o hito de kickoff documentado).
2. Declara el outcome verificable por segmento; no mezcles outcomes incompatibles sin segmentar.
3. Define líderes: time-to-portal (&lt;48h target típico), time-to-first-training (&lt;14d), time-to-first-opportunity (&lt;45d), cert rate.
4. Define rezagadas: time-to-first-deal, 90-day activation/retention, first-deal conversion, pNPS onboarding.
5. Propón umbral de riesgo (p. ej. alerta a 60d sin opp; crítico &gt;120d sin deal) — etiqueta como benchmark externo vs baseline local.
6. Especifica instrumentación: evento, sistema, owner de dato, cadencia de review.
7. Entrega scorecard + diccionario de métricas + alertas.

## Salida

```md
## Definición TTFV (fórmula + outcome)
## Segmentación
## Métricas líderes
## Métricas rezagadas
## Umbrales y alertas
## Diccionario / fuente de datos
## Limitaciones de medición
```

## Casos límite

- Sin CRM/PRM → scorecard manual mínimo + plan de instrumentación; no inventes datos.
- Partner solo referral → TTFV = primer lead aceptado / primera opp referida, no “closed-won” forzado.
- Benchmarks externos vs realidad local → usa externos como hipótesis; prioriza baseline de cohorte interna.

## Validación

- TTFV tiene outcome único por segmento.
- Cada métrica tiene fuente y owner.
- Vanity (solo course completion) no es KPI primario.
- Umbrales etiquetados (local vs benchmark).

## Criterios de terminado

- Scorecard adoptable en QBR / weekly.
- Alertas accionables con playbook de dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Reseller + CRM + LMS | TTFV + líderes/rezagadas + alertas |
| Ambiguo | “Queremos medir onboarding” | Diccionario propuesto + 3 preguntas de outcome |
| Límite | Sin sistemas | Scorecard CSV semanal + backlog de instrumentación |

## Fuentes

- Gainsight Time to Value — https://www.gainsight.com/guides/time-to-value/ (consultado 2026-08-04).
- Magentrix Partner Onboarding Guide — https://www.magentrix.com/blog/partner-onboarding-the-complete-guide-to-ramping-channel-partners-fast (2026-08-04).
- Pedowitz — Align enablement with CS — https://www.pedowitzgroup.com/align-partner-enablement-with-customer-success (2026-08-04).
