---
name: sintetizar-insights-y-handoff
description: Sintetiza hallazgos de UX research en insights priorizados con evidencia y produce HANDOFF_UX_RESEARCH para Nami/Perona/Vivi. Úsala al cerrar un estudio o al consolidar notas de varias sesiones.
metadata:
  author: yzylabs
  version: "1.0"
---

# Sintetizar insights y handoff

## Propósito

Convertir evidencia cruda en decisiones accionables sin inventar certeza ni mezclar hallazgos con opiniones de diseño.

## Entradas

- Preguntas de investigación originales.
- Registros de sesión / notas / métricas autorizadas.
- Límites de muestra y método usado.
- Consumidor del handoff (Nami, Perona, Vivi, QA).

## Procedimiento

1. Relee las preguntas de investigación; ignora hallazgos fuera de alcance salvo riesgos graves.
2. Agrupa evidencia por tema (affinity): patrones ≥ outliers etiquetados.
3. Para cada insight: enunciado + evidencia (observado/dicho) + severidad/impacto + confianza.
4. Separa explícitamente **Recomendaciones** (propuestas) de **Hallazgos** (evidencia).
5. Declara límites: N, sesgo de reclutamiento, artefacto (prototipo vs prod), moderación.
6. Responde cada pregunta: respondida / parcialmente / bloqueada.
7. Redacta `HANDOFF_UX_RESEARCH` autocontenido para el consumidor.
8. Sugiere siguiente paso (retest, diseño, survey a escala, analytics) sin coordinar la misión.

## Salida

```md
## HANDOFF_UX_RESEARCH
### Decisión / preguntas
### Método y N
### Hallazgos (prioridad)
### Evidencia clave
### Recomendaciones (separadas)
### Límites y sesgos
### Riesgos / vacíos
### Artefactos
### NEXT: consumidor sugerido (Nami | Perona | Vivi | QA)
```

## Casos límite

- Un solo participante outlier dramático: no lo conviertas en “verdad”; márcalo.
- Stakeholder quiere solo quotes positivas: incluye fricciones; no censures.
- Evidencia insuficiente: `COMPLETED_WITH_LIMITATIONS` o `BLOCKED`, no relleno narrativo.

## Validación

- Cada hallazgo top tiene evidencia.
- No hay PII.
- Recomendaciones no se presentan como hechos.
- Preguntas originales están trazadas.

## Criterios de terminado

- Perona/Nami pueden actuar sin releer todas las grabaciones.
- Confianza y límites son visibles.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | 5 sesiones de onboarding | 4–8 insights priorizados + handoff |
| Ambiguo | Notas mezcladas sin preguntas | Exige reanclar a preguntas o marca incompleto |
| Límite | N=2 con pedido de “conclusión definitiva” | Limitaciones fuertes; no generaliza |

## Fuentes

- NN/g — Mixed-Methods / research synthesis practices (consultado 2026-08-04).
- ISO 9241-210 — evaluación centrada en el usuario como motor del diseño (consultado 2026-08-04).
- Contrato de reporte Nakamas: `organization/contratos/report-contract.md`.
