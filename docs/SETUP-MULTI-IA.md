# Setup Nakamas Agents — multi-IA (Cursor, Codex, Claude, Antigravity)

SoT versionada: este repo (`namakas-agents`). Runtime Cursor ya documentado en [`SETUP-OTRA-MAC.md`](SETUP-OTRA-MAC.md).

## Principio

- **Una flota, dos (o más) árboles instalables:**
  - Cursor: `runtime/cursor/agents/` (symlink compat: `runtime-agents/`)
  - Claude: `runtime/claude/agents/` (frontmatter nativo Claude Code)
- **Oda:** en Cursor = rule / User Rule (no subagente Cursor). En Claude = **agent file** `oda.md` (SoT invocable) + rule de refuerzo.
- **Formato nativo** por herramienta (no copia ciega del frontmatter Cursor → Claude).
- **No se borran** configs ajenas (rules legacy, AGENTS.md previos, etc.).
- Modelos Cursor (`composer-2.5[]`, `cursor-grok-4.5-high`) **solo** en árbol Cursor. Claude: [`MODELS-CLAUDE.md`](MODELS-CLAUDE.md).

## Installer

```bash
cd /ruta/a/namakas-agents
chmod +x scripts/install-nakamas.sh
./scripts/install-nakamas.sh --target=all
# o uno: --target=cursor|codex|claude|antigravity
# Cursor opcional: --symlink
# Claude: regenerar SoT desde Cursor antes de copiar:
./scripts/install-nakamas.sh --target=claude --regenerate
```

Helpers:

- `scripts/lib/generate_claude_agents.py` — Cursor SoT → Claude SoT (validación incluida)
- `scripts/lib/convert_agent.py` — Codex / Antigravity / rules (no es el camino preferido Claude)
- `scripts/lib/upsert_marked_section.py`

Re-sync tras `git pull`: mismo comando.

---

## Cursor

| Artefacto | Path |
|-----------|------|
| Subagentes | `~/.cursor/agents/*.md` ← `runtime/cursor/agents/` |
| Oda rule | `~/.cursor/rules/oda.mdc` |
| Graphify / CRG / Serena | `~/.cursor/rules/nakamas-*.mdc` |
| User Rule Oda | Settings → Rules ← `ODA/INSTRUCTIONS.md` |

Invocación: Task tool / Custom Agents por `name`.

Detalle: [`SETUP-OTRA-MAC.md`](SETUP-OTRA-MAC.md).

**Nota:** en `~/.cursor/agents/` pueden existir extras locales (Editor: buggy, alvida, …) fuera de `runtime/cursor/agents/`. El installer **no** los toca ni los propaga a otras IAs.

---

## GPT Codex

| Artefacto | Path |
|-----------|------|
| Custom agents | `~/.codex/agents/<name>.toml` ← convertidos desde `runtime/cursor/agents/` |
| Oda + code-intel (markdown) | `~/.codex/nakamas-rules/*.md` |
| Instrucciones raíz (sección marcada) | `~/.codex/AGENTS.md` → bloques `<!-- NAKAMAS:BEGIN/END -->` |

### Formato

Cursor YAML frontmatter → TOML Codex:

- `name`, `description`
- `developer_instructions` = cuerpo + nota de runtime
- `readonly: true` → `sandbox_mode = "read-only"`
- `model: cursor-grok-4.5-high` → `model_reasoning_effort = "high"` (sin fijar slug Cursor)
- `composer-2.5[]` → omitido (hereda sesión)

### Cómo invocar

Custom / sub-agents Codex por el campo `name` del TOML (misma cadena Oda → capitán → tripulación). Ver [Codex subagents](https://developers.openai.com/codex/subagents).

### Limitaciones

- No hay equivalencia 1:1 de Task `model:` Cursor.
- El installer **no** sobrescribe MCP, hooks ni el resto de `AGENTS.md`.

---

## Claude Code

| Artefacto | Path |
|-----------|------|
| Subagentes + Oda | `~/.claude/agents/*.md` ← **copia** de `runtime/claude/agents/` (incluye `oda.md`) |
| Oda rule (refuerzo) | `~/.claude/rules/oda.md` — agent file es la SoT invocable |
| Graphify / CRG / Serena | `~/.claude/rules/nakamas-*.md` |
| Puntero en user CLAUDE.md | sección `<!-- NAKAMAS:BEGIN/END -->` |

### Formato (oficial)

Markdown + YAML frontmatter — [Create custom subagents](https://code.claude.com/docs/en/sub-agents):

**Required:** `name`, `description`  
**Optional:** `tools`, `disallowedTools`, `model` (`sonnet`\|`opus`\|`haiku`\|`fable`\|full ID\|`inherit`), `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color`, `initialPrompt`  
**Body** = system prompt

- Oda + capitanes decisión (Law, Edison, Lucci): `model: opus` + `effort: high`
- Especialistas: `model: sonnet`
- Capitanes / Oda: `tools: Agent(<allowlist>), Read, Grep, …`
- Verifiers read-heavy: sin `Edit`/`Write` (Chopper sí puede editar)
- **Prohibido:** `composer-2.5[]`, `cursor-grok-*` en árbol Claude
- `oda.md` es **Claude-only** (no viene de Cursor); `--regenerate` no lo pisa

Regenerar SoT Claude desde Cursor:

```bash
python3 scripts/lib/generate_claude_agents.py
python3 scripts/lib/generate_claude_agents.py --validate-only
```

### Cómo invocar

- **Oda:** `claude --agent oda` o @-mention `oda` (también Agent por `name` si otro contexto lo despacha).
- **Flota:** `Agent` con el `name` del frontmatter (ej. `trafalgar-d-water-law`). Listar `~/.claude/agents/` o reiniciar Claude Code tras el primer create del directorio.

### Limitaciones

- Coexiste con rules legacy (`tripulacion.md` / brd-*). Para **Engineering Loop Nakamas**, manda el agent `oda` (+ rule de refuerzo).
- Ver [`MODELS-CLAUDE.md`](MODELS-CLAUDE.md).

---

## Antigravity (Google)

Paths reales en esta Mac:

| Artefacto | Path |
|-----------|------|
| Rules (Oda, fleet, code-intel) | `~/.antigravity/.agent/rules/` |
| Personas (no registry nativo) | `~/.antigravity/.agent/agents/*.md` ← convertidos desde Cursor |
| Puntero global | `~/.gemini/GEMINI.md` → `<!-- NAKAMAS:BEGIN/END -->` |

### Cómo invocar (equivalente)

1. Rule `oda.md` = agente raíz.
2. Leer `~/.antigravity/.agent/agents/<name>.md`.
3. Despachar con `invoke_subagent` tipos built-in (`self` / `research`) **incluyendo** el prompt de persona.

### Limitaciones

- Sin spawn por `name` tipado Nakamas.
- No se modifican extensions ni `mcp_config.json` existentes.

---

## MCP compartidos (multi-IA)

**Meta Developer Tools** — endpoint `https://mcp.facebook.com/devtools` (doc: [Meta DevTools MCP](https://developers.facebook.com/documentation/mcp/devtools-mcp)). OAuth **por cliente**.

| Cliente | Config |
|---------|--------|
| Cursor | `~/.cursor/mcp.json` |
| Codex | `~/.codex/config.toml` / `codex mcp add …` |
| Claude Code | `claude mcp add --transport http --scope user meta-developer-tools https://mcp.facebook.com/devtools` |

El installer Nakamas **no** sobrescribe estos MCP.

---

## Checklist (esta Mac)

- [ ] `./scripts/install-nakamas.sh --target=all`
- [ ] Cursor: User Rule Oda + chat Grok High
- [ ] Codex: `ls ~/.codex/agents/*.toml \| wc -l` ≈ 23
- [ ] Claude: `ls ~/.claude/agents/*.md \| wc -l` ≈ 24 (23 flota + `oda.md`); `rg 'composer-2.5\|cursor-grok' ~/.claude/agents` → vacío
- [ ] Claude: `test -f ~/.claude/agents/oda.md` && `head ~/.claude/agents/oda.md` → `model: opus` / `effort: high`
- [ ] Claude: `head ~/.claude/agents/trafalgar-d-water-law.md` → `model: opus` / `effort: high`
- [ ] Antigravity: `~/.antigravity/.agent/agents/` + `rules/oda.md`
- [ ] Prueba mínima: pedir a Oda un Agent a Law

## Re-sync

```bash
cd /Users/randydominguez/Developer/namakas-agents
git pull origin main
./scripts/install-nakamas.sh --target=all
# Solo Claude tras cambios de prompt Cursor:
./scripts/install-nakamas.sh --target=claude --regenerate
```
