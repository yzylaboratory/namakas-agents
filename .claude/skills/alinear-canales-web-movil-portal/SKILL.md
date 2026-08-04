---
name: alinear-canales-web-movil-portal
description: Alinea journeys y estándares entre web, móvil y portal del desarrollador (paridad, deltas, handoffs a Nami/Sabo). Úsala cuando haya que unificar experiencia multi-canal, documentar divergencias o coordinar portal con producto cliente/API.
metadata:
  author: yzylabs
  version: "1.0"
---

# Alinear canales web, móvil y portal

## Propósito

Evitar tres “productos” inconsistentes: asegurar paridad razonable de journeys críticos o deltas explícitos entre Cavendish, Reiju y Koala.

## Entradas

- Journeys o superficies a alinear.
- Estado actual por canal (screenshots, specs, deuda).
- Dependencias de design system (Nami) y de APIs (Robin/Sabo).
- Restricciones de plataforma (capacidades nativas vs web).

## Procedimiento

1. Lista journeys críticos y marca canal primario vs secundarios.
2. Para cada journey: define **paridad requerida** vs **delta permitido** (y por qué).
3. Compara patrones: navegación, formularios, errores, autenticación, a11y, performance.
4. Produce matriz de gaps con dueño (Cavendish / Reiju / Koala / Nami).
5. Si el portal participa: separa UX de developer (Koala) de promesas de API (Sabo); alinea mensajes y estados (sandbox, keys, errores).
6. Prioriza convergencia (shared components/tokens) vs aceptación temporal de delta.
7. Emite plan Now/Next y criterios de “alineado”.

## Salida

```md
## Alcance multi-canal
## Matriz de paridad
| Journey | Web | Móvil | Portal | Paridad/Delta | Dueño |
## Gaps y riesgos
## Plan de convergencia
## Handoffs (Nami / Sabo / Backend)
## Criterios de alineado
```

## Casos límite

- Capacidad nativa sin equivalente web: documenta delta; no fuerces UX absurda.
- Portal white-label vs app marca: reglas de marca distintas; alinea información, no necesariamente skin.
- Un canal legacy: plan de migración; no congeles los otros al peor ritmo sin decisión explícita.

## Validación

- Cada gap tiene dueño.
- Deltas tienen justificación y fecha de revisión.
- No se asigna a Koala trabajo de producto API de Sabo.

## Criterios de terminado

- Matriz usable por el squad y por Luffy.
- Plan de convergencia o aceptación de deltas claro.

## Fuentes

- W3C WCAG2ICT (aplicabilidad a software no-web) — https://www.w3.org/TR/wcag2ict-22/ (2026-08-04)
- Catálogo Nakamas Frontend + relación Sabo/Koala — repo nakamas-agents (2026-08-04)
