---
name: revisar-salud-partners-qbr
description: Ejecuta o prepara revisiones de salud de partners y QBR (activación, pipeline conjunto, time-to-first-deal, fricciones, acciones). Úsala cuando toque QBR, partner health check o depurar partners inactivos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Revisar salud de partners (QBR)

## Propósito

Convertir la relación con partners en un ciclo de inspección con métricas, fricciones y acciones — no en un ritual de slides.

## Entradas

- Partner(s) prioritarios y tier.
- Métricas: pipeline conjunto, revenue sourced/influenced, onboarding completion, certificaciones, time-to-first-deal, support tickets.
- Feedback cualitativo (PAM, partner, enablement).
- Operating model / atribución vigentes.

## Procedimiento

1. Fija el periodo del review y el tier del partner.
2. Mira métricas vs targets (active status, pipeline, deals, time-to-first-deal; referencia <90 días a first deal cuando el motion lo permita).
3. Diagnostica fricción en: onboarding, messaging, deal registration, enablement, delivery, incentives.
4. Separa causas: vendor-side vs partner-side vs joint.
5. Decide disposition: Scale / Maintain / Remediate / Sunset.
6. Acuerda 3–5 acciones con dueños (Bon Clay, Mr. 3, Crocodile, partner leadership) y fechas.
7. Actualiza health score y flags para el próximo pipeline review / QBR.
8. Escala a Legal/Finanzas si hay renegociación de términos o conflicto de canal.

## Salida

```md
## Partner / periodo / tier
## Scorecard de salud
| Métrica | Actual | Target | Trend |
## Fricciones
| Área | Causa | Severidad | Owner |
## Disposition
## Acciones
| Acción | Owner | Due | Evidencia de done |
## Implicaciones para forecast / programa
## Escalaciones
```

## Casos límite

- Partner logo-only (0 pipeline tras ventana de activación): Remediate o Sunset; no “Maintain” por política.
- Datos de atribución incompletos: health provisional; pide fix CRM/Finance.
- QBR sin pipeline review previo: limita a structural health; no finjas forecast accuracy.

## Validación

- Disposition justificada con métricas o gaps explícitos.
- Acciones con owner y due date.
- No se confunde co-marketing vanity con revenue health.

## Criterios de terminado

- Health review actionable para Bon Clay / Mr. 3 / Crocodile.
- Lista Scale/Remediate/Sunset clara para Buggy y Luffy.

## Fuentes

- Forecastable — monthly joint pipeline + QBR + annual reset — https://forecastable.com/b2b-partnerships/ (2026-08-04)
- Sales Enablement Collective — partner performance monthly + quarterly reviews — https://www.salesenablementcollective.com/partner-enablement/ (2026-08-04)
- The Point Company — time-to-first-deal as partner health metric — https://thepointco.com/channel-partner-pipeline-generation-how-to-build-a-co-sell-motion-that-generates-revenue/ (2026-08-04)
