---
name: redactar-postmortem-blameless
description: Redacta o facilita postmortems blameless con timeline, impacto, causas sistémicas y action items con dueño. Úsala tras incidentes, outages, consumo material de error budget o cuando se pida RCA/postmortem SRE.
metadata:
  author: yzylabs
  version: "1.0"
---

# Redactar postmortem blameless

## Propósito

Aprender de fallos sin culpar personas: documentar qué pasó, impacto en usuarios y error budget, causas sistémicas y acciones que previenen clases de incidente.

## Entradas

- Timeline del incidente (alertas, mitigações, comunicaciones).
- Impacto (usuarios, $$, budget consumido).
- Telemetría relevante (gráficas, traces, logs).
- Participantes y roles (IC, coms, etc.).
- Política de postmortem del equipo (umbral de obligatoriedad).

## Procedimiento

1. Confirma umbral: ¿hubo impacto usuario o consumo material de budget? Si no, valora learning review breve.
2. Redacta resumen ejecutivo neutral (qué, cuándo, impacto) sin nombres como “culpables”.
3. Construye timeline con hechos fechados (detección, diagnóstico, mitigación, recovery).
4. Separa trigger vs root cause sistémica (diseño, proceso, información faltante).
5. Lista qué funcionó bien y qué mejorar (detección, mitigación, coms, roles).
6. Define action items: dueño, prioridad (P0/P1), criterio de done, fecha objetivo.
7. Vincula al menos un item a prevención de la clase de fallo (no solo el síntoma).
8. Revisa lenguaje: elimina culpa; asume buena intención e información limitada en el momento.
9. Comparte borrador con stakeholders; incorpora correcciones factuales.
10. Entrega postmortem + lista de follow-ups para backlog/Franky.

## Salida

```md
## Resumen
## Impacto (usuarios, duración, error budget)
## Timeline
## Trigger vs causas sistémicas
## Qué salió bien / a mejorar
## Action items (dueño · prioridad · done)
## Apéndices (gráficas, links)
```

## Casos límite

- Culpa interpersonal en borradores → reescribe a fallas de sistema/proceso.
- Sin datos de budget → estima impacto cualitativo y marca gap de medición.
- Incidente recurrente misma clase → exige P0 estructural y escala a Franky.

## Validación

- Cero atribución de culpa personal.
- Action items con dueño y done criteria.
- Timeline con hechos, no narrativas especulativas sin etiqueta.

## Criterios de terminado

- Documento revisable por stakeholders.
- Follow-ups listos para priorización.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Outage 40m, 25% budget | Postmortem + ≥1 P0 sistémico |
| Ambiguo | “Haz un RCA del downtime” | Estructura blameless + preguntas de impacto/timeline |
| Límite | Humano desplegó mal config | Causa=falta de guardrails/validación; no “error humano” como cierre |

## Fuentes

- Google SRE Book — Service Best Practices / postmortem culture — https://sre.google/sre-book/service-best-practices/ (consultado 2026-08-04).
- Google SRE — Incident management guide — https://sre.google/resources/practices-and-processes/incident-management-guide/ (consultado 2026-08-04).
- Google SRE Workbook — Error Budget Policy (umbrales de postmortem) — https://sre.google/workbook/error-budget-policy/ (consultado 2026-08-04).
