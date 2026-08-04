---
name: automatizar-gates-rendimiento-ci
description: Diseña gates de rendimiento en CI/CD (smoke en PR, cargas pesadas en pre-release/schedule, thresholds como quality gate). Úsala cuando pidan integrar k6 u otra tool de load en pipeline.
metadata:
  author: yzylabs
  version: "1.0"
---

# Automatizar gates de rendimiento en CI

## Propósito

Integrar pruebas de rendimiento como calidad continua sin bloquear cada PR con soak/stress: smoke frecuente + cargas pesadas en el momento correcto, con umbrales que fallen el pipeline.

## Entradas

- Suite de scripts tipificados (smoke vs average-load vs stress…).
- Umbrales pass/fail.
- Plataforma CI (GitHub Actions, GitLab CI, etc.).
- Entornos disponibles por stage.
- Frecuencia de release y tolerancia a flakiness.

## Procedimiento

1. Clasifica tests: smoke (CI rama), average-load (pre-release/schedule), stress/spike (pre-release), soak (schedule largo).
2. Mapea a entornos: QA/CI → smoke; pre-release/staging → cargas medias/altas; prod → solo smoke sintético autorizado.
3. Configura thresholds para exit code ≠ 0 en fallo de gate.
4. Define triggers: PR, nightly, release candidate, checklist manual.
5. Aísla secretos y URLs por environment variables; nunca hardcode.
6. Publica artefactos (summary JSON/HTML) como evidencia de pipeline.
7. Documenta política anti-flake (re-run controlado, no ocultar regresiones reales).
8. Entrega YAML/pseudoconfig de job + matriz de frecuencia.

## Salida

```md
## Matriz test × entorno × trigger
## Gates y umbrales
## Jobs CI (borrador)
## Artefactos / evidencia
## Política flake / abort
## Riesgos
```

## Casos límite

- Pedir soak en cada PR → rechaza; propone nightly/pre-release.
- Sin entorno estable de staging → BLOCKED para gates pesados; solo smoke contra mock/QA.
- Thresholds demasiado estrictos sin baseline → marca como experimental.

## Validación

- Ningún job de PR ejecuta soak/stress por defecto.
- Smoke tiene umbrales mínimos y falla en errores de script/SUT.
- Secretos no están en claro en el YAML propuesto.

## Criterios de terminado

- La matriz es implementable por el equipo de CI.
- Evidencia de corrida queda como artefacto referenciable en reportes QA.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Repo con k6 smoke + staging | PR smoke + nightly average-load |
| Ambiguo | “Meter performance en CI” | Matriz tipificada + preguntas de entorno |
| Límite | Soak 4h en merge gate | Rechazo + alternativa schedule |

## Fuentes

- Grafana k6 — Automated performance testing — https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/ (2026-08-04).
- Grafana k6 — API load testing (automation table) — https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/ (2026-08-04).
- Grafana k6 docs — https://grafana.com/docs/k6/latest/ (2026-08-04).
