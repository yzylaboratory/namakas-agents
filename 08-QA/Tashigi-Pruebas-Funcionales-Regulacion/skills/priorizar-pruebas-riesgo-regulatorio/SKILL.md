---
name: priorizar-pruebas-riesgo-regulatorio
description: Prioriza suites y ciclos de prueba según riesgos de negocio, técnicos y regulatorios. Úsala cuando el tiempo sea limitado, haya regresión masiva o se deba justificar el orden de ejecución ante Usopp o auditoría.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar pruebas por riesgo regulatorio

## Propósito

Ordenar condiciones y casos de prueba para maximizar detección temprana de fallos de alto impacto (pérdida financiera, sanción, reputación, integridad de datos) bajo restricciones de tiempo.

## Entradas

- Inventario de casos o condiciones de prueba.
- Riesgos conocidos (negocio, técnico, regulatorio) o hipótesis de riesgo.
- Controles críticos citados (si existen).
- Ventana de tiempo / recursos del ciclo.

## Procedimiento

1. Identifica objetos de riesgo: flujos, montos, consentimientos, reportes, estados de cuenta, interfaces externas.
2. Clasifica cada ítem: impacto (Alto/Medio/Bajo) × probabilidad (Alto/Medio/Bajo) o escala acordada por Usopp.
3. Marca factores regulatorios: multa potencial, obligación de evidencia, dato sensible, reporte obligatorio.
4. Asigna prioridad de prueba P0–P3 alineada al score.
5. Define orden de ejecución y qué queda fuera del ciclo con justificación (riesgo residual aceptado explícitamente).
6. Propón mitigaciones: más casos, automatización (handoff Kuma), o bloqueo de release.
7. Entrega backlog priorizado + residual risk documentado.

## Salida

```md
## Priorización por riesgo — [Alcance]

### Método de scoring
### Backlog
| ID | Ítem | Impacto | Prob. | Regulación | Prioridad | Orden |
### Fuera de ciclo (con justificación)
### Riesgo residual
### Recomendaciones a Usopp
```

## Casos límite

- Sin datos de probabilidad → prioriza por impacto regulatorio/negocio y declara supuesto.
- Todo marcado P0 → fuerza ranking relativo; no permitas inflación de prioridad.
- Solo riesgos de performance → handoff a Kaido; no conviertas Tashigi en performance tester.

## Validación

- Cada P0 tiene justificación de impacto.
- Ítems fuera de ciclo tienen residual risk escrito.
- No se ocultan controles críticos “por tiempo” sin escalar a Usopp.

## Criterios de terminado

- Backlog ordenado entregado.
- Residual risk explícito.
- Criterio de scoring documentado.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 30 casos + 3 controles críticos | Controles críticos en P0 con orden |
| Ambiguo | Lista de casos sin riesgos | Scoring por impacto funcional + supuestos listados |
| Límite | Ventana que excluye un control crítico | Escalamiento a Usopp; no silenciar |

## Fuentes

- ISTQB CT-FT Syllabus v1.0 § Risk-Based Testing — categories, prioritization, residual risk (2026-05-27; consultado 2026-08-04).
- ISTQB CT-FT BO3 — risk-based testing according to business, technical and regulatory risks (consultado 2026-08-04).
- Referencia metodológica PRISMA citada en CT-FT (Veenendaal, 2012) como enfoque de áreas de alto riesgo (secundaria; 2026-08-04).
