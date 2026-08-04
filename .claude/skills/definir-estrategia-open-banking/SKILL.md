---
name: definir-estrategia-open-banking
description: Define la estrategia y hoja de ruta de Open Banking / Open Finance (cumplimiento vs premium, secuenciación de capacidades, outcomes). Úsala cuando se pida estrategia OB, roadmap de productos API o posicionamiento Open Finance por jurisdicción.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia Open Banking

## Propósito

Convertir objetivos de negocio y restricciones jurisdiccionales en una estrategia accionable de Open Banking / Open Finance, con secuencia de capacidades y métricas.

## Entradas

- Objetivo de negocio y mercado objetivo.
- Jurisdicción(es) y rol de la institución (ASPSP, TPP, ambos, data provider).
- Estado actual: APIs expuestas, consentimientos, partners, gaps conocidos.
- Restricciones de plazo, riesgo y capacidad del squad.

## Procedimiento

1. Fija el horizonte (p. ej. 2–4 trimestres) y el outcome principal (adopción, compliance deadline, revenue premium).
2. Clasifica iniciativas en: **mandatorio**, **premium Open Finance**, **plataforma/habilitadores**.
3. Secuencia capacidades fundacionales antes de escala:
   - Consentimiento y experiencia de autorización.
   - Seguridad de grado financiero (p. ej. perfiles FAPI donde aplique).
   - Calidad y ownership de datos a externalizar.
   - Operación API (SLA, observabilidad, soporte TPP).
   - Productos AIS/PIS y extensiones (seguros, inversiones, etc.) según mercado.
4. Define Now / Next / Later con dueño (Jinbe / Lucci / FIBO / Sabo / otros).
5. Declara supuestos, no-objetivos y riesgos regulatorios de alto nivel.
6. Propón 3–6 KPIs (consentimientos activos, API success rate, time-to-onboard, NPS partner, % breaking changes planificados).

## Salida

```md
## Estrategia OB / Open Finance
- Jurisdicción / rol:
- Outcome:
- Mandatorio vs premium:
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap de productos API
| Producto | Valor | Dependencias | Riesgo |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Multi-país: una estrategia por jurisdicción o capa común + deltas locales; no mezclar obligaciones.
- Regla en transición/litigio (p. ej. CFPB 1033): estrategia con escenarios, no certeza falsa.
- Solo cumplimiento: explícita el costo de oportunidad de no construir premium.

## Validación

- Hay separación cumplimiento vs valor.
- La secuencia no salta consentimiento/seguridad/datos.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones regulatorias citan fuente/fecha.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones legales/arquitectura identificadas cuando correspondan.

## Fuentes

- Berlin Group NextGenPSD2 / openFinance — https://www.berlin-group.org/psd2-access-to-bank-accounts (2026-08-04)
- OpenID FAPI WG — https://openid.net/wg/fapi/ (2026-08-04)
- EBA OBWG operating model readiness (síntesis) — ABE/EBA, consultado 2026-08-04
- Dunnixer / prácticas de secuenciación OB→Open Finance (secundaria, contrastada) — 2026-08-04
