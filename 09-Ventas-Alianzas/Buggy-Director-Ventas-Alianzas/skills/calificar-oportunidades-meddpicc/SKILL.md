---
name: calificar-oportunidades-meddpicc
description: Califica oportunidades B2B o co-sell con MEDDPICC (Metrics, Economic Buyer, Decision Criteria/Process, Paper Process, Pain, Champion, Competition) y produce scorecard de forecast. Úsala cuando se audite calidad de pipeline, commit o deals con partners.
metadata:
  author: yzylabs
  version: "1.0"
---

# Calificar oportunidades MEDDPICC

## Propósito

Imponer un lenguaje común de calificación para que el forecast departamental sea defendible y el co-sell no sea adivinanza.

## Entradas

- Oportunidad(es) o deal pack (notes, stakeholders, stage, amount).
- Motion: directo, co-sell o partner-led.
- Evidencia disponible (emails, mutual action plan, security/legal status) — sin secretos.

## Procedimiento

1. Identifica el motion y si hay partner en el deal (co-sell vs selling-to-partner).
2. Evalúa cada elemento MEDDPICC con evidencia / gap / next step:
   - **M**etrics — impacto cuantificado.
   - **E**conomic Buyer — autoridad de presupuesto confirmada.
   - **D**ecision Criteria — scorecard / requisitos.
   - **D**ecision Process — pasos y fechas del buying committee.
   - **P**aper Process — legal/procurement/security path.
   - **I**dentify Pain — costo de inacción.
   - **C**hampion — advocate con influencia real.
   - **C**ompetition — alternativas incl. status quo.
3. Marca score por elemento: Strong / Weak / Missing.
4. Asigna bucket de forecast: Commit / Best case / Pipeline / Disqualify.
5. Si hay partner: valida ownership (deal registration), rol del partner en cada elemento y riesgo de mensaje inconsistente.
6. Define 1–3 next steps con dueño (Crocodile / partner / Legal / SE).

## Salida

```md
## Deal
- Nombre / amount / stage / motion / partner:
## Scorecard MEDDPICC
| Elemento | Score | Evidencia | Gap | Next step | Owner |
## Forecast bucket
## Riesgos
## Recomendación (advance / hold / kill)
```

## Casos límite

- Champion sin acceso a EB: no Commit.
- Paper Process desconocido en enterprise: cap a Best case máximo.
- Partner “introduce” pero desaparece: tratar como riesgo de Competition/Champion; exigir re-engagement o kill.

## Validación

- Cada score cita evidencia o declara Missing.
- Commit solo con EB + Pain + Champion materiales (y Paper Process iniciado en enterprise).
- Partner role explícito en co-sell.

## Criterios de terminado

- Scorecard usable en pipeline review.
- Bucket de forecast justificado.
- Next steps con dueños.

## Fuentes

- MEDDIC Academy — MEDDPICC® framework — https://meddpicc.net/ y https://meddpicc.net/understanding-the-meddpicc-sales-framework/ (2026-08-04)
- MEDDICC — Partner selling / co-sell shared language — https://meddicc.com/programs/partner-selling (2026-08-04)
