---
name: diagnosticar-salud-riesgo-onboarding
description: Diagnostica salud y riesgo de churn/abandono durante el onboarding del partner y propone playbooks de intervención. Úsala cuando un partner esté estancado, silencioso o fuera de umbral TTFV.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diagnosticar salud y riesgo en onboarding

## Propósito

Detectar temprano partners en riesgo durante los primeros 90–120 días y convertir señales en intervenciones con owner y fecha.

## Entradas

- Scorecard TTFV / hitos 30-60-90 actuales.
- Señales de engagement (portal, LMS, CRM, reuniones).
- Feedback cualitativo (pNPS, tickets, quejas).
- Contexto comercial (capacidad, competencia, cambio de sponsor).

## Procedimiento

1. Clasifica estado: on-track / watch / at-risk / critical según umbrales del programa.
2. Inventaría señales líderes fallidas (sin portal login, sin cert, sin opp a día X).
3. Separa causa probable: admin friction, enablement gap, fit comercial, capacidad partner, producto/técnico.
4. Selecciona playbook: re-engagement, office hours, co-sell assist, enablement refresh (Mr. 3), revisión de fit (Buggy).
5. Define intervención SMART (quién, qué, cuándo) y criterio de recuperación.
6. Si riesgo es estratégico o de desinversión → escala a Buggy con evidencia.
7. Entrega ficha de riesgo + plan de recuperación + métricas de salida.

## Salida

```md
## RAG / severidad
## Señales observadas (hechos)
## Hipótesis de causa (inferencias)
## Playbook de intervención
## Criterio de recuperación
## Escalamiento a Buggy / otros
```

## Casos límite

- Silencio total post-firma → playbook de “ghost partner” + decision gate a 30d.
- Opp registrada pero sin avance → co-sell / deal support, no más training genérico.
- Riesgo técnico de integración → no diagnostiques solo “engagement”; handoff Sabo.

## Validación

- Hechos vs inferencias etiquetados.
- Intervención tiene owner y fecha.
- No se recomienda “más contenido” sin evidencia de gap de enablement.
- Severidad alineada a umbrales documentados.

## Criterios de terminado

- Ficha de riesgo usable en weekly de alianzas.
- Next action claro o escalamiento explícito.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Día 45 sin opp | Watch/at-risk + playbook co-sell |
| Ambiguo | “El partner va mal” | Preguntas mínimas + hipótesis etiquetadas |
| Límite | Día 120 sin deal + sponsor cambió | Critical + gate de desinversión a Buggy |

## Fuentes

- Gainsight Channel Partner Success — https://www.gainsight.com/essential-guide/channel-partner-success/ (2026-08-04).
- Gainsight Aligning with Partners on CS — https://www.gainsight.com/blog/aligning-with-partners-on-customer-success/ (2026-08-04).
- 76nord First 90 Days (riesgo &gt;120d) — https://76nord.com/blog/20250618-partner-onboarding-90-days/ (2026-08-04).
- TechClass First 90 Days (trigger-based re-engagement) — https://www.techclass.com/resources/learning-and-development-articles/the-first-90-days-optimizing-partner-onboarding-tracks-to-accelerate-revenue (2026-08-04).
