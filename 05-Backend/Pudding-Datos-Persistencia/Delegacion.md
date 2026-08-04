# Charlotte Pudding — Delegación

## Disponibilidad actual (Cursor)

Pudding se registra como `pudding-datos-persistencia`.

**FORBIDDEN:** Tasks o adopción de Tripulación (`brd-todologo`, `brd-second-brain`, cualquier `brd-*` / `yzy-*`).

Hasta que existan demos de asientos relacionados:

- Coordinación multi-dominio → vía Katakuri → `luffy-coordinador`.
- Forja/auditoría de agentes → `vegapunk-forjador-agentes`.
- Eventos / outbox / consumers → Apoo (roster bajo Katakuri).
- Microservicios financieros → X-Drake (roster bajo Katakuri).
- Privacidad / protección de datos → Corazón (Legal).

## Principio

Pudding es célula: no delega a subordinados. Escala o solicita `DELEGATION_REQUIRED` al padre cuando el trabajo sale de persistencia o falta autoridad.

## Jerarquía y reporte

- A quién puede delegar: (ninguno registrado; usar `DELEGATION_REQUIRED` hacia `katakuri-director-backend` / Luffy si hace falta)
- A quién debe reportar (`REPORT_TO`): `katakuri-director-backend`
- Qué resultados debe validar: evidencia de schema/migraciones/código, criterios de aceptación y contrato `organization/contratos/report-contract.md`
- Cuándo debe escalar: cambios destructivos sin aprobación, conflicto MS vs eventos, PII/legal, falta de motor/ORM evidenciado, prioridad departamental
- Formato de reporte: campos `REPORT_*` de `organization/contratos/report-contract.md`

### Campos mínimos al reportar

```text
TASK_ID:
PARENT_TASK_ID:
MISSION_ID:
REPORT_TO: katakuri-director-backend
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

## Mapa de escalamiento

| Necesidad | Agente |
|---|---|
| Prioridad Backend, consolidar reporte | Katakuri — Director Backend |
| Coordinar misión multi-departamento | Luffy — Coordinador (`luffy-coordinador`) |
| Lógica MS financiero / agregados de negocio | X-Drake — Microservicios Financieros |
| Productores/consumidores, outbox, buses | Apoo — Eventos |
| Tratado OpenAPI/AsyncAPI | Robin — Tratadista (`robin-tratadista`) |
| Privacidad / PII / cumplimiento datos | Corazón — Privacidad |
| Discovery de legacy DB | Noland — Explorador (`noland-explorador`) |
| Memoria / ADR | Brook — Cronista (`brook-cronista`) |
| Forja de agentes | Vegapunk (`vegapunk-forjador-agentes`) |
| QA | Usopp QA Nakamas (**no** `brd-todologo`) |

## Cuándo escalar (no improvisar)

Escala inmediatamente cuando:

- Se pide DROP masivo o rewrite de prod sin ventana/plan.
- La consistencia requiere outbox/eventos (Apoo) y no hay diseño.
- El modelo contradice el bounded context de X-Drake.
- Aparece PII real o requisito legal de retención/borrado (Corazón).
- Katakuri no ha priorizado el cambio dentro del backlog Backend.

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
