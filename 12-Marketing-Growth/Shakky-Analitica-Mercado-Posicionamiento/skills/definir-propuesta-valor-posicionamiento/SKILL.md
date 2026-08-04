---
name: definir-propuesta-valor-posicionamiento
description: Construye Value Proposition Canvas y positioning statement con proof points por target. Úsala cuando se pida propuesta de valor, UVP, messaging de posicionamiento o product-market fit narrativo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir propuesta de valor y posicionamiento

## Propósito

Alinear oferta y customer profile (Strategyzer VPC) y producir un positioning statement defendible: para quién, qué necesidad, en qué categoría, con qué diferencia y por qué creerlo.

## Entradas

- Target segment priorizado.
- Jobs, pains, gains (o hipótesis a validar).
- Capacidades/producto reales (no roadmap fantasioso).
- Mapa competitivo / POD-POP (si existe).
- Evidencia: métricas, casos, certificaciones, demos.

## Procedimiento

1. Completa Customer Profile: jobs (funcionales/sociales/emocionales), pains, gains priorizados.
2. Completa Value Map: products/services, pain relievers, gain creators.
3. Evalúa fit: qué pains/gains están cubiertos vs sobrantes del producto.
4. Redacta positioning statement:
   - For [target] who [need], [brand] is the [frame of reference] that [point of difference] because [reason to believe].
5. Deriva messaging hierarchy light: beneficio headline, 3 RTB, anti-claims (qué no prometemos).
6. Lista experimentos de validación (entrevistas, landing, fake-door) sin ejecutar adopción (Carrot).
7. Marca claims que requieren legal/compliance antes de publicar.

## Salida

```md
## Target
## VPC — Customer Profile
## VPC — Value Map
## Fit / gaps
## Positioning statement
## Messaging hierarchy (light)
## Proof points
## Anti-claims
## Validación pendiente
## Riesgos
```

## Casos límite

- Producto con features sin pains relevantes → no fuerces fit; recomienda pivot de mensaje o de target.
- Múltiples targets → un statement por target; no un frankenstein.
- Sin proof → statement tentativo + `COMPLETED_WITH_LIMITATIONS`.

## Validación

- Statement nombra target, need, category, POD y RTB.
- VPC no inventa jobs sin etiquetar hipótesis.
- Anti-claims previenen overpromise.

## Criterios de terminado

- Un copywriter o Carrot/Bartolomeo puede activar sin reinterpretar el “para quién”.
- Gaps de evidencia son explícitos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Target TPP + features API | VPC + statement + 3 RTB |
| Ambiguo | “Define nuestra UVP” | Preguntas de target + 2 statements candidatos |
| Límite | Solo features técnicas | Fit gaps + rechazo de claim genérico |

## Fuentes

- Strategyzer — Value Proposition Canvas — https://www.strategyzer.com/library/the-value-proposition-canvas (2026-08-04).
- Strategyzer — Value Proposition — https://www.strategyzer.com/value-proposition (2026-08-04).
- Umbrex — Positioning statement template — https://umbrex.com/resources/frameworks/strategy-frameworks/stp-framework/ (2026-08-04).
