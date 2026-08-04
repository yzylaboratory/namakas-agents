---
name: definir-modelo-canonico-integracion
description: Define o evoluciona el modelo canónico transport-agnostic y tablas de mapeo canal↔canónico↔core. Úsala cuando haya que estabilizar datos de integración antes de conectar protocolos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir modelo canónico de integración

## Propósito

Establecer una representación interna versionada, independiente del wire format, que desacople canales y core.

## Entradas

- Campos de negocio del flujo (pagos, cuentas, clientes, etc.).
- Payloads de canal y del core (si existen).
- Política de versionado del equipo.
- Requisitos de auditoría / campos obligatorios regulatorios.

## Procedimiento

1. Nombra el agregado canónico y su versión semántica.
2. Lista entidades y atributos con tipo, obligatoriedad y sensibilidad.
3. Exige transport-agnostic: no embeds de XML MT/MX crudo como modelo interno.
4. Construye tablas de mapeo canal → canónico y canónico → core.
5. Marca additive vs breaking; documenta política de consumidores.
6. Identifica campos que se pierden en traducción y riesgo operativo.
7. Define identificadores de correlación (negocio + técnico).
8. Entrega schema de referencia (JSON Schema u otro acordado) + changelog.

## Salida

```md
## Canónico (nombre + versión)
## Entidades / atributos
## Mapeo canal → canónico
## Mapeo canónico → core
## Política de versionado
## Pérdidas / truncation
## Correlación
## Schema / changelog
```

## Casos límite

- Core usa códigos propietarios opacos → documenta diccionario + dueño; no inventes semántica.
- Conflicto con OpenAPI de producto (Robin) → escala; no forks silenciosos.
- Solo hay ejemplo feliz → exige unhappy fields (rechazos, parciales).

## Validación

- Canónico versionado y sin dependencia de un solo wire format.
- Mapeos bidireccionales materiales cubiertos.
- Truncation explícita.

## Criterios de terminado

- Un implementador puede generar codecs sin preguntar “qué es la verdad”.
- Breaking changes tienen plan de coordinación.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | pacs.008 + API interna de transferencia | Canónico PaymentInstruction v1 + mapeos |
| Ambiguo | “Normalicemos los mensajes” | Preguntas de agregado + borrador de entidades |
| Límite | Canal con campo libre vs core estructurado | Truncation documentada + decisión requerida |

## Fuentes

- IoT Digital Twin PLM — canonical model pattern (2026) — https://iotdigitaltwinplm.com/iso-20022-migration-payments-architecture-2026/ (2026-08-04).
- ISO 20022 Catalogue — https://www.iso20022.org/catalogue-messages (2026-08-04).
- 6B Core Banking Integration — https://6b.finance/insight/core-banking-system-integration-using-iso-20022-rest-apis-and-legacy-message-queues/ (2026-08-04).
