# ADR 0002: Contexto local SQLite para Cursor, Codex y Claude

## Status

accepted

Fecha: 2026-08-05  
Decisor: Randy  
Reemplaza: ADR 0001

## Context

El repositorio tiene miles de líneas de reglas y definiciones de agentes. Inyectarlas completas en cada conversación consume tokens aunque la mayoría no sea relevante. La solución anterior también exigía Supabase y embeddings remotos.

## Decision

Usaremos SQLite FTS5 dentro de `.nakamas/context.sqlite3` como índice local de todos los agentes. Un único servidor MCP expondrá recuperación limitada a Cursor, Codex y Claude Code. La respuesta tendrá 1,200 tokens estimados por defecto, máximo de cuatro fragmentos recomendado y topes duros de ocho fragmentos y 4,000 tokens.

Las reglas extensas de Cursor dejan de ser `alwaysApply`; una regla compacta enseña a recuperar detalles bajo demanda. Codex y Claude reciben la misma política compacta mediante `AGENTS.md` y `CLAUDE.md`.

## Consequences

- No hay cuenta, servicio, SQL remoto, embeddings ni API key para indexar o recuperar contexto.
- El índice se reconstruye automáticamente cuando cambia el corpus y permanece fuera de Git.
- La búsqueda léxica no entiende sinónimos tan bien como embeddings; las consultas deben incluir términos del dominio.
- `OPENAI_API_KEY` queda reservado para el chat LangGraph opcional, no para MCP.
