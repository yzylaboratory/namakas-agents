---
name: construir-onboarding-self-service-ui
description: Diseña los flujos UI de onboarding self-service del portal (registro, keys, scopes, rotación, test mode). Úsala cuando se pida alta de developers, API keys en UI o reducir TTFHW vía portal.
metadata:
  author: yzylabs
  version: "1.0"
---

# Construir onboarding self-service (UI)

## Propósito

Especificar pantallas y estados que lleven de landing/signup al primer call exitoso con mínima fricción y sin tickets manuales innecesarios.

## Entradas

- Política de auth (API key, OAuth2/OIDC, FAPI).
- Requisitos legales (T&Cs, KYC partner).
- Capacidad real de provisioning (gateway/IdP).
- Meta TTFHW (Sabo o Sanji).
- Restricciones de audiencia (público vs invite-only).

## Procedimiento

1. Mapea UI journey: land → signup/SSO → accept terms → credentials → first call CTA.
2. Exige test/sandbox mode por defecto; etiqueta entorno en header siempre visible.
3. Coloca la key/credencial de prueba en el primer pantallazo post-signup (no en settings profundos).
4. Define gestión de keys: crear, rotar, revocar, scopes visibles, aviso de expiración.
5. Si el provisioning es manual por regulación, documenta cola + SLA y automatiza lo permitido.
6. Incluye quickstart embebido con snippet que use la key del usuario cuando sea posible.
7. Lista eventos a instrumentar (signup_ok, key_issued, first_call_ok).

## Salida

```md
## Journey UI (pasos + estados)
## Self-service mínimo
## Pantallas / componentes
## Excepciones manuales + SLA
## Eventos TTFHW
## Gaps + owners
```

## Casos límite

- OAuth/FAPI complejo → simplifica “hello world” con API key de sandbox si la política lo permite; documenta path completo aparte.
- Invite-only partners → flujo de invitación + waitlist; no signup abierto falso.
- Sin gateway self-service → BLOCKED parcial + DELEGATION_REQUIRED a plataforma.

## Validación

- Camino al primer call sin SDK obligatorio.
- Credencial visible temprano.
- Entorno sandbox vs prod inequívoco.
- No se inventan tiers de monetización (Du-Feld/Sabo).

## Criterios de terminado

- Flujos UI listos para implementación o prototipo.
- Eventos de activación definidos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API key sandbox + portal | Flujo signup→key→CTA first call |
| Ambiguo | “Self-service” sin IdP | Lista de dependencias bloqueantes |
| Límite | Alta solo vía Legal | Híbrido + SLA + lo automatizable |

## Fuentes

- Skene Developer onboarding under 5 minutes — https://www.skene.ai/resources/blog/developer-onboarding-guide (2026-08-04).
- APIScout Developer Portal 2026 — https://apiscout.dev/guides/building-developer-portal-api-2026 (2026-08-04).
- DigitalAPI self-serve onboarding — https://www.digitalapi.ai/blogs/enterprise-api-developer-portal-must-have-requirements-and-best-practices (2026-08-04).
