---
name: coordinar-squad-frontend
description: Coordina el squad Sanji→Cavendish (web), Reiju (móvil) y Koala (portal) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa Frontend requiera alinear varios canales o resolver choques de prioridad entre web, móvil y portal.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Frontend

## Propósito

Orquestar el trabajo departamental sin que Sanji absorba implementación, y sin que los canales avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental.
- Estado de artefactos (apps web/móvil, portal, design system, specs API).
- Restricciones de plazo y dependencias externas (Nami, Backend, Sabo, QA).

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - Cavendish: web.
   - Reiju: móvil.
   - Koala: portal desarrollador.
3. Elabora RACI por entregable (Sanji Accountable).
4. Decide secuencia vs paralelo:
   - Paralelo temprano: spikes de canal.
   - Gate de congelación de journey/API/tokens antes de pulir los tres frentes.
5. Emite contratos de delegación autocontenidos.
6. Al sincronizar: detecta contradicciones (patrón UI distinto, a11y desigual, copy divergente) y resuelve o escala a Nami/Luffy.
7. Entrega consolidado departamental a Luffy.

## Salida

```md
## Objetivo de la iniciativa
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas
## Contradicciones y resoluciones
## Pendientes / bloqueos
## Listo para
```

## Casos límite

- Célula sin demo Cursor / stub: planifica roster; no inventes Task `brd-*`; marca BLOCKED o DELEGATION_REQUIRED.
- Portal depende de Sabo: incluye handoff de requisitos; Koala no redefine el producto API.
- Solo un canal en alcance: RACI mínimo; no forces trabajo artificial a los otros.

## Validación

- Cada especialista tiene entregable distinto.
- Hay un accountable (Sanji) por iniciativa.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para Tasks cuando existan agentes forjados.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- Catálogo Nakamas Frontend (Cavendish, Reiju, Koala) — `catalogo/agentes-one-piece.yaml`
- Prácticas de frontend platform governance — síntesis 2026-08-04
