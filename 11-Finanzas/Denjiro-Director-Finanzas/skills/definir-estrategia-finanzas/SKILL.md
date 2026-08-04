---
name: definir-estrategia-finanzas
description: Define la estrategia y hoja de ruta financiera-FinOps (visibilidad, allocation, budgeting, unit economics, monetización). Úsala cuando se pida estrategia de Finanzas, roadmap FinOps o posicionamiento del gasto tecnológico como valor de negocio.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia de Finanzas

## Propósito

Convertir objetivos de negocio y fricción de costo/revenue en una estrategia accionable de FinOps + monetización + integridad contable, con secuencia de capacidades y métricas.

## Entradas

- Objetivo de negocio y horizonte presupuestal.
- Estado actual: billing/cost data, allocation, forecasts, pricing API, ledger/reconciliación.
- Restricciones de plazo, riesgo y capacidad del squad.
- Categorías tecnológicas en scope (cloud, SaaS, AI, data platform, etc.).

## Procedimiento

1. Fija el horizonte (p. ej. 2–4 trimestres) y el outcome principal (visibilidad, unit economics, margen API, forecast accuracy).
2. Clasifica iniciativas en: **Inform** (visibilidad/allocation), **Optimize** (uso/rate/unit cost), **Operate** (governance, budgets, anomalies), **Monetize** (pricing/metering), **Ledger** (integridad contable).
3. Secuencia capacidades fundacionales antes de escala:
   - Ingestión y normalización de billing (preferir FOCUS-aligned cuando exista).
   - Allocation y ownership por scope (producto / cost center / entorno).
   - Budgeting + forecasting + anomaly management.
   - Unit economics (costo por unidad de negocio).
   - Metering/pricing (Du Feld) solo tras ownership de costo.
   - Reconciliación ledger (Gild Tesoro) antes de cobro en producción.
4. Define Now / Next / Later con dueño (Denjiro / King Riku / Du Feld / Gild Tesoro / otros).
5. Declara supuestos, no-objetivos y riesgos (austeridad ciega, vanity savings, pricing sin costo).
6. Propón 3–6 KPIs (unallocated %, forecast accuracy, unit cost trend, anomaly MTTR, API margin).

## Salida

```md
## Estrategia Finanzas / FinOps
- Outcome:
- Scopes / categorías:
- Inform vs Optimize vs Operate vs Monetize vs Ledger:
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap
| Iniciativa | Valor | Dependencias | Riesgo |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Solo “comprar tool FinOps”: rechaza estrategia centrada en vendor sin scopes, allocation ni ownership.
- Presión de monetizar APIs sin costo unitario: bloquea P0 de cobro; permite discovery de packaging.
- Multi-cloud + AI tokens: scopes separados; no mezclar unit economics incompatibles sin puente explícito.

## Validación

- Hay separación Inform / Optimize / Operate / Monetize / Ledger.
- La secuencia no salta allocation ni ledger antes de cobro real.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones FinOps/FOCUS citan fuente/fecha.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones Legal/Arquitectura/OB identificadas cuando correspondan.

## Fuentes

- FinOps Foundation Framework — https://www.finops.org/framework/ (consultado 2026-08-04)
- FinOps Phases Inform/Optimize/Operate — https://www.finops.org/framework/phases/
- FOCUS Specification — https://focus.finops.org/ (consultado 2026-08-04)
