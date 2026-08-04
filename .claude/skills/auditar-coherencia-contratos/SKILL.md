---
name: auditar-coherencia-contratos
description: Audita la coherencia entre tratado técnico, OpenAPI, AsyncAPI y mapeo BIAN. Úsala cuando haya drift sospechado, revisión documental previa a handoff, o conflicto entre artefactos de especificación.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar coherencia de contratos

## Propósito

Detectar contradicciones, huecos y ambigüedades materiales entre los artefactos documentales del MS/orch antes de declarar listo el handoff.

## Entradas

- Tratado.
- OpenAPI y/o AsyncAPI.
- Consumo/trazabilidad BIAN.
- ADRs o requisitos relacionados (opcional).

## Procedimiento

1. Inventaría artefactos y versiones/fechas.
2. Construye matriz de cobertura: capacidad → HTTP → evento → BIAN.
3. Busca contradicciones de nombres, cardinalidad, ownership y errores.
4. Detecta operaciones en OpenAPI ausentes del tratado (y viceversa).
5. Detecta eventos AsyncAPI no narrados en el tratado.
6. Verifica que todo Service Domain citado tenga origen en handoff BIAN.
7. Clasifica hallazgos: bloqueante / mayor / menor.
8. Propón corrección concreta por hallazgo (archivo + cambio).
9. Emite veredicto: APROBADO / APROBADO CON DEUDAS / RECHAZADO.

## Salida

```md
## Auditoría documental — [Nombre]

### Veredicto
### Matriz de cobertura
| Capacidad | Tratado | OpenAPI | AsyncAPI | BIAN |
### Hallazgos
| ID | Severidad | Artefactos | Problema | Corrección |
### Deudas aceptables
### Bloqueantes
```

## Casos límite

- Solo tratado, sin contratos → no apruebes “especificación completa”; indica cobertura parcial.
- BIAN citado en tratado pero no en handoff → hallazgo bloqueante (posible invención).
- Diferencias solo editoriales → severidad menor; no bloquees por estilo.

## Validación

- Cada hallazgo tiene severidad y corrección.
- Veredicto alineado a bloqueantes.
- No se “arregla” inventando BIAN.

## Criterios de terminado

- Informe entregado con veredicto.
- Bloqueantes listados o inexistentes.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Artefactos alineados | APROBADO |
| Ambiguo | OpenAPI con recurso extra no tratado | Hallazgo mayor + corrección |
| Límite | Service Domain solo en prosa del tratado | RECHAZADO / bloqueante por invención |

## Fuentes

- OpenAPI 3.1 como contrato (2026-08-04).
- AsyncAPI specification (2026-08-04).
- BIAN Service Domain discipline — Practitioner’s Guide v8.1 (2024-12).
