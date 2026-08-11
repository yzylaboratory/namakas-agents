# namakas-agents

Repositorio de **versionado** de agentes Nakama (SoT para otras Mac / multi-IA).

## Runtime vs versionado

| Qué | Dónde |
|-----|--------|
| Ejecución Cursor | `~/.cursor/agents/` + `~/.cursor/rules/oda.mdc` + User Rule Oda |
| Ejecución Claude | `~/.claude/agents/` + `~/.claude/rules/oda.md` |
| Versionado | este repo |

### Layout instalable (separado Cursor / Claude)

```
runtime/
  cursor/agents/*.md   # SoT Cursor (frontmatter Cursor + slugs Composer/Grok)
  claude/agents/*.md   # SoT Claude (frontmatter nativo — docs oficiales sub-agents)
runtime-agents/        # symlink → runtime/cursor/agents (compat)
```

PLANNER / IMPLEMENTER / VERIFIER / ODA siguen siendo la organización de flota y docs de dominio; las **definiciones instalables** viven en `runtime/{cursor,claude}/`.

Instalar:

```bash
./scripts/install-nakamas.sh --target=all   # cursor + codex + claude + antigravity
./scripts/install-nakamas.sh               # solo Cursor (compat)
./scripts/install-nakamas.sh --target=claude --regenerate
```

- Multi-IA: [`docs/SETUP-MULTI-IA.md`](docs/SETUP-MULTI-IA.md)
- Solo Cursor / otra Mac: [`docs/SETUP-OTRA-MAC.md`](docs/SETUP-OTRA-MAC.md)

Code intel: [`docs/CODE-INTEL.md`](docs/CODE-INTEL.md) — Graphify · code-review-graph · Serena.

## Grupos

| Carpeta | Capitán | Model Cursor (capitán) | Model Claude (capitán) |
|---------|---------|------------------------|-------------------------|
| `ODA/` | Oda (raíz, no subagente) | Grok 4.5 High (chat) | Sesión Opus (rule) |
| `PLANNER/` | Law | `cursor-grok-4.5-high` | `opus` + `effort: high` |
| `IMPLEMENTER/` | Luffy | `composer-2.5[]` | `sonnet` |
| `VERIFIER/` | Lucci | `cursor-grok-4.5-high` | `opus` + `effort: high` |

## Modelos

- Cursor: [`docs/MODELS.md`](docs/MODELS.md) — Composer default; Grok en Oda/Law/Edison/Lucci.
- Claude: [`docs/MODELS-CLAUDE.md`](docs/MODELS-CLAUDE.md) — Sonnet default; Opus+high en Law/Edison/Lucci. **Sin** slugs Cursor en el árbol Claude.
