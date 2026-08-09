# Graphify — mapa de conocimiento para Nakamas

SoT operativo para que Oda y todos los subagentes consulten el grafo del proyecto antes de explorar código a ciegas.

## Qué es

[Graphify](https://github.com/Graphify-Labs/graphify) construye un knowledge graph del repo (AST + clustering). Artefacto principal:

```
<project>/graphify-out/
├── graph.json       # queryable (MCP + CLI)
├── GRAPH_REPORT.md  # hubs, communities, freshness
├── graph.html       # viz interactiva
└── cache/           # incremental
```

El MCP Cursor `user-graphify-remote` (nombre de servidor `graphify-remote`) lee `graphify-out/graph.json` vía `project_path` = raíz absoluta del proyecto.

## Instalar CLI (una vez por máquina)

Paquete PyPI: `graphifyy`. Comando: `graphify`.

```bash
uv tool install graphifyy
# alternativa: pipx install graphifyy
# sin instalar: uvx --from graphifyy graphify <cmd>
```

## Crear / refrescar el grafo en un repo

Desde la **raíz del proyecto**:

```bash
graphify update .
# o: uvx --from graphifyy graphify update .
```

- Primera vez: crea `graphify-out/` (AST, sin LLM / sin costo de API).
- Incremental: re-extrae solo cambios; el reporte pide `graphify update .` cuando el grafo está stale vs `git rev-parse HEAD`.
- No regenerar en cada turno: reutilizar `graph.json` existente salvo stale, pedido explícito del usuario, o ausencia.

Opcional (full + semantic LLM, CI/scripts): `graphify extract .`

## Consultar (preferido: MCP)

Servidor: `user-graphify-remote`. Pasar `project_path` a la raíz del repo que contiene `graphify-out/graph.json`.

| Tool | Uso |
|------|-----|
| `graph_stats` | ¿Existe grafo? nodos/edges/communities |
| `query_graph` | Pregunta NL (`mode`: bfs\|dfs) |
| `god_nodes` | Hubs arquitectónicos |
| `get_node` / `get_neighbors` | Detalle de un concepto |
| `get_community` | Subsistema por community id |
| `shortest_path` | Camino entre dos conceptos |
| `list_prs` / `get_pr_impact` / `triage_prs` | Impacto de PRs sobre el grafo |

CLI equivalente: `graphify query "…"`, `graphify path "A" "B"`, `graphify god-nodes`, `graphify explain "X"`.

## Política Nakamas (quién crea)

1. Antes de grep masivo / exploración ciega del codebase: consultar el grafo.
2. Si falta `graphify-out/graph.json`: **el primero que lo detecte lo genera** con `graphify update .` en la raíz del proyecto. No esperar a otro grupo ni a un especialista “dueño”.
3. Preferir Fast Path (Oda Nivel 0/1, o el agente en curso). Franky/Jinbe pueden hacerlo si ya están en la misión de plataforma; no es requisito despertarlos solo para esto.
4. Capitanes: cuando el mapa del sistema importe, mencionar en handoffs si se usó el grafo (o que se acaba de crear).
5. Detalle normativo: rule `nakamas-graphify.mdc` (`~/.cursor/rules/` vía `scripts/install-nakamas.sh`).

## Capas (no confundir)

Graphify = mapa de sistema. Para blast radius de **reviews** → `docs/CODE-REVIEW-GRAPH.md`. Para leer/editar por **símbolo** → `docs/SERENA.md`. Vista conjunta: `docs/CODE-INTEL.md`.

## No hacer

- No inventar API Graphify.
- No meter tokens/secretos del MCP en docs o reglas.
- No regenerar el grafo “por si acaso” cada turno.
- No reemplazar personalidad, routing ni Engineering Loop de Oda.
- No usar Graphify como editor de símbolos (eso es Serena) ni como review-blast-radius (eso es code-review-graph).
