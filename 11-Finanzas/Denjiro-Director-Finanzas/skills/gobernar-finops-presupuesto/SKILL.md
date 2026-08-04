---
name: gobernar-finops-presupuesto
description: Define políticas y gates de FinOps para allocation, budgeting, forecasting, unit economics y anomalías de gasto. Úsala cuando haya que gobernar presupuesto de infraestructura, chargeback/showback interno o madurez de visibilidad de costos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar FinOps y presupuesto

## Propósito

Establecer el paved road financiero de visibilidad y control de gasto tecnológico a nivel dirección, dejando la ejecución operativa a King Riku.

## Entradas

- Scopes objetivo (producto, cost center, entorno, categoría tecnológica).
- Estado de billing datasets (FOCUS-aligned o no), tags/allocation, budgets actuales.
- Señales de anomalía y forecast vs actual.
- Dueños de workloads conocidos o gaps de ownership.

## Procedimiento

1. Declara scopes y categorías en alcance (cloud, SaaS, AI, etc.).
2. Define política de allocation mínima: campos/tags requeridos, % unallocated máximo tolerado, dueño por scope.
3. Define budgeting + forecasting: cadencia, variance thresholds, quién actúa en breach.
4. Define unit economics canónicos para el scope (p. ej. costo por API call, por tenant, por entorno).
5. Define anomaly management: severidad, routing al owner de engineering, escalamiento a Denjiro.
6. Define showback/chargeback interno (si aplica) sin confundirlo con monetización externa (Du Feld).
7. Lista gates Crawl→Walk→Run y deuda explícita; asigna ejecución a King Riku vía contrato.
8. Escala a Legal/Arquitectura/Plataforma cuando falte dato, contrato o capacidad técnica.

## Salida

```md
## Política FinOps / presupuesto
- Scopes:
- Allocation mínima:
- Budgets / forecasts:
- Unit economics:
- Anomaly routing:
- Showback/chargeback interno:
## Gates Crawl / Walk / Run
## Deuda y excepciones
## Delegación a King Riku
## Escalaciones
```

## Casos límite

- Billing no FOCUS: documenta mapping manual y riesgo; no declares “FOCUS compliant”.
- AI/token spend compartido: exige regla de back-allocation; no dejes “shared” eterno en P0.
- Commitment discounts prematuros: bloquea hasta rightsizing/allocation básica.

## Validación

- Cada scope P0 tiene owner.
- Umbrales de variance/unallocated son numéricos o explícitamente TBD con fecha.
- Showback interno no se etiqueta como revenue de partner.

## Criterios de terminado

- Política usable por King Riku y Luffy.
- Gates y KPIs explícitos.
- Excepciones con dueño y caducidad.

## Fuentes

- FinOps Capabilities — Allocation, Budgeting, Forecasting, Unit Economics, Anomaly Management — https://www.finops.org/framework/capabilities/ (consultado 2026-08-04)
- FOCUS — https://focus.finops.org/ (consultado 2026-08-04)
- FinOps Maturity Crawl–Walk–Run — https://www.finops.org/framework/maturity-model/
