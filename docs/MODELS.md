# Nakamas — política de modelos

SoT de slugs `model:` en frontmatter. Runtime: `~/.cursor/agents/*.md`. Espejo: `runtime-agents/`.

## Reglas de grupo

| Grupo | Modelos permitidos |
|-------|-------------------|
| **Oda** (chat raíz) | Solo `cursor-grok-4.5-high` |
| **Implementer** | Solo `composer-2.5[]` o `cursor-grok-4.5-high` |
| **Verifier** | Solo `composer-2.5[]` o `cursor-grok-4.5-high` |
| **Planner** | Grok, Composer, y premiums: `gpt-5.6-sol-high`, `gpt-5.3-codex-high`, `claude-sonnet-5-thinking-high`, `claude-opus-5-thinking-high` |

Prohibido asignar GPT / Claude Sonnet / Claude Opus / Codex a Implementer o Verifier.

## Tabla completa

### Oda

| Agente | slug | Nota |
|--------|------|------|
| Oda | `cursor-grok-4.5-high` | Selector del chat (no es subagente) |

### Planner

| Agente | slug | Razón |
|--------|------|-------|
| Law | `cursor-grok-4.5-high` | Capitán Planner |
| Noland | `composer-2.5[]` | Discovery ejecución |
| Robin | `claude-sonnet-5-thinking-high` | Análisis de sistemas profundo |
| Edison | `cursor-grok-4.5-high` | Arquitectura / SDD |
| Doflamingo | `gpt-5.6-sol-high` | Integraciones / BIAN complejas |
| Beckman | `gpt-5.3-codex-high` | Plan técnico ejecutable (Codex liberado de Imp) |
| Clover | `composer-2.5[]` | Docs |
| Iceburg | `composer-2.5[]` | OpenSpec CLI/workflow (artefactos, validate, sync/archive) |

**Premium absorbido desde Imp/Ver:** Sol → Doflamingo; Codex → Beckman; Sonnet → Robin. `claude-opus-5-thinking-high` queda como premium Planner disponible (p. ej. análisis L3+ / override Robin si Law lo pide); no va a Imp/Ver.

### Implementer

| Agente | slug | Razón |
|--------|------|-------|
| Luffy | `composer-2.5[]` | Capitán ejecución |
| Franky | `cursor-grok-4.5-high` | TL / plataforma — decisión técnica |
| Usopp | `composer-2.5[]` | Frontend |
| Sanji | `composer-2.5[]` | Backend |
| Nami | `composer-2.5[]` | Data |
| Jinbe | `composer-2.5[]` | DevOps |
| Zoro | `cursor-grok-4.5-high` | Código crítico / hard path |
| Brook | `composer-2.5[]` | Events / async |

### Verifier

| Agente | slug | Razón |
|--------|------|-------|
| Lucci | `cursor-grok-4.5-high` | Capitán arbitra |
| Tashigi | `composer-2.5[]` | QA |
| Chopper | `cursor-grok-4.5-high` | RCA difícil |
| Stussy | `cursor-grok-4.5-high` | Security compleja |
| Fujitora | `composer-2.5[]` | Performance |
| Sengoku | `composer-2.5[]` | Compliance |
| Kaku | `composer-2.5[]` | Architecture conformance |

## Notas operativas

- `composer-2.5[]` = Composer **base** (no Fast). Alternativa: `composer-2.5[fast=false]`.
- Al invocar Task: no pasar `model` distinto del frontmatter salvo override explícito del usuario.
- Tras instalar en otra Mac: `rg -n '^model:' ~/.cursor/agents/*.md | sort` y comparar con esta tabla.
