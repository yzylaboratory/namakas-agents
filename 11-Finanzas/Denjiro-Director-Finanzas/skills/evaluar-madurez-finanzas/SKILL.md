---
name: evaluar-madurez-finanzas
description: Evalúa la madurez financiera-FinOps del departamento o de un scope (Crawl/Walk/Run) con gaps, gates y plan de mejora. Úsala cuando se pida assessment FinOps, readiness de monetización o diagnóstico de allocation/forecasting/ledger.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar madurez de Finanzas

## Propósito

Diagnosticar madurez (Crawl–Walk–Run) en visibilidad de costos, unit economics, monetización e integridad contable, con evidencia y plan priorizado — sin declarar “maduro” por tool instalada.

## Entradas

- Scope a evaluar (org, producto, entorno, categoría tecnológica).
- Evidencia: reports de costo, budgets, forecasts, pricing, reconciliaciones, incidentes.
- Capacidad actual del squad y dependencias externas.

## Procedimiento

1. Acota el scope y la fecha del assessment.
2. Puntúa dimensiones (Crawl / Walk / Run o N/A) con evidencia:
   - Data ingestion / normalización (FOCUS u otro).
   - Allocation & ownership.
   - Reporting & analytics.
   - Budgeting & forecasting.
   - Anomaly management.
   - Unit economics.
   - Monetización / metering / packaging.
   - Integridad ledger / reconciliación.
   - Governance & executive alignment.
3. Identifica blockers P0 (p. ej. >X% unallocated, sin owner, cobro sin reconciliación).
4. Propón plan Now/Next/Later amarrado a King Riku / Du Feld / Gild Tesoro.
5. Declara lo que **no** se evaluó y riesgos de sesgo (datos incompletos).
6. Entrega scorecard a Luffy; no inventes benchmarks numéricos sin fuente.

## Salida

```md
## Scope y fecha
## Scorecard de madurez
| Dimensión | Nivel | Evidencia | Gap |
## Blockers P0
## Plan Now / Next / Later
## No evaluado
## Recomendación principal
```

## Casos límite

- Solo hay factura cloud mensual: máximo Crawl en la mayoría de dimensiones; no Walk por “tenemos AWS bill”.
- Monetización avanzada con allocation rota: Walk/Run en pricing no compensa; marca riesgo sistémico.
- Stubs de células: assessment de dirección válido; ejecución marcada `DELEGATION_REQUIRED`.

## Validación

- Cada nivel citado tiene evidencia o está marcado inferido.
- Blockers P0 tienen dueño propuesto.
- No se declara Run global si una dimensión fundacional está Crawl.

## Criterios de terminado

- Scorecard usable para priorización.
- Plan acoplado al squad.
- Limitaciones del assessment explícitas.

## Fuentes

- FinOps Maturity Model Crawl–Walk–Run — https://www.finops.org/framework/maturity-model/ (consultado 2026-08-04)
- FinOps Assessment (Foundation WG) — https://www.finops.org/wg/finops-assessment/ (consultado 2026-08-04)
- State of FinOps 2026 — https://data.finops.org/ (consultado 2026-08-04)
