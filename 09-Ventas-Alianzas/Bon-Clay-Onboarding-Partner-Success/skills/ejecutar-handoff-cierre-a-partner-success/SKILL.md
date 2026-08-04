---
name: ejecutar-handoff-cierre-a-partner-success
description: Ejecuta y valida el handoff estructurado desde cierre comercial / alianzas hacia partner success (success plan, stakeholders, riesgos, aceptación). Úsala al transferir un partner recién cerrado o una cuenta canal post-deal.
metadata:
  author: yzylabs
  version: "1.0"
---

# Ejecutar handoff cierre → partner success

## Propósito

Evitar el “email handoff” informal: exigir un paquete trazable con valor prometido, stakeholders, riesgos y mutual success plan aceptado antes de que Bon Clay asuma la activación.

## Entradas

- Deal / acuerdo cerrado (resumen, fecha, tier).
- Promesas comerciales y scope.
- Stakeholders vendor y partner.
- Riesgos conocidos (capacidad, competencia, gaps técnicos).
- Artefactos de enablement o técnicos disponibles.

## Procedimiento

1. Checklist de handoff obligatorio: valor/outcome esperado, timeline, contacts, pricing/tier, exclusiones, riesgos, assets.
2. Redacta o completa mutual success plan (90 días) a partir del handoff.
3. Valida aceptación bilateral (vendor PS + partner sponsor) con fecha.
4. Marca gaps: enablement (Mr. 3), técnico API (Sabo), comercial (Buggy), legal.
5. Abre tracking de hitos fase 1 (portal, kickoff, primera opp seed).
6. Si el handoff está incompleto → `REQUIRES_CORRECTION` / no asumas ownership pleno.
7. Entrega acta de handoff + estado accepted/rejected + next steps.

## Salida

```md
## Acta de handoff
## Success plan (borrador o aceptado)
## Stakeholders / RACI
## Riesgos transferidos
## Gaps + owners
## Decisión: accepted | rejected | conditional
```

## Casos límite

- Promesas fuera de producto → documenta; escala Buggy/Legal; no “absorbas” la promesa.
- Cuenta estratégica → co-ownership con Crocodile; no robes el account plan.
- Cierre sin sponsor partner → rechazo condicional hasta nominar sponsor.

## Validación

- Checklist completo o gaps explícitos.
- Aceptación (o rechazo) con fecha y nombres de rol.
- Success plan ligado al outcome de TTFV.
- No se renegocia precio en el handoff.

## Criterios de terminado

- Acta de handoff firmada/aceptada o rechazo motivado.
- Bon Clay puede iniciar activación sin ambigüedad de ownership.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Deal cerrado + contacts | Acta accepted + success plan |
| Ambiguo | “Te lo paso por chat” | Rejected/conditional + checklist faltante |
| Límite | Promesa de feature inexistente | Gap Buggy/producto + conditional accept |

## Fuentes

- Pedowitz — Align partner enablement with CS (deal→success handoff) — https://www.pedowitzgroup.com/align-partner-enablement-with-customer-success (2026-08-04).
- Gainsight Aligning with Partners on CS — https://www.gainsight.com/blog/aligning-with-partners-on-customer-success/ (2026-08-04).
- Customer Science Partner Onboarding Playbook — https://customerscience.com.au/uncategorized/partner-onboarding-playbook/ (2026-08-04).
