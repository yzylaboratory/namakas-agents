---
name: definir-estrategia-sistemas-core
description: Define la estrategia y hoja de ruta de Sistemas Core (coexistencia vs modernización, secuenciación de capacidades, outcomes). Úsala cuando se pida estrategia de core bancario, roadmap de modernización o posicionamiento del system of record.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia Sistemas Core

## Propósito

Convertir objetivos de negocio y restricciones operativas en una estrategia accionable de Sistemas Core, con secuencia de capacidades y métricas.

## Entradas

- Objetivo de negocio y productos/flujos afectados.
- Mapa actual del core (ledger, cuentas, batch, interfaces).
- Deuda de coexistencia y ventanas de cambio conocidas.
- Restricciones de riesgo, plazo y capacidad del squad.

## Procedimiento

1. Fija el horizonte (p. ej. 2–4 trimestres) y el outcome principal (reducir breaks, habilitar rail, apagar path legacy, bajar latencia).
2. Clasifica iniciativas en: **coexistencia controlada**, **modernización estructural**, **habilitadores de canal/plataforma**.
3. Secuencia capacidades fundacionales antes de escala:
   - Integridad de saldos y reconciliación.
   - Idempotencia y semántica de reintentos.
   - Contratos de interfaz / modelo canónico.
   - Observabilidad y rollback.
   - Migración de flujos / strangler por dominio.
4. Define Now / Next / Later con dueño (Iceburg / Crocus / Tom / Kaku / otros).
5. Declara supuestos, no-objetivos y riesgos de cutover.
6. Propón 3–6 KPIs (break rate, dual-run parity %, STP, p99, time-to-rollback, % interfaces con owner).

## Salida

```md
## Estrategia Sistemas Core
- Capa / productos:
- Outcome:
- Coexistencia vs modernización:
## Secuencia de capacidades
| Capacidad | Now/Next/Later | Dueño | Gate de salida |
## Roadmap de iniciativas
| Iniciativa | Valor | Dependencias | Riesgo cutover |
## KPIs
## Supuestos y no-objetivos
## Riesgos y escalamientos
```

## Casos límite

- Multi-core / multi-libro: una estrategia por system of record o capa común + deltas; no mezclar ledgers.
- Mandato de rail en curso (ISO 20022): estrategia con coexistencia temporal acotada, no “traducción eterna”.
- Solo apagar fuego operacional: explícita el costo de no modernizar estructura.

## Validación

- Hay separación coexistencia vs modernización estructural.
- La secuencia no salta integridad/idempotencia/contratos.
- Cada ítem Now tiene dueño y gate.
- Afirmaciones de estándar/rail citan fuente/fecha.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Roadmap y KPIs explícitos.
- Escalaciones Arquitectura/Seguridad/Plataforma identificadas cuando correspondan.

## Fuentes

- Swift ISO 20022 hub — https://www.swift.com/standards/iso-20022 (2026-08-04)
- ISO 20022 — https://www.iso20022.org/ (2026-08-04)
- `references/mapa-gobierno-sistemas-core.md` — 2026-08-04
