---
name: disenar-escenarios-carga
description: Diseña escenarios de carga realistas (flujos, stages, VUs vs arrival-rate, think time, datos). Úsala cuando ya hay tipo de prueba y hay que modelar el perfil o el script de carga.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar escenarios de carga

## Propósito

Traducir el tipo de prueba en un perfil ejecutable: journeys, ramping, concurrencia o RPS, datos y checks básicos — listos para herramienta (p. ej. k6) sin inventar tráfico irreal.

## Entradas

- Tipo de prueba aprobado (smoke / average-load / stress / spike / breakpoint / soak).
- Flujos críticos (OpenAPI, user journeys, contratos).
- Objetivo de carga (VUs, RPS, duración) o baseline de tráfico.
- Restricciones de datos y rate limits.
- Herramienta objetivo (k6 preferida si no hay estándar de equipo).

## Procedimiento

1. Selecciona journeys representativos (no solo un healthcheck).
2. Decide modelo: VUs (concurrencia) vs arrival-rate/RPS (throughput garantizado).
3. Define stages: ramp-up, sustain, ramp-down (o spike vertical) acorde al tipo.
4. Añade think time / sleep realista entre pasos de usuario.
5. Especifica checks de respuesta (status, schema mínimo) separados de thresholds.
6. Diseña datos: pool sintético, idempotencia, cleanup; sin PII.
7. Declara precondiciones (auth tokens de test, seeding) y teardown.
8. Entrega pseudocódigo o estructura de script (options + scenario) versionable.

## Salida

```md
## Journeys
## Modelo (VU | arrival-rate)
## Stages / duración
## Datos y auth de prueba
## Checks
## Estructura de script / options
## Supuestos
## Riesgos
```

## Casos límite

- Solo RPS de un GET → advierte coverage pobre; propone journey de negocio.
- Spike sin ramp-down → documenta expectativa de recuperación.
- Auth OAuth real de prod → BLOCKED; exige credenciales de test.

## Validación

- Stages coherentes con el tipo tipificado.
- Think time y datos presentes o justificados.
- Sin secretos embebidos.

## Criterios de terminado

- Un ingeniero puede implementar/ejecutar el escenario sin adivinar el perfil.
- Smoke del script es factible antes de la carga pesada.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Average-load login→list→pay en staging | Stages + VUs/RPS + checks + datos sintéticos |
| Ambiguo | “1000 users” sin duración | Clarifica VU vs RPS + propone stages |
| Límite | Spike con tokens de prod | BLOCKED + alternativa test credentials |

## Fuentes

- Grafana k6 — Smoke testing — https://grafana.com/docs/k6/latest/testing-guides/test-types/smoke-testing/ (2026-08-04).
- Grafana k6 — Stress testing — https://grafana.com/docs/k6/latest/testing-guides/test-types/stress-testing/ (2026-08-04).
- Grafana k6 — API load testing — https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/ (2026-08-04).
