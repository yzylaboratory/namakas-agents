---
name: auditar-documentacion-producto
description: Audita documentación de producto existente en busca de huecos, docs muertas, duplicación y mezcla confusa de tipos. Úsala cuando el usuario pida revisar, auditar o sanear docs/README/guías antes de reescribir en masa.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar documentación de producto

## Propósito

Evaluar el estado de la documentación orientada a humanos y producir un informe accionable priorizado, sin reescribir todo de golpe salvo que se pida.

## Entradas

- Rutas o árbol de docs a revisar.
- Audiencias esperadas.
- Fuente de verdad del producto (código, release notes, owners).
- Criterios de “buena doc” del equipo, si existen.

## Procedimiento

1. Inventaría archivos relevantes (README, guías, tutorials, explicaciones).
2. Para cada uno, clasifica tipo Diátaxis predominante y audiencia.
3. Detecta:
   - Docs muertas o claramente obsoletas.
   - Duplicación / divergencia.
   - Afirmaciones sin evidencia.
   - Mezcla confusa de tipos en un mismo flujo de lectura.
   - Falta de landing (README) o de “siguiente paso”.
4. Contrasta muestras críticas contra el producto cuando sea factible.
5. Prioriza hallazgos por riesgo al lector (engaño > hueco > estilo).
6. Recomienda el mínimo conjunto de acciones (borrar, fusionar, reescribir, enlazar).
7. No reescribas en masa dentro de esta skill salvo que la tarea lo incluya explícitamente.

## Salida

```md
## Alcance auditado

- […]

## Hallazgos

| Severidad | Archivo | Problema | Acción recomendada |
|---|---|---|---|
| alta/media/baja | … | … | … |

## Mapa de tipos (Diátaxis)

| Archivo | Tipo predominante | Notas |
|---|---|---|

## Riesgos de exactitud

- […]

## Plan mínimo recomendado

1. […]
2. […]

## Fuera de esta auditoría

- […]
```

## Casos límite

- Docs externas (Notion/Confluence) solo enlazadas: audita el puente desde el repo; no inventes el contenido remoto si no fue proveído.
- Monorepo enorme: acota por paquete o pide prioridad; declara el límite.
- Hallazgo que es contrato API: deriva a Robin; no conviertas OpenAPI en “guía amable” dentro del informe como si fuera tu entrega.
- Ningún problema grave: decláralo; no fabriques trabajo.

## Validación

- Cada hallazgo apunta a evidencia (ruta, cita breve).
- Severidades coherentes con impacto al lector.
- Acciones son concretas y priorizadas.
- No se reescribió fuera de alcance.

## Criterios de terminado

- Informe entregado con plan mínimo.
- Alcance y límites explícitos.
- Al menos una recomendación priorizada o justificación de “saludable”.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Carpeta docs/ con README roto y guía duplicada | Hallazgos alta/media + plan de fusión |
| Ambiguo | “Audita toda la documentación” en monorepo | Acotar alcance; no fingir cobertura total |
| Límite | Doc que contradice el código | Severidad alta; no “arreglar” código aquí |

## Fuentes

- Diátaxis — https://diataxis.fr/ (2026-08-04)
- Google docguide best practices (mínimo viable, borrar docs muertas, evitar duplicación) — https://github.com/google/styleguide/blob/HEAD/docguide/best_practices.md (2026-08-04)
