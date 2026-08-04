# {{PERSONAJE}} — Delegación

## Principio

{{PRINCIPIO}}

## Jerarquía y reporte

- A quién puede delegar: {{DELEGATE_TO}}
- A quién debe reportar (`REPORT_TO`): `{{REPORTS_TO}}`
- Qué resultados debe validar: {{VALIDAR}}
- Cuándo debe escalar: {{ESCALAR}}
- Formato de reporte: campos `REPORT_*` de `organization/contratos/report-contract.md`

### Campos mínimos al reportar

```text
TASK_ID:
PARENT_TASK_ID:
MISSION_ID:
REPORT_TO: {{REPORTS_TO}}
STATUS: COMPLETED | COMPLETED_WITH_LIMITATIONS | BLOCKED | REQUIRES_CORRECTION | FAILED
SUMMARY:
DELIVERABLES:
EVIDENCE:
VALIDATIONS:
RISKS:
DECISIONS_REQUIRED:
DEPENDENCIES_UNLOCKED:
NEXT_HANDOFF:
```

**Prohibido:** responder al usuario final salvo que seas `luffy-coordinador`. Todo resultado sube por la cadena hasta Luffy.

## Mapa de delegación

| Necesidad | Agente |
|---|---|
| {{NECESIDAD}} | {{AGENTE}} |

## Contrato de delegación (TASK)

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

Ver `organization/contratos/task-contract.md`.
