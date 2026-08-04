# Contrato HANDOFF_EDA

Plantilla de handoff del especialista Event-Driven (Enel) hacia Law, Robin, Backend, DevOps o QA.

## Campos obligatorios

```yaml
HANDOFF_EDA:
  version: "1.0"
  producer_agent: enel-arquitectura-event-driven
  recipient: # law-director-arquitectura | robin-tratadista | backend | devops | qa
  mission_id:
  task_id:
  summary: |
    Una frase del outcome EDA.
  topology:
    bounded_contexts: []
    producers: []
    consumers: []
    channels: []
  catalog:
    events: []
    # cada event: name, type, producer, consumers, channel, key, idempotency, schema_ref
  envelope:
    standard: CloudEvents
    specversion: "1.0"
    required_attributes: [id, source, type]
    recommended_attributes: [time, dataschema, datacontenttype]
    extensions: []
  schema_policy:
    format: # json-schema | avro | protobuf | TBD
    compatibility: # BACKWARD | BACKWARD_TRANSITIVE | NONE | TBD
    registry: # URI o TBD
  patterns:
    chosen: []
    delivery_guarantee: # at-most-once | at-least-once | exactly-once-semantic
    dlq_retries: TBD
  decided: []
  assumptions: []
  blocked: []
  next_actions: []
  risks: []
  evidence_paths: []
```

## Reglas

1. No omitas `blocked` si hay huecos materiales.
2. No presentes comandos como eventos de dominio sin etiquetarlos.
3. No inventes Service Domains ni clases FIBO en este handoff.
4. Robin consume este handoff para AsyncAPI formal; Enel no lo sustituye.
5. Law valida alineación con arquitectura global antes de cerrar el depto.

## Criterio de aceptación del handoff

El receptor puede:

- Nombrar los eventos del alcance.
- Saber quién publica y quién consume (o ver TBD explícito).
- Conocer envelope y política de schema.
- Conocer el siguiente paso concreto.
