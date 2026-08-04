---
name: registrar-decisiones-arquitectura
description: Redacta y valida Architecture Decision Records (ADR) con contexto, opciones, decisión y consecuencias. Úsala cuando haya una decisión estructural material, se pida ADR/RFC de decisión, o deba documentarse una excepción/dispensa arquitectónica.
metadata:
  author: yzylabs
  version: "1.0"
---

# Registrar decisiones de arquitectura

## Propósito

Capturar decisiones arquitectónicas materiales de forma ligera, auditable y accionable (estilo Nygard/MADR), enlazando stakeholders/concerns cuando aporte trazabilidad.

## Entradas

- Problema o fuerza que motiva la decisión.
- Opciones consideradas (mínimo dos cuando existan).
- Contexto técnico y de negocio.
- Impacto esperado y riesgos.
- Relación con principios/estándares vigentes.

## Procedimiento

1. Confirma que la decisión es material (cambia boundaries, stack, patrón de integración, modelo de consistencia, trust boundary o paved road).
2. Escribe el ADR:
   - Título corto y status (`proposed` | `accepted` | `superseded` | `deprecated`).
   - Contexto.
   - Opciones (con pros/contras).
   - Decisión.
   - Consecuencias (positivas, negativas, follow-ups).
3. Si aplica, añade enlace 42010-light: stakeholders/concerns/views afectados (sin fingir AD completo).
4. Define dueño, fecha y criterios de revisión/supersesión.
5. Indica si Brook debe capturar la decisión en memoria/vault.
6. Si es dispensa temporal, fija vencimiento y plan de retorno (coordina con `gobernar-arquitectura-empresa`).

## Salida

```md
# ADR-XXX: <título>
- Status:
- Date:
- Deciders:
## Context
## Options
## Decision
## Consequences
## Follow-ups
## Links (principios, PRs, diagrams)
```

## Casos límite

- Decisión ya tomada en código sin ADR: redacta ADR retrospectivo y marca deuda de gobernanza.
- Bicicleta de opciones infinitas: limita a 2–4 opciones reales; decide con evidencia.
- Conflicto entre ADRs: marca supersesión explícita; no dejes dos accepted contradictorios.

## Validación

- Hay al menos contexto, decisión y consecuencias.
- Status y dueño claros.
- Consecuencias negativas no omitidas.
- No sustituye un tratado Robin ni un threat model Fujitora.

## Criterios de terminado

- ADR listo para repo/memoria.
- Follow-ups con dueño.
- Señal a Brook si la decisión es material para el vault.

## Fuentes

- Michael Nygard — Documenting Architecture Decisions (ADR) — prácticas canónicas ADR (2026-08-04)
- MADR — Markdown Architectural Decision Records — https://adr.github.io/madr/ (2026-08-04)
- ISO/IEC/IEEE 42010 y decisiones en AD — http://www.iso-architecture.org/42010/ / https://adr.zone/iso-42010 (2026-08-04)
