---
name: especificar-openapi
description: Elabora o actualiza un contrato OpenAPI 3.1 contract-first (paths, schemas, errores, seguridad, versionado). Úsala cuando se pida especificar APIs HTTP de un microservicio o alinear el tratado con un contrato REST.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar contrato OpenAPI

## Propósito

Definir el contrato HTTP como fuente de verdad machine-readable alineada al tratado y al mapeo de dominio recibido.

## Entradas

- Tratado o alcance del MS.
- Recursos y operaciones requeridas.
- Modelos de datos acordados.
- Esquema de errores y seguridad del ecosistema.
- Mapeo BIAN / operaciones de servicio cuando existan.
- Spec existente a evolucionar (si hay).

## Procedimiento

1. Fija `openapi: 3.1.x` salvo restricción documentada del repo.
2. Define `info`, servidores y tags estables.
3. Modela recursos con paths orientados a nombres (no verbos en segmentos).
4. Asigna `operationId` único y estable a cada operación.
5. Declara `components.schemas`, parameters, responses y securitySchemes reutilizables.
6. Documenta 2xx y errores relevantes; prefiere Problem Details (`application/problem+json`) si el ecosistema lo permite.
7. Documenta auth/scopes por operación.
8. Añade ejemplos realistas sintéticos (sin secretos ni PII real).
9. Si hay mapeo BIAN, anota trazabilidad (extensiones `x-bian-*` o sección en el tratado — no inventes dominios).
10. Revisa breaking changes si actualizas una spec existente.

## Salida

- Archivo OpenAPI YAML (preferido) o JSON.
- Resumen de operaciones y breaking changes.
- Lista de pendientes (paginación, idempotencia, etc.).

## Casos límite

- Spec legacy 2.0 / 3.0 → plan de migración explícito; no mezcles versiones en un mismo documento.
- Solo eventos, sin HTTP → no fuerces OpenAPI; usa `especificar-asyncapi`.
- Operación sin modelo de error → no marques completo hasta definir errores materiales.

## Validación

- `openapi` version explícita.
- Cada operación tiene `operationId`, responses y seguridad aplicable.
- Schemas en `components` con `$ref` (evitar inline masivo).
- Sin secretos en ejemplos.
- Alineación con el tratado en recursos y semántica.

## Criterios de terminado

- Spec parseable y revisable en PR.
- Coherente con tratado/mapeo disponible.
- Breaking changes señalados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Tratado con 3 recursos CRUD | OpenAPI 3.1 con components y errores |
| Ambiguo | “API de clientes” sin campos | Spec mínima + pendientes de schema; no inventar PII |
| Límite | Cambio que elimina un campo published | Diff de breaking change + opción de versionado |

## Fuentes

- OpenAPI Specification 3.1.0 — https://spec.openapis.org/oas/v3.1.0 (2026-08-04).
- RFC 7807 Problem Details — https://www.rfc-editor.org/rfc/rfc7807 (2026-08-04).
