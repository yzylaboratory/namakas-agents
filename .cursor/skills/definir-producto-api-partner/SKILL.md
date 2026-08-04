---
name: definir-producto-api-partner
description: Define un producto de API externa/partner (audiencia, valor, límites, tiers, SLAs y catálogo). Úsala cuando se pida diseñar o empaquetar APIs para terceros, no solo listar endpoints.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir producto de API partner

## Propósito

Convertir capacidades técnicas en un producto de API adoptabile: para quién es, qué valor entrega, qué queda fuera y bajo qué condiciones de acceso.

## Entradas

- Objetivo de negocio / ecosistema.
- Audiencias candidatas (TPP, fintech, corporativo, interno).
- Jurisdicción y estándar aplicable (si existe).
- Capacidades o specs existentes.
- Restricciones de seguridad, cuotas y compliance.

## Procedimiento

1. Nombra el producto y el problema que resuelve para el consumidor de la API.
2. Segmenta audiencias y jobs-to-be-done (no mezcles TPP regulado con partner B2B genérico sin etiquetar).
3. Declara alcance incluido / excluido del producto.
4. Define tiers de acceso (scopes, rate limits, sandbox vs prod) a nivel light.
5. Especifica SLAs observables (disponibilidad, latencia objetivo, soporte).
6. Lista dependencias (consent, identidad, datos maestros) y dueños.
7. Separa “API de compliance mínima” vs “API de ecosistema” si ambas existen.
8. Produce catálogo corto: operaciones, sensibilidad de datos, madurez (alpha/beta/ga).

## Salida

```md
## Producto
## Audiencias
## Valor / Jobs
## Incluido / Excluido
## Tiers y acceso
## SLAs
## Catálogo (ops)
## Dependencias y dueños
## Riesgos / pendientes
```

## Casos límite

- Solo hay mandato regulatorio → documenta compliance product y gaps de DX por separado.
- Varias audiencias incompatibles → no fuerces un solo tier; propone productos o planes distintos.
- Capacidad interna sin dueño de datos → no publiques; escala bloqueo.

## Validación

- Audiencia y valor explícitos.
- Límites del producto claros.
- Tiers/SLAs sin inventar pricing profundo (eso es Du-Feld).
- Estándar citado si el producto es Open Banking regional.

## Criterios de terminado

- Un partner entiende qué compra/integra sin leer el código del MS.
- Gaps de portal/monetización/seguridad tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | AIS account info para TPPs | Producto con audiencia TPP, scopes, SLA, catálogo |
| Ambiguo | “Abrir nuestras APIs” | Preguntas de audiencia + borrador de 2 productos candidatos |
| Límite | Solo PSD2 mínimo sin DX | Producto compliance + lista explícita de déficits de ecosistema |

## Fuentes

- Halkwinds Open Banking & API Economy Report 2026 — https://www.halkwinds.com/research/open-banking-api-economy-report-2026 (2026-08-04).
- Zuplo API-as-a-Product 2026 — https://zuplo.com/learning-center/api-as-a-product-guide-2026 (2026-08-04).
- Bamboodt API Management for Banks — https://www.bamboodt.com/building-a-secure-api-management-platform-for-banks-a-blueprint-for-open-banking-and-fintech-collaboration/ (2026-08-04).
