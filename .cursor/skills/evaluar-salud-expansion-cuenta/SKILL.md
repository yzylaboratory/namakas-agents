---
name: evaluar-salud-expansion-cuenta
description: Evalúa salud, riesgo de churn y oportunidades de expansión de una cuenta estratégica B2B con señales y acciones. Úsala cuando se pida account health, retención, NRR/expansión o early-warning — no para clasificar el portfolio completo (usa clasificar-cuentas-estrategicas).
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar salud y expansión de cuenta

## Propósito

Diagnosticar el estado de la relación y el revenue: señales de salud, riesgo de pérdida y vías de expansión — con acciones dueño+fecha y sin inventar métricas.

## Entradas

- Cuenta + plan/mapa existentes (si hay).
- Señales: uso/adopción, tickets, engagement, pipeline, competencia, renewals.
- Contexto financiero disponible (ARR, wallet share) o declaración de ausencia.
- Horizonte (30/90/180 días).

## Procedimiento

1. Define dimensiones de salud (adopción, satisfacción/engagement, relación/cobertura, valor entregado, competitividad, contractual).
2. Puntúa cada dimensión con evidencia; marca `unknown` si falta dato.
3. Clasifica riesgo de churn (bajo/medio/alto/crítico) con triggers observados.
4. Identifica oportunidades de expansión (nuevos BUs, upsell, cross-sell, geographic) ligadas a value map.
5. Propón acciones de retención y expansión (owner + due + señal).
6. Separa lo que es SAM vs lo que escala a producto, enablement, legal o partner success.
7. Resume outlook NRR/expansión solo si hay base; si no, lista instrumentación faltante.

## Salida

```md
## Cuenta / horizonte
## Health scorecard
| Dimensión | Estado | Evidencia | Gap |
## Riesgo de churn
## Oportunidades de expansión
## Acciones (retención / expansión)
## Escalaciones
## Datos a instrumentar
```

## Casos límite

- Champion quiet + uso estable → riesgo relacional aunque métricas “verdes”.
- Expansión pedida sin value fit → rechaza chase; vuelve a co-discovery.
- Solo hay feeling comercial → health cualitativo etiquetado; no inventes NRR.

## Validación

- Cada claim de riesgo/oportunidad tiene evidencia o `unknown`.
- Acciones tienen owner + due.
- No confunde health de una cuenta con tiering de portfolio.
- Sin promesas de descuento/SLA.

## Criterios de terminado

- Buggy ve riesgo y upside en una página accionable.
- Early warnings tienen trigger y respuesta.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Uso + tickets + renewal en 90 días | Scorecard + riesgo + plan retención |
| Ambiguo | “¿Cómo está la cuenta?” sin datos | Dimensiones + unknowns + datos mínimos |
| Límite | Competidor entrante + blocker económico | Riesgo alto + multi-thread + escalación |

## Fuentes

- SAMA — Realize/Expand Value; outcome-based tracking — https://strategicaccounts.org/sama-fundamentals/ (2026-08-04).
- SAMA — Seven Factors for Strategic Account Growth — https://strategicaccounts.org/the-essential-seven-factors-for-unlocking-strategic-account-growth/ (2026-08-04).
- Salesmotion — signal dashboard / stale plans — https://salesmotion.io/blog/strategic-account-planning-top-companies (2026-08-04).
- B2B Sales Training — signal-based triggers — https://b2bsalestraining.org/strategic-account-planning (2026-08-04).
