---
name: investigar-documentacion-y-repos
description: Investiga documentación, specs y repositorios relacionados priorizando fuentes oficiales y vigentes. Úsala cuando el reconocimiento dependa de contexto externo, ADRs, READMEs o repos hermanos — no solo del árbol local.
metadata:
  author: yzylabs
  version: "1.0"
---

# Investigar documentación y repos

## Propósito

Reunir contexto documental y de repositorios con trazabilidad de fuentes, sin instalar ni ejecutar contenido externo.

## Entradas

- Preguntas de descubrimiento.
- URLs, nombres de productos, estándares o repos candidatos.
- Restricciones (no instalar, no ejecutar scripts opacos).

## Procedimiento

1. Formula consultas concretas por pregunta.
2. Prioriza: docs oficiales → specs → repos oficiales → fuentes secundarias.
3. Registra fecha/versión/vigencia de cada fuente material.
4. Contrasta al menos dos fuentes cuando la afirmación cambie una decisión.
5. Revisa READMEs, ADRs, OpenAPI existentes, runbooks y changelogs en el workspace.
6. Busca repos hermanos o paquetes compartidos referenciados por el código.
7. Descarta blogs únicos como base material; úsalos solo como pista.
8. Nunca instales skills/scripts externos; no copies secretos.

## Salida

```md
## Fuentes primarias
| Fuente | Fecha/versión | Hallazgo usable |

## Fuentes secundarias
## Conflictos entre docs y código
## Implicaciones para el mapa
## Riesgos de obsolescencia
```

## Casos límite

- Docs internas ausentes: marca vacío y apoya el mapa solo en código.
- Versiones contradictorias: tabula y recomienda cuál verificar en runtime/config.
- Marketplace/skills públicas: solo referencia secundaria; no ejecución.

## Validación

- Fuentes primarias identificadas cuando existan.
- Cada hallazgo material tiene cita.
- Conflictos documentados, no “resueltos” en silencio.

## Criterios de terminado

- Las preguntas documentales están respondidas o bloqueadas con causa.
- Hay tabla de fuentes con vigencia.
- Ninguna instalación/ejecución externa no autorizada.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | “¿Qué versión de BIAN usa el tratado?” | Fuente oficial/repo + versión citada |
| Ambiguo | “Investiga mejores prácticas” | Exige dominio concreto; prioriza oficiales |
| Límite | Skill GitHub con script de install | Reporta idea; no instala; señala riesgo |

## Fuentes

- Política de investigación Vegapunk (`references/politica-investigacion.md`).
- Cursor / Agent Skills docs (consultado 2026-08-04) — skills on-demand vs subagents.
