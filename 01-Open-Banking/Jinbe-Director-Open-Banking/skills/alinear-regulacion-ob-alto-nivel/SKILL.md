---
name: alinear-regulacion-ob-alto-nivel
description: Mapea una iniciativa Open Banking / Open Finance a requisitos regulatorios de alto nivel por jurisdicción (PSD2/NextGenPSD2, Open Finance BR, CDR, CFPB 1033, FAPI) sin dictamen legal. Úsala cuando haya que alinear producto/roadmap a un marco regulatorio o comparar obligaciones entre mercados.
metadata:
  author: yzylabs
  version: "1.0"
---

# Alinear regulación OB (alto nivel)

## Propósito

Producir un mapa de alineación regulatoria orientado a producto y gobierno: qué obliga el marco, qué implica para APIs/consentimiento/seguridad, y qué debe escalarse a Legal.

## Entradas

- Jurisdicción(es) y rol de la entidad.
- Productos/journeys en alcance (AIS, PIS, data sharing, premium).
- Fecha de análisis (el marco puede estar en transición).
- Restricciones de negocio conocidas.

## Procedimiento

1. Identifica el marco primario y artefactos técnicos asociados:
   - UE: PSD2 / EBA RTS; Berlin Group NextGenPSD2; evolución openFinance / PSD3 (seguimiento).
   - Brasil: Open Finance BCB (manuales de APIs y de escopo; gobernanza del ecosistema).
   - Australia: CDR + Consumer Data Standards (+ perfil de seguridad FAPI según CDS).
   - EE.UU.: Section 1033 / CFPB Personal Financial Data Rights (vigencia/litigio/reconsideración); FDX como estándar de industria.
2. Para cada obligación de alto nivel, traduce a impacto de producto:
   - Consentimiento y límites de uso/retención.
   - Autenticación fuerte / SCA cuando aplique.
   - Interfaces estandarizadas vs principios-based.
   - Acreditación/participantes/directorios.
   - Prohibiciones o transiciones de screen scraping.
   - Gratuidad / fees de acceso a datos (si el marco lo trata).
3. Separa: **requisito de producto**, **hipótesis**, **debe escalar a Legal**.
4. Añade perfil de seguridad esperado (FAPI 1/2) cuando el ecosistema lo adopte; recuerda: FAPI no define el modelo de datos.
5. Lista gaps vs estado actual y recomienda secuencia de cierre (sin inventar fechas legales).

## Salida

```md
## Contexto
- Jurisdicción / rol / fecha de análisis:
## Marco aplicable
| Marco | Artefacto técnico | Estado (vigente/transición) | Fuente |
## Requisitos → impacto producto
| Requisito | Impacto API/consent/security | Owner sugerido | Escala a Legal? |
## Gaps
## No cubierto / incertidumbre
## Recomendación de alineación
```

## Casos límite

- Regla litigada o en reconsideración: presentar escenarios A/B; no afirmar compliance date como hecho.
- Multi-jurisdicción: tabla por país; capa común solo donde sea realmente común.
- Pedido de “opinión legal”: rechaza y escala a Sengoku/Tsuru con el mapa preparado.

## Validación

- Cada afirmación material tiene fuente o está marcada como hipótesis.
- Hay al menos una columna de escalamiento legal cuando corresponda.
- No se confunde FAPI (seguridad) con estándar de datos del ecosistema.

## Criterios de terminado

- Mapa usable por producto/squad.
- Gaps priorizables.
- Límites del análisis (no es memo legal) explícitos.

## Fuentes

- Berlin Group NextGenPSD2 / openFinance — https://www.berlin-group.org/psd2-access-to-bank-accounts (2026-08-04)
- OpenID FAPI — https://openid.net/wg/fapi/ (FAPI 2.0 Final 2025-02-19; consultado 2026-08-04)
- CFPB Personal Financial Data Rights — https://www.consumerfinance.gov/personal-financial-data-rights/ (2026-08-04)
- CRS / Congreso — IF13117 Access to Consumer Financial Data (contexto 1033, litigio) — 2026-08-04
- Open Finance Brasil — Manual de APIs v7.0 vía IN BCB 615/2025 — 2026-08-04
- Consumer Data Standards Australia — https://consumerdatastandardsaustralia.github.io/standards/ (2026-08-04)
- LatAm Open Finance panorama (Ozone/Mastercard, secundaria) — 2026-08-04
