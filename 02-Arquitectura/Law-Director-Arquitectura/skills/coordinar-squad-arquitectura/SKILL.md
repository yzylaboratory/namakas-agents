---
name: coordinar-squad-arquitectura
description: Coordina el squad Law→Enel (EDA), Fujitora (seguridad/gobierno técnico) y Wapol (composable) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa de arquitectura requiera alinear a varios especialistas del departamento o resolver choques de prioridad entre eventos, seguridad y composición.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Arquitectura

## Propósito

Orquestar el trabajo departamental sin que Law absorba EDA, seguridad o composable, y sin que los especialistas avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental.
- Estado de artefactos (diagramas, ADRs, threat notes, boundaries).
- Restricciones de plazo y dependencias externas (Robin, Franky, Jinbe, Backend).

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - Enel: event-driven / mensajería / consistencia.
   - Fujitora: seguridad y gobierno técnico.
   - Wapol: composición modular / límites reutilizables.
3. Elabora RACI por entregable.
4. Decide secuencia vs paralelo:
   - Paralelo temprano: exploración Enel+Wapol.
   - Gate Fujitora antes de nuevos trust boundaries.
   - ADR consolidado por Law antes de handoff a implementación.
5. Emite contratos de delegación autocontenidos (objetivo, alcance, entradas, criterios, validación).
6. Si la célula es stub / sin Task vivo: emite `DELEGATION_REQUIRED` a Luffy; no inventes `brd-*`.
7. Al sincronizar: detecta contradicciones (evento vs módulo vs control) y resuelve o escala.
8. Entrega consolidado departamental a Luffy o al siguiente eslabón.

## Salida

```md
## Objetivo de la iniciativa
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas / DELEGATION_REQUIRED
## Contradicciones y resoluciones
## Pendientes / bloqueos
## Listo para
```

## Casos límite

- Especialista sin demo Cursor: planifica roster y ejecuta solo la parte de dirección; no inventes Task Tripulación.
- Choque Enel vs Wapol (“todo es evento” vs “todo es módulo”): Law decide boundary y ADR.
- Fujitora bloquea por seguridad: documenta condiciones; no bypass silencioso.

## Validación

- Cada especialista tiene un entregable distinto.
- Hay al menos un accountable (Law) por iniciativa.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para Tasks cuando existan agentes, o `DELEGATION_REQUIRED` explícito.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- The Open Group — Architecture Board roles / governance operating model (síntesis TOGAF) — 2026-08-04
- Catálogo Nakamas Arquitectura (Enel, Fujitora, Wapol) — `00-Agentes-Generales/Vegapunk-Forjador-Agentes/catalogo/agentes-one-piece.yaml`
- `organization/organigrama.yaml` — nodo `law-director-arquitectura`
