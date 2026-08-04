---
name: definir-umbrales-slo-rendimiento
description: Traduce SLOs/NFRs/baselines a umbrales pass/fail (p95/p99, error rate, checks) para tools como k6. Úsala cuando se necesite criterio de aceptación de rendimiento o gates medibles.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir umbrales SLO de rendimiento

## Propósito

Evitar veredictos subjetivos: mapear objetivos de servicio a thresholds/checks que fallen de forma explícita (incl. exit code en CI).

## Entradas

- SLOs/SLAs/NFRs o baseline histórica.
- Endpoints/flujos bajo prueba.
- Tipo de prueba (umbrales pueden diferir smoke vs stress).
- Tooling (k6 thresholds, etc.).

## Procedimiento

1. Lista SLOs candidatos: latencia (p95/p99), disponibilidad/error rate, throughput mínimo.
2. Etiqueta fuente de cada número (SLA firmado, NFR, baseline medida, propuesta).
3. Traduce a umbrales de herramienta (p. ej. `http_req_duration: ['p(95)<…']`, `http_req_failed: ['rate<…']`, `checks: ['rate>…']`).
4. Separa: checks = corrección funcional bajo carga; thresholds = aceptación de performance.
5. Define política `abortOnFail` solo cuando el valor de abortar supera el costo de seguir midiendo.
6. Documenta excepciones por entorno (prod smoke más estricto en errores; stress puede esperar degradación controlada).
7. Entrega matriz SLO ↔ umbral ↔ acción (fail CI / fail release / solo alerta).

## Salida

```md
## SLOs y fuente
## Matriz umbrales
## Checks vs thresholds
## abortOnFail / política
## Gaps (números faltantes)
```

## Casos límite

- Sin ningún número → no inventes SLA; entrega propuesta marcada “propuesta” + pide dueño de producto.
- Stress con mismos umbrales que average-load → ajusta expectativas o tipifica mal el test.
- p99 sin telemetría suficiente → advierte incertidumbre estadística en corridas cortas.

## Validación

- Cada umbral tiene fuente o etiqueta de propuesta.
- Matriz actionable en CI o release checklist.
- No se presenta propuesta como SLA contractual.

## Criterios de terminado

- Pass/fail es reproducible por otro agente/ingeniero.
- Gaps de SLO tienen `DECISIONS_REQUIRED`.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | SLA p95<300ms error<1% | Thresholds k6 + checks |
| Ambiguo | “Que sea rápido” | Propuesta etiquetada + preguntas |
| Límite | Soak 8h sin umbral de degradación | Exige trend/error budget o BLOCKED |

## Fuentes

- Grafana k6 — Automated performance testing (Thresholds / quality gates) — https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/ (2026-08-04).
- Grafana k6 docs — https://grafana.com/docs/k6/latest/ (2026-08-04).
- ISO/IEC 25010 — time behaviour / capacity — https://iso25000.com/en/iso-25000-standards/iso-25010 (2026-08-04).
