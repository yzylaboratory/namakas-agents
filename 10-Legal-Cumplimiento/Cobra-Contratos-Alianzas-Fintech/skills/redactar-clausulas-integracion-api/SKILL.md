---
name: redactar-clausulas-integracion-api
description: Redacta o completa el schedule contractual de integración API (licencia, auth, ambientes, fallos, límites). Úsala cuando la alianza fintech dependa de APIs y el MSA carezca de cláusulas operativas de integración.
metadata:
  author: yzylabs
  version: "1.0"
---

# Redactar cláusulas de integración API

## Propósito

Producir un API schedule / appendix contractual que gobierne licencia de uso, credenciales, ambientes, límites, responsabilidad por fallos y materiales de integración — alineado al producto externo sin reescribir OpenAPI técnico.

## Entradas

- MSA o framework agreement base.
- Descripción del producto API / catálogo (de Sabo u otro).
- Ambientes (sandbox/prod), auth prevista, rate limits conocidos.
- Quién notifica al cliente final ante fallos.

## Procedimiento

1. Define alcance de la licencia API (no exclusivo, no transferible, no sublicenciable salvo excepción).
2. Lista APIs/operations cubiertas y Purpose / Permitted Use.
3. Especifica Access Credentials: custodia, prohibición de redistribución, rotación, notificación de compromiso.
4. Separa sandbox vs producción y criterios de promoción.
5. Define responsabilidad por fallos (timeout, auth error, downtime, mapping incorrecto) y deber de notificación.
6. Incluye cumplimiento de API Materials / security requirements y derecho a suspender por abuso.
7. Remite OpenAPI/specs a Sabo/Robin como fuente técnica; el schedule no inventa campos.
8. Lista exclusiones (uso fraudulento, scraping fuera de cuota, reverse engineering no autorizado).

## Salida

```md
## API Schedule (borrador)
### Licencia y Purpose
### APIs cubiertas
### Credenciales y seguridad
### Ambientes
### Fallos y notificación
### Límites / suspension
### Referencias técnicas (OpenAPI/owners)
### Gaps
```

## Casos límite

- No hay OpenAPI → redacta schedule con placeholders y bloquea “partner-ready contractual”.
- Multi-party marketplace → define quién es licensee y quién es sub-processor/integrador.
- Credenciales embebidas en apps de cliente final → prohíbelo explícitamente.

## Validación

- Licencia, credenciales, ambientes y fallos están cubiertos.
- No se inventan endpoints; se referencian specs o gaps.
- Handoff a Sabo si falta producto/sandbox.

## Criterios de terminado

- Un negociador puede anexar el schedule al MSA.
- Responsabilidad por fallos de API está asignada.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Partnership AIS con OpenAPI existente | Schedule completo referenciando ops |
| Ambiguo | “Pon cláusulas de API” sin catálogo | Preguntas + schedule mínimo + gaps |
| Límite | Partner redistribuye tokens a terceros | Cláusula de prohibición + suspensión |

## Fuentes

- Ulster Bank Open Banking — API Framework Agreement — https://openapi.ulsterbank.co.uk/bankofapis/v1.0/dynamic-content/content/assets/solutions/variable-recurring-payment/api-framework-agreement.pdf (2026-08-04).
- Mayer Brown — Collaboration Agreements… (API/platform control themes) (2025-11-21) (2026-08-04).
