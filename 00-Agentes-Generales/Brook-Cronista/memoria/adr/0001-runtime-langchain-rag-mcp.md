# ADR 0001: Runtime LangChain RAG + MCP (PoC Brook)

## Status

superseded by ADR 0002

Fecha: 2026-08-05  
Decisores: Randy, Luffy, Katakuri  
Misión relacionada: rag_langchain_runtime / PoC brook-cronista

## Context

Nakamas Agents se definen en markdown y se orquestan como Custom Agents en Cursor. No hay runtime LangChain. Brook ya tiene vault en `memoria/` y skill de consulta; el historial se afirma a veces sin retrieval estructurado. Se necesita indexación vectorial + function calling, y el mismo retrieval desde Cursor vía MCP, sin inventar un segundo camino de búsqueda.

## Decision

Usaremos un runtime Python (`runtime/`) con LangGraph + LangChain tools, Supabase pgvector (`SupabaseVectorStore`, embeddings `text-embedding-3-small` 1536), PoC solo `brook-cronista`, y un MCP `nakamas-rag` que reutiliza el mismo código. Fallaremos hard sin keys. Actualizaremos adapter/skill de Brook para obligar `nakamas_retrieve` antes de afirmar historial.

## Consequences

Más fácil: citas con path, ingest reproducible, puente Cursor↔RAG sin duplicar SQL.  
Más difícil: setup Supabase/OpenAI obligatorio; schema Python (`uuid`) distinto de ejemplos JS (`bigserial`).  
Fuera de v1: multi-agente LangGraph, indexar 61 agentes, LangGraph Cloud.
