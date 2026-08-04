# nakamas-agents

Definiciones de agentes (personalidad, rol, reglas, skills) para la tripulación nakamas.

## Disponibilidad actual (Cursor)

**Diez Custom Agents vivos** — seis en `00-Agentes-Generales` y cuatro en `01-Open-Banking`:

### 00 — Agentes Generales

| Agent | Rol | Docs |
|-------|-----|------|
| `luffy-coordinador` | Coordinación multi-paso / multi-dominio | [`00-Agentes-Generales/Luffy-Coordinador/`](00-Agentes-Generales/Luffy-Coordinador/) |
| `vegapunk-forjador-agentes` | Crear / investigar / auditar agentes y skills | [`00-Agentes-Generales/Vegapunk-Forjador-Agentes/`](00-Agentes-Generales/Vegapunk-Forjador-Agentes/) |
| `brook-cronista` | Bitácoras, memoria, ADR, SECOND_BRAIN_RECORD | [`00-Agentes-Generales/Brook-Cronista/`](00-Agentes-Generales/Brook-Cronista/) |
| `noland-explorador` | Discovery / legacy / mapas / reconocimiento | [`00-Agentes-Generales/Noland-Explorador/`](00-Agentes-Generales/Noland-Explorador/) |
| `vivi-escritor` | README, guías, historias de usuario, prosa humana | [`00-Agentes-Generales/Vivi-Escritor/`](00-Agentes-Generales/Vivi-Escritor/) |
| `robin-tratadista` | Tratados MS/orch, OpenAPI/AsyncAPI, handoffs BIAN/FIBO | [`00-Agentes-Generales/Robin-Tratadista/`](00-Agentes-Generales/Robin-Tratadista/) |

### 01 — Open Banking

| Agent | Rol | Docs |
|-------|-----|------|
| `jinbe-director-open-banking` | Estrategia OB / Open Finance, priorización, gobierno APIs | [`01-Open-Banking/Jinbe-Director-Open-Banking/`](01-Open-Banking/Jinbe-Director-Open-Banking/) |
| `lucci-estandarizacion-procesos-bian` | Mapeo BIAN / Service Domains / HANDOFF_BIAN | [`01-Open-Banking/Lucci-Estandarizacion-Procesos-BIAN/`](01-Open-Banking/Lucci-Estandarizacion-Procesos-BIAN/) |
| `vegapunk-arquitectura-semantica-fibo` | Semántica FIBO / HANDOFF_FIBO (≠ forjador Stella) | [`01-Open-Banking/Vegapunk-Arquitectura-Semantica-FIBO/`](01-Open-Banking/Vegapunk-Arquitectura-Semantica-FIBO/) |
| `sabo-ecosistemas-abiertos-apis` | DX, partner APIs, sandboxes, versionado externo | [`01-Open-Banking/Sabo-Ecosistemas-Abiertos-APIs/`](01-Open-Banking/Sabo-Ecosistemas-Abiertos-APIs/) |

Reglas de proyecto (override Tripulación):

- [`.cursor/rules/nakamas-live-agents-only.mdc`](.cursor/rules/nakamas-live-agents-only.mdc)
- [`.cursor/rules/nakamas-agents.mdc`](.cursor/rules/nakamas-agents.mdc)

Adapters Cursor: [`.cursor/agents/`](.cursor/agents/) — los diez ids anteriores. Claude: [`.claude/agents/`](.claude/agents/).

## Routing en este repo

1. Multistep / multi-dominio → **Luffy** (`luffy-coordinador`).
2. Crear / auditar / forjar agentes → **Vegapunk Stella** (`vegapunk-forjador-agentes`).
3. Bitácoras / memoria / ADR → **Brook** (`brook-cronista`) — no Olvia.
4. Discovery / legacy / recon → **Noland** (`noland-explorador`) — no Nami/`brd-luperon`.
5. Docs de producto para humanos → **Vivi** (`vivi-escritor`) — no Kaya/`brd-docia`.
6. Tratados / OpenAPI / AsyncAPI → **Robin** (`robin-tratadista`) — no Hostos.
7. Cadena Open Banking: **Jinbe** → **Lucci** / **FIBO-Vegapunk** / **Sabo** → **Robin** según necesidad.
8. Edición simple aislada → directa, sin Task.
9. **FORBIDDEN** enrutar a Tripulación (`brd-todologo`, `brd-second-brain`, cualquier `brd-*` / `yzy-*`).
10. **No** inventar Task a asientos nakamas futuros sin demo (p. ej. Usopp-QA, Law).

Los demás asientos (otros departamentos / células) pueden aparecer en `Delegacion.md` / catálogo como **roster objetivo**; no son Custom Agents vivos todavía.

## Fuera de este repo

Workspaces Banreservas / Tripulación siguen usando las reglas globales `mandatory-delegation` y `yzy-dispatch` (Task → especialistas / Usopp / Olvia). Ese flujo **no** aplica dentro de `nakamas-agents`.
