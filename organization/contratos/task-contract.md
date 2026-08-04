# Contrato de tarea (TASK)

Toda delegación entre agentes Nakamas **debe** emitir un bloque de tarea con estos campos. Sin `REPORT_TO` la delegación es inválida.

## Campos obligatorios

```text
TASK_ID:                # Identificador único de la tarea (ej. T-001)
PARENT_TASK_ID:         # Tarea padre; `ROOT` si Luffy la crea directamente
MISSION_ID:             # Identificador de misión compartido (ej. M-2026-08-04-OB-API)
ASSIGNED_BY:            # id del agente que asigna (debe ser el supervisor o Luffy)
ASSIGNED_TO:            # id del agente receptor (registrado en organigrama.yaml)
REPORT_TO:              # id del agente al que se debe devolver el reporte (padre)
OBJECTIVE:              # Resultado concreto esperado
CONTEXT:                # Contexto autocontenido; no asumir conversación previa
SCOPE:                  # Alcance incluido
OUT_OF_SCOPE:           # Exclusiones explícitas
INPUTS:                 # Archivos, contratos, decisiones, enlaces
CONSTRAINTS:            # Técnicas, regulatorias, de tiempo o seguridad
EXPECTED_DELIVERABLE:   # Formato y contenido del artefacto
ACCEPTANCE_CRITERIA:    # Condiciones verificables de done
VALIDATION_REQUIRED:    # Pruebas, revisiones o evidencia exigida
```

## Reglas

1. `ASSIGNED_TO` y `REPORT_TO` deben existir en `organization/organigrama.yaml`.
2. `REPORT_TO` debe coincidir con el `reports_to` del receptor (o Luffy en coordinación transversal).
3. Un director solo asigna a sus `direct_reports` (células).
4. Una célula solo asigna a especialistas bajo su célula (si existen) o emite `DELEGATION_REQUIRED`.
5. Luffy puede asignar a agentes generales y directores.
6. Si el entorno no permite lanzar subagentes, el padre emite la tarea y el hijo responde con el contrato de reporte.
7. **Título UI (Cursor Task `description`, fuera de este bloque TASK_*):** preferir `{Especialista} ← {Director}: {acción breve en español}`; admitido `{Personaje}: {acción}` si el prompt lleva `REPORT_TO` visible. No sustituye `TASK_ID` / `ASSIGNED_TO` / `REPORT_TO`. El slug no va en el título UI. Ver `00-Agentes-Generales/Luffy-Coordinador/Delegacion.md`.
8. **`REPORT_TO` es obligatorio y visible** en el prompt de Task (además del bloque TASK_*). La cadena Luffy→Director→célula debe poder reconstruirse desde `ASSIGNED_BY` / `ASSIGNED_TO` / `REPORT_TO` + título UI.
9. **FORBIDDEN** asignar trabajo de usuario a Task types Cursor genéricos (`shell`, `generalPurpose`, `explore`, …) que no estén en el organigrama Nakamas.

## Plantilla corta

```md
TASK_ID:
PARENT_TASK_ID:
MISSION_ID:
ASSIGNED_BY:
ASSIGNED_TO:
REPORT_TO:
OBJECTIVE:
CONTEXT:
SCOPE:
OUT_OF_SCOPE:
INPUTS:
CONSTRAINTS:
EXPECTED_DELIVERABLE:
ACCEPTANCE_CRITERIA:
VALIDATION_REQUIRED:
```
