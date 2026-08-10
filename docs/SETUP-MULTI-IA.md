# Setup Nakamas Agents — multi-IA (Cursor, Codex, Claude, Antigravity)

SoT versionada: este repo (`namakas-agents`). Runtime Cursor ya documentado en [`SETUP-OTRA-MAC.md`](SETUP-OTRA-MAC.md).

## Principio

- **Una flota:** solo los `.md` de `runtime-agents/` (hoy 23). No se inventan agentes.
- **Oda no es subagente** en ninguna plataforma.
- **Formato nativo** por herramienta (no copia ciega del frontmatter Cursor).
- **No se borran** configs ajenas (rules legacy, AGENTS.md previos, etc.).
- Modelos Cursor (`composer-2.5[]`, `cursor-grok-4.5-high`) **solo aplican en Cursor**. En el resto: `inherit` / sesión + hints. SoT política: [`MODELS.md`](MODELS.md).

## Installer

```bash
cd /ruta/a/namakas-agents
chmod +x scripts/install-nakamas.sh
./scripts/install-nakamas.sh --target=all
# o uno: --target=cursor|codex|claude|antigravity
# Cursor opcional: --symlink
```

Helpers: `scripts/lib/convert_agent.py`, `scripts/lib/upsert_marked_section.py`.

Re-sync tras `git pull`: mismo comando.

---

## Cursor

| Artefacto | Path |
|-----------|------|
| Subagentes | `~/.cursor/agents/*.md` |
| Oda rule | `~/.cursor/rules/oda.mdc` |
| Graphify / CRG / Serena | `~/.cursor/rules/nakamas-*.mdc` |
| User Rule Oda | Settings → Rules ← `ODA/INSTRUCTIONS.md` |

Invocación: Task tool / Custom Agents por `name`.

Detalle: [`SETUP-OTRA-MAC.md`](SETUP-OTRA-MAC.md).

**Nota:** en `~/.cursor/agents/` pueden existir extras locales (Editor: buggy, alvida, …) fuera de `runtime-agents/`. El installer **no** los toca ni los propaga a otras IAs.

---

## GPT Codex

| Artefacto | Path |
|-----------|------|
| Custom agents | `~/.codex/agents/<name>.toml` |
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

Si la UI no lista un agent: comprobar que el TOML parsea (`name`, `description`, `developer_instructions` obligatorios).

### Limitaciones

- No hay equivalencia 1:1 de Task `model:` Cursor.
- Skills preload / tools allowlist de Claude no aplican; el migrador oficial Claude→Codex documenta diferencias en `~/.codex/skills/migrate-to-codex/references/differences.md`.
- El installer **no** sobrescribe MCP, hooks ni el resto de `AGENTS.md`.

---

## Claude Code

| Artefacto | Path |
|-----------|------|
| Subagentes | `~/.claude/agents/*.md` |
| Oda | `~/.claude/rules/oda.md` |
| Graphify / CRG / Serena | `~/.claude/rules/nakamas-*.md` |
| Puntero en user CLAUDE.md | sección `<!-- NAKAMAS:BEGIN/END -->` |

### Formato

- Frontmatter Claude: `name`, `description`, `model: inherit`
- Cuerpo = persona + nota de runtime
- Se eliminan campos solo-Cursor (`is_background`, slugs `composer-*` / `cursor-*`)

### Cómo invocar

Agent / Task subagents con el `name` del frontmatter (ej. `trafalgar-d-water-law`). Docs: [Claude Code subagents](https://code.claude.com/docs/en/subagents).

Ver flota: `/agents` o listar `~/.claude/agents/`.

### Limitaciones

- Coexiste con rules legacy (`tripulacion.md` / brd-*). Para **Engineering Loop Nakamas**, manda `oda.md`.
- Sin Grok/Composer: el modelo es el de la sesión Claude (`inherit`).
- Experimental Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`) es ortogonal; no sustituye la flota Nakamas.

---

## Antigravity (Google)

Paths reales en esta Mac:

| Artefacto | Path |
|-----------|------|
| Rules (Oda, fleet, code-intel) | `~/.antigravity/.agent/rules/` |
| Personas (no registry nativo) | `~/.antigravity/.agent/agents/*.md` |
| Puntero global | `~/.gemini/GEMINI.md` → `<!-- NAKAMAS:BEGIN/END -->` |

App: `Antigravity.app` / `Antigravity IDE.app`. Datos: `~/Library/Application Support/Antigravity*`, CLI/state bajo `~/.gemini/antigravity*`.

### Cómo invocar (equivalente)

Antigravity **no** tiene custom agent types Nakamas como Cursor. Equivalente nativo:

1. Rule `oda.md` = agente raíz.
2. Leer `~/.antigravity/.agent/agents/<name>.md`.
3. Despachar con `invoke_subagent` tipos built-in (`self` / `research`) **incluyendo** el prompt de persona, o adoptar el rol en nivel 0–2.

Referencia tools: skill `using-superpowers` → `references/antigravity-tools.md`.

### Limitaciones

- Sin spawn por `name` tipado (no hay `trafalgar-d-water-law` como TypeName).
- Graphify/Serena/CRG dependen de MCP/CLI disponibles en esa sesión.
- No se modifican extensions ni `mcp_config.json` existentes.

---

## MCP compartidos (multi-IA)

**Meta Developer Tools** — endpoint `https://mcp.facebook.com/devtools` (doc: [Meta DevTools MCP](https://developers.facebook.com/documentation/mcp/devtools-mcp)). OAuth **por cliente** (Cursor / Codex / Claude no comparten sesión).

| Cliente | Config | Snippet |
|---------|--------|---------|
| Cursor | `~/.cursor/mcp.json` | `"Meta Developer Tools": { "url": "https://mcp.facebook.com/devtools", "type": "http" }` |
| Codex | `~/.codex/config.toml` | `[mcp_servers.meta_developer_tools]` + `url = "https://mcp.facebook.com/devtools"` — o `codex mcp add meta_developer_tools --url https://mcp.facebook.com/devtools` → `codex mcp login meta_developer_tools` |
| Claude Code | `~/.claude.json` → `mcpServers` | `claude mcp add --transport http --scope user meta-developer-tools https://mcp.facebook.com/devtools` → `claude mcp login meta-developer-tools` (o `/mcp` en la TUI) |

El installer Nakamas **no** sobrescribe estos MCP.

---

## Checklist (esta Mac)

- [ ] `./scripts/install-nakamas.sh --target=all`
- [ ] Cursor: User Rule Oda + chat Grok High
- [ ] Codex: `ls ~/.codex/agents/*.toml | wc -l` ≈ 23; bloque NAKAMAS en `AGENTS.md`
- [ ] Claude: `ls ~/.claude/agents/*.md | wc -l` ≈ 23; `~/.claude/rules/oda.md`
- [ ] Antigravity: `~/.antigravity/.agent/agents/` + `rules/oda.md`
- [ ] Meta DevTools MCP: Cursor + Codex + Claude (`claude mcp login meta-developer-tools` si Needs authentication)
- [ ] Prueba mínima: pedir a Oda un Task/Agent a Law con una pregunta trivial de routing

## Re-sync

```bash
cd /Users/randydominguez/Developer/namakas-agents
git pull origin main
./scripts/install-nakamas.sh --target=all
```
