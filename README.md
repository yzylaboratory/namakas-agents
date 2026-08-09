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

## Modelos (default barato + escalación)

Ver [`docs/MODELS.md`](docs/MODELS.md) (SoT). Resumen: Composer por defecto; Grok fijo en Oda chat + Law/Edison/Lucci; premiums Planner y Grok en Franky/Zoro/Chopper/Stussy solo vía escalación L3+/alta complejidad.
