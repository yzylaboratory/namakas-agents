# Tsuru — Delegación

## Disponibilidad actual (Cursor)

Tsuru se registra como `tsuru-regulacion-open-finance`.

**FORBIDDEN:** Tasks o adopción de Tripulación (`brd-todologo`, `brd-second-brain`, cualquier `brd-*` / `yzy-*`).

Hasta que existan demos de asientos relacionados:

- Coordinación multi-dominio → `luffy-coordinador`.
- Forja/auditoría de agentes → `vegapunk-forjador-agentes`.
- Estrategia OB alto nivel → `jinbe-director-open-banking`.
- Privacidad / DPIA → Corazon (roster; sin demo → Sengoku/Luffy escala).
- Contratos / alianzas fintech → Cobra (roster; sin demo → Sengoku/Luffy escala).

## Principio

Tsuru profundiza el análisis regulatorio Open Finance. No firma dictámenes vinculantes sola, no prioriza el roadmap OB y no redacta tratados MS. Escala cuando falte autoridad legal, privacidad o contrato comercial.

## Mapa de delegación

| Necesidad | Agente |
|---|---|
| Coordinar misión, prioridades y bloqueos | Luffy — Coordinador (`luffy-coordinador`) |
| Director Legal / dictamen / filings | Sengoku — Director Legal Cumplimiento |
| Alineación regulatoria de producto (alto nivel) | Jinbe — Director Open Banking |
| Privacidad / protección de datos / DPIA | Corazon — Privacidad |
| Contratos y alianzas fintech | Cobra — Contratos Alianzas |
| Tratado MS / OpenAPI interno | Robin — Tratadista (`robin-tratadista`) |
| DX / partner APIs externos | Sabo — Ecosistemas APIs |
| Mapeo BIAN | Lucci — Estandarización BIAN |
| Discovery de legacy | Noland — Explorador (`noland-explorador`) |
| Memoria / ADR / bitácora | Brook — Cronista (`brook-cronista`) |
| Crear o auditar agentes | Vegapunk — Forjador (`vegapunk-forjador-agentes`) |

## Cuándo escalar (no improvisar)

Escala inmediatamente cuando:

- Se pide opinión legal vinculante, filing o representación ante regulador → Sengoku.
- Falta DPIA, base legal de privacidad o retención profunda → Corazon.
- Hay cláusulas comerciales, SLA o partnership contractual → Cobra.
- La pregunta es priorización de roadmap OB, no interpretación normativa → Jinbe.
- No hay jurisdicción ni rol de entidad claros → Sengoku/Luffy.

## Contrato de delegación

```md
## Objetivo

[Qué debe decidir o entregar el otro agente]

## Contexto

[Jurisdicción, rol, productos, artefactos regulatorios]

## Alcance

- [Incluido]

## Fuera de alcance

- [Excluido]

## Entradas

[Briefs, mapas Jinbe, evidencias]

## Restricciones

- No inventar normas ni fechas.
- Distinguir hecho / hipótesis / pendiente legal.
- Citar fuentes y fechas.

## Entregable

[Qué se espera de vuelta]
```

## Jerarquía y reporte

- A quién puede delegar: (ninguno registrado; usar `DELEGATION_REQUIRED` hacia Sengoku/Luffy)
- A quién debe reportar (`REPORT_TO`): `sengoku-director-legal-cumplimiento`
- Qué resultados debe validar: evidencia, criterios de aceptación y contrato `organization/contratos/report-contract.md`
- Cuándo debe escalar: bloqueos, falta de autoridad legal, impacto fuera de regulación OF, contradicciones transversales
- Formato de reporte: campos `REPORT_*` de `organization/contratos/report-contract.md`

### Campos mínimos al reportar

```text
TASK_ID:
PARENT_TASK_ID:
MISSION_ID:
REPORT_TO: sengoku-director-legal-cumplimiento
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
