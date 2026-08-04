---
name: especificar-sandbox-api
description: Especifica sandbox de API externa (paridad, datos sintéticos, unhappy paths, reset). Úsala cuando se pida entorno de prueba para partners, try-it-now o certificación previa a producción.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar sandbox de API

## Propósito

Definir un entorno de prueba seguro que permita a partners validar integración realista — incluyendo fallos — sin exponer producción ni datos personales reales.

## Entradas

- Producto de API y flujos críticos (auth/consent, AIS/PIS, etc.).
- OpenAPI externo.
- Restricciones de datos y seguridad.
- Capacidad de gateway/mocks existente.

## Procedimiento

1. Declara propósito del sandbox (exploración, certificación, demos, CI de partners).
2. Define paridad con producción: versiones de API, auth flows, códigos de error, límites.
3. Especifica datos sintéticos/enmascarados y política de refresh/reset.
4. Lista escenarios obligatorios: happy path + unhappy paths (consent denied, 401/403, 429, timeouts, idempotency conflicts).
5. Define isolation (tenant/partner) y prohibiciones (no write-through a prod).
6. Especifica try-it-now vs mock vs sandbox dedicado y cuándo usar cada uno.
7. Define criterios de promoción sandbox→prod (certificación, scopes, revisión).
8. Entrega matriz escenario → evidencia esperada → owner de implementación.

## Salida

```md
## Propósito sandbox
## Paridad con producción
## Datos y reset
## Escenarios (happy/unhappy)
## Isolation y prohibiciones
## Try-it / mock / dedicado
## Promoción a producción
## Matriz de evidencia
```

## Casos límite

- Solo mock estático → válido para exploración temprana; no basta para certificación de pagos/consent.
- Latencia sintética requerida → documenta perfiles de delay si el producto lo necesita.
- Datos de producción “anonimizados” deficientes → rechaza; exige sintéticos verificables.

## Validación

- Unhappy paths materiales presentes.
- Sin PII real en fixtures.
- Paridad de versión documentada.
- Criterios de promoción explícitos.

## Criterios de terminado

- Spec de sandbox implementable por platform/gateway.
- Riesgos de fuga a producción listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | AIS + OAuth partner API | Sandbox con consent success/fail + 429 + reset |
| Ambiguo | “Pon un sandbox” | Preguntas de paridad + borrador de escenarios mínimos |
| Límite | PIS con money movement | Sandbox sin fondos reales + simulación de estados de pago |

## Fuentes

- APIScout Developer Portal 2026 (sandbox ROI) — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- Bamboodt API Management for Banks — https://www.bamboodt.com/building-a-secure-api-management-platform-for-banks-a-blueprint-for-open-banking-and-fintech-collaboration/ (2026-08-04).
- TYPZA Open banking API buyers (sandbox unhappy paths) — https://www.typza.com/insights/open-banking-website-design-for-api-buyers (2026-08-04).
