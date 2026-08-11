# Nakamas — política de modelos (Claude Code)

SoT de slugs `model:` / `effort:` en frontmatter Claude. Runtime: `~/.claude/agents/*.md`. Espejo: `runtime/claude/agents/`.

Cursor (Composer / Grok): ver [`MODELS.md`](MODELS.md). **No mezclar** slugs entre árboles.

## Principio: default barato + escalación

1. **Sonnet** es el default de ejecución (equivalente Composer en Cursor).
2. **Opus + `effort: high`** solo en puntos de decisión / arbitraje (Oda, capitanes Law/Lucci, arquitecto Edison).
3. **Haiku** solo para exploración barata si se define un agente explore-only (no es el default de la flota Engineering).
4. **`inherit`** está permitido cuando el agente deba seguir el modelo de la sesión; la flota Nakamas fija `opus`/`sonnet` explícitos.

## Mapeo Cursor → Claude

| Rol Cursor | Slug Cursor | Claude `model` / `effort` |
|------------|-------------|---------------------------|
| Oda (raíz) | `cursor-grok-4.5-high` (chat / User Rule) | Agent `oda`: `opus` + `effort: high`. SoT: `~/.claude/agents/oda.md`. Rule refuerzo: `~/.claude/rules/oda.md`. Invocar: `claude --agent oda` / @oda |
| Law, Edison, Lucci | `cursor-grok-4.5-high` | `opus` + `effort: high` |
| Resto de la flota | `composer-2.5[]` | `sonnet` |
| Explore-only (si aplica) | — | `haiku` |
| Premiums Planner (escalación) | Sonnet/Sol/Codex/Opus Cursor | Ver tabla de escalación abajo |

**Prohibido** en `runtime/claude/` y `~/.claude/agents/`: `composer-2.5[]`, `cursor-grok-*`, u otros slugs Cursor.

**Nota Cursor:** Oda **no** se instala como subagente en `runtime/cursor/agents/` ni `~/.cursor/agents/`.

## Tabla completa (defaults de frontmatter Claude)

### Oda

| Agente | model | effort | Nota |
|--------|-------|--------|------|
| Oda | `opus` | `high` | Agent file Claude-only; rule `oda.md` es refuerzo |

### Planner

| Agente | model | effort | Razón |
|--------|-------|--------|-------|
| Law | `opus` | `high` | Capitán / arbitraje |
| Noland | `sonnet` | — | Discovery |
| Robin | `sonnet` | — | Análisis; escalación vía Law |
| Edison | `opus` | `high` | Arquitectura / SDD |
| Doflamingo | `sonnet` | — | Integraciones |
| Beckman | `sonnet` | — | Plan técnico |
| Clover | `sonnet` | — | Docs |
| Iceburg | `sonnet` | — | OpenSpec |

### Implementer

| Agente | model | Razón |
|--------|-------|-------|
| Luffy | `sonnet` | Capitán ejecución |
| Franky, Usopp, Sanji, Nami, Jinbe, Zoro, Brook | `sonnet` | Especialistas |

### Verifier

| Agente | model | effort | Razón |
|--------|-------|--------|-------|
| Lucci | `opus` | `high` | Capitán arbitra |
| Tashigi, Chopper, Stussy, Fujitora, Sengoku, Kaku | `sonnet` | — | Especialistas |

## Escalación (cuándo subir)

| Quién pide | Agente | Override Claude | Cuándo |
|------------|--------|-----------------|--------|
| Law | Robin | `opus` o `sonnet` + `effort: high` | Análisis L3+/L4 |
| Law | Doflamingo / Beckman | `opus` | Integraciones / plan L3+/L4 de alto riesgo |
| Law | (cualquier Planner) | `opus` + `effort: high` | Override excepcional L4 |
| Luffy | Franky / Zoro | `opus` | Hard path / TL transversal |
| Lucci | Chopper / Stussy | `opus` + `effort: high` | RCA profunda o threat model L3+ |

Reglas:

- Capitanes pueden pasar `model` en la invocación `Agent` solo según esta tabla; documentar en consolidado.
- Oda no reasigna modelos en silencio.
- Sin justificación L3+ → se queda el frontmatter.

## Tools (Claude Code)

Frontmatter `tools:` usa nombres reales de Claude Code (`Read`, `Grep`, `Glob`, `Bash`, `Edit`, `Write`, `Agent`, …). Ver [sub-agents](https://code.claude.com/docs/en/sub-agents).

- Capitanes: `Agent(<tripulación>)` + herramientas de lectura/orquestación.
- Verifiers read-heavy: sin `Edit`/`Write` (Chopper sí puede editar al corregir).
- Implementers: set completo razonable + `acceptEdits` donde aplique.

## Regenerar / validar

```bash
python3 scripts/lib/generate_claude_agents.py
python3 scripts/lib/generate_claude_agents.py --validate-only
./scripts/install-nakamas.sh --target=claude
```
