---
name: definir-estrategia-backend
description: Define la estrategia y hoja de ruta de plataforma backend (microservicios, persistencia, eventos, resiliencia, outcomes). Úsala cuando se pida estrategia backend, roadmap de servicios o paved road departamental.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia Backend

## Propósito

Convertir objetivos de negocio y restricciones técnicas en una estrategia accionable de backend, con secuencia de capacidades y métricas.

## Entradas

- Objetivo de negocio y dominios/bounded contexts afectados.
- Estado actual: catálogo de servicios, stores, topics, SLOs, incidentes.
- Restricciones de plazo, riesgo, compliance y capacidad del squad.
- Dependencias externas (Law, Franky, Robin, Jinbe, Core).

## Procedimiento

1. Fija el horizonte (p. ej. 2–4 trimestres) y el outcome principal (fiabilidad, time-to-market, modernización, cumplimiento).
2. Clasifica iniciativas en: **plataforma/habilitadores**, **servicios de dominio**, **deuda operativa**.
3. Secuencia capacidades fundacionales antes de escala:
   - Ownership de servicio y de datos (database-per-service).
   - Contratos API/eventos versionados.
   - Patrones de consistencia (outbox, idempotencia, sagas donde aplique).
   - Observabilidad (logs/métricas/traces) y SLOs.
   - Operación (rollback, runbooks, capacity).
4. Define Now / Next / Later con dueño (Katakuri / X-Drake / Pudding / Apoo / otros).
5. Declara supuestos, no-objetivos y riesgos de blast radius.
6. Propón 3–6 KPIs (error budget, p99, lag de consumidores, % servicios con owner+spec, MTTR).

## Salida

```md
## Estrategia Backend
- Outcome:
- Plataforma vs dominio vs deuda:
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap de servicios / iniciativas
| Ítem | Valor | Dependencias | Riesgo |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Células en stub: estrategia y gates sí; ejecución marcada BLOCKED / forja requerida.
- Modernización big-bang: partir en bounded contexts; no “rewrite total” sin dueños.
- Solo presión de features: explicitar costo de saltar plataforma (incidentes, acoplamiento).

## Validación

- Hay separación plataforma vs features.
- La secuencia no salta ownership/contratos/observabilidad.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones de patrón citan fuente/fecha.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones Law/Franky/seguridad identificadas cuando correspondan.

## Fuentes

- Azure Architecture Center — Microservices — https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices (2026-08-04)
- Microsoft — Data considerations for microservices — https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations (2026-08-04)
- 12-Factor App — https://12factor.net/ (2026-08-04)
