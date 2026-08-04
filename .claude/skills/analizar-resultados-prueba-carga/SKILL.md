---
name: analizar-resultados-prueba-carga
description: Analiza resultados de una corrida de carga (percentiles, errores, saturación, cuellos de botella) y emite veredicto con evidencia. Úsala tras ejecutar o al recibir métricas/logs de performance.
metadata:
  author: yzylabs
  version: "1.0"
---

# Analizar resultados de prueba de carga

## Propósito

Convertir salidas del generador y del SUT en un informe accionable: ¿pasó umbrales?, ¿dónde degradó?, ¿el generator es válido?, ¿quién debe actuar?

## Entradas

- Tipo de prueba y perfil ejecutado.
- Umbrales/SLOs acordados.
- Salida del tool (k6 summary, reportes, CSV).
- Métricas del SUT (CPU, memoria, DB, colas, APM) si existen.
- Condiciones del load generator (CPU del runner).

## Procedimiento

1. Verifica validez de la corrida: script errors, generator saturado, entorno incorrecto.
2. Contrasta métricas vs umbrales (pass/fail por criterio).
3. Examina ramp: ¿dónde empieza la degradación de latencia/errores?
4. Separa fallos de aplicación vs timeouts vs rate limits vs infra.
5. Correlaciona con observabilidad del SUT; no culpes “la app” sin señal.
6. Clasifica cuellos de botella (app CPU, DB, pool, red, dependencia externa).
7. Emite veredicto: PASS | FAIL | INVALID_RUN | INCONCLUSIVE.
8. Lista acciones recomendadas con dueño propuesto.

## Salida

```md
## Validez de la corrida
## Veredicto vs umbrales
## Hallazgos (percentiles, errores, throughput)
## Correlación SUT
## Cuellos de botella / dueños
## Riesgos residuales
## Evidencia (rutas/artefactos)
```

## Casos límite

- Generator al 100% CPU → INVALID_RUN; no uses números para release.
- Pass de umbrales pero errores de negocio en checks → FAIL funcional bajo carga.
- Sin métricas de SUT → INCONCLUSIVE parcial; lista gap de observabilidad.

## Validación

- Veredicto etiquetado y justificado.
- Umbrales citados.
- Evidencia adjunta o referenciada.

## Criterios de terminado

- Usopp puede consolidar pass/fail de release con este informe.
- INVALID_RUN no se disfraza de PASS.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Summary k6 + umbrales + CPU SUT | PASS/FAIL con cuello de botella |
| Ambiguo | Solo screenshot de dashboard | INCONCLUSIVE + lista de artefactos faltantes |
| Límite | Latencia alta y runner al 95% CPU | INVALID_RUN |

## Fuentes

- Grafana k6 — Automated performance testing — https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/ (2026-08-04).
- Grafana k6 — Stress testing (degradación en ramp) — https://grafana.com/docs/k6/latest/testing-guides/test-types/stress-testing/ (2026-08-04).
- ISO/IEC 25010 — resource utilization / time behaviour — https://iso25000.com/en/iso-25000-standards/iso-25010 (2026-08-04).
