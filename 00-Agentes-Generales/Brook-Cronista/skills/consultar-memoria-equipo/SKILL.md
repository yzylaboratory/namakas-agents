---
name: consultar-memoria-equipo
description: Busca y resume bitácoras, decisiones y ADR existentes en memoria/ para responder qué se hizo o por qué se decidió algo. Úsala antes de reabrir un debate o cuando pidan el historial del equipo.
metadata:
  author: yzylabs
  version: "1.1"
---

# Consultar memoria del equipo

## Propósito

Recuperar evidencia escrita del vault antes de afirmar que “no hay registro” o de repetir una discusión.

## Entradas

- Pregunta de recuperación (tema, fecha, agente, ADR, misión).
- Alcance opcional (solo diario / solo adr / todo).
- Ventana temporal opcional.

## Procedimiento

1. Normaliza palabras clave y fechas.
2. **Obligatorio:** llama al MCP `nakamas_retrieve` con `agent_id=brook-cronista` y la query (opcional `source_type=memoria`).
3. Si hace falta índice o cita literal: `nakamas_list_memory` (`subdir` = `diario` | `decisiones` | `permanente` | `adr`) y/o `nakamas_read_memory` con el `path` del retrieve.
4. Prioriza coincidencias por fecha reciente y por título/ADR number.
5. Extrae citas cortas con ruta relativa (`path` de metadata).
6. Si hay contradicciones, preséntalas sin elegir ganador.
7. Si no hay resultados, dilo explícitamente y sugiere términos o rangos de fecha.

**FORBIDDEN:** omitir `nakamas_retrieve` y “buscar solo con grep” como camino silencioso alternativo cuando el MCP `nakamas-rag` esté disponible. Si el índice local falla, reporta el error — no inventes extractos. No requiere Supabase ni API keys.

Runtime compartido: `runtime/src/nakamas_runtime/tools/brook.py` + `rag.py` (misma lógica que el CLI LangGraph).

## Salida

```md
## Respuesta

[síntesis factual]

## Evidencias

| Ruta | Fecha | Extracto |
|---|---|---|

## Lagunas

- ...
```

## Casos límite

- Pregunta vaga (“¿qué pasó?”) → pedir acotación o devolver los últimos N días con índice vía `nakamas_list_memory`.
- Vault vacío / retrieve vacío → “sin registros” + convención de rutas.
- Solo memoria oral en el prompt sin archivos → no fingir que está en vault; ofrece capturarla.
- MCP no registrado → `STATUS`/bloqueo explícito; no fingir retrieve.

## Casos de evaluación

- Normal: “¿por qué solo Luffy y Vegapunk vivos?” → cita ADR/decisión si existe (vía retrieve).
- Ambiguo: “lo de ayer” sin zona horaria → usar fecha del contexto y declararla.
- Límite: dos decisiones opuestas → tabla de conflicto.

## Validación

- Toda afirmación fuerte cita ruta o se marca como inferencia.
- No se inventan extractos.
- No se modifican archivos en esta skill (solo lectura), salvo que la misión pida capturar el hallazgo después.
- Se usó `nakamas_retrieve` antes de afirmar historial.

## Criterios de terminado

- Pregunta respondida con evidencias o laguna explícita.
- Rutas verificables.
- Evidencia de llamada MCP RAG (o bloqueo documentado).

## Fuentes

- `references/estructura-memoria.md`
- `docs/runtime-langchain-rag.md`
- Hábito Second Brain: buscar el vault antes de re-investigar — 2026-08-04.
- Runtime RAG + MCP — 2026-08-05.
