---
name: definir-estrategia-arquitectura
description: Define la estrategia y hoja de ruta de arquitectura (principios, target-state, paved roads, outcomes). Úsala cuando se pida estrategia de arquitectura, principios empresariales, target-state o posicionamiento del departamento Arquitectura.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia de arquitectura

## Propósito

Convertir objetivos de negocio y restricciones técnicas en una estrategia accionable de arquitectura, con principios, secuencia de capacidades y métricas.

## Entradas

- Objetivo de negocio y sistemas críticos.
- Restricciones de plazo, riesgo, presupuesto y deuda conocida.
- Estado as-is (inventario, diagramas, ADRs previos).
- Capacidad del squad Enel / Fujitora / Wapol.

## Procedimiento

1. Fija el horizonte (p. ej. 2–4 trimestres) y el outcome principal (reducir acoplamiento, habilitar eventos, paved road, compliance de diseño).
2. Clasifica iniciativas en: **gobierno/estándares**, **modernización**, **deuda estructural**, **habilitadores de producto**.
3. Propón 5–9 principios accionables (no eslóganes): cada principio con implicación verificable.
4. Secuencia capacidades fundacionales antes de escala:
   - Límites de contexto / composición.
   - Integración y eventos.
   - Trust boundaries y controles.
   - Observabilidad y operabilidad.
   - Paved roads hacia implementación.
5. Define Now / Next / Later con dueño (Law / Enel / Fujitora / Wapol / otros).
6. Declara supuestos, no-objetivos y riesgos.
7. Propón 3–6 KPIs (tiempo de decisión ADR, % excepciones abiertas, lead time de revisión, incidentes por acoplamiento conocido).

## Salida

```md
## Estrategia de arquitectura
- Outcome:
- Principios (con implicación):
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap
| Iniciativa | Valor | Dependencias | Riesgo |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Multi-landscape (legado + cloud): capa común de principios + deltas locales; no unificar a la fuerza.
- Solo “dibujar C4”: rechaza como estrategia; exige principios, target-state y dueños.
- Presión de producto sin gobierno: estrategia con MVP acotado + deuda explícita, no bloqueo teatral.

## Validación

- Hay principios con implicación verificable.
- La secuencia no salta trust boundaries ni límites de contexto.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones de marco (TOGAF/42010) citan fuente/fecha.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones identificadas cuando correspondan.

## Fuentes

- The Open Group — TOGAF® Standard, 10th Edition (Capability and Governance) — https://publications.opengroup.org/c220 (2026-08-04)
- ISO/IEC/IEEE 42010:2022 — Architecture description — https://standards.ieee.org/ieee/42010/6846/ (2026-08-04)
