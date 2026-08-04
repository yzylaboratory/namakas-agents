---
name: consolidar-second-brain-record
description: Normaliza uno o más bloques SECOND_BRAIN_RECORD a bitácora diaria y, si aplica, a notas de decisión o ADR. Úsala al cierre de un turno cuando trabajadores o Luffy aporten ese bloque.
metadata:
  author: yzylabs
  version: "1.0"
---

# Consolidar SECOND_BRAIN_RECORD

## Propósito

Convertir bloques de cierre de turno en memoria durable sin depender de Olvia ni `brd-second-brain`.

## Entradas

- Uno o más bloques `SECOND_BRAIN_RECORD` (ver `references/formato-second-brain-record.md`).
- Fecha del turno.
- Contexto mínimo de la misión.

## Procedimiento

1. Extrae campos: quién pidió, qué se hizo, agentes, archivos, decisiones, aprendizajes, abiertos.
2. Descarta ruido listado en “No registrar” y cualquier secreto (redactar).
3. Escribe o amplía `memoria/diario/YYYY-MM-DD.md` con una sección por bloque/misión.
4. Si hay decisión material, crea o actualiza `memoria/decisiones/YYYY-MM-DD-slug.md`.
5. Si la decisión es arquitectónicamente significativa, invoca el flujo de `redactar-adr` (o déjalo encolado en Abiertos si faltan Context/Decision/Consequences).
6. Reporta rutas creadas/actualizadas y campos faltantes.

## Salida

```md
## Consolidación

| Origen | Diario | Decisión/ADR | Notas |
|---|---|---|---|

## Abiertos

- ...
```

## Casos límite

- Bloque incompleto → registra lo disponible; lista faltantes; no inventes.
- Varios bloques del mismo día → una sección por bloque.
- Bloque que solo dice “ok” → omite o marca como no material.

## Casos de evaluación

- Normal: bloque completo → diario + decisión si aplica.
- Ambiguo: “archivos tocados: varios” sin rutas → Abiertos pide rutas.
- Límite: decisión arquitectónica sin consecuencias → ADR proposed incompleto o encolar.

## Validación

- Diario actualizado o justificación de omisión.
- Ningún `brd-*` mencionado como ejecutor.
- Secretos redactados.

## Criterios de terminado

- Cada bloque material tiene rastro en diario.
- Decisiones materiales tienen nota o ADR o están en Abiertos con motivo.

## Fuentes

- `references/formato-second-brain-record.md`
- `.cursor/rules/nakamas-live-agents-only.mdc` — Second Brain Nakamas ≠ Olvia.
