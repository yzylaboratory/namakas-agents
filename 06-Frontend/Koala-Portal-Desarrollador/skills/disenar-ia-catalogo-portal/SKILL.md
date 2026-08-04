---
name: disenar-ia-catalogo-portal
description: Diseña la arquitectura de información y el catálogo de APIs del developer portal (navegación, audiencias gated, búsqueda). Úsala cuando se pida estructura del portal, home, catálogo o IA de docs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar IA y catálogo del portal

## Propósito

Definir la estructura navegable del developer portal para que un desarrollador encuentre APIs, quickstarts y soporte sin perderse, con separación clara de audiencias.

## Entradas

- Audiencias (público, partner, interno).
- Catálogo de productos/APIs y versiones.
- Assets disponibles (OpenAPI, SDKs, changelog, status).
- Restricciones SSO/RBAC y branding.
- Design system o stack Frontend (si existe).

## Procedimiento

1. Lista jobs-to-be-done del visitante: descubrir, evaluar, integrar, operar, obtener ayuda.
2. Propón mapa de IA: Home → Catálogo → Quickstart → Referencia → SDKs → Changelog → Soporte → Cuenta.
3. Define qué es público vs gated; documenta pantallas post-login.
4. Diseña catálogo: fichas (nombre, descripción, estado, versión, TTFHW estimado), filtros y búsqueda.
5. Especifica empty states y zero-results (sugerencias, contactar owner).
6. Entrega wireframe textual + checklist de navegación crítica al primer call.

## Salida

```md
## Audiencias y gating
## Mapa de IA
## Catálogo (ficha + filtros)
## Búsqueda / zero-results
## Camino crítico al primer call
## Gaps + owners
```

## Casos límite

- Multi-producto / multi-marca → namespaces claros; no un dump plano de endpoints.
- Solo APIs internas → SSO obligatorio; oculta registro público.
- Catálogo vacío → landing de “coming soon” + waitlist, no hub engañoso.

## Validación

- Existe camino ≤3 clics desde home a quickstart o referencia.
- Gating explícito por audiencia.
- Cada sección tiene propósito único.
- No se inventa política de producto API (Sabo).

## Criterios de terminado

- Mapa de IA accionable para implementación.
- Gaps con dueño (Koala / Sabo / seguridad).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 3 APIs partner + OpenAPI | IA + catálogo + gating partner |
| Ambiguo | “Haz un portal” sin APIs | IA mínima + lista de inputs bloqueantes |
| Límite | Mix público + confidencial | Árbol gated + requisitos SSO |

## Fuentes

- APIScout Developer Portal 2026 — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- DigitalAPI Enterprise Portal requirements — https://www.digitalapi.ai/blogs/enterprise-api-developer-portal-must-have-requirements-and-best-practices (2026-08-04).
- Mintlify Enterprise API Developer Portals — https://www.mintlify.com/library/api-developer-portals-for-enterprise (2026-08-04).
