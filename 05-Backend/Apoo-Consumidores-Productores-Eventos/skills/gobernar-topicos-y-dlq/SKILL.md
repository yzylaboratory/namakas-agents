---
name: gobernar-topicos-y-dlq
description: Gobierna tópicos/canales, grupos de consumo, retención y dead-letter queues. Úsala cuando debas nombrar, particionar o definir políticas operativas de mensajería para pub/sub.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar tópicos y DLQ

## Propósito

Dar dueño, nombre, retención y política de fallos a cada canal de eventos para que productores y consumidores no improvisen infraestructura.

## Entradas

- Matriz de eventos pub/sub.
- Broker (Kafka, Service Bus, RabbitMQ, etc.).
- Requisitos de retención, throughput y compliance.
- AsyncAPI existente (canales).

## Procedimiento

1. Inventaría canales/tópicos actuales vs necesarios.
2. Aplica convención de nombres alineada a dominio (`{dominio}.{entidad}.events` o la del AsyncAPI).
3. Define particionado/sesiones solo si el orden por clave es requisito.
4. Asigna consumer groups y dueños por servicio.
5. Fija retención, compactación (si log compactado) y cuotas.
6. Define DLQ por cola/suscripción: criterios, alertas, runbook de replay.
7. Documenta ACLs mínimas (quién publica / quién consume).
8. Si falta canal en AsyncAPI → gap para Robin; no publiques “tópico sombra” sin registro.

## Salida

```md
## Inventario de canales
## Convención de nombres
## Grupos / dueños
## Retención / particionado
## Política DLQ + replay
## ACLs
## Gaps AsyncAPI
```

## Casos límite

- Un tópico multi-dominio → propone split; no mezcles bounded contexts sin justificación.
- Retención infinita con PII → conflicto de compliance; escala.
- DLQ compartida global → evita; preferir DLQ por suscripción.

## Validación

- Cada canal tiene dueño y al menos un productor/consumidor.
- DLQ y retención no son “TBD”.
- Nombres no rompen AsyncAPI existente sin deprecación.

## Criterios de terminado

- Ops puede crear el canal con la spec escrita.
- Replay desde DLQ tiene pasos concretos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 3 eventos billing → Kafka | 1–N tópicos + groups + DLQ |
| Ambiguo | “Usemos un topic events” | Riesgo multi-dominio + split propuesto |
| Límite | Retención 7 años + PII en payload | Minimización + retención justificada o bloqueo |

## Fuentes

- AsyncAPI Specification — https://www.asyncapi.com/docs/reference/specification/latest (2026-08-04).
- CloudEvents Spec 1.0.2 — https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md (2026-08-04).
