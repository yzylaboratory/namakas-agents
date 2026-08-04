---
name: emitir-memo-cumplimiento
description: Redacta un memorando de cumplimiento estructurado (hechos, marco, análisis, recomendación, supuestos y fuentes) con límites explícitos. Úsala cuando pidan opinión legal/compliance de producto, alineación normativa o recomendación documentada — no como sustituto de abogado colegiado.
metadata:
  author: yzylabs
  version: "1.0"
---

# Emitir memo de cumplimiento

## Propósito

Entregar una posición clara y auditable para Luffy/producto, sin fingir representación legal formal.

## Entradas

- Pregunta concreta y jurisdicción.
- Hechos y artefactos (flujos, specs, contratos, mapa de obligaciones).
- Restricciones de tiempo y confidencialidad.
- Opiniones parciales de células (si existen).

## Procedimiento

1. Reformula la pregunta en una sola issue justiciable/operativa.
2. Lista hechos materiales vs supuestos.
3. Identifica marco aplicable (instrumentos + secciones si se conocen).
4. Analiza opciones (A/B/C) con riesgos y mitigaciones.
5. Emite recomendación principal y alternativas.
6. Añade bloque **Límites del memo**:
   - No es dictamen de abogado colegiado.
   - No autoriza filings ni firma ante regulador.
   - Vigencia ligada a hechos y fuentes a la fecha del memo.
7. Indica cuándo escalar a counsel externo / DPO / célula stub pendiente de forja.
8. Cierra con fuentes y fecha de consulta.

## Salida

```md
## Issue
## Hechos
## Supuestos
## Marco aplicable
## Análisis
## Recomendación
## Alternativas
## Residual risk
## Límites del memo
## Escalamiento recomendado
## Fuentes (con fecha)
```

## Casos límite

- Pedido de “garantízame que somos legales”: rechaza garantía; ofrece memo + residual risk.
- Hechos incompletos: memo provisional marcado; lista datos faltantes.
- Conflicto entre células: consolida y escala a Luffy si es apetito de negocio.

## Validación

- Recomendación ligada a hechos y fuentes.
- Límites del memo presentes.
- No hay citas inventadas.

## Criterios de terminado

- Memo usable por Luffy sin reinterpretar la issue.
- Escalados claros.

## Fuentes

- ISO 37301:2021 — documentación y evidencia de cumplimiento — 2026-08-04
- EDPB / GDPR — cuando el issue sea privacidad — Guidelines 4/2019 y texto GDPR — 2026-08-04
- Instrumentos OF según jurisdicción del issue (BCB, Berlin Group, CFPB, etc.) — citar los usados en el memo
