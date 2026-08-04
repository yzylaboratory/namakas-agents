---
name: disenar-composicion-solucion
description: Diseña cómo se ensamblan PBCs en una solución o journey (blueprint de composición, buy/build y puntos de integración). Úsala cuando haya que componer un producto a partir de capacidades, no solo listar servicios.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar composición de solución

## Propósito

Producir un blueprint que muestre cómo PBCs se ensamblan en un outcome de negocio, con puntos de integración, ownership y decisiones buy/build.

## Entradas

- Outcome / journey objetivo.
- Catálogo PBC (existente o borrador).
- Restricciones de Law, vendors candidatos, canales (web/móvil/partner).
- Preferencias de orquestación (sync/async).

## Procedimiento

1. Fija el outcome medible del journey (qué se compone y para quién).
2. Selecciona PBCs participantes e indica rol (source, enricher, sink, experience).
3. Dibuja secuencia de composición (pasos + contratos entre PBCs).
4. Marca puntos buy vs build con trade-offs (lock-in, time-to-value, control).
5. Identifica capa de experiencia (headless) vs capacidades de backend.
6. Señala dónde hace falta orquestación (y si debe escalarse a skill de orquestación o a Enel).
7. Lista no-objetivos: qué no se fusiona en un solo componente.
8. Entrega blueprint + riesgos de monolito oculto.

## Salida

```md
## Outcome / journey
## PBCs participantes
## Blueprint de composición (pasos)
## Contratos entre capacidades
## Buy vs build
## Experiencia / canales
## No-objetivos
## Riesgos (incl. monolito oculto)
## Decisiones para Law
```

## Casos límite

- Un solo PBC cubre todo → cuestiona si realmente es composable o monolito.
- Vendor “suite” que reintroduce silo → documenta pérdida de swap.
- Journey cruza compliance sensible → escala Fujitora vía Law.

## Validación

- Outcome y PBCs trazables.
- Buy/build con trade-offs, no preferencia estética.
- No-objetivos explícitos.

## Criterios de terminado

- Un implementador entiende el ensamblaje sin reinterpretar el journey.
- Law puede aprobar o pedir ADR sobre puntos conflictivos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Onboarding digital con KYC + accounts | Blueprint multi-PBC |
| Ambiguo | “Arquitectura composable para el banco” | Exige journey concreto |
| Límite | Suite vendor all-in-one | Blueprint + riesgo de silo / swap nulo |

## Fuentes

- Conscia — Composable architecture / orchestration — https://www.conscia.ai/post/what-is-a-composable-architecture (2026-08-04).
- Apidog — Composable architecture — https://apidog.com/blog/composable-architecture/ (2026-08-04).
- MACH Architecture — https://macharchitecture.com/ (2026-08-04).
