# Code intel Nakamas — 3 capas

Mapa de herramientas de inteligencia de código. Cada capa tiene dueño y momento; no se sustituyen entre sí.

```
Graphify
  ↓  ¿Dónde está / qué depende de esto?  (mapa de sistema)
Serena
  ↓  Dame solo ClassX.methodY (+ refs)   (símbolos LSP)
Cursor / agente
  ↓  modifica únicamente eso
```

Para **reviews** (blast radius del diff), insertar **code-review-graph** en la ruta Verifier — no reemplaza Graphify ni Serena.

## Tabla

| Capa | Qué es | Cuándo | Quién | SoT |
|------|--------|--------|-------|-----|
| **Graphify** | Knowledge graph del repo (`graphify-out/`) — hubs, communities, caminos, impacto PR a nivel sistema | Antes de explorar a ciegas (cualquier misión) | Toda la flota (rule alwaysApply) | `docs/GRAPHIFY.md`, `nakamas-graphify.mdc` |
| **code-review-graph** | Grafo Tree-sitter local (`.code-review-graph/`) — diff, callers/deps/tests, blast radius, `context_savings` | Reviews / security / bugbot | Lucci, Stussy, skills `/review-security`·`/review-bugbot`, Task `security-review`·`bugbot` | `docs/CODE-REVIEW-GRAPH.md`, `nakamas-code-review-graph.mdc` |
| **Serena** | MCP + language servers — find/replace/rename por **símbolo** | Leer o editar código con mínimo contexto (esp. TS/NestJS) | Implementer (Sanji, Usopp, Zoro, Franky, Nami, Brook, Jinbe) + Luffy; Robin/Edison/Law opc. read-only; Verifier solo lectura puntual | `docs/SERENA.md`, `nakamas-serena.mdc` |

## Flujos típicos

### Implementar (Implementer)

1. Graphify → ubicar módulo / comunidad.
2. Serena → `find_symbol` / `get_symbols_overview` / `find_referencing_symbols`.
3. Editar con `replace_symbol_body` (u insert/rename) — no volcar el archivo entero si basta el símbolo.

### Review / security (Verifier)

1. code-review-graph → `detect_changes` / `get_impact_radius` / `get_review_context`.
2. Graphify si hace falta mapa de sistema.
3. Serena **read-only** solo si un finding necesita inspección simbólica puntual.

### Oda (routing)

- Mapa / exploración → Graphify (ya alwaysApply).
- Reviews → Lucci/Stussy + code-review-graph.
- Implementación que toca código → handoff a Luffy; tripulación usa Graphify→Serena→edit.

## Reglas Cursor

| Rule | alwaysApply |
|------|-------------|
| `nakamas-graphify.mdc` | `true` |
| `nakamas-code-review-graph.mdc` | `false` (requestable / agentes Verifier) |
| `nakamas-serena.mdc` | `false` (requestable / agentes Implementer) |
