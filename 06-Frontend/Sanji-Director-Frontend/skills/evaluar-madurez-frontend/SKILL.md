---
name: evaluar-madurez-frontend
description: Evalúa la madurez del departamento Frontend (a11y, performance, design system, multi-canal, DX portal, observabilidad) y propone gates de readiness. Úsala cuando se pida assessment de madurez frontend, readiness de release multi-canal o diagnóstico de plataforma UI.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar madurez Frontend

## Propósito

Diagnosticar el estado del departamento Frontend con dimensiones observables y un plan de gates — sin teatro de maturity models genéricos.

## Entradas

- Inventario de superficies (web, móvil, portal).
- Evidencias: auditorías, RUM, cobertura tests UI, adopción DS, incidentes.
- Objetivo de negocio o release que motiva la evaluación.

## Procedimiento

1. Evalúa dimensiones (0–3 o Red/Amber/Green) con evidencia:
   - Accesibilidad operativa (política, CI, manual, deuda).
   - Performance (budgets, RUM, umbrales por canal).
   - Design system (tokens, versionado, adopción, docs).
   - Entrega por canal (Cavendish/Reiju/Koala readiness).
   - Alineación multi-canal.
   - DX portal (si aplica).
   - Observabilidad UX / errores cliente.
   - Seguridad de superficie (XSS/sesión) — flag para Fujitora si débil.
2. Identifica bloqueadores para el outcome pedido.
3. Propón gates de readiness (qué debe ser Green antes de escalar).
4. Recomienda 3–5 movimientos de mayor apalancamiento (plataforma > features cosméticos).
5. Señala dependencias externas (Nami, Backend, Sabo, Franky).

## Salida

```md
## Contexto y outcome
## Scorecard de madurez
| Dimensión | Nivel | Evidencia | Gap |
## Bloqueadores
## Gates de readiness
## Movimientos recomendados (Now)
## Dependencias / escalamientos
```

## Casos límite

- Sin datos: madurez “desconocida” en esa dimensión + plan de medición; no inventes scores.
- Solo portal en alcance: scorecard reducido; no penalices móvil ausente si no hay mandato.
- Células stub: refleja riesgo de ejecución en scorecard.

## Validación

- Cada score cita evidencia o declara “sin datos”.
- Gates son binarios/verificables.
- Recomendaciones tienen dueño sugerido.

## Criterios de terminado

- Scorecard defendible ante Luffy.
- Gates listos para usar en priorización.

## Fuentes

- web.dev Web Vitals — https://web.dev/articles/vitals (2026-08-04)
- W3C WCAG 2.2 — https://www.w3.org/TR/WCAG22/ (2026-08-04)
- Smashing Magazine — a11y operational capability — 2026-06
