---
name: priorizar-riesgo-pruebas
description: Identifica y prioriza riesgos de calidad y deriva el esfuerzo de prueba (RBT). Úsala cuando haya que enfocar QA por riesgo, recortar alcance de pruebas o replanificar ante nuevos defectos o plazos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Priorizar riesgo de pruebas

## Propósito

Producir un backlog de mitigación por pruebas defendible (risk-based testing), evitando cobertura uniforme o priorización por el stakeholder más ruidoso.

## Entradas

- Lista de features / journeys / APIs / NFR candidatos.
- Contexto de negocio y compliance conocido.
- Historial de defectos o incidentes (si existe).
- Capacidad del squad y fecha de release.

## Procedimiento

1. Facilita identificación de **riesgos de calidad** (qué puede fallar y a quién duele).
2. Evalúa cada riesgo: probabilidad × impacto (escala 1–5 o L/M/H documentada).
3. Clasifica mitigación: prueba profunda / muestra / monitoreo / aceptar residual.
4. Ordena ítems P0/P1/P2 de prueba; limita WIP de mitigaciones P0.
5. Asigna dueño de mitigación (Tashigi / Kalifa / Kuma / Kaido).
6. Documenta riesgos aceptados: quién acepta, hasta cuándo, trigger de reevaluación.
7. Revisa tras defectos críticos o cambio de alcance.

## Salida

```md
## Riesgos de calidad
| ID | Riesgo | Prob | Impacto | Prioridad | Mitigación | Dueño | Residual |
## Backlog de pruebas por riesgo
| P | Ítem de prueba | Riesgo cubierto | Dueño |
## Riesgos aceptados
## Preguntas abiertas
```

## Casos límite

- Dos P0 “regulatorios”: desempata por severidad real y evidencia; escala Legal si la obligación es incierta.
- Riesgo alto sin ambiente: mitiga con diseño de casos + bloqueo explícito; no finjas ejecución.
- “Todo es P0”: fuerza ranking; si no, `BLOCKED` por falta de priorización de negocio.

## Validación

- Cada P0 tiene dueño y mitigación concreta.
- Hay riesgo residual explícito o justificación de cobertura.
- No se priorizó solo por volumen de casos fáciles.

## Criterios de terminado

- Backlog RBT ordenado y reproducible.
- Aceptaciones de residual documentadas o escaladas a Luffy.
- Listo para delegar a células o emitir `DELEGATION_REQUIRED`.

## Fuentes

- ISTQB CTAL-TM v3.0 — Risk-based Testing (identification, assessment, mitigation) — https://istqb.org/certifications/certified-tester-advanced-level-test-management-ctal-tm-v3-0/ (2026-08-04)
- ISTQB Glossary — risk-based testing, product risk (2026-08-04)
