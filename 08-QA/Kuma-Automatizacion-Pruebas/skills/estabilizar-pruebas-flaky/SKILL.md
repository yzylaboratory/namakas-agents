---
name: estabilizar-pruebas-flaky
description: Diagnostica y corrige tests intermitentes (flaky): timing, selectores, estado, paralelismo o entorno. Úsala cuando CI “a veces falla”, haya retries crónicos o se pida cuarentena.
metadata:
  author: yzylabs
  version: "1.0"
---

# Estabilizar pruebas flaky

## Propósito

Reducir señal falsa en CI: clasificar causa raíz, aplicar fix o cuarentena controlada, y medir flaky rate — sin ocultar defectos con reintentos ciegos.

## Entradas

- Nombre(s) de test flaky y tasa aproximada.
- Logs/CI artifacts (trace, video, screenshot, JUnit).
- Config de retries, workers/paralelismo, browsers.
- Cambios recientes en SUT o harness.

## Procedimiento

1. Reproduce con seed/worker aislado; captura trace si el framework lo permite.
2. Clasifica hipótesis: timing/race, locator ambiguo, estado compartido, datos, red/terceros, infra CI, defecto real de producto.
3. Confirma con evidencia (no intuición): qué actionability falló, qué assertion timeout.
4. Aplica fix preferente:
   - Locator más específico / test-id.
   - Aserción web-first en lugar de sleep.
   - Aislamiento de estado / fixtures.
   - Mock de tercero inestable.
5. Si no hay fix inmediato: cuarentena con owner, ticket, fecha de salida y test aún listado en reporte.
6. Limita retries: documenta por qué existen; no uses retries como “solución”.
7. Re-ejecuta N veces (acordado, p. ej. 10–20) o en CI nightlies para validar estabilidad.
8. Reporta flaky rate antes/después.

## Salida

```text
FLAKY_REPORT:
- test:
  failure_rate_before:
  root_cause_class:
  evidence:
  fix:
  quarantine: yes|no
  owner:
  exit_date:
  failure_rate_after:
PRODUCT_BUGS_FOUND:
```

## Casos límite

- Falla solo en CI Linux / no local → compara browsers, timezone, recursos, race de paralelismo.
- “Flaky” que es bug de producto intermitente → reporta como producto; no lo marques solo harness.
- Suite entera inestable → pausa nuevos E2E; escala testability a Usopp.

## Validación

- Causa clasificada con evidencia.
- Si cuarentena: owner + fecha de salida obligatorios.
- Retries no aumentaron sin justificación.
- Métrica post-fix registrada o plan de medición explícito.

## Criterios de terminado

- Fix merged o cuarentena documentada.
- Instrucciones de reproducción.
- Riesgo residual explícito para Usopp.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | click timeout 30% | Locator/assert fix; rate ↓ |
| Ambiguo | “CI rojo a veces” sin nombre | Pedir artifacts; triaging set |
| Límite | Pedido retries:10 sin análisis | Rechazo; diagnóstico primero |

## Fuentes

- Playwright Auto-waiting / Best Practices (2026-08-04).
- ISTQB CTAL-TAE v2.0 — verificación de la solución de automatización y mejora continua (Caps. 7–8, 2024).
