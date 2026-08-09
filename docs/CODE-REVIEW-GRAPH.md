# Code-review-graph — reviews / security (Nakamas)

SoT para **Verifier y reviews**: grafo local incremental orientado a diff, blast radius y contexto mínimo de revisión. **No** es el mapa de sistema de toda la flota.

Upstream: [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) · PyPI: `code-review-graph` · sitio: https://code-review-graph.com

## Quién lo usa (scope)

| Rol / superficie | ¿Usa CRG? |
|------------------|-----------|
| Stussy (security) | Sí |
| Rob Lucci (capitán Verifier) | Sí, en campañas de review / impacto |
| Skills `/review-security`, `/review-bugbot` | Sí (paso previo + Custom Instructions) |
| Task subagents `security-review`, `bugbot` | Sí (documentado; el prompt debe pedirlo) |
| Planner / Implementer completo | **No** |
| Oda (alwaysApply) | Solo 1 línea de routing: reviews → Lucci/Stussy + CRG |
| Graphify (`nakamas-graphify.mdc`) | Sigue alwaysApply para **todos**; CRG no lo reemplaza |

## vs Graphify / Serena

**Graphify** = mapa de sistema (toda la flota). **Serena** = símbolos LSP para implementar. **code-review-graph** = review-scoped (diff + blast radius + `context_savings`). Vista: `docs/CODE-INTEL.md`.

**code-review-graph**: Tree-sitter → grafo en `.code-review-graph/`, incremental, MCP para que un review lea solo el diff + callers/dependents/tests. No sustituye Graphify/Serena ni se reparte a Planner/Implementer.

## Install (máquina)

Python ≥ 3.10. Preferir `uv` / `uvx` o `pipx`.

```bash
# CLI en PATH (recomendado)
uv tool install code-review-graph
# o: pipx install code-review-graph
# o: pip install code-review-graph

# Opción A — MCP global (recomendado en esta Mac Nakamas)
# Entrada en ~/.cursor/mcp.json:
#   "code-review-graph": { "command": "uvx", "args": ["code-review-graph", "serve"] }
# Luego reiniciar Cursor / recargar MCP.

# Opción B — por repo (cwd fijado al proyecto)
# Desde la raíz del repo a revisar:
code-review-graph install --platform cursor --no-instructions --no-skills --no-hooks
# Escribe <repo>/.cursor/mcp.json (no toques AGENTS.md/.cursorrules: usa --no-instructions).
```

Sin instalar globalmente: `uvx --from code-review-graph code-review-graph <cmd>`.

Servidor MCP: **`code-review-graph`** (`uvx code-review-graph serve` o `code-review-graph serve`). Si no aparece en GetMcpTools, el review sigue con Graphify + lectura del diff; no inventar tools.

**Importante:** no uses `install` sin `--no-instructions` — el upstream puede inyectar instrucciones en `AGENTS.md` / `.cursorrules` del repo. Nakamas ya lleva el scope en Lucci/Stussy + `nakamas-code-review-graph.mdc`.

## Generar / actualizar el grafo (por repo)

Desde la **raíz del proyecto** bajo review:

```bash
code-review-graph build            # parse completo (primera vez)
code-review-graph update           # incremental (archivos cambiados)
code-review-graph status           # salud del grafo
code-review-graph detect-changes --brief   # impacto + panel Token Savings (read-only)
code-review-graph update --brief           # refresh cambios + mismo panel
code-review-graph watch            # opcional: auto-update
```

Artefacto local: `.code-review-graph/` (SQLite; suele ir en `.gitignore` del proyecto). No regenerar en cada turno si el grafo está fresco.

También vía MCP: `build_or_update_graph_tool`.

## MCP server y tools (reales, upstream 2.3.x)

Servidor: **`code-review-graph`** (`code-review-graph serve` / alias `mcp`).

Documentar solo tools publicados por el upstream. Clave para reviews:

| Tool | Uso en review |
|------|----------------|
| `build_or_update_graph_tool` | Crear o actualizar el grafo |
| `get_minimal_context_tool` | Contexto ultra-compacto — llamar primero |
| `detect_changes_tool` | Impacto con risk score sobre el diff |
| `get_impact_radius_tool` | Blast radius de archivos cambiados |
| `get_review_context_tool` | Contexto de review token-optimizado |
| `query_graph_tool` | Callers, callees, tests, imports, inheritance |
| `get_affected_flows_tool` | Flujos afectados por el cambio |
| `list_graph_stats_tool` | Tamaño / salud del grafo |
| `semantic_search_nodes_tool` | Búsqueda de entidades por nombre/sentido |
| `get_architecture_overview_tool` | Overview (también puede traer `context_savings`) |

Lista completa upstream (30 tools): `run_postprocess_tool`, `traverse_graph_tool`, `embed_graph_tool`, `get_docs_section_tool`, `find_large_functions_tool`, `list_flows_tool`, `get_flow_tool`, `list_communities_tool`, `get_community_tool`, `get_hub_nodes_tool`, `get_bridge_nodes_tool`, `get_knowledge_gaps_tool`, `get_surprising_connections_tool`, `get_suggested_questions_tool`, `refactor_tool`, `apply_refactor_tool`, `generate_wiki_tool`, `get_wiki_page_tool`, `list_repos_tool`, `cross_repo_search_tool`.

MCP prompts upstream: `review`, `architecture`, `debug`, `onboard`, `pre-merge`.

### Context savings (v2.3.4+)

Las respuestas de `get_impact_radius`, `get_review_context`, `detect_changes` y `get_architecture_overview` pueden incluir `context_savings` (estimación compacta: full vs graph tokens). El CLI muestra el panel **Token Savings** con `detect-changes --brief` / `update --brief`. Etiquetar como **estimado**; opcional `--verify` (tiktoken) en CLI. No inventar cifras si el campo no viene en la respuesta.

## Flujo Nakamas (review amplio)

1. Asegurar grafo: `build` / `update` o `build_or_update_graph_tool` si falta o está stale.
2. `get_minimal_context_tool` → `detect_changes_tool` / `get_review_context_tool` / `get_impact_radius_tool`.
3. `query_graph_tool` / `get_affected_flows_tool` según el hallazgo.
4. Leer solo archivos que el grafo marque. **No** grep ciego del repo entero si el grafo cubre el diff.
5. Graphify sigue válido para mapa de sistema / hubs; no mezclar responsabilidades.
6. Si el MCP no está instalado: decirlo en el consolidado y continuar con diff + Graphify; no fingir tools.

## Skills Cursor y Task subagents

- Skills: `~/.cursor/skills-cursor/review-security`, `review-bugbot` — incluyen paso CRG antes/al lanzar el subagent.
- Task enum: `security-review`, `bugbot` — al invocarlos, el prompt / Custom Instructions debe pedir consulta a `code-review-graph` (blast radius, review context) cuando el servidor esté disponible.

## Rule / install

- Rule agent-requestable: `rules/nakamas-code-review-graph.mdc` (`alwaysApply: false`).
- `scripts/install-nakamas.sh` la copia a `~/.cursor/rules/`.
- Instrucciones embebidas en agentes versionados + runtime: Stussy, Lucci.

## No hacer

- No repartir CRG a Planner/Implementer “por si acaso”.
- No poner `alwaysApply: true` global en Oda para CRG.
- No inventar nombres de tools MCP.
- No romper ni debilitar `nakamas-graphify.mdc`.
- No commitear secretos ni datos de `.code-review-graph/` con paths sensibles.
