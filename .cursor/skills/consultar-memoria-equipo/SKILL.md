---
name: consultar-memoria-equipo
description: Busca y resume bitácoras, decisiones y ADR existentes en memoria/ para responder qué se hizo o por qué se decidió algo. Úsala antes de reabrir un debate o cuando pidan el historial del equipo.
metadata:
  author: yzylabs
  version: "1.0"
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
2. Busca en `memoria/diario/`, `memoria/decisiones/`, `memoria/adr/`, `memoria/permanente/` (grep/listado).
3. Prioriza coincidencias por fecha reciente y por título/ADR number.
4. Extrae citas cortas con ruta relativa.
5. Si hay contradicciones, preséntalas sin elegir ganador.
6. Si no hay resultados, dilo explícitamente y sugiere términos o rangos de fecha.

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

- Pregunta vaga (“¿qué pasó?”) → pedir acotación o devolver los últimos N días con índice.
- Vault vacío → “sin registros” + convención de rutas.
- Solo memoria oral en el prompt sin archivos → no fingir que está en vault; ofrece capturarla.

## Casos de evaluación

- Normal: “¿por qué solo Luffy y Vegapunk vivos?” → cita ADR/decisión si existe.
- Ambiguo: “lo de ayer” sin zona horaria → usar fecha del contexto y declararla.
- Límite: dos decisiones opuestas → tabla de conflicto.

## Validación

- Toda afirmación fuerte cita ruta o se marca como inferencia.
- No se inventan extractos.
- No se modifican archivos en esta skill (solo lectura), salvo que la misión pida capturar el hallazgo después.

## Criterios de terminado

- Pregunta respondida con evidencias o laguna explícita.
- Rutas verificables.

## Fuentes

- `references/estructura-memoria.md`
- Hábito Second Brain: buscar el vault antes de re-investigar — 2026-08-04.
