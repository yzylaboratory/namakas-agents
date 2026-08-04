---
name: gobernar-experiencia-versiones-portal
description: Diseña la experiencia de versionado, deprecación y changelog en el developer portal (switcher, banners, migración). Úsala cuando se pida UX de versiones de API, notices de breaking change o changelog en portal.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar experiencia de versiones en el portal

## Propósito

Hacer visibles majors, deprecaciones y migraciones en la UI del portal, alineados a la política de versionado de producto (Sabo), sin inventarla.

## Entradas

- Política de versionado/deprecación (Sabo u OBL-like).
- Majors publicados y ventanas de soporte.
- Changelogs / notices existentes.
- OpenAPI por major.
- Fechas de sunset (si hay).

## Procedimiento

1. Inventaría majors activos y estado (current, deprecated, sunset).
2. Diseña switcher de versión en catálogo y referencia; URL o ruta estable por major.
3. Especifica banners de deprecación (qué cambia, hasta cuándo, enlace a guía).
4. Define página/changelog consumible (filtros por API/major, breaking vs compatible).
5. Enlaza guías de migración; no dejes solo un PDF suelto.
6. Si falta política de producto, marca gap y escala a Sabo — no inventes ventanas.

## Salida

```md
## Matriz de majors / estados
## UX switcher + URLs
## Banners y copy mínimo
## Changelog UX
## Gaps de política (Sabo) + owners
```

## Casos límite

- Solo un major → oculta switcher; muestra versión en header.
- Breaking sin notice → bloquea “listo”; exige notice + owner.
- Convivencia temporal de majors → documenta default y cómo elegir.

## Validación

- Cada major tiene referencia propia o separación clara.
- Deprecación visible antes del sunset.
- No se inventan fechas de soporte.

## Criterios de terminado

- UX de versiones implementable.
- Gaps de política explícitos hacia Sabo.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | v1 deprecated, v2 current | Switcher + banner + changelog |
| Ambiguo | “Versiona el portal” sin política | Preguntas + DELEGATION_REQUIRED Sabo |
| Límite | Sunset en 14 días sin guía | BLOCKED + migración obligatoria |

## Fuentes

- APIScout Developer Portal 2026 (versioned docs) — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- DigitalAPI lifecycle / deprecation — https://www.digitalapi.ai/blogs/enterprise-api-developer-portal-must-have-requirements-and-best-practices (2026-08-04).
- UK OBL Notification of a Change (patrón notices vía portal) — https://standards.openbanking.org.uk/operational-guidelines/change-and-communication-management/notification-of-a-change/v3-1-9/ (v3.1.9; consultado 2026-08-04).
