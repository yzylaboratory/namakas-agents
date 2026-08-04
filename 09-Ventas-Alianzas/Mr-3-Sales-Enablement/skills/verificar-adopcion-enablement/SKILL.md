---
name: verificar-adopcion-enablement
description: Diseña y ejecuta la capa de verificación de adopción (uso de playbook en deals, certificaciones, métricas leading/lagging). Úsala cuando haya que probar si el enablement se usa de verdad, no solo si existe.
metadata:
  author: yzylabs
  version: "1.0"
---

# Verificar adopción de enablement

## Propósito

Comprobar deal-by-deal (o por muestra) si reps siguieron el molde, y reportar leading/lagging metrics sin inventar ROI.

## Entradas

- Framework/playbook vigentes.
- Muestra de closed-won/lost o deals activos.
- Datos de uso de contenido / certificación (si existen).
- Hipótesis de impacto (ramp, win-rate) sin tratarlas como hechos.

## Procedimiento

1. Define la pregunta de verificación: ¿se usó el playbook/mapa en este deal?
2. Selecciona muestra (p. ej. 5 closed-lost / mes) y criterios de pass/fail.
3. Revisa evidencia: assets adjuntos, campos de metodología, coaching notes.
4. Calcula verification pass rate y adoption rate por cohort si hay datos.
5. Separa leading (uso, certificación, pass rate) vs lagging (ramp, win-rate lift).
6. Etiqueta hipótesis de impacto; no afirmes causalidad sin diseño.
7. Produce hallazgos accionables (qué etapa falla, qué asset no se usa).
8. Reporta a Buggy con dueños de corrección (contenido, coaching, managers).

## Salida

```md
## Pregunta de verificación
## Muestra y método
## Pass/fail por deal (resumen)
## Métricas leading / lagging
## Hallazgos por etapa
## Acciones y dueños
## Límites de evidencia / hipótesis
```

## Casos límite

- Sin datos de CRM → verificación cualitativa con managers; STATUS limitado.
- “Demo del LMS = adopción” → rechaza; exige uso en deals.
- Win-rate sube sin pass rate → no atribuyas a enablement automáticamente.

## Validación

- Método de muestra documentado.
- Hechos vs hipótesis etiquetados.
- Acciones tienen dueño.

## Criterios de terminado

- Buggy puede ver si el framework es papel o conducta.
- Hay al menos un ciclo de verificación ejecutado o un plan fechado con dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 5 closed-lost + playbook | Pass rate + hallazgos por etapa |
| Ambiguo | “¿Funciona el enablement?” | Plan de muestra + métricas leading |
| Límite | Solo completions LMS | Rechazo como proxy; pide evidencia de deals |

## Fuentes

- GTMonly — Layer 4 Verification — https://gtmonly.com/sales-enablement-framework/ (2026-08-04).
- Allego State of Sales Enablement Report 2025 — measurement themes (2026-08-04).
- GTMonly / industry metrics discussions on adoption vs activity (2026-08-04).
