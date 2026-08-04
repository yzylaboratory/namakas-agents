---
name: planificar-estrategia-rendimiento
description: Define la estrategia de pruebas de rendimiento (objetivo, tipo smoke/average-load/stress/spike/breakpoint/soak, entorno, riesgos y orden de madurez). Úsala cuando pidan un plan de carga o “probar performance” sin tipificar aún.
metadata:
  author: yzylabs
  version: "1.0"
---

# Planificar estrategia de rendimiento

## Propósito

Convertir una petición vaga de “load test” en un plan tipificado, ordenado y seguro: qué probar, en qué entorno, con qué perfil y qué se considera éxito.

## Entradas

- Objetivo de negocio o hipótesis (capacidad, regresión, estabilidad, spike).
- Entorno candidato y restricciones.
- SLOs/SLAs/NFRs o baselines previas (si existen).
- Flujos/endpoints críticos.
- Calendario de release o ventana disponible.

## Procedimiento

1. Reformula el objetivo en una pregunta medible (p. ej. “¿p95 < X a Y RPS durante Z?”).
2. Tipifica la prueba según Grafana k6 / guías de performance: smoke, average-load, stress, spike, breakpoint, soak.
3. Declara el orden: smoke del script → average-load → (stress|spike|soak) según necesidad; no saltes a stress sin baseline.
4. Fija entorno, datos, ventana y plan de aborto; marca producción como alto riesgo.
5. Lista métricas ISO/IEC 25010 relevantes: time behaviour, resource utilization, capacity.
6. Identifica dependencias (observabilidad, datos sintéticos, cupos de terceros).
7. Propón calendario: qué corre en CI vs pre-release vs schedule.
8. Entrega riesgos y dueños (app/infra/seguridad).

## Salida

```md
## Objetivo medible
## Tipo(s) de prueba y justificación
## Orden de ejecución
## Entorno / datos / aborto
## Métricas y SLOs candidatos
## Calendario (CI vs pesadas)
## Riesgos / dueños
## Pendientes
```

## Casos límite

- Solo hay “hacerlo más rápido” sin número → no inventes SLO; exige NFR o propone baseline exploratoria etiquetada.
- Piden soak en producción mañana → BLOCKED sin mandato/ventana/límites.
- Múltiples objetivos mezclados → separa planes (regresión vs capacidad).

## Validación

- Tipo de prueba explícito.
- Entorno y riesgos documentados.
- Orden de madurez coherente.
- Sin umbrales inventados presentados como SLA firmado.

## Criterios de terminado

- Un director QA puede priorizar la corrida sin reinterpretar el plan.
- Gaps de SLO/entorno tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Validar p95 checkout en staging antes de release | Plan average-load + smoke previo + umbrales candidatos |
| Ambiguo | “Hagan un load test” | Preguntas + 2–3 tipos candidatos con trade-offs |
| Límite | Stress en prod sin ventana | BLOCKED con gaps de mandato |

## Fuentes

- Grafana k6 — API load testing (test types) — https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/ (2026-08-04).
- Grafana k6 — Automated performance testing — https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/ (2026-08-04).
- ISO/IEC 25010 performance efficiency — https://iso25000.com/en/iso-25000-standards/iso-25010 (2026-08-04).
