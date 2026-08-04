---
name: definir-estrategia-frontend
description: Define la estrategia y hoja de ruta Frontend (producto vs plataforma, canales web/móvil/portal, outcomes de experiencia). Úsala cuando se pida estrategia frontend, roadmap de experiencias digitales o posicionamiento multi-canal.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia Frontend

## Propósito

Convertir objetivos de negocio y restricciones de canal en una estrategia accionable de Frontend, con secuencia de capacidades y métricas.

## Entradas

- Objetivo de negocio y audiencia.
- Canales afectados (web, móvil, portal) y stack conocido.
- Estado actual: design system, deuda a11y/perf, apps, portal.
- Restricciones de plazo, riesgo y capacidad del squad.

## Procedimiento

1. Fija el horizonte (p. ej. 2–4 trimestres) y el outcome principal (conversión, adopción portal, remediación a11y, unificación multi-canal).
2. Clasifica iniciativas en: **producto/journeys**, **plataforma frontend** (DS, tooling, CI), **deuda de calidad** (a11y/perf).
3. Secuencia capacidades fundacionales antes de escala:
   - Accesibilidad operativa (WCAG objetivo + DoD).
   - Performance de campo (CWV web / métricas nativas móvil).
   - Tokens/componentes y gobernanza de design system.
   - Observabilidad de UX (RUM, errores de UI, crash-free).
   - DX del portal (si hay terceros/partners).
4. Define Now / Next / Later con dueño (Sanji / Cavendish / Reiju / Koala / Nami).
5. Declara supuestos, no-objetivos y riesgos (incluyendo dependencia Backend/API).
6. Propón 3–6 KPIs (CWV p75, % journeys WCAG, adopción DS, TTFHW portal, crash-free, time-to-ship).

## Salida

```md
## Estrategia Frontend
- Canales / audiencia:
- Outcome:
- Producto vs plataforma vs deuda:
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap de experiencias
| Experiencia | Valor | Dependencias | Riesgo |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Solo un canal: estrategia acotada; no inventes roadmap móvil/portal sin mandato.
- Portal sin producto API claro: alinear con Sabo/Jinbe antes de invertir UI.
- Deuda a11y legal (EAA etc.): estrategia con escenarios y escalamiento Legal; no dictamen.

## Validación

- Hay separación producto / plataforma / deuda.
- La secuencia no salta a11y/perf/DS cuando el outcome lo requiere.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones de estándar citan fuente/fecha.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones UX/Arquitectura/Legal identificadas cuando correspondan.

## Fuentes

- W3C WCAG 2 Overview — https://www.w3.org/WAI/standards-guidelines/wcag/ (2026-08-04)
- web.dev Web Vitals — https://web.dev/articles/vitals (2026-08-04)
- Smashing Magazine — Accessibility as operational capability — 2026-06
