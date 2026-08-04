---
name: auditar-coherencia-arquitectura-web
description: Audita una app web existente frente a arquitectura acordada (renderizado, módulos, datos, estado, CWV). Úsala para detectar drifts y remediación priorizada; no para reescribir sin mandato.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar coherencia de arquitectura web

## Propósito

Comparar el estado real del frontend web con la arquitectura objetivo y producir drifts accionables con prioridad y dueño.

## Entradas

- Arquitectura objetivo (matriz renderizado, módulos, BFF, estado, CWV) o ausencia documentada.
- Acceso de lectura al repo / rutas.
- Métricas CWV si existen.
- Restricciones de alcance (qué no tocar).

## Procedimiento

1. Delimita alcance de auditoría (apps/paquetes/rutas).
2. Inventaría hallazgos por eje: renderizado, módulos/deps, secretos/datos, estado, CWV.
3. Clasifica severidad: bloqueante / alto / medio / bajo.
4. Propón remediación incremental (no big-bang salvo mandato).
5. Marca lo que requiere Sanji/Law/Backend/UX.
6. Lista evidencias (paths, patrones, métricas).
7. Emite veredicto: coherente / coherente con gaps / divergente.

## Salida

```md
## Alcance
## Hallazgos por eje
## Severidad y remediación
## Evidencia (paths)
## Escalaciones
## Veredicto
```

## Casos límite

- Sin arquitectura objetivo → produce baseline + “arquitectura implícita” y recomienda forjar matriz.
- Solo lectura parcial del monorepo → limita veredicto; no inventes carpetas no vistas.
- Pedido de rewrite total → escala a Sanji; entrega auditoría, no rewrite.

## Validación

- Cada hallazgo tiene evidencia (path o métrica).
- Severidades no están todas “críticas” por default.
- Remediaciones son accionables y priorizadas.

## Criterios de terminado

- Sanji puede decidir prioridad con el informe solo.
- No se declara rewrite completo sin mandato explícito.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | App con matriz previa + repo | Drifts con paths y prioridad |
| Ambiguo | “Revisa el frontend” | Alcance preguntado + auditoría acotada |
| Límite | Todo `"use client"` en pages | Hallazgos INP/JS + plan por rutas |

## Fuentes

- Next.js Rendering — https://nextjs.org/docs/app/building-your-application/rendering (2026-08-04).
- web.dev Web Vitals — https://web.dev/articles/vitals (2026-08-04).
- React Server Components — https://react.dev/reference/rsc/server-components (2026-08-04).
