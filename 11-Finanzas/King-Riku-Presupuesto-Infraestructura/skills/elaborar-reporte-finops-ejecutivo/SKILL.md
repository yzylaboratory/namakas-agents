---
name: elaborar-reporte-finops-ejecutivo
description: Elabora un reporte ejecutivo FinOps de infraestructura (spend, forecast accuracy, allocation, drivers, savings pipeline, decisiones). Úsala cuando Denjiro o liderazgo necesiten un paquete de decisión — no un dump de billing crudo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Elaborar reporte FinOps ejecutivo

## Propósito

Empaquetar la práctica FinOps de infraestructura en un informe accionable para decisión de funding, priorización y accountability.

## Entradas

- Spend del periodo y comparación vs presupuesto/forecast.
- % allocated / unallocated.
- Top drivers y anomalías.
- Pipeline de optimización y estado de commits.
- Madurez deseada (Crawl/Walk/Run) si se evalúa la práctica.
- Decisiones pendientes para Denjiro.

## Procedimiento

1. Define audiencia y pregunta de decisión (techo, hire infra, commit, freeze).
2. Resume estado en 5–10 líneas: qué pasó, por qué importa, qué se pide decidir.
3. Presenta KPIs: spend, variance, forecast accuracy, % allocated, unit cost (si existe).
4. Destaca top 3–5 drivers con owners.
5. Incluye savings pipeline (estimado vs realizado) sin inflar.
6. Separa hechos / inferencias / recomendaciones.
7. Lista decisiones requeridas con opciones y trade-offs.
8. Adjunta fuentes (billing/FOCUS/Framework) y límites del dato.

## Salida

```md
## Executive summary
## KPIs
## Drivers y owners
## Allocation health
## Savings pipeline
## Decisiones requeridas
## Riesgos / límites de datos
## Fuentes
```

## Casos límite

- Datos parciales → reporte `COMPLETED_WITH_LIMITATIONS` con gaps.
- Pedido de “dashboard bonito” sin decisión → fuerza pregunta de decisión o marca uso informativo.
- Conflicto finance vs engineering → documenta posiciones; no elijas en nombre de Denjiro.

## Validación

- Hay al menos una decisión o next action clara.
- KPIs son reproducibles a partir de fuentes citadas.
- No mezcla monetización de APIs ni P&L de producto API.
- No declara COMPLETED sin EVIDENCE.

## Criterios de terminado

- Denjiro puede decidir en una lectura sin abrir la consola cloud.
- Owners y fechas de follow-up están explícitos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Cierre mensual multi-cuenta | Reporte con KPIs + 2 decisiones |
| Ambiguo | “Prepara algo para la junta” | Pregunta de decisión + draft de 1 página |
| Límite | 40% unallocated | Reporte + decisión de remediación priorizada |

## Fuentes

- FinOps Framework — Reporting & Analytics — https://www.finops.org/framework/capabilities/reporting-analytics/ (consultado 2026-08-04).
- FinOps Framework — KPIs & Benchmarking — https://www.finops.org/framework/capabilities/kpis-benchmarking/ (2026).
- FinOps Maturity Model — https://www.finops.org/framework/maturity-model/ (Crawl/Walk/Run).
