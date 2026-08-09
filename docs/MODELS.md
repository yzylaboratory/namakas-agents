# Nakamas — política de modelos

SoT de slugs `model:` en frontmatter. Runtime: `~/.cursor/agents/*.md`. Espejo: `runtime-agents/`.

## Principio: default barato + escalación

1. **Composer** (`composer-2.5[]`) es el default de ejecución.
2. **Grok** (`cursor-grok-4.5-high`) solo en puntos de decisión / arbitraje (Oda chat, capitanes Law/Lucci, arquitecto Edison).
3. **Premiums Planner** (Sonnet / Sol / Codex / Opus) **no** van fijos en frontmatter: Composer por defecto; Law puede pedir override en L3+/L4.
4. Imp/Ver **nunca** usan GPT/Claude/Codex — solo Composer o Grok.

## Reglas de grupo

| Grupo | Modelos permitidos |
|-------|-------------------|
| **Oda** (chat raíz) | `cursor-grok-4.5-high` (default intencional). Opción de ahorro: Composer en chat rutinario — tradeoff: peor routing/arbitraje; solo si el usuario lo decide. |
| **Implementer** | Solo `composer-2.5[]` o `cursor-grok-4.5-high` |
| **Verifier** | Solo `composer-2.5[]` o `cursor-grok-4.5-high` |
| **Planner** | Default Composer/Grok según tabla; premiums opcionales vía escalación Law |

## Escalación (cuándo subir de modelo)

| Quién pide | Agente | Override permitido | Cuándo |
|------------|--------|-------------------|--------|
| Law | Robin | `claude-sonnet-5-thinking-high` | Análisis L3+/L4 o ambigüedad sistémica alta |
| Law | Doflamingo | `gpt-5.6-sol-high` | Integraciones/BIAN L3+/L4 complejas |
| Law | Beckman | `gpt-5.3-codex-high` | Plan técnico L3+/L4 de alto riesgo |
| Law | (cualquier Planner) | `claude-opus-5-thinking-high` | Override excepcional L4 |
| Luffy | Franky / Zoro | `cursor-grok-4.5-high` | Hard path / TL transversal de alta complejidad |
| Lucci | Chopper / Stussy | `cursor-grok-4.5-high` | RCA profunda o threat model L3+ |

Reglas de override:

- Capitanes **pueden** pasar `model` en Task **solo** en filas de esta tabla; documentar motivo en consolidado.
- Oda **no** reasigna modelos en silencio ni “por si acaso”.
- Sin justificación L3+/alta complejidad → se queda el frontmatter (Composer).

## Tabla completa (defaults de frontmatter)

### Oda

| Agente | slug | Nota |
|--------|------|------|
| Oda | `cursor-grok-4.5-high` | Selector del chat (no es subagente) |

### Planner

| Agente | slug | Razón |
|--------|------|-------|
| Law | `cursor-grok-4.5-high` | Capitán / arbitraje |
| Noland | `composer-2.5[]` | Discovery |
| Robin | `composer-2.5[]` | Análisis; premium vía escalación Law |
| Edison | `cursor-grok-4.5-high` | Arquitectura / SDD |
| Doflamingo | `composer-2.5[]` | Integraciones; premium vía escalación Law |
| Beckman | `composer-2.5[]` | Plan técnico; premium vía escalación Law |
| Clover | `composer-2.5[]` | Docs |
| Iceburg | `composer-2.5[]` | OpenSpec |

### Implementer

| Agente | slug | Razón |
|--------|------|-------|
| Luffy | `composer-2.5[]` | Capitán ejecución |
| Franky | `composer-2.5[]` | TL; Grok vía escalación Luffy |
| Usopp | `composer-2.5[]` | Frontend |
| Sanji | `composer-2.5[]` | Backend |
| Nami | `composer-2.5[]` | Data |
| Jinbe | `composer-2.5[]` | DevOps |
| Zoro | `composer-2.5[]` | Código crítico; Grok vía escalación Luffy |
| Brook | `composer-2.5[]` | Events / async |

### Verifier

| Agente | slug | Razón |
|--------|------|-------|
| Lucci | `cursor-grok-4.5-high` | Capitán arbitra |
| Tashigi | `composer-2.5[]` | QA |
| Chopper | `composer-2.5[]` | RCA; Grok vía escalación Lucci |
| Stussy | `composer-2.5[]` | Security; Grok vía escalación Lucci |
| Fujitora | `composer-2.5[]` | Performance |
| Sengoku | `composer-2.5[]` | Compliance |
| Kaku | `composer-2.5[]` | Architecture conformance |

## Notas operativas

- `composer-2.5[]` = Composer **base** (no Fast). Alternativa: `composer-2.5[fast=false]`.
- Tras instalar en otra Mac: `rg -n '^model:' ~/.cursor/agents/*.md | sort` y comparar con esta tabla.
- Editor (Buggy et al.) fuera de esta flota Engineering: preferir Composer salvo override explícito del usuario.
