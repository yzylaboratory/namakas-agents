---
name: definir-estrategia-pruebas
description: Define la estrategia de pruebas de proyecto alineada al contexto y a la estrategia organizacional (objetivos, niveles/tipos, approach, alcance). Úsala cuando se pida estrategia QA, approach de testing o alinear pruebas a un release/ciclo de vida.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir estrategia de pruebas

## Propósito

Convertir objetivos de calidad y contexto de desarrollo en una estrategia de pruebas de proyecto accionable, sin confundirla con el plan táctico de una sola célula.

## Entradas

- Objetivo de negocio / release y stakeholders.
- Ciclo de vida (ágil, híbrido, secuencial) y restricciones de plazo.
- Estrategia organizacional de pruebas (si existe).
- Artefactos disponibles (historias, tratados, OpenAPI, arquitectura).
- Capacidad del squad QA.

## Procedimiento

1. Fija objetivos de prueba medibles (qué riesgo o valor se mitiga).
2. Analiza contexto: stakeholders, niveles de prueba, tipos de prueba, entornos.
3. Elige approach(es): risk-based, requirements-based, model-based, experience-based — documenta por qué.
4. Define alcance y no-alcance; lista dependencias de datos/ambientes/herramientas a nivel dirección.
5. Asigna dueños por tipo/nivel: Tashigi / Kalifa / Kuma / Kaido / fuera de QA.
6. Declara criterios de entrada/salida de alto nivel y supuestos.
7. Propón 3–6 métricas de monitoreo alineadas a los objetivos.

## Salida

```md
## Estrategia de pruebas del proyecto
- Producto / release:
- Objetivos de prueba:
- Approach:
## Niveles y tipos
| Nivel/Tipo | Dueño | Enfoque | Entrada/Salida |
## Alcance / No-alcance
## Dependencias (ambientes, datos, tools)
## Métricas
## Supuestos y riesgos de estrategia
```

## Casos límite

- Sin estrategia organizacional: documenta supuestos locales y marca deuda.
- Solo “hay que probar todo”: rechaza; exige riesgos u objetivos priorizados.
- Células stub: estrategia con dueños roster; ejecución vía `DELEGATION_REQUIRED`.

## Validación

- Objetivos son verificables.
- Hay dueño por tipo crítico del release.
- Approach justificado por contexto, no por moda.
- No se inventaron resultados de prueba.

## Criterios de terminado

- Estrategia usable por Luffy y el squad sin reinterpretar el rumbo.
- Métricas y no-alcance explícitos.
- Escalaciones de ambiente/legal/seguridad identificadas si aplican.

## Fuentes

- ISTQB CTAL-TM v3.0 — Project Test Strategy / Choosing a Test Approach — https://istqb.org/certifications/certified-tester-advanced-level-test-management-ctal-tm-v3-0/ (2026-08-04)
- ISTQB Glossary — test strategy, test approach (2026-08-04)
