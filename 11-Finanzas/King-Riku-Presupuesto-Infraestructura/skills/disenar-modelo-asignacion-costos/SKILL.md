---
name: disenar-modelo-asignacion-costos
description: Diseña el modelo de allocation/showback de costos de infraestructura (tags, shared services, unallocated). Úsala cuando se pida atribuir gasto a equipos/productos o montar showback — no chargeback contable profundo ni monetización de APIs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar modelo de asignación de costos

## Propósito

Hacer el gasto de infraestructura atribuible y accionable: quién paga (o ve) qué, con qué driver, y qué queda unallocated.

## Entradas

- Jerarquía de funding (productos, cost centers, entornos).
- Inventario de tags / labels actuales y % de cobertura.
- Shared services (red, observabilidad, cluster compartido, data platform).
- Política deseada: showback vs chargeback.
- Fuentes de billing (cuenta, suscripción, proyecto).

## Procedimiento

1. Define dimensiones de allocation (mínimo: owner, application, environment, cost_center).
2. Mide cobertura de tagging; lista recursos/cuentas sin tag.
3. Diseña reglas para shared services (driver: vCPU, GB, requests, equal-split — con justificación).
4. Separa showback (visibilidad) de chargeback (asiento/cobro); no mezcles sin mandato Denjiro.
5. Define tratamiento de unallocated (cuantificar, dueño de remediación, SLA de reducción).
6. Propón enforcement at creation (policy/CI), no solo cleanup post-facto.
7. Documenta excepciones temporales con fecha de caducidad.
8. Entrega matriz allocation + plan de remediación de gaps.

## Salida

```md
## Dimensiones y tags requeridos
## Cobertura actual / gap
## Reglas shared services
## Showback vs chargeback
## Unallocated (monto/%, dueño)
## Enforcement propuesto
## Plan de remediación
## Riesgos
```

## Casos límite

- Multi-cloud con taxonomías distintas → mapea a dimensiones canónicas; menciona FOCUS si ayuda.
- Shared cluster sin métricas → no inventes driver; propone instrumentación o equal-split explícito como temporal.
- Pedido de chargeback inmediato sin política → entrega showback + DECISION_REQUIRED a Denjiro.

## Validación

- Toda regla de shared service tiene driver y owner.
- Unallocated está cuantificado, no oculto.
- No inventa tags “obligatorios” sin plan de enforcement.
- No deriva asientos de libro mayor (Gild Tesoro).

## Criterios de terminado

- Un equipo puede ver su porción de costo o el gap que lo impide.
- Remediación tiene dueño y fecha objetivo.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 70% tagged, shared EKS | Modelo + driver de shared + plan 30% gap |
| Ambiguo | “Haz chargeback a todos” | Showback primero + decisión Denjiro |
| Límite | 0% tags | Bloqueo allocation-first + enforcement mínimo |

## Fuentes

- FinOps Framework — Allocation capability — https://www.finops.org/framework/capabilities/allocation/ (consultado 2026-08-04).
- FinOps Framework — Invoicing & Chargeback — https://www.finops.org/framework/capabilities/invoicing-chargeback/ (2026).
- FOCUS™ — https://focus.finops.org/ (normalización multi-vendor).
