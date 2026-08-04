---
name: diagnosticar-fallo-pipeline
description: Diagnostica fallos de CI/CD con evidencia (job, step, logs, artefactos, flaky vs regresión). Úsala cuando un pipeline falle, sea rojo intermitente o un deploy se quede a medias; no para incidentes de runtime de producto (Viola) salvo señales del pipeline.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diagnosticar fallo de pipeline

## Propósito

Determinar causa raíz probable de un fallo CI/CD y proponer remediación verificable con evidencia.

## Entradas

- Enlace o ID de run/pipeline.
- Diff/commit asociado.
- Logs y artefactos disponibles.
- Historial reciente (¿flaky? ¿infra?).

## Procedimiento

1. Fija el job/step que falló primero (no el último síntoma).
2. Clasifica: código/test, config pipeline, secreto/permiso, runner/infra, flaky, dependencia externa.
3. Extrae evidencia: exit code, snippet de log (sin secretos), duración anómala, cache miss.
4. Reproduce localmente o en job de debug cuando sea seguro.
5. Si es flaky: cuarentena + dueño; no “re-run hasta verde” como solución.
6. Si es secreto/permiso: remedia y rota si hubo exposición.
7. Si el síntoma es runtime post-deploy: handoff a Viola con contexto del pipeline.
8. Entrega RCA corta + fix propuesto + validación (pipeline verde o prueba).

## Salida

```md
## Síntoma
## Clasificación
## Evidencia
## Causa raíz probable
## Remediación
## Validación
## Follow-ups
```

## Casos límite

- Logs con secretos → no copies secretos al reporte; rota y redacta.
- Fallo solo en self-hosted → sospecha entorno; no culpes al código sin evidencia.
- Rojo en main sin dueño → escala a Franky con impacto (merge freeze si aplica).

## Validación

- Evidencia citada (run ID, job, step).
- Clasificación coherente con logs.
- Remediación testeable.
- Sin secretos en el informe.

## Criterios de terminado

- Franky/equipo puede actuar sin re-investigar desde cero.
- Flaky/regresión distinguido.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Unit test fail en PR | RCA a test/código + fix |
| Ambiguo | “CI rojo” sin link | Pide run ID; hipótesis por síntomas parciales |
| Límite | Fallo intermitente e2e | Flaky policy + cuarentena; no ignore |

## Fuentes

- GitHub Docs — Using workflow run logs — https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs (2026-08-04).
- GitLab Docs — Debugging CI/CD — https://docs.gitlab.com/ee/ci/debugging.html (2026-08-04).
- DORA — Time to restore service (contexto de recuperación) — https://dora.dev/ (2026-08-04).
