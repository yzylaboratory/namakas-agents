---
name: producir-handoff-eda
description: Empaqueta HANDOFF_EDA (topología, catálogo, envelope, schemas, patrones y pendientes) para Law, Robin, Backend o DevOps. Úsala al cerrar un diseño EDA o al transferir a especificación/implementación.
metadata:
  author: yzylabs
  version: "1.0"
---

# Producir HANDOFF_EDA

## Propósito

Consolidar el diseño event-driven en un paquete accionable para el siguiente responsable, sin dejar decisiones implícitas.

## Entradas

- Topología, catálogo, envelope, política de schemas y patrones ya elaborados (o stubs parciales).
- Destinatario del handoff (Robin / Backend / DevOps / Law).
- Criterios de aceptación de la tarea padre.

## Procedimiento

1. Identifica el destinatario y lo que debe poder hacer sin reinterpretar el alcance.
2. Consolida artefactos: topología, catálogo, CloudEvents, schemas, patrones, operación (DLQ/lag).
3. Separa **decidido**, **supuesto** y **bloqueado**.
4. Lista archivos/rutas y versiones de fuentes citadas.
5. Define NEXT_HANDOFF (p. ej. Robin para AsyncAPI formal; Backend para outbox).
6. Emite `DELEGATION_REQUIRED` embebido si falta especialidad (seguridad, BIAN, etc.).
7. Completa el reporte a Law con EVIDENCE.
8. No declares COMPLETED si faltan productor, schema o garantía material sin TBD explícito aceptado por Law.

## Salida

Usa la plantilla en `references/contrato-handoff-eda.md` y el bloque:

```text
HANDOFF_EDA:
  recipient:
  topology_ref:
  catalog_ref:
  envelope:
  schema_policy:
  patterns:
  decided:
  assumptions:
  blocked:
  next_actions:
  risks:
```

## Casos límite

- Handoff parcial pedido explícitamente → `COMPLETED_WITH_LIMITATIONS` + blocked list.
- Destinatario Robin → incluye matriz canal/mensaje lista para AsyncAPI; no sustituyas su spec formal.
- Destinatario Fujitora → enfatiza PII, retención y superficies de ataque del payload.

## Validación

- Recipient y next_actions claros.
- Decided vs blocked separados.
- EVIDENCE con rutas o contenido adjunto.

## Criterios de terminado

- El receptor puede continuar sin preguntar “qué eventos existen”.
- Reporte a `law-director-arquitectura` listo.
- Riesgos y dependencias listados.

## Fuentes

- Contrato interno Nakamas — `02-Arquitectura/Enel-Arquitectura-Event-Driven/references/contrato-handoff-eda.md`.
- CloudEvents + AsyncAPI como piezas del handoff — https://cloudevents.io/ ; https://www.asyncapi.com/docs/reference/specification/latest (2026-08-04).
