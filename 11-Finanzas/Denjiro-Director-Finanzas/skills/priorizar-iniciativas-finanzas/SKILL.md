---
name: priorizar-iniciativas-finanzas
description: Prioriza el backlog del departamento Finanzas con valor de negocio, riesgo de overspend, dependencias y dueños. Úsala cuando haya que ordenar iniciativas FinOps/monetización/ledger, elegir Now/Next/Later o replanificar tras anomalías de costo o gaps de revenue.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar iniciativas de Finanzas

## Propósito

Convertir un backlog desordenado de tools, recortes y requests de pricing en una cola priorizada con justificación explícita y gates de madurez financiera.

## Entradas

- Backlog candidato (epics FinOps, pricing, ledger, toil de reporting).
- Capacidad del squad King Riku / Du Feld / Gild Tesoro.
- Riesgos abiertos (unallocated alto, anomalías, reconciliación rota, pricing sin metering).
- Señales disponibles (forecast vs actual, unit costs, margen API).

## Procedimiento

1. Normaliza cada ítem: problema, outcome, esfuerzo relativo, riesgo de no hacer.
2. Puntúa con criterios explícitos (documenta pesos):
   - Impacto en valor de negocio / margen.
   - Reducción de riesgo financiero (overspend, fuga de revenue, integridad).
   - Desbloqueo de otros equipos (OB, plataforma, producto).
   - Costo de delay / toil de reporting acumulado.
3. Aplica gates:
   - No P0 de commitment discounts si allocation es débil.
   - No P0 de cobro externo si falta metering o reconciliación ledger.
4. Ordena Now (capacidad real) / Next / Later / Won’t.
5. Asigna dueño celular o Denjiro (dirección) y criterio de salida verificable.
6. Declara trade-offs rechazados (qué no se hará este ciclo).

## Salida

```md
## Criterios y pesos
## Backlog priorizado
| Ítem | Now/Next/Later | Valor | Riesgo | Dependencias | Dueño | Gate de salida |
## Rechazados / diferidos
## Capacidad asumida
## Riesgos de la priorización
```

## Casos límite

- Anomalía de gasto P1: pausa roadmap cosmético; prioriza containment + root cause con King Riku.
- Request ejecutivo de “bajar 30% cloud”: traduce a unit economics + scopes o marca como Won’t/discovery.
- Células stub: prioriza igual; marca ejecución como `DELEGATION_REQUIRED` / forja pendiente.

## Validación

- Todo ítem Now tiene dueño y gate.
- No hay dos Now que peleen el mismo recurso crítico sin regla de merge.
- Gates de allocation/ledger/metering no se saltan por urgencia comercial.

## Criterios de terminado

- Cola accionable para el ciclo.
- Trade-offs explícitos.
- Lista lista para contratos de delegación.

## Fuentes

- FinOps Framework — Quantify Business Value / Optimize Usage & Cost domains — https://www.finops.org/framework/domains/ (consultado 2026-08-04)
- State of FinOps 2026 — priorización Allocation, Forecasting, Budgeting — https://data.finops.org/ (consultado 2026-08-04)
