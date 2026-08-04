---
name: coordinar-squad-sistemas-core
description: Coordina el squad Crocus/Tom/Kaku con contratos de delegación, RACI y consolidación de reportes. Úsala cuando una iniciativa de core requiera orquestar legacy, integración y procesamiento transaccional.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Sistemas Core

## Propósito

Orquestar al squad sin solapamientos ambiguos: Iceburg prioriza y valida; las células ejecutan su oficio o se declara bloqueo por stub.

## Entradas

- Objetivo de la iniciativa y criterios de aceptación.
- Estado de cada célula (vivo / stub).
- Dependencias y handoffs esperados.
- Restricciones de ventana y riesgo.

## Procedimiento

1. Descompón el trabajo por mandato:
   - Crocus → legacy / coexistencia / strangler sobre herencia.
   - Tom → adapters / canónico / versionado de interfaces.
   - Kaku → semántica transaccional / idempotencia / posting.
2. Emite contratos de delegación autocontenidos (ver `Delegacion.md`).
3. Si la célula es stub o no hay Custom Agent: emite `DELEGATION_REQUIRED` a Luffy; no inventes ejecución.
4. Define secuencia vs paralelo (ver reglas de paralelización).
5. Recolecta reportes hijos con EVIDENCE; rechaza “done” sin reconciliación/tests cuando aplique.
6. Consolida reporte departamental a Luffy.

## Salida

```md
## Plan de coordinación
| Trabajo | Agente | Estado worker | Entregable | Dependencia |
## DELEGATION_REQUIRED (si aplica)
## RACI breve
## Consolidado para Luffy
DEPARTMENT: Sistemas Core
DIRECTOR: iceburg-director-sistemas-core
CHILD_REPORTS_RECEIVED:
CHILD_REPORTS_PENDING:
CONSOLIDATED_RESULT:
VALIDATION:
RISKS:
REPORT_TO: luffy-coordinador
```

## Casos límite

- Solo una célula necesaria: coordina igual; no inventes trabajo para las otras.
- Conflicto Tom vs Kaku sobre semántica: Iceburg decide prioridad temporal y escala a Law si es estructural.
- Todos stub: plan + `DELEGATION_REQUIRED` / `COMPLETED_WITH_LIMITATIONS` o `BLOCKED` según impacto.

## Validación

- Cada entrega tiene dueño y criterios verificables.
- No se simuló trabajo de stub.
- El consolidado es un único reporte departamental.

## Criterios de terminado

- Squad alineado o bloqueos explícitos.
- Handoffs listos para el siguiente actor.
- Reporte a Luffy con EVIDENCE.

## Fuentes

- `Delegacion.md` del agente — 2026-08-04
- `organization/contratos/report-contract.md` — vigente en repo
