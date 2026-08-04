---
name: definir-estrategia-experiencia
description: Define la estrategia y hoja de ruta de experiencia de usuario (principios, outcomes, secuencia HCD). Úsala cuando se pida estrategia UX, visión de experiencia, principios de diseño o roadmap de journeys.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia de experiencia

## Propósito

Convertir objetivos de negocio y jobs de usuario en una estrategia accionable de UX/UI, con principios, secuencia de capacidades y métricas.

## Entradas

- Objetivo de producto y audiencia.
- Contextos de uso (web, móvil, portal, backoffice) y restricciones de marca/plataforma.
- Estado actual: flujos críticos, design system, deuda UX, hallazgos previos.
- Restricciones de plazo, accesibilidad y capacidad del squad.

## Procedimiento

1. Fija horizonte (p. ej. 1–2 trimestres) y outcome principal (completitud de tarea, reducción de errores, adopción, NPS/CSAT de flujo).
2. Declara 4–7 principios de diseño verificables (no eslóganes).
3. Clasifica iniciativas en: **fundacionales** (research ops, a11y, sistema), **journeys críticos**, **deuda UX**.
4. Secuencia según ISO 9241-210 a nivel departamental: contexto → requisitos → soluciones → evaluación → iteración.
5. Define Now / Next / Later con dueño (Nami / Chopper / Perona / Miss Goldenweek / Frontend).
6. Declara no-objetivos, supuestos y riesgos (a11y, consistencia, capacidad).
7. Propón 3–6 KPIs (task success, time-on-task, error rate, adopción de componentes, % flujos con research).

## Salida

```md
## Estrategia de experiencia
- Audiencia / contextos:
- Outcome:
- Principios:
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap de journeys
| Journey | Valor | Dependencias | Riesgo |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Multi-producto / multi-marca: capa común de sistema + deltas locales; no unificar a la fuerza.
- Solo “hacerlo bonito”: rechazar como estrategia; exigir jobs y outcomes.
- Sin research histórico: estrategia con discovery Now obligatorio antes de rediseño amplio.

## Validación

- Hay principios verificables y KPIs.
- La secuencia no salta evaluación/accesibilidad en journeys de alto riesgo.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones de estándar (ISO/WCAG) citan fuente.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones Frontend/Legal identificadas cuando correspondan.

## Fuentes

- ISO 9241-210 — Human-centred design for interactive systems (referencia de proceso) — consultado 2026-08-04
- Nielsen Norman Group — State of UX in 2026 — https://www.nngroup.com/articles/state-of-ux-2026/ (2026-08-04)
- W3C WAI — WCAG 2 Overview — https://www.w3.org/WAI/standards-guidelines/wcag/ (2026-08-04)
