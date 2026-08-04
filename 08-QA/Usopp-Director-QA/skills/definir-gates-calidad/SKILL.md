---
name: definir-gates-calidad
description: Define entry/exit criteria y quality gates (go / no-go / go-with-risks) con evidencia mínima. Úsala cuando se pida gobernar gates de calidad, criterios de salida de fase o política de liberación desde QA.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir gates de calidad

## Propósito

Establecer puertas de calidad verificables para fases y releases, evitando aprobaciones por opinión o presión de calendario.

## Entradas

- Estrategia de pruebas y riesgos P0/P1.
- Tipos de evidencia disponibles (funcional, contrato, auto, perf).
- Política de severidad de defectos.
- Restricciones de release (fecha, mercado, regulación).

## Procedimiento

1. Lista gates del flujo (p. ej. ready-for-integration, ready-for-UAT, ready-for-prod).
2. Por gate, define **entry criteria** y **exit criteria** binarios o condicionales.
3. Exige evidencia mínima por tipo crítico del producto (no copies un template genérico ciego).
4. Define reglas de defectos: qué severidades bloquean; qué puede quedar abierta con waivers.
5. Define opción **go-with-risks**: formato de residual + aceptador de negocio (vía Luffy).
6. Publica checklist operable por el squad y por Luffy.
7. Revisa gates tras cambios de alcance o incidentes.

## Salida

```md
## Gates
| Gate | Entry | Exit | Evidencia mínima | Bloqueadores |
## Política de defectos abiertos
## Go-with-risks (plantilla)
## Waivers / excepciones
## Dueño del gate
```

## Casos límite

- Fecha fija con P0 abiertos: no-go o go-with-risks explícito; nunca “verde implícito”.
- Falta de ambiente: entry criteria falla; no inventes exit.
- Producto solo API: prioriza evidencia Kalifa + Kaido según SLO; no exijas UI inexistente.

## Validación

- Cada exit criterion es verificable con artefacto.
- Hay dueño de decisión del gate (Usopp recomienda; Luffy/negocio acepta residual de negocio).
- No hay criterios imposibles (“cero defectos” sin definición).

## Criterios de terminado

- Checklist de gates listo para usar en el release.
- Plantilla go-with-risks incluida.
- Alineado al backlog RBT del proyecto.

## Fuentes

- ISTQB CTAL-TM v3.0 — Test monitoring/control; test completion; exit criteria (business outcomes) — https://istqb.org/certifications/certified-tester-advanced-level-test-management-ctal-tm-v3-0/ (2026-08-04)
- Prácticas de release readiness / quality gates en ágil e híbrido — síntesis contrastada 2026-08-04
