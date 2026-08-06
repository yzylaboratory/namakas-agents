# Decisión: Runtime LangChain/LangGraph + MCP RAG (PoC Brook)

Fecha: 2026-08-05  
Decisores: Luffy (misión), Katakuri (Backend), Randy  
Estado: superseded por ADR 0002  
Misión: Build LangChain/LangGraph + Supabase RAG runtime (PoC Brook) then MCP bridge for Cursor

## Contexto

Los agentes Nakamas viven como markdown + adapters Cursor (`.cursor/agents/`). No ejecutan LangChain. Se necesita un runtime que indexe el vault de Brook y exponga retrieval fiable tanto a un CLI LangGraph como a los Custom Agents vía MCP, sin duplicar lógica SQL.

## Decisión

1. Añadir paquete Python `runtime/` (3.12+, `uv`/`pyproject.toml`) con LangGraph tool-calling y LangChain `@tool`.
2. Usar Supabase `pgvector` vía `SupabaseVectorStore` + embeddings OpenAI `text-embedding-3-small` (1536).
3. PoC únicamente `brook-cronista` con tools `retrieve_memory` / `list_memory_files` / `read_memory_file`.
4. Exponer las mismas implementaciones como MCP `nakamas_retrieve` / `nakamas_list_memory` / `nakamas_read_memory`.
5. Fail-hard si faltan `SUPABASE_URL` / `SUPABASE_SERVICE_KEY` / `OPENAI_API_KEY` (sin fallbacks).
6. Obligar a Brook (adapter + skill `consultar-memoria-equipo`) a usar `nakamas_retrieve` antes de afirmar historial.

## Consecuencias

- Positivo: un solo código de retrieval para CLI y Cursor; citas con `path` en metadata; camino claro para ampliar a más agentes.
- Negativo: Randy debe aplicar SQL y proveer `.env` real antes de demo end-to-end; dependencia de OpenAI + Supabase.
- Neutral: Custom Agents Cursor y runtime conviven; orquestación multi-agente LangGraph queda fuera de v1.

## Artefactos

- `runtime/` (código + SQL + README)
- `docs/runtime-langchain-rag.md`
- `.cursor/mcp.json` (`nakamas-rag`)
- Adapter/skill Brook actualizados

## Seguimiento

Esta decisión fue reemplazada por el índice local SQLite FTS5 documentado en ADR 0002. Ya no requiere Supabase, SQL remoto ni embeddings.

- [x] Reemplazar Supabase por SQLite FTS5 local
- [x] Compartir el mismo MCP con Cursor, Codex y Claude Code
- [ ] Reiniciar los clientes y aprobar el MCP del proyecto cuando lo soliciten
