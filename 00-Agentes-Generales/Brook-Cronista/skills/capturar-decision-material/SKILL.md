---
name: capturar-decision-material
description: Extrae y persiste una decisión de equipo (contexto, opción elegida, alternativas, consecuencias) en memoria/decisiones/. Úsala para veredictos materiales que no requieren un ADR completo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Capturar decisión material

## Propósito

Dejar rastro de veredictos del equipo (alcance, prioridad, naming, proceso, handoffs) sin inflar el catálogo de ADR.

## Entradas

- Enunciado de la decisión.
- Contexto breve.
- Alternativas consideradas (si existen).
- Consecuencias o implicaciones.
- Quién decidió / misión.
- Fecha.

## Procedimiento

1. Evalúa materialidad: ¿cambiaría el trabajo futuro si se olvidara? Si no, solo bitácora.
2. Si es arquitectónicamente significativa → deriva a `redactar-adr`.
3. Busca en `memoria/decisiones/` y diario por tema similar para evitar duplicados; si existe, actualiza o enlaza.
4. Crea `memoria/decisiones/YYYY-MM-DD-slug-corto.md` con:

```md
# Decisión: <título>

- Fecha:
- Estado: vigente | reemplazada | en duda
- Decisores:
- Misión:

## Contexto
## Decisión
## Alternativas
## Consecuencias
## Enlaces
```

5. Añade referencia en el diario del día.
6. Reporta ruta.

## Salida

```md
## Decisión capturada

- Ruta: ...
- Estado: ...
- ADR recomendado: sí/no
```

## Casos límite

- Solo opinión sin veredicto → no crear decisión; anotar en Abiertos.
- Decisión contradictoria con otra vigente → documentar conflicto y escalar a Luffy.
- Alternativas desconocidas → sección Alternativas = “no aportadas”.

## Casos de evaluación

- Normal: veredicto de alcance → nota + enlace diario.
- Ambiguo: “decidimos mejorar calidad” → pedir enunciado concreto.
- Límite: contradicción con decisión previa → conflicto explícito, sin borrar la anterior.

## Validación

- Archivo creado o actualizado.
- Separación Contexto / Decisión / Consecuencias.
- Diario enlazado o Abiertos justifica la omisión.

## Criterios de terminado

- Decisión recuperable por fecha y slug.
- Sin invención de alternativas no dichas.

## Fuentes

- `references/estructura-memoria.md`
- Distinción ADR vs. decisión ligera según criterio de significancia de Nygard (2011) — 2026-08-04.
