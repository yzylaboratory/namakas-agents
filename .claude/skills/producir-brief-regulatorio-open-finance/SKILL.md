---
name: producir-brief-regulatorio-open-finance
description: Produce el artefacto HANDOFF_REG / brief regulatorio Open Finance para Sengoku con obligaciones, gaps, riesgos y decisiones. Úsala al cerrar un análisis o cuando Sengoku/Jinbe/Luffy pidan el handoff consumible.
metadata:
  author: yzylabs
  version: "1.0"
---

# Producir brief / HANDOFF_REG Open Finance

## Propósito

Empaquetar el análisis regulatorio en el contrato Nakamas que Sengoku consume sin reinterpretar ni inventar obligaciones.

## Entradas

- Salidas de mapeo, gaps, consentimiento y/o cambio (según alcance).
- Objetivo / decisión a desbloquear.
- Jurisdicción, rol, fecha de análisis.

## Procedimiento

1. Abre `references/contrato-produccion-handoff-reg.md`.
2. Completa metadatos: fecha, agente `tsuru-regulacion-open-finance`, estado.
3. Transcribe **solo** obligaciones con fuente o hipótesis marcada.
4. Incluye brechas y consentimiento si existen; si no, indica N/D.
5. Añade resumen opcional para Jinbe etiquetado como **no dictamen**.
6. Lista decisiones requeridas para Sengoku/counsel.
7. Asigna estado `completo` | `parcial` | `borrador` coherente con huecos.
8. Escribe el archivo en la ruta acordada o entrega el bloque en el reporte.

## Salida

Bloque `## HANDOFF_REG` conforme a `references/contrato-produccion-handoff-reg.md`.

## Casos límite

- Pedido de estado `completo` con huecos → rechaza; usa `parcial`.
- Pedido de “opinión legal firmada” → handoff + DELEGATION_REQUIRED Sengoku.
- Alcance cambió a mitad → actualiza objetivo y estado.

## Validación

- Campos mínimos presentes.
- Cero obligación material sin fuente/hipótesis.
- Estado coherente con huecos.
- FAPI y estándar de datos no mezclados.

## Criterios de terminado

- Handoff autocontenido para Sengoku.
- Decisiones requeridas explícitas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Mapeo + gaps BR | HANDOFF parcial/completo coherente |
| Ambiguo | Solo borrador de mapa | Estado borrador |
| Límite | Sin fuentes primarias | No completo; exigir o bloquear |

## Fuentes

- `references/contrato-produccion-handoff-reg.md`
- Fuentes primarias citadas en el análisis (fecha en cada fila)
