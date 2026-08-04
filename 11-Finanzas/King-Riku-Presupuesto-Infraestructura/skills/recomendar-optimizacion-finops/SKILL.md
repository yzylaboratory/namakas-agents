---
name: recomendar-optimizacion-finops
description: Prioriza recomendaciones de optimización FinOps (rightsizing, idle, scheduling, rate/commits) con evidencia de utilización y riesgo de servicio. Úsala cuando se pida reducir costo de infra o evaluar Savings Plans/RI — no para ejecutar cambios en la nube ni para pricing de APIs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Recomendar optimización FinOps

## Propósito

Producir un backlog accionable de ahorro de infraestructura basado en evidencia, ordenado por valor/riesgo, sin saltarse allocation ni rightsizing.

## Entradas

- Datos de utilización (CPU/mem/IOPS/network) y costo por recurso/servicio.
- Estado de allocation/ownership.
- Commits existentes y cobertura.
- Restricciones de SLO, compliance y ventanas de cambio.
- Forecast/presupuesto del periodo.

## Procedimiento

1. Verifica prerrequisito allocation-first; si falla, detén y lista gaps.
2. Inventaría waste: idle, orphan, oversized, storage frío, transfer innecesario.
3. Prioriza usage optimization antes de rate optimization.
4. Estima ahorro (rango) y esfuerzo; anota riesgo de servicio/SLO.
5. Evalúa commits (RI/SP/CUD) solo sobre baseline estable post-rightsizing.
6. Propón scheduling no-prod y políticas de TTL donde aplique.
7. Asigna dueño técnico (Franky/equipo) por ítem; tú no ejecutas.
8. Empaqueta pipeline de savings con quick wins vs structural.

## Salida

```md
## Prerrequisitos (allocation/utilización)
## Backlog priorizado
## Estimación ahorro (rango) / esfuerzo / riesgo
## Commits (sí/no y por qué)
## Dueños de ejecución
## Impacto en forecast
## No-hacer / anti-patrones
```

## Casos límite

- Sin métricas de utilización → no rightsizing; pide observabilidad.
- Pedido de “compra SP ya” → rechaza si baseline no está limpio; ofrece plan en 2 fases.
- Ahorro que viola SLO/DR → descarta o exige aceptación explícita de riesgo.

## Validación

- Cada ítem tiene evidencia (métrica o query) y owner.
- Usage antes que rate, salvo justificación documentada.
- No declara “ahorro realizado” sin evidencia post-cambio del dueño técnico.
- No incluye monetización de APIs.

## Criterios de terminado

- Backlog listo para que plataforma ejecute o rechace con datos.
- Riesgos SLO/lock-in visibles para Denjiro.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Fleet con 40% CPU p95 bajo | Rightsizing backlog + owners |
| Ambiguo | “Recorta 30% el cloud” | Escenarios de impacto + quick wins realistas |
| Límite | SP proposal sin tags | BLOCKED allocation-first |

## Fuentes

- FinOps Framework — Usage Optimization — https://www.finops.org/framework/capabilities/usage-optimization/ (consultado 2026-08-04).
- FinOps Framework — Rate Optimization — https://www.finops.org/framework/capabilities/rate-optimization/ (2026).
- FinOps Framework — Phases Inform/Optimize/Operate — https://www.finops.org/framework/phases/ (2026).
