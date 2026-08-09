# namakas-agents

Repositorio de **versionado** de agentes Nakama (SoT para otras Mac).

## Runtime vs versionado

| Qué | Dónde |
|-----|--------|
| Ejecución Cursor | `~/.cursor/agents/` + `~/.cursor/rules/oda.mdc` + User Rule Oda |
| Versionado | este repo |

Instalar: `./scripts/install-nakamas.sh` — guía: [`docs/SETUP-OTRA-MAC.md`](docs/SETUP-OTRA-MAC.md).

## Grupos

| Carpeta | Capitán | Model (capitán) |
|---------|---------|-----------------|
| `ODA/` | Oda (raíz, no subagente) | Grok 4.5 High (chat) |
| `PLANNER/` | Law | `cursor-grok-4.5-high` |
| `IMPLEMENTER/` | Luffy | `composer-2.5[]` |
| `VERIFIER/` | Lucci | `cursor-grok-4.5-high` |

`runtime-agents/` = espejo plano de `~/.cursor/agents/`.

## Modelos (definitivos)

Ver [`docs/MODELS.md`](docs/MODELS.md) (política completa) y tablas en `docs/SETUP-OTRA-MAC.md` / `ODA/INSTRUCTIONS.md`.

**Regla:** Implementer y Verifier → solo `composer-2.5[]` o `cursor-grok-4.5-high`. Premiums (GPT / Claude / Codex) → solo Planner. Oda → Grok.

Destacados Planner: Robin `claude-sonnet-5-thinking-high`, Doflamingo `gpt-5.6-sol-high`, Beckman `gpt-5.3-codex-high`. Imp hard path: Franky/Zoro Grok. Verifier hard path: Lucci/Chopper/Stussy Grok.
