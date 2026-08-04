---
name: coordinar-squad-open-banking
description: Coordina el squad Jinbe→Lucci (BIAN), FIBO-Vegapunk (semántica) y Sabo (ecosistema/APIs) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa OB requiera alinear a varios especialistas del departamento o resolver choques de prioridad entre dominio, datos y exposición.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Open Banking

## Propósito

Orquestar el trabajo departamental sin que Jinbe absorba BIAN, FIBO ni gateway, y sin que los especialistas avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental.
- Estado de artefactos (mapeo BIAN, modelo semántico, specs/gateway, portal).
- Restricciones de plazo y dependencias externas (Law, Robin, Legal, Core).

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - Lucci: procesos / BIAN.
   - FIBO-Vegapunk: semántica / términos de datos.
   - Sabo: exposición, pasarela, onboarding ecosistema.
3. Elabora RACI (Responsible/Accountable/Consulted/Informed) por entregable.
4. Decide secuencia vs paralelo:
   - Paralelo temprano: exploración Lucci+FIBO.
   - Gate de congelación semántica/dominio antes de exponer contratos estables vía Sabo/Robin.
5. Emite contratos de delegación autocontenidos (objetivo, alcance, entradas, criterios, validación).
6. Al sincronizar: detecta contradicciones (término FIBO ≠ campo API ≠ capability BIAN) y resuelve o escala.
7. Entrega consolidado departamental a Luffy o al siguiente eslabón.

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

- Especialista sin demo Cursor: planifica roster y ejecuta solo la parte de dirección; no inventes Task `brd-*`.
- Choque Lucci vs Sabo (“el dominio no está listo pero hay que publicar”): Jinbe decide gate o MVP acotado documentado.
- Robin necesita contratos ya: exige handoff mínimo de semántica/dominio o marca contrato como draft inestable.

## Validación

- Cada especialista tiene un entregable distinto.
- Hay al menos un accountable (Jinbe) por iniciativa.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para pegar en Tasks cuando existan agentes.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- Modelo operativo OB con CoE / roles claros — EBA OBWG readiness (consultado 2026-08-04)
- Catálogo Nakamas Open Banking (Lucci, FIBO, Sabo) — `catalogo/agentes-one-piece.yaml`
