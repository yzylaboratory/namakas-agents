---
name: versionar-design-system
description: Gobierna versionado, deprecación y migración de tokens y componentes del design system. Úsala cuando haya breaking changes, releases del DS o retiro de tokens/componentes.
metadata:
  author: yzylabs
  version: "1.0"
---

# Versionar y evolucionar el design system

## Propósito

Evolucionar el sistema sin romper consumidores en silencio: SemVer (o política explícita), deprecación datada y guías de migración.

## Entradas

- Diff de tokens/componentes (antes/después).
- Política de versionado del repo/paquetes.
- Lista de consumidores conocidos.
- Fecha objetivo de retiro.

## Procedimiento

1. Clasifica cambios: additive, change (compat), breaking.
2. Asigna bump de versión (major/minor/patch) con justificación.
3. Para breaking: define reemplazo, periodo de deprecación y fecha de retiro.
4. Redacta guía de migración (antes → después) por token/componente.
5. Comunica impacto a Nami / Perona / Frontend vía reporte (no al usuario).
6. Actualiza changelog del sistema.
7. Verifica que tokens deprecated sigan resolviendo durante la ventana.

## Salida

```md
## Resumen de cambios
## Clasificación (additive/compat/breaking)
## Versión propuesta
## Deprecaciones (tabla)
## Guía de migración
## Changelog entry
## Riesgos / consumidores impactados
```

## Casos límite

- Renombrado masivo sin alias → major obligatorio + aliases temporales recomendados.
- Sin consumidores → igual versiona; documenta asunción.
- Pedido de “cambiar primary ya” en prod → plan de major; no silent overwrite.

## Validación

- Todo breaking tiene migración.
- Fechas de deprecación explícitas.
- No se borra token publicado sin major o excepción de Nami.

## Criterios de terminado

- Consumidores saben qué actualizar y para cuándo.
- El artefacto de versión es trazable.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Nuevo semántico + fix typo | minor/patch + changelog |
| Ambiguo | “Actualiza colores” | Clasificación + preguntas de breaking |
| Límite | Eliminar `color.text.muted` en uso | major + deprecación + migración |

## Fuentes

- DTCG 2025.10 stability / exchange expectations — https://www.designtokens.org/tr/2025.10/ (consultado 2026-08-04).
- Prácticas de deprecación en sistemas tipo Spectrum design-data / token pipelines (consultado 2026-08-04).
