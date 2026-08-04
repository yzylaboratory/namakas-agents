---
name: especificar-componentes-ui
description: Especifica componentes de UI en contexto de pantalla (variantes, props, estados). Úsala cuando haya que detallar botones, forms, tablas o patrones del DS en una interfaz concreta — no para crear el sistema de diseño completo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar componentes UI

## Propósito

Traducir el layout a una tabla de componentes implementable: qué pieza del DS usar, en qué variante/estado, y qué contenido muestra.

## Entradas

- Spec de layout o pantallas objetivo.
- Catálogo / tokens del DS (Miss Goldenweek) o referencia al DS vigente.
- Contenido (labels, datos) o placeholders.
- Restricciones de plataforma y densidad.

## Procedimiento

1. Inventaría elementos interactivos y de presentación por región.
2. Mapea cada elemento a un componente del DS; marca gaps.
3. Para cada componente lista: variante, tamaño/densidad, contenido, acción.
4. Define estados obligatorios: default, focus/hover (si aplica), disabled, loading, error, empty.
5. Especifica validación inline y mensajes de error cortos (UI microcopy).
6. Señala dependencias de datos (skeleton vs spinner) y permisos.
7. Emite `DELEGATION_REQUIRED` a Miss Goldenweek si falta el componente en el DS.

## Salida

```md
# Componentes — [Pantalla]

| ID | Región | Componente DS | Variante | Contenido | Estados | Notas |
|---|---|---|---|---|---|---|

## Gaps DS
- [componente faltante → escalar Miss Goldenweek]

## Microcopy UI
| Elemento | Texto | Notas |
```

## Casos límite

- DS ausente: especifica semántica (“primary button”) y escala; no inventes hex.
- Componente custom único: justifica y escala al DS antes de proliferar one-offs.
- Formularios largos: agrupa; un error por campo; resumen de errores accesible.
- Tablas densas: define empty + loading + truncated cells.

## Validación

- Cada control interactivo tiene estado focus/disabled documentado o N/A.
- Gaps DS explícitos.
- Sin tokens de color/spacing inventados.

## Criterios de terminado

- Tabla de componentes completa para el alcance.
- Estados críticos cubiertos.
- Gaps y microcopy listados.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Form login + DS básico | Inputs, CTA, errores inline |
| Ambiguo | “Usa cards modernas” sin DS | Semántica + escalamiento DS |
| Límite | Acción irreversible | Confirmación + disabled mientras procesa |

## Fuentes

- W3C WCAG 2.2 — input assistance / name, role, value (2026-08-04) — https://www.w3.org/TR/WCAG22/
- Material / Android canonical component usage vía docs oficiales de layout (2026-08-04)
- Apple HIG — componentes de plataforma según target (2026-08-04)
