---
name: evaluar-impacto-privacidad-dpia
description: Evalúa si un tratamiento requiere DPIA/PIA y produce o revisa la evaluación de impacto a derechos de titulares. Úsala ante alto riesgo, nueva tecnología, scoring, vigilancia o datos sensibles.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar impacto de privacidad (DPIA)

## Propósito

Determinar necesidad de DPIA y documentar riesgos a derechos y libertades, mitigaciones y riesgo residual — antes de iniciar o ampliar el tratamiento de alto riesgo.

## Entradas

- Descripción del tratamiento y diagrama de datos.
- Categorías de datos/titulares y volumen.
- Tecnologías (IA/ML, biometría, tracking, profiling).
- RoPA / inventario previo.
- Controles existentes (seguridad, acceso, retención).
- Jurisdicción (GDPR Art. 35 / equivalentes locales).

## Procedimiento

1. Aplica screening de alto riesgo (profiling sistemático, datos sensibles a gran escala, vigilancia, nueva tecnología, vulnerabilidad de titulares).
2. Si no hay alto riesgo plausible, documenta justificación de no-DPIA con evidencia.
3. Si hay DPIA: describe tratamiento, necesidad y proporcionalidad.
4. Identifica riesgos a titulares (discriminación, pérdida de control, daño económico, etc.).
5. Propón mitigaciones (minimización, opt-in, seudonimización, límites de retención, DPA).
6. Evalúa riesgo residual; si sigue alto e inaceptable, recomienda consulta a autoridad / bloqueo.
7. Registra roles consultados (seguridad, producto, legal) y fecha.
8. Define revisiones (cambio material del tratamiento → re-DPIA).

## Salida

```md
## Screening / necesidad DPIA
## Descripción del tratamiento
## Necesidad y proporcionalidad
## Riesgos a titulares
## Mitigaciones
## Riesgo residual y decisión
## Consulta a autoridad (sí/no/por qué)
## Revisión / triggers
## Fuentes
```

## Casos límite

- Producto ya en producción sin DPIA → DPIA retrospectiva + plan de remediación; no fingir aprobación previa.
- Solo “cumplimos ISO” sin análisis de titulares → insuficiente; exige riesgos a personas.
- Conflicto negocio vs riesgo residual alto → escala a Sengoku; no apruebes en silencio.

## Validación

- Screening explícito con criterios.
- Riesgos formulados desde el titular, no solo desde la empresa.
- Mitigaciones accionables con dueño.
- Cita GDPR Art. 35 / EDPB DPIA o marco local aplicable.

## Criterios de terminado

- Decisión (DPIA / no-DPIA / consulta autoridad) está justificada.
- Riesgo residual y dueños de mitigación quedan documentados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Credit scoring con datos financieros | DPIA completa + mitigaciones |
| Ambiguo | “Usaremos IA en el call center” | Screening + preguntas de profiling/grabación |
| Límite | Biometría en sucursales sin alternativa | DPIA + riesgo residual alto + escala Sengoku |

## Fuentes

- EDPB — DPIA topic — https://www.edpb.europa.eu/topics/accountability-and-compliance-tools/data-protection-impact-assessment_en (2026-08-04).
- GDPR Art. 35 — https://eur-lex.europa.eu/eli/reg/2016/679/oj (consultado 2026-08-04).
- WP29/EDPB Guidelines on DPIA (WP248 rev.01) — referenciadas por EDPB/DPC (consultado 2026-08-04).
