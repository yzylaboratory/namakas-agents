---
name: auditar-adopcion-design-system
description: Audita la adopción del design system (hard-codes, forks, tokens huérfanos, contraste fallido) y prioriza remediación. Úsala cuando se pida revisar consistencia o deuda visual frente al DS.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar adopción del design system

## Propósito

Medir y priorizar desviaciones entre el sistema publicado y lo que diseño/código realmente usan.

## Entradas

- Inventario de tokens/componentes “fuente de verdad”.
- Superficies a auditar (Figma, CSS, app web/móvil).
- Severidad objetivo (a11y, breaking, cosmética).
- Ventana temporal / alcance de productos.

## Procedimiento

1. Fija el baseline del sistema (versión de tokens/componentes).
2. Muestrea o escanea superficies: valores crudos, componentes fork, tokens deprecated en uso.
3. Clasifica hallazgos: `a11y`, `contrato`, `deuda`, `falso positivo`.
4. Prioriza (a11y > ruptura de contrato > deuda cosmética).
5. Asigna dueño sugerido (Perona / Frontend / Nami) sin delegar tú mismo.
6. Propón remediación mínima (mapear a semántico, retirar fork, actualizar tema).
7. Resume métricas (%% adopción, top N desviaciones).

## Salida

```md
## Baseline / alcance
## Hallazgos (tabla: id, severidad, evidencia, dueño sugerido)
## Métricas de adopción
## Plan de remediación
## Riesgos residuales
```

## Casos límite

- Sin baseline versionado → primero establece versión; auditoría `COMPLETED_WITH_LIMITATIONS`.
- Marketing pages fuera de DS → segrega alcance; no forces 100%.
- Solo capturas → auditoría cualitativa etiquetada como muestreo.

## Validación

- Cada hallazgo material tiene evidencia (ruta, captura, snippet).
- Severidades consistentes.
- No se inventan fallos de contraste sin pares medidos o criterio explícito.

## Criterios de terminado

- Nami puede priorizar backlog de remediación con la tabla.
- Top desviaciones a11y están explícitas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App + tokens v1.2 | Tabla priorizada + métricas |
| Ambiguo | “Está inconsistente” | Alcance propuesto + muestreo inicial |
| Límite | Sin DS versionado | BLOCKED/limitations + pedido de baseline |

## Fuentes

- WCAG 2.2 contrast criteria — https://www.w3.org/TR/WCAG22/ (consultado 2026-08-04).
- Prácticas de gobernanza token/component (Spectrum design-data validation patterns) — https://github.com/adobe/spectrum-design-data (consultado 2026-08-04).
