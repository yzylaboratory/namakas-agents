---
name: disenar-layout-interfaz
description: Diseña la estructura y jerarquía de una pantalla o conjunto de pantallas (regiones, breakpoints, wireframe). Úsala cuando haya que componer layout UI, no cuando solo se pidan tokens del sistema de diseño o research de usuario.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar layout de interfaz

## Propósito

Producir una especificación de layout accionable: regiones, jerarquía visual, densidad y adaptación por tamaño de ventana/pantalla.

## Entradas

- Objetivo de la pantalla (job único).
- Audiencia y plataforma (web / iOS / Android / desktop).
- Brief o restricciones de marca/DS.
- Breakpoints o window size classes conocidos.
- Contenido real o placeholders marcados.
- Layouts canónicos de referencia si aplican (list-detail, feed, supporting pane).

## Procedimiento

1. Nombra el job de la pantalla en una frase; si hay varios jobs, propón separación o priorización.
2. Lista regiones (header, nav, primary, supporting, footer) y su prioridad.
3. Elige un patrón de layout (single column, list-detail, feed, supporting pane, custom justificado).
4. Define comportamiento por breakpoint (compact / medium / expanded u HIG equivalent).
5. Dibuja wireframe ASCII o descripción ordenada top→bottom / primary→secondary.
6. Fija reglas de spacing y densidad coherentes con el DS (sin inventar tokens).
7. Lista supuestos y riesgos (overflow, line length, scroll atrapado).

## Salida

```md
# Layout — [Pantalla]

## Job
[una frase]

## Regiones
| Región | Contenido | Prioridad |

## Patrón
[list-detail | feed | supporting-pane | single | otro]

## Breakpoints
| Clase | Comportamiento |

## Wireframe
[ASCII o bullets estructurales]

## Supuestos / riesgos
- …
```

## Casos límite

- Brief sin audiencia: pregunta o declara supuesto; no inventes personas.
- Multi-job en un viewport: recomienda split o progressive disclosure.
- Solo móvil legacy: documenta compact-first; no finjas layouts expanded.
- Conflicto con DS: escala a Miss Goldenweek; no crees grid paralelo.

## Validación

- Un implementador puede colocar regiones sin adivinar.
- Hay al menos un comportamiento para el breakpoint primario del producto.
- No hay tokens inventados.

## Criterios de terminado

- Spec de layout entregada.
- Wireframe o estructura explícita.
- Supuestos y riesgos listados.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Pantalla listado + detalle web | Layout list-detail + breakpoints |
| Ambiguo | “Hazla bonita” sin job | Preguntas/supuestos; no ornamentar |
| Límite | Tres CTAs primarios en hero | Priorización; un CTA primario |

## Fuentes

- Android Developers — Canonical layouts (2026-08-04) — https://developer.android.com/design/ui/mobile/guides/layout-and-content/canonical-layouts
- Android Developers — Window size classes (2026-08-04) — https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes
- Apple HIG — Layout (2026-08-04) — https://developer.apple.com/design/human-interface-guidelines/layout
