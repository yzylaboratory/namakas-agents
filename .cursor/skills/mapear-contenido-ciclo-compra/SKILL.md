---
name: mapear-contenido-ciclo-compra
description: Audita y mapea contenido comercial a personas y etapas del ciclo de compra. Úsala cuando haya caos de decks/battlecards o se pida una biblioteca usable mid-call.
metadata:
  author: yzylabs
  version: "1.0"
---

# Mapear contenido al ciclo de compra

## Propósito

Convertir carpetas desordenadas en un mapa etapa→asset con owner, frescura y uso esperado, priorizando findability sobre volumen.

## Entradas

- Inventario de assets (decks, battlecards, casos, ROI, emails).
- Etapas del deal y personas/ICP.
- Datos de uso si existen (opens, CRM attachments).
- Restricciones de branding/legal.

## Procedimiento

1. Inventaría assets existentes con owner y última actualización.
2. Clasifica por persona y etapa (discovery, demo, negociación, handoff, lost).
3. Marca stale, duplicados y claims sin evidencia.
4. Completa el mapa: etapa → contenido necesario → gap.
5. Prioriza el mínimo viable que cubra etapas críticas.
6. Define regla de archivo (>90 días sin uso o supersedido, salvo excepción).
7. Especifica dónde vive el mapa (CRM/LMS/wiki) para acceso <30s.
8. Escala prosa de producto a Vivi y claims a Legal cuando falte.

## Salida

```md
## Inventario (resumen)
## Mapa persona × etapa × asset
## Stale / duplicados / a archivar
## Gaps prioritarios
## Reglas de frescura y findability
## Dueños de actualización
## Riesgos / pendientes
```

## Casos límite

- Cero datos de uso → audita por fecha + input de top performers; etiqueta incertidumbre.
- Assets partner-only → no mezclar con sales-led sin Bon Clay.
- Marketing dump sin etapas → rechaza publicación hasta mapear.

## Validación

- Cada asset priorizado tiene persona + etapa + owner.
- Gaps de etapas críticas están listados.
- No se añade volumen sin archivar stale cuando aplique.

## Criterios de terminado

- Un rep sabe qué abrir en cada etapa sin preguntar en Slack.
- Buggy ve cobertura y huecos en una tabla.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 40 decks sin mapa | Mapa + lista stale + top gaps |
| Ambiguo | “Ordena SharePoint” | Preguntas de etapas/personas + auditoría inicial |
| Límite | Solo casos de éxito genéricos | Mapa con gaps en discovery/negociación explícitos |

## Fuentes

- GTMonly Sales Enablement Framework (content-to-stage map) — https://gtmonly.com/sales-enablement-framework/ (2026-08-04).
- MicroEstimates Sales Enablement Best Practices 2025 — https://microestimates.com/blog/sales-enablement-best-practices (2026-08-04).
- Allego State of Sales Enablement Report 2025 — content relevance (2026-08-04).
