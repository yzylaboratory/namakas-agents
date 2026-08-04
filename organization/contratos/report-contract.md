# Contrato de reporte (REPORT)

Toda respuesta de un subordinado a su padre **debe** usar este contrato. Un reporte sin `EVIDENCE` (o justificación explícita de por qué no hay evidencia) es inválido.

## Campos obligatorios

```text
TASK_ID:                 # Misma TASK_ID recibida
PARENT_TASK_ID:          # PARENT_TASK_ID de la tarea
MISSION_ID:              # MISSION_ID de la misión
REPORT_TO:               # Agente padre (debe coincidir con el de la tarea)
STATUS:                  # Uno de los valores del enum
SUMMARY:                 # Resumen ejecutivo del resultado
DELIVERABLES:            # Artefactos / rutas / salidas
EVIDENCE:                # Pruebas, citas, comandos, archivos, capturas
VALIDATIONS:             # Qué se validó y resultado
RISKS:                   # Riesgos abiertos
DECISIONS_REQUIRED:      # Decisiones que el padre o Randy deben tomar
DEPENDENCIES_UNLOCKED:   # Qué desbloquea este reporte
NEXT_HANDOFF:            # Siguiente agente o `NONE`
```

## Enum `STATUS`

Solo valores permitidos:

| STATUS | Significado |
|--------|-------------|
| `COMPLETED` | Criterios cubiertos con evidencia |
| `COMPLETED_WITH_LIMITATIONS` | Hecho con limitaciones documentadas |
| `BLOCKED` | No se puede avanzar; falta dependencia, forja o permiso |
| `REQUIRES_CORRECTION` | El padre debe devolver correcciones |
| `FAILED` | No se alcanzó el objetivo |

## Reglas

1. `REPORT_TO` obligatorio; sin él el reporte se rechaza.
2. `EVIDENCE` obligatorio; si no hay, `STATUS` no puede ser `COMPLETED`.
3. Nadie excepto `luffy-coordinador` entrega consolidado al usuario.
4. El padre no marca la tarea padre como completa hasta validar todos los reportes hijos.
5. Directores añaden campos departamentales (ver protocolo):

```text
DEPARTMENT:
DIRECTOR:
CHILD_REPORTS_RECEIVED:
CHILD_REPORTS_PENDING:
CONSOLIDATED_RESULT:
VALIDATION:
RISKS:
DECISIONS_REQUIRED:
REPORT_TO: luffy-coordinador
```

## Plantilla corta

```md
TASK_ID:
PARENT_TASK_ID:
MISSION_ID:
REPORT_TO:
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
