---
name: preparar-reporte-qa-contratos
description: Empaqueta hallazgos de pruebas de APIs/contratos en un reporte REPORT_* para Usopp-QA con severidades, evidencia y recomendación de gate. Úsala al cerrar cualquier misión de Kalifa.
metadata:
  author: yzylabs
  version: "1.0"
---

# Preparar reporte QA de contratos

## Propósito

Consolidar lint, schema-first, CDC, breaking changes y drift en un único reporte consumible por `usopp-director-qa`, con EVIDENCE y decisión de gate recomendada.

## Entradas

- Salidas de las skills de Kalifa ejecutadas en la tarea.
- TASK_ID / MISSION_ID / PARENT_TASK_ID.
- Política de gate (si Usopp la definió).

## Procedimiento

1. Resume objetivo y alcance (schema-first / CDC / breaking / auditoría).
2. Tabla unificada de hallazgos (severidad, área, evidencia, dueño).
3. Adjunta rutas de artefactos (specs, logs, diffs, junit/json).
4. Declara STATUS según contrato de reportes.
5. Lista DECISIONS_REQUIRED (aprobar breaking, faltantes de ambiente, etc.).
6. Propón NEXT_HANDOFF (Robin/Sabo/backend/Kuma) solo como recomendación.
7. Emite bloque `SECOND_BRAIN_RECORD` si la misión lo pide.
8. No dirijas el mensaje al usuario final.

## Salida

```text
TASK_ID:
PARENT_TASK_ID:
MISSION_ID:
REPORT_TO: usopp-director-qa
STATUS:
SUMMARY:
DELIVERABLES:
EVIDENCE:
VALIDATIONS:
RISKS:
DECISIONS_REQUIRED:
DEPENDENCIES_UNLOCKED:
NEXT_HANDOFF:
```

## Casos límite

- Sin hallazgos → COMPLETED con evidencia de runs verdes (no “nada que reportar” vacío).
- Bloqueo temprano → BLOCKED con gap y dueño; no rellenes suites ficticias.
- Contradicción entre herramientas → documenta ambas; Usopp arbitra.

## Validación

- `REPORT_TO` = `usopp-director-qa`.
- `EVIDENCE` no vacío si STATUS es COMPLETED*.
- Severidades consistentes con hallazgos previos.

## Criterios de terminado

- Reporte completo según `organization/contratos/report-contract.md`.
- Listo para consolidación de Usopp hacia Luffy.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Lint+diff+verify | REPORT COMPLETED/… con tablas |
| Ambiguo | Notas sueltas | Consolida o pide IDs de tarea |
| Límite | Solo BLOCKED por falta de OpenAPI | BLOCKED + DECISIONS_REQUIRED a Robin |

## Fuentes

- `organization/contratos/report-contract.md` (repo).
- `organization/protocolo-reportes.md` (repo).
