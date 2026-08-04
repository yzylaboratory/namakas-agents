---
name: coordinar-squad-marketing-growth
description: Coordina el squad Marketing/Growth (Carrot, Shakky, Bartolomeo) con RACI, handoffs y consolidación departamental. Úsala cuando Luffy delegue una iniciativa de growth que requiera varias células o cuando haya que sincronizar adopción, analítica y comunidad.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Marketing / Growth

## Propósito

Orquestar trabajo entre Carrot, Shakky y Bartolomeo con contratos claros, evitando solapamientos y consolidando un solo reporte departamental para Luffy.

## Entradas

- Objetivo de la iniciativa y segmento.
- Alcance, plazos y restricciones de marca/presupuesto.
- Estado de forja de cada célula (vivo vs stub).
- Entregables previos (estrategia, North Star, backlog).

## Procedimiento

1. Descompón la iniciativa en frentes: adopción (Carrot), mercado/posicionamiento/métricas (Shakky), comunidad/evangelización (Bartolomeo).
2. Asigna RACI por entregable; Morgans es accountable departamental.
3. Emite contratos de delegación autocontenidos (objetivo, alcance, entradas, criterios, evidencia).
4. Si una célula es **stub**: no simules su trabajo; emite `DELEGATION_REQUIRED` / planifica forja vía Luffy→Vegapunk y documenta el gap.
5. Define secuencia vs paralelo (ver Delegacion.md): no contaminar la misma métrica primaria con dos experiments sin owner.
6. Consolida reportes hijos en el bloque departamental hacia Luffy; marca pendientes y riesgos.

## Salida

```md
## Plan de coordinación
| Frente | Agente | Estado (vivo/stub) | Entregable | Due date | Dependencias |
## RACI
## Contratos emitidos / DELEGATION_REQUIRED
## Consolidado para Luffy
CHILD_REPORTS_RECEIVED:
CHILD_REPORTS_PENDING:
CONSOLIDATED_RESULT:
## Riesgos
```

## Casos límite

- Solo una célula aplicable: coordina igual (RACI + reporte); no inventes trabajo para las otras.
- Conflicto Carrot vs Bartolomeo (producto no listo para community): pausa advocacy; escala a Luffy si hay presión política.
- Handoff a Ventas/UX: no captures su mandato; pide coordinación vía Luffy.

## Validación

- Cada frente tiene dueño o `DELEGATION_REQUIRED` explícito.
- No hay doble ownership de la métrica primaria.
- El consolidado es un solo mensaje a `luffy-coordinador`.

## Criterios de terminado

- Squad alineado o gaps de stub documentados.
- Handoffs listos para ejecución o forja.
- Reporte departamental listo para Luffy.

## Fuentes

- Cadena de mando Nakamas — `organization/protocolo-reportes.md`, `organization/contratos/report-contract.md`
- Práctica RACI en squads de growth (síntesis) — 2026-08-04
