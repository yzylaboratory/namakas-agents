---
name: evaluar-alineacion-mach
description: Evalúa la alineación MACH (Microservices, API-first, Cloud-native, Headless) de un sistema o propuesta con evidencia por eje. Úsala cuando se pida auditar madurez composable o afirmar que algo es MACH-ready.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar alineación MACH

## Propósito

Producir una evaluación por eje MACH con evidencia, gaps y remedios — sin certificaciones inventadas.

## Entradas

- Sistema, producto o blueprint a evaluar.
- Inventario de servicios, APIs, deploy y canales de experiencia.
- Restricciones cloud/plataforma y ownership.
- Afirmaciones previas de “somos MACH/composable” (si existen).

## Procedimiento

1. Define el alcance evaluado (sistema completo vs dominio).
2. Evalúa **M — Microservices / modularidad deployable**: unidades independientes de deploy y ownership.
3. Evalúa **A — API-first**: capacidades expuestas por contrato; UI no es el único acceso.
4. Evalúa **C — Cloud-native**: elasticidad, managed runtime, CI/CD, resilience básica documentada.
5. Evalúa **H — Headless**: desacople experiencia ↔ backend; multi-canal posible.
6. Asigna por eje: `aligned` | `partial` | `missing` | `unknown` con evidencia.
7. Lista gaps priorizados y dueños (Law / Enel / Fujitora / plataforma).
8. No uses un solo eje fuerte para declarar alineación total.

## Salida

```md
## Alcance
## Scorecard MACH
| Eje | Estado | Evidencia | Gap | Dueño |
| M | | | | |
| A | | | | |
| C | | | | |
| H | | | | |
## Veredicto
## Remedios priorizados
## Riesgos / pendientes
```

## Casos límite

- Solo hay APIs sobre monolito → A partial; M missing; no declarar MACH.
- Headless frontend sobre backend acoplado por DB → H partial con riesgo.
- Falta inventario → `unknown` + pedir Noland/Law; no inventar.

## Validación

- Cuatro ejes evaluados por separado.
- Evidencia o `unknown` explícito; sin certificaciones inventadas.
- Veredicto coherente con el scorecard.

## Criterios de terminado

- Law puede priorizar remedios sin reinterpretar el alcance.
- Queda claro qué falta para afirmar composabilidad MACH.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Comercio con CMS headless + APIs + K8s | Scorecard mixto con evidencia |
| Ambiguo | “Somos MACH porque tenemos microservicios” | Exige A/C/H; no certifica |
| Límite | Monolito + API gateway | A partial; M missing; veredicto no-MACH |

## Fuentes

- MACH Alliance — https://machalliance.org/ (2026-08-04).
- MACH Architecture — https://macharchitecture.com/ (2026-08-04).
- Apidog composable/MACH guide — https://apidog.com/blog/composable-architecture/ (2026-08-04).
