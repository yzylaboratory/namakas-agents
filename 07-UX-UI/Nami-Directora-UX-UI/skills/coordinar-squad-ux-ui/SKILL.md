---
name: coordinar-squad-ux-ui
description: Coordina el squad Chopper/Perona/Miss Goldenweek con contratos de delegación y secuencia research→UI→sistema. Úsala cuando haya que orquestar el departamento UX/UI, repartir trabajo o sincronizar handoffs.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad UX/UI

## Propósito

Orquestar al squad UX/UI con RACI claro, contratos de delegación y sincronización de dependencias — incluyendo el caso de células no disponibles en runtime.

## Entradas

- Objetivo de la misión y criterios de aceptación.
- Estado de forja/disponibilidad de Chopper, Perona y Miss Goldenweek.
- Artefactos previos (research, flows, librería).
- Dependencias externas (Frontend, Vivi, QA, Legal).

## Procedimiento

1. Descompón la misión en paquetes por especialidad:
   - Chopper: research / insights
   - Perona: UI / flujos / prototipo
   - Miss Goldenweek: patrones / tokens / componentes
2. Define secuencia o paralelismo (ver Delegacion.md).
3. Redacta contrato de delegación por paquete (objetivo, alcance, entradas, criterios, validación).
4. Si la célula no está disponible en runtime: emite `DELEGATION_REQUIRED` a Luffy con el contrato listo; no inventes entregables de la célula.
5. Define puntos de sync (insight freeze, UI critique, system intake, handoff eng).
6. Consolida reportes hijos o documenta `CHILD_REPORTS_PENDING`.
7. Prepara reporte departamental a Luffy.

## Salida

```md
## Plan de coordinación UX/UI
- Objetivo:
- RACI:
## Paquetes
| Paquete | Agente | Estado runtime | Entregable | Criterios |
## DELEGATION_REQUIRED (si aplica)
## Secuencia / paralelo
## Sync points
## Riesgos
## Reporte departamental (borrador)
```

## Casos límite

- Squad parcial offline: limita entregables al alcance ejecutable; bloquea craft de células ausentes.
- Conflicto research vs estética: prioriza evidencia de tarea; escala a Luffy si Producto impone vanity.
- Handoff a Frontend sin sistema: exige mapeo a componentes existentes o intake a Miss Goldenweek.

## Validación

- Cada paquete tiene dueño y criterios.
- Células no disponibles no se presentan como COMPLETED.
- Cadena REPORT_TO = luffy-coordinador.

## Criterios de terminado

- Plan ejecutable o bloqueos explícitos con `DELEGATION_REQUIRED`.
- Contratos listos para células o para Luffy.
- Consolidado departamental preparado.

## Fuentes

- Contratos Nakamas — `organization/contratos/task-contract.md`, `organization/contratos/report-contract.md`
- ISO 9241-210 — iteración multidisciplinar HCD — consultado 2026-08-04
