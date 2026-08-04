---
name: definir-estrategia-plataforma
description: Define la estrategia y hoja de ruta de plataforma interna (IDP, golden paths, self-service, outcomes DORA/DevEx). Úsala cuando se pida estrategia de DevOps/plataforma, roadmap de paved road o posicionamiento de plataforma como producto.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia de plataforma

## Propósito

Convertir fricción de desarrolladores y objetivos de entrega en una estrategia accionable de Internal Developer Platform / paved road, con secuencia de capacidades y métricas.

## Entradas

- Objetivo de negocio/entrega y equipos consumidores.
- Estado actual: CI/CD, GitOps, IaC, observabilidad, self-service, toil conocido.
- Restricciones de plazo, riesgo y capacidad del squad.
- Incidentes o hallazgos de discovery relevantes.

## Procedimiento

1. Fija el horizonte (p. ej. 2–4 trimestres) y el outcome principal (adopción de path, lead time, reducción de change failure, time to restore).
2. Clasifica iniciativas en: **habilitadores de plataforma**, **remediación de riesgo/toil**, **extensiones de path**.
3. Secuencia capacidades fundacionales antes de escala:
   - Journey crítico (p. ej. “nuevo servicio a producción”).
   - CI/CD template + quality gates.
   - Provisionamiento IaC / entornos.
   - GitOps / deploy declarativo.
   - Observabilidad baseline + rollback/restore.
   - Self-service y feedback loop (catálogo, docs, clear task feedback).
4. Define Now / Next / Later con dueño (Franky / Capone / Viola / Haredas / Paulie / otros).
5. Declara supuestos, no-objetivos y riesgos (ticket-ops, golden cage, big-bang).
6. Propón 3–6 KPIs (adopción de golden path, DORA keys relevantes, task success, CSAT/DevEx).

## Salida

```md
## Estrategia de plataforma
- Outcome:
- Consumidores:
- Habilitadores vs toil vs extensiones:
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap de journeys
| Journey | Valor | Dependencias | Riesgo |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Multi-cloud / multi-runtime: una capa común de journeys + deltas; no forzar un único stack sin escape hatch.
- Plataforma inmadura + presión AI coding: priorizar gates de test/deploy (DORA: AI amplifica disfunción si la plataforma es débil).
- Solo “comprar tool”: rechaza estrategia centrada en vendor sin journeys ni adopción.

## Validación

- Hay separación habilitadores vs toil.
- La secuencia no salta seguridad baseline / observabilidad / rollback.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones DORA/CNCF citan fuente/fecha.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones Seguridad/Arquitectura identificadas cuando correspondan.

## Fuentes

- DORA Platform engineering — https://dora.dev/capabilities/platform-engineering/ (2026-01-12; consultado 2026-08-04)
- CNCF Platforms White Paper — Platforms WG / TAG App Delivery (consultado 2026-08-04)
