---
name: redactar-adr
description: Redacta o actualiza un Architecture Decision Record al estilo Michael Nygard (Status, Context, Decision, Consequences) en memoria/adr/. Úsala cuando una decisión afecte estructura, NFR, dependencias, interfaces o técnicas de construcción.
metadata:
  author: yzylabs
  version: "1.0"
---

# Redactar ADR

## Propósito

Documentar decisiones arquitectónicamente significativas de forma corta y recuperable.

## Entradas

- Título (frase nominal).
- Context (fuerzas / tensiones).
- Decision (voz activa).
- Consequences (positivas, negativas, neutrales).
- Status deseado (`proposed` | `accepted` | …).
- ADR a superseder (opcional).

## Procedimiento

1. Confirma que la decisión es “architecturally significant” (Nygard). Si no, usa `capturar-decision-material`.
2. Lista `memoria/adr/` y calcula el siguiente `NNNN`.
3. Crea `memoria/adr/NNNN-titulo-kebab.md` con la plantilla de `references/plantilla-adr-nygard.md`.
4. Rellena Status, Context, Decision, Consequences; añade fecha y decisores.
5. Si supersede a otro ADR: marca el anterior `superseded by ADR NNNN` con enlace relativo.
6. Añade enlace desde el diario del día.
7. Reporta rutas.

## Salida

```md
## ADR

- Archivo: memoria/adr/NNNN-....md
- Status: ...
- Supersede: ... | ninguno
```

## Casos límite

- Falta Consequences → no marques `accepted`; deja `proposed` y Abiertos.
- Título vago (“mejoras”) → reformula a frase nominal concreta.
- Decisión reversible menor de proceso → no ADR; nota de decisión.

## Casos de evaluación

- Normal: contexto + decisión + consecuencias → ADR accepted.
- Ambiguo: “usar X” sin fuerzas → pedir Context antes de accepted.
- Límite: supersede → ambos archivos actualizados con enlaces cruzados.

## Validación

- Secciones Status, Context, Decision, Consequences presentes.
- Numeración única.
- Enlace en diario del día (o Abiertos si el diario se pospone explícitamente).

## Criterios de terminado

- ADR en disco con plantilla completa o `proposed` con faltantes listados.
- Sin secretos en claro.

## Fuentes

- Michael Nygard — *Documenting Architecture Decisions* (2011-11-15), Cognitect: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions — consultado 2026-08-04.
- `references/plantilla-adr-nygard.md`
