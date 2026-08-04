---
name: gobernar-integracion-core
description: Define políticas y checklists de integración core (adapters, anti-corruption, modelo canónico, deprecación). Úsala cuando se gobierne coexistencia, interfaces core↔canales o migración de formatos de rail.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar integración Core

## Propósito

Establecer el paved road de integración para que el core no quede acoplado a rails/formatos de borde y la coexistencia tenga dueño, versión y plan de apagado.

## Entradas

- Inventario de interfaces / consumidores.
- Formatos actuales (files, MT/MX, APIs internas, eventos).
- Objetivos de migración o de nuevo canal.
- Restricciones de no-breaking y ventanas.

## Procedimiento

1. Clasifica cada frontera: inbound / outbound / sync / async / batch.
2. Exige **modelo canónico interno** versionado; codecs en el borde.
3. Define anti-corruption: qué se traduce, qué se rechaza, qué va a quarantine/DLQ.
4. Fija política de versionado y deprecación (ventana, comunicación, dual-run).
5. Asigna ownership por interfaz y métricas mínimas (error rate, lag, poison count).
6. Documenta criterios para apagar path legacy (parity, breaks, rollback).

## Salida

```md
## Política de integración Core
### Principios
### Catálogo de interfaces
| Interfaz | Tipo | Owner | Versión | Deprecación |
### Modelo canónico
### Dual-run / strangler
### Quarantine / DLQ
### Checklist de cambio
```

## Casos límite

- Consumidor no puede cambiar a tiempo: coexistencia temporal con fecha de caducidad y owner.
- Pérdida de campos ricos ISO 20022 en traducción: marcar riesgo compliance/fraud; no aceptar truncado silencioso.
- Event-driven + dual-write a ledger: exigir estrategia de consistencia explícita.

## Validación

- Ninguna regla acopla lógica profunda a un rail concreto sin justificación.
- Cada interfaz crítica tiene owner y métricas.
- Hay plan de deprecación o justificación de permanencia.

## Criterios de terminado

- Política usable por Tom/Crocus y revisable por Law/Franky.
- Checklist de cambio accionable.
- Riesgos de truncado/coexistencia explícitos.

## Fuentes

- Swift ISO 20022 / CBPR+ — https://www.swift.com/standards/iso-20022 (2026-08-04)
- Patrones canónicos + adapters de rail (síntesis contrastada, 2026-08-04)
- `references/mapa-gobierno-sistemas-core.md` — 2026-08-04
