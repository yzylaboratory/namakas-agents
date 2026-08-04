---
name: gobernar-ciclo-vida-apis-abiertas
description: Define y aplica gobierno del ciclo de vida de APIs abiertas (ownership, versionado, deprecación, contratos, onboarding, métricas). Úsala cuando se pida política de APIs abiertas, revisión de catálogo expuesto, reglas de breaking change o paved road para TPP/partners.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar ciclo de vida de APIs abiertas

## Propósito

Establecer guardrails de producto y operación para APIs expuestas a terceros, de modo que el ecosistema sea seguro, predecible y operable.

## Entradas

- Catálogo o lista de APIs candidatas/expuestas.
- Estándares de diseño existentes (OpenAPI, security profile).
- Modelo de consumidores (TPP, partners, internos).
- Restricciones regulatorias de alto nivel relevantes.

## Procedimiento

1. Clasifica cada API: **interna**, **partner**, **open banking mandatoria**, **premium**.
2. Exige mínimo viable de gobierno por API pública:
   - Owner de producto + owner técnico.
   - Spec OpenAPI versionada.
   - Política de versionado y deprecación.
   - Perfil de seguridad y scopes/consentimientos asociados.
   - SLOs y alertas básicas.
3. Define reglas de cambio: qué es breaking; ventana mínima de aviso; convivencia de versiones.
4. Define onboarding: sandbox, credenciales, directorio/certificación si el ecosistema lo requiere, docs de portal.
5. Preferir enforcement en CI (lint Spectral/reglas de casa, contract tests) sobre revisión manual de cada PR.
6. Produce checklist de go-live y lista de excepciones documentadas (con caducidad).

## Salida

```md
## Política de gobierno APIs abiertas
## Inventario / gaps
| API | Clase | Owner | Spec | Seguridad | Versión | SLO | Gap |
## Reglas de versionado y deprecación
## Onboarding TPP/partner
## Guardrails automatizables
## Excepciones (con expiry)
## Riesgos
```

## Casos límite

- API “shadow” sin owner: bloquear exposición externa hasta asignar ownership.
- Breaking change urgente por seguridad: permitir fast-track con comunicación y plan de rollback.
- Multi-estándar (Berlin Group vs CDS vs OFB): gobernar por producto/jurisdicción, no un único estilo global ciego.

## Validación

- Toda API pública listada tiene owner y spec.
- Hay regla explícita de deprecación.
- Excepciones tienen fecha de revisión.

## Criterios de terminado

- Política o checklist aplicable por el squad y por Sabo/Robin/QA.
- Gaps priorizados.
- Ninguna recomendación depende de un board manual como único control.

## Fuentes

- API governance best practices (automatización, excepciones, lifecycle) — síntesis digitalML/Tyk contrastada 2026-08-04
- Open Banking API management lifecycle — síntesis industria 2026-08-04
- OpenAPI como contrato de producto — práctica contract-first 2026-08-04
