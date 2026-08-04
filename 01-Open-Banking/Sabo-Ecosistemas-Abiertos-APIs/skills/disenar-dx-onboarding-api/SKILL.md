---
name: disenar-dx-onboarding-api
description: Diseña el journey de developer experience y onboarding (TTFHW, auth, docs, self-service, errores). Úsala cuando se pida mejorar adopción de partners, DX o Time to First Hello World.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar DX y onboarding de API

## Propósito

Definir un camino medible desde el landing del portal hasta el primer call exitoso y la promoción a producción, con fricciones explícitas y owners.

## Entradas

- Producto de API / audiencias.
- Mecanismo de auth (API key, OAuth2/OIDC, FAPI).
- Estado del portal y del sandbox.
- Docs y OpenAPI actuales.
- Métricas o quejas de partners (si hay).

## Procedimiento

1. Mapea el journey: discover → register → credentials → first call → certify/promote → operate.
2. Fija un objetivo de TTFHW (p. ej. menos de 30 min self-service) y los pasos bloqueantes actuales.
3. Exige guías de autenticación paso a paso (redirect, tokens, renew, consent si aplica).
4. Exige referencia de errores machine-readable y ejemplos de manejo.
5. Define self-service mínimo: alta, keys/scopes, rotación, visibilidad de cuotas.
6. Lista assets DX: quickstart, samples, changelog, status page, canal de soporte.
7. Separa contenido pre-login (pricing público/tiers visibles, capabilities) de lo gated.
8. Entrega checklist de DX con dueño por gap (Sabo / Koala / gateway / seguridad).

## Salida

```md
## Journey DX
## Meta TTFHW
## Bloqueos actuales
## Requisitos auth/docs/errores
## Self-service mínimo
## Checklist DX + owners
## Métricas propuestas
```

## Casos límite

- Onboarding manual obligatorio por regulación → documenta SLA de provisioning y automatiza lo permitido.
- Docs escritas a mano divergentes del OpenAPI → marca drift; prioriza generación desde spec.
- Solo happy-path samples → exige unhappy-path en quickstart.

## Validación

- TTFHW definido y medible.
- Auth y errores cubiertos.
- Cada gap tiene owner.
- No se sustituye UI de portal (Koala) por prosa interminable.

## Criterios de terminado

- Checklist accionable para portal/gateway/docs.
- Riesgos de abandono en onboarding listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Partner API con OAuth + portal básico | Journey + TTFHW + gaps self-service |
| Ambiguo | “Mejorar DX” sin métricas | Baseline propuesto + 5 fricciones hipotéticas a validar |
| Límite | Registro solo por email a legal | Flujo híbrido + escalamiento Legal + cola medible |

## Fuentes

- APIScout Developer Portal 2026 — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- TYPZA Open banking website design — https://www.typza.com/insights/open-banking-website-design-for-api-buyers (2026-08-04).
- Halkwinds Open Banking & API Economy Report 2026 — https://www.halkwinds.com/research/open-banking-api-economy-report-2026 (2026-08-04).
