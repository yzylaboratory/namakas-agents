---
name: clasificar-cuentas-estrategicas
description: Clasifica y prioriza cuentas B2B en tiers estratégicos con criterios explícitos (revenue, potencial, fit, riesgo, complejidad). Úsala cuando haya que decidir qué cuentas merecen plan SAM completo vs foco abreviado.
metadata:
  author: yzylabs
  version: "1.0"
---

# Clasificar cuentas estratégicas

## Propósito

Concentrar capacidad SAM en las cuentas correctas: definir criterios, asignar tiers y justificar inclusiones/exclusiones sin diluir el programa.

## Entradas

- Lista de cuentas candidatas (nombre, revenue actual/potencial, segmento).
- Capacidad del equipo (cuántas Tier 1 sostenibles).
- Criterios de negocio (si existen) o mandato de Buggy.
- Datos de riesgo (churn, competencia, concentración).

## Procedimiento

1. Declara criterios de calificación (mínimo: valor actual, potencial de expansión, strategic fit, riesgo/complejidad, influencia en roadmap).
2. Define tiers (p. ej. Tier 1 plan completo, Tier 2 abreviado, Outside = no SAM intensivo).
3. Puntúa cada cuenta con evidencia; etiqueta `dato faltante` cuando no haya fuente.
4. Ajusta al cupo de capacidad (no sobrecargues Tier 1).
5. Lista exclusiones y qué tratamiento reciben (enablement genérico, partner success, nurture).
6. Entrega matriz y recomendaciones de foco para Buggy.

## Salida

```md
## Criterios
## Capacidad (cupo Tier 1/2)
## Matriz de cuentas
| Cuenta | Tier | Score / justificación | Datos faltantes | Tratamiento |
## Recomendaciones
## Riesgos
```

## Casos límite

- Todas las cuentas “son estratégicas” → fuerza priorización por cupo y trade-offs.
- Sin datos de revenue → no inventes; clasifica provisional + lista de datos requeridos.
- Conflicto político por incluir una cuenta débil → documenta evidencia y escala a Buggy.

## Validación

- Criterios explícitos y aplicables.
- Cupo de capacidad respetado o gap declarado.
- Ningún score inventado sin marcar inferencia.
- Distinción clara Tier 1 vs Outside.

## Criterios de terminado

- Buggy puede aprobar/rechazar el foco con la matriz.
- Cuentas Outside tienen tratamiento alternativo nombrado (Mr. 3 / Bon Clay / nurture).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 20 cuentas con revenue y potencial | Matriz con ~5–10 Tier 1 justificadas |
| Ambiguo | “Todas son key accounts” | Cupo + ranking forzado + exclusiones |
| Límite | Lista sin métricas | Clasificación provisional + datos faltantes bloqueantes |

## Fuentes

- B2B Sales Training — Strategic Account Planning (tiering) — https://b2bsalestraining.org/strategic-account-planning (2026-08-04).
- SAMA Fundamentals — Understanding Organizational Priorities — https://strategicaccounts.org/sama-fundamentals/ (2026-08-04).
- Salesmotion — Strategic Account Planning Framework — https://salesmotion.io/blog/strategic-account-planning-top-companies (2026-08-04).
