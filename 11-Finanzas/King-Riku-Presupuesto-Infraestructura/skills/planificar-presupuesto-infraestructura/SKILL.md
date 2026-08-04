---
name: planificar-presupuesto-infraestructura
description: Elabora un presupuesto de infraestructura tecnológica por scope (producto, cost center, entorno) con ciclo, techos, holdback y owners. Úsala cuando se pida planificar, fijar o revisar el budget de cloud/SaaS de plataforma/data center — no para pricing de APIs ni asientos contables.
metadata:
  author: yzylabs
  version: "1.0"
---

# Planificar presupuesto de infraestructura

## Propósito

Convertir el gasto esperado de infraestructura en un plan financiero operable: líneas, owners, ciclo de revisión y buffer para lo no planificado.

## Entradas

- Objetivo y periodo (mes/trimestre/año).
- Scope FinOps (productos, equipos, entornos, proveedores).
- Histórico de billing o baseline actual.
- Roadmap de capacidad / releases que impacten costo.
- Políticas de techo, CapEx/OpEx y holdback (si existen).

## Procedimiento

1. Nombra el presupuesto y delimita el scope (qué entra / qué queda fuera).
2. Elige granularidad operativa (mensual por equipo ≥ solo agregado anual).
3. Separa baseline comprometido vs gasto variable.
4. Asigna owner por línea (`cost_center` / producto / entorno).
5. Define holdback (%) o monto para unplanned; justifica el porcentaje.
6. Declara supuestos (crecimiento, precios, commits, FX si aplica).
7. Define umbrales de alerta (p. ej. 50/80/100% del forecast o del techo).
8. Lista gaps de datos y dueños antes de cerrar el plan.

## Salida

```md
## Presupuesto
## Scope incluido / excluido
## Líneas (owner, monto, tipo baseline|variable)
## Holdback
## Ciclo de revisión
## Umbrales de alerta
## Supuestos
## Gaps / riesgos
```

## Casos límite

- Sin histórico → presupuesto provisional con rangos y plan de instrumentación.
- Shared services sin driver → no repartas a ciegas; propone driver o deja unallocated etiquetado.
- Solo techo anual → deriva cuota mensual/trimestral y holdback explícito.

## Validación

- Cada línea tiene owner.
- Holdback y ciclo están documentados.
- No incluye pricing de APIs ni asientos de libro mayor.
- Supuestos numerados y falsables.

## Criterios de terminado

- Denjiro puede aprobar o rechazar el plan sin reinterpretar raw billing.
- Gaps de allocation/datos tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Cloud trimestral por 3 productos | Presupuesto por producto + holdback + umbrales |
| Ambiguo | “Arma el budget de infra” | Preguntas de scope + borrador con 2 scopes candidatos |
| Límite | Sin tags ni owners | Plan bloqueado parcial + lista de gaps allocation-first |

## Fuentes

- FinOps Framework — Budgeting capability — https://www.finops.org/framework/capabilities/budgeting/ (consultado 2026-08-04).
- FinOps Framework Overview — https://www.finops.org/framework/ (2026).
