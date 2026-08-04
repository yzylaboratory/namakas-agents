---
name: productizar-openapi-exposicion-externa
description: Productiza OpenAPI 3.1 para exposición externa (portal, lint, anti-drift, servers, seguridad publicada). Úsala cuando el contrato externo deba alimentar portal/gateway sin sustituir el tratado MS de Robin.
metadata:
  author: yzylabs
  version: "1.0"
---

# Productizar OpenAPI para exposición externa

## Propósito

Convertir el contrato OpenAPI en artefacto de producto externo: estable, lintable, sincronizable al portal y separado del detalle interno de microservicios.

## Entradas

- OpenAPI existente o borrador.
- Definición de producto de API / audiencias.
- Políticas de auth y errores del ecosistema.
- Pipeline CI / portal / gateway (si hay).
- Tratado interno Robin (si existe) para proyección controlada.

## Procedimiento

1. Fija `openapi: 3.1.x` salvo restricción documentada.
2. Completa `info` (title, version de producto, contact, license/terms).
3. Declara `servers` por ambiente (sandbox, prod) sin secretos.
4. Publica solo operaciones/schemas del producto externo; oculta internos.
5. Asegura `operationId` estables, tags de producto, securitySchemes y errores estructurados.
6. Añade ejemplos sintéticos y descripciones orientadas a partners.
7. Define pipeline anti-drift: lint (p. ej. Spectral), validación en CI, sync portal on merge.
8. Si hay tratado Robin, documenta proyección (qué se publica vs qué queda interno) sin inventar BIAN.
9. Versiona el documento OpenAPI alineado al major público del producto.

## Salida

- OpenAPI externo (YAML preferido).
- Diff vs interno (si aplica).
- Requisitos de CI/portal sync.
- Lista de campos/ops no publicables y razón.

## Casos límite

- Spec 2.0/3.0 legacy → plan de migración a 3.1; no mezclar versiones en un documento.
- Drift portal vs gateway → prioriza single source OpenAPI; marca incidente de DX.
- Robin y producto divergen → gap explícito; no “arreglar” inventando semántica de dominio.

## Validación

- Parseable OpenAPI 3.1.x.
- Servers/auth/errores presentes.
- Sin secretos ni PII real.
- Pipeline anti-drift descrito o enlazado.
- Alcance externo acotado.

## Criterios de terminado

- Spec lista para portal/gateway.
- Separación interno/externo documentada.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OpenAPI interno con 20 ops | Spec externa filtrada + CI lint + servers sandbox/prod |
| Ambiguo | “Publica el swagger” | Preguntas de audiencia + borrador de filtro de ops |
| Límite | Portal muestra campos deprecados ausentes en gateway | Informe de drift + plan de resync |

## Fuentes

- OpenAPI Specification 3.1.x — https://spec.openapis.org/oas/v3.1 (2026-08-04).
- Zuplo API-as-a-Product 2026 — https://zuplo.com/learning-center/api-as-a-product-guide-2026 (2026-08-04).
- APIScout Developer Portal 2026 — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- Berlin Group OpenAPI YAML — https://gitlab.com/the-berlin-group/nextgenpsd2 (2026-08-04).
- STET PSD2 Framework v1.6.3.1 — https://www.stet.eu/assets/files/site/PSD2/1-6-3/api-dsp2-stet-v1.6.3.1-part-1-framework.pdf (2026-08-04).
