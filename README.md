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
| `VERIFIER/` | Lucci | `claude-sonnet-5-thinking-high` |

`runtime-agents/` = espejo plano de `~/.cursor/agents/`.

## Modelos (definitivos)

Ver tabla completa en `docs/SETUP-OTRA-MAC.md` y `ODA/INSTRUCTIONS.md` → **Política de modelos**. Destacados: Franky/Zoro `gpt-5.6-sol-high`, Sanji `gpt-5.3-codex-high`, Chopper/Stussy `claude-opus-5-thinking-high`.
