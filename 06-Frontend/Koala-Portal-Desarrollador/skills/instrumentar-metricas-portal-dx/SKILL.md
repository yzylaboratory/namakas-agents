---
name: instrumentar-metricas-portal-dx
description: Define instrumentación y métricas DX del portal (TTFHW, funnel de activación, search zero-results). Úsala cuando se pida medir adopción del portal, analytics de docs o Time to First Hello World.
metadata:
  author: yzylabs
  version: "1.0"
---

# Instrumentar métricas DX del portal

## Propósito

Especificar eventos y tablero mínimo para medir si el portal convierte desarrolladores hasta el primer call y dónde abandonan.

## Entradas

- Journey UI acordado (onboarding + playground).
- Stack de analytics disponible.
- Meta TTFHW objetivo.
- Restricciones de privacidad (sin PII en eventos).
- Dueños Sanji/Sabo para revisión semanal.

## Procedimiento

1. Define TTFHW: timestamps signup_ok → key_issued → first_call_ok (sandbox).
2. Lista eventos de funnel: view_home, view_quickstart, signup_start/ok, key_issued, try_it_run, first_call_ok, search_query, search_zero_results.
3. Especifica propiedades mínimas (api_id, major, env=sandbox|prod, error_code) sin PII.
4. Propón tablero semanal: mediana TTFHW, activation rate, top zero-results, top playground errors.
5. Define alertas simples (p. ej. zero-results spike, TTFHW p50 > umbral).
6. Escala revenue/conversión comercial a Du-Feld; aquí solo DX de portal.

## Salida

```md
## Definición TTFHW
## Catálogo de eventos
## Tablero mínimo
## Privacidad / PII
## Cadencia de revisión
## Gaps + owners
```

## Casos límite

- Sin backend de analytics → especifica eventos + adapter; no finjas métricas.
- first_call solo en gateway → correlaciona portal user_id pseudónimo con API logs (Fujitora/privacidad).
- Tráfico de agentes AI a docs → métrica separada si el stack lo permite (Mintlify-like).

## Validación

- TTFHW es medible con los eventos definidos.
- No se capturan secrets ni PII en payloads.
- Hay owner de revisión semanal.

## Criterios de terminado

- Catálogo de eventos listo para ingeniería.
- Tablero mínimo acordado con Sanji/Sabo.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Portal con signup + playground | Eventos + TTFHW + tablero |
| Ambiguo | “Mide DX” sin stack | Eventos canónicos + opciones de adapter |
| Límite | Solo docs estáticas sin auth | Proxy metrics (scroll, search) + límites |

## Fuentes

- APIScout API Analytics / Measuring DX 2026 — https://apiscout.dev/guides/api-analytics-measuring-developer-experience-2026 (2026-08-04).
- APIScout Developer Portal 2026 (TTFHW) — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- Mintlify enterprise analytics / AI traffic — https://www.mintlify.com/library/api-developer-portals-for-enterprise (2026-08-04).
