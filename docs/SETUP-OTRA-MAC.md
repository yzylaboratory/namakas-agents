# Setup Nakamas Agents en otra Mac

Guía reproducible para instalar el runtime **Cursor** desde este repo (`namakas-agents` = SoT versionada).

Para **Codex / Claude Code / Antigravity** (misma flota, formatos nativos): [`SETUP-MULTI-IA.md`](SETUP-MULTI-IA.md) — `./scripts/install-nakamas.sh --target=all`.

## 1. Clonar o actualizar el repo

```bash
# Primera vez
git clone git@github.com:yzylaboratory/namakas-agents.git
cd namakas-agents

# Mac que ya lo tiene
cd /ruta/a/namakas-agents
git pull origin main
```

## 2. Instalar subagentes en `~/.cursor/agents/`

```bash
cd /ruta/a/namakas-agents
chmod +x scripts/install-nakamas.sh
./scripts/install-nakamas.sh          # copia
# ./scripts/install-nakamas.sh --symlink   # opcional
```

El script instala todos los `.md` de `runtime-agents/` en `~/.cursor/agents/`, `ODA/oda.mdc` en `~/.cursor/rules/oda.mdc`, y `rules/nakamas-graphify.mdc` en `~/.cursor/rules/nakamas-graphify.mdc`.

**No** crees `~/.cursor/agents/oda.md`. Oda no es subagente.

Code intel (3 capas): ver [`CODE-INTEL.md`](CODE-INTEL.md).

- Graphify (mapa): [`GRAPHIFY.md`](GRAPHIFY.md). CLI: `uv tool install graphifyy`; `graphify update .` → `graphify-out/graph.json`. MCP: `user-graphify-remote`.
- code-review-graph (Verifier / reviews): [`CODE-REVIEW-GRAPH.md`](CODE-REVIEW-GRAPH.md). CLI: `uv tool install code-review-graph`; MCP global `uvx code-review-graph serve` o install por repo con `--no-instructions`. Rule: `nakamas-code-review-graph.mdc` (`alwaysApply: false`).
- Serena (símbolos / Implementer): [`SERENA.md`](SERENA.md). Rule: `nakamas-serena.mdc` (`alwaysApply: false`).
  - **Esta Mac (Randy):** ya cableado — CLI `uv tool install -p 3.13 serena-agent`, `serena init` (LSP), entrada `serena` en `~/.cursor/mcp.json` con `start-mcp-server --context ide` (binario absoluto `~/.local/bin/serena`). Reiniciar Cursor / reload MCP si no aparece.
  - **Otra Mac:** `uv tool install -p 3.13 serena-agent && serena init`, luego merge en `~/.cursor/mcp.json`:
    ```json
    "serena": {
      "command": "serena",
      "args": ["start-mcp-server", "--context", "ide"]
    }
    ```
    Si `command: serena` no resuelve PATH en Cursor, usa `which serena` (típ. `~/.local/bin/serena`). No commitear `mcp.json` con secrets.

```bash
ls ~/.cursor/agents/*.md | wc -l   # 23+ (flota Nakamas en runtime-agents; puede haber extras locales)
rg -n '^model:' ~/.cursor/agents/*.md | sort
```

## 3. Sync rule Oda

| Superficie | Dónde |
|------------|--------|
| Rule alwaysApply | `~/.cursor/rules/oda.mdc` (script) |
| User Rule | Settings → Rules → **«Oda — runtime raíz Nakamas»** = `ODA/INSTRUCTIONS.md` |
| SoT | `ODA/INSTRUCTIONS.md` |

Chat raíz: selecciona **Grok 4.5 High** (`cursor-grok-4.5-high`) para Oda.

## 4. Modelos (default barato + escalación)

Política completa: [`MODELS.md`](MODELS.md).

**Imp/Ver:** solo `composer-2.5[]` | `cursor-grok-4.5-high`. **Planner:** Composer default; premiums solo L3+/L4 vía Law. **Oda:** Grok High (chat).

**Grok fijo:** Law, Edison, Lucci (+ Oda chat). **Composer default:** resto (Robin, Doflamingo, Beckman, Franky, Zoro, Chopper, Stussy, …).

Escalación documentada en `MODELS.md`. `composer-2.5[]` = base (no Fast) — confirma en dashboard Task.

## 5. Capitanes, especialistas y Engineering Loop

```
Usuario → Oda → Capitán → Tripulación
Law → READY_FOR_IMPLEMENTATION → Luffy → READY_FOR_VERIFICATION → Lucci → VERIFIED → DONE
```

Detalle: `ODA/INSTRUCTIONS.md` (routing 0–4 + L0–L4 + loop).

## Checklist

- [ ] `git pull`
- [ ] `./scripts/install-nakamas.sh`
- [ ] User Rule Oda = `ODA/INSTRUCTIONS.md`
- [ ] Chat Oda en Grok 4.5 High
- [ ] 22 agentes; modelos = tabla de arriba
- [ ] Prueba Task: Composer base (no Fast)
