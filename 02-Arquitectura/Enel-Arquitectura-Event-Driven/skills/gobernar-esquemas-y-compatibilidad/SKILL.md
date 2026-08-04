---
name: gobernar-esquemas-y-compatibilidad
description: Define política de schema registry, compatibilidad (p. ej. backward) y evolución/versionado de payloads de eventos. Úsala cuando haya que prevenir breaking changes o gobernar Avro/JSON Schema/Protobuf en EDA.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar esquemas y compatibilidad

## Propósito

Evitar roturas silenciosas entre productores y consumidores mediante contratos de schema, compatibilidad y plan de evolución.

## Entradas

- Catálogo de eventos y envelope (p. ej. `dataschema`).
- Formato de schema (JSON Schema, Avro, Protobuf) si está decidido.
- Tooling de registry disponible o previsto.
- Consumidores conocidos y su tolerancia a cambios.

## Procedimiento

1. Elige formato de schema por ecosistema; no mezcles formatos en el mismo canal sin puente.
2. Define política de compatibilidad por defecto (recomendación: **BACKWARD** o **BACKWARD_TRANSITIVE** en registries tipo Confluent/Apicurio).
3. Reglas de evolución segura: añadir campos opcionales con default; no renombrar/eliminar sin versión nueva.
4. Breaking change → nuevo `type`/subject versionado + dual-publish o consumidores paralelos + fecha de deprecación.
5. Exige que `dataschema` (CloudEvents) o referencia AsyncAPI apunte al schema canónico.
6. Define gate de CI: rechazar publish incompatible antes de llegar a producción.
7. Documenta ownership del schema (equipo productor) y proceso de review.
8. Lista excepciones temporales con dueño y expiry.

## Salida

```md
## Política de schemas
- Formato:
- Registry:
- Compatibilidad por defecto:
## Reglas de evolución
## Breaking change playbook
## Gates CI/CD
## Excepciones
```

## Casos límite

- Sin registry → bloquea “schema libre en prod” o exige repo versionado + review humano.
- Event sourcing con modelos largos → compatibilidad más estricta; documenta snapshots si aplica.
- Dos productores del mismo `type` → un solo owner de schema; el resto es violación.

## Validación

- Política de compatibilidad explícita.
- Playbook de breaking change con convivencia.
- Owner por schema/evento.

## Criterios de terminado

- Productores saben qué cambios son seguros.
- Hay gate o proceso de review definido.
- Pendientes de tooling listados.

## Fuentes

- CloudEvents — `dataschema` y versionado (Primer / spec) — https://github.com/cloudevents/spec/blob/ce@v1.0.2-branch/cloudevents/spec.md (2026-08-04).
- AsyncAPI — schemas en messages/components — https://www.asyncapi.com/docs/reference/specification/latest (2026-08-04).
- Prácticas Schema Registry compatibility (BACKWARD / BACKWARD_TRANSITIVE) — síntesis contrastada con tooling Confluent/Apicurio (2026-08-04).
