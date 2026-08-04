---
name: implementar-docs-as-code-portal
description: Define el pipeline docs-as-code OpenAPI→referencia interactiva del portal y el control anti-drift. Úsala cuando se pida documentación de API en portal, sync CI o referencia Swagger/Redoc.
metadata:
  author: yzylabs
  version: "1.0"
---

# Implementar docs-as-code en el portal

## Propósito

Asegurar que la referencia del portal se genera desde OpenAPI publicado y se publica vía CI, evitando drift entre contrato, gateway y UI.

## Entradas

- OpenAPI 3.1.x (o versión documentada) externo publicado.
- Herramienta de portal/docs (build vs buy).
- Pipeline CI existente.
- Reglas Spectral/lint (si hay).
- Dueño del contrato (Sabo/Robin).

## Procedimiento

1. Declara OpenAPI como única fuente de verdad de la referencia API.
2. Define pipeline: validate/lint → generate reference → publish portal → smoke links.
3. Especifica dónde vive la spec (repo, artifact registry) y el job de publish.
4. Exige ejemplos, auth schemes y error schemas presentes en la spec o en overlays controlados.
5. Prohíbe edición manual de la referencia en CMS como master.
6. Define checklist anti-drift (versión portal == versión publicada; changelog enlazado).
7. Coordina con Sabo si falta productización de la spec; no inventes campos del contrato.

## Salida

```md
## Fuente de verdad
## Pipeline CI (etapas)
## Overlays / ejemplos permitidos
## Checklist anti-drift
## Gaps + owners
```

## Casos límite

- Spec incompleta (sin auth/errores) → bloquea “referencia lista”; escala a Sabo/Robin.
- Multi-major → publicar referencias por major, no mezclar.
- Buy (ReadMe/Stoplight/Mintlify/…) → documenta sync API/CI, no solo upload manual.

## Validación

- Pipeline tiene lint + publish automatizable.
- No queda CMS como master de paths/schemas.
- Versión de spec visible en UI.

## Criterios de terminado

- Spec de pipeline accionable.
- Criterio verificable de “sin drift material”.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OpenAPI 3.1 + CI GitHub | Pipeline + anti-drift |
| Ambiguo | “Pon Swagger” sin repo | Requisitos mínimos + inputs faltantes |
| Límite | Spec v1 y v2 conviviendo | Dos referencias + switcher |

## Fuentes

- OpenAPI Specification 3.1.x — https://spec.openapis.org/oas/v3.1 (consultado 2026-08-04).
- APIScout Developer Portal 2026 — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- Mintlify Enterprise portals — https://www.mintlify.com/library/api-developer-portals-for-enterprise (2026-08-04).
