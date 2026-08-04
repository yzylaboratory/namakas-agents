---
name: disenar-capa-integracion-core
description: Diseña la capa de integración hacia el core (adaptadores de canal, anti-corruption, orquestación). Úsala cuando haya que conectar canales o sistemas al core sin definir aún el canónico completo ni el corte.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar capa de integración core

## Propósito

Producir un diseño accionable de la capa entre canales/sistemas y el core: límites, adaptadores, flujos y ownership — evitando glue punto a punto.

## Entradas

- Objetivo de negocio del flujo.
- Inventario de sistemas origen/destino y protocolos.
- Restricciones del core (APIs, batch, throughput).
- Requisitos de auditoría y disponibilidad.
- Hallazgos de discovery (si existen).

## Procedimiento

1. Nombra el flujo y el efecto deseado en el core (sin diseñar el posting: eso es Kaku).
2. Lista productores y consumidores; etiqueta sync vs async.
3. Propón topología: adaptadores de borde → normalización → (opcional) orquestación stateful → entrega al core.
4. Define anti-corruption: qué no debe “filtrarse” al core desde el canal.
5. Asigna ownership por componente (Tom/Iceburg/Kaku/Crocus/ops).
6. Identifica puntos de fallo y necesidad de DLQ/circuit breaker (detalle en skill de resiliencia).
7. Declara fuera de alcance (ledger, UI, APIs partner).
8. Produce diagrama lógico (textual o mermaid) + lista de decisiones abiertas.

## Salida

```md
## Flujo
## Topología / adaptadores
## Sync vs async
## Anti-corruption
## Ownership
## Fallos previstos
## Fuera de alcance
## Decisiones abiertas
```

## Casos límite

- Solo hay un batch nocturno → diseña ventana y backpressure; no fuerces API real-time sin mandato.
- Múltiples canales al mismo efecto core → exige canónico compartido; no copies mappings N veces.
- Core sin API documentada → BLOCKED / DELEGATION_REQUIRED a Crocus/Noland/Iceburg.

## Validación

- Ningún acoplamiento canal↔core sin capa intermedia justificada.
- Ownership explícito Tom vs Kaku vs Crocus.
- Decisiones abiertas listadas (no escondidas).

## Criterios de terminado

- Iceburg puede priorizar implementación por componentes.
- Queda claro qué falta (canónico, contratos, corte).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Canal móvil → consulta saldo core vía API | Capa con adaptador REST + límites + ownership |
| Ambiguo | “Integrar el core con todo” | Preguntas de flujos prioritarios + borrador de 1–2 topologías |
| Límite | Core solo MQ legacy sin docs | BLOCKED + DELEGATION_REQUIRED a Crocus/Noland |

## Fuentes

- 6B Core Banking Integration — https://6b.finance/insight/core-banking-system-integration-using-iso-20022-rest-apis-and-legacy-message-queues/ (2026-08-04).
- IoT Digital Twin PLM ISO 20022 Architecture 2026 — https://iotdigitaltwinplm.com/iso-20022-migration-payments-architecture-2026/ (2026-08-04).
- BlazeTrends Core Banking APIs — https://blazetrends.com/how-core-banking-apis-connect-with-external-financial-systems/ (2026-08-04).
