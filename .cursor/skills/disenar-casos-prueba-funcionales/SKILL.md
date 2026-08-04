---
name: disenar-casos-prueba-funcionales
description: Diseña casos de prueba funcionales con técnicas black-box (equivalencia, límites, tablas de decisión, estados) a partir de requisitos y criterios de aceptación. Úsala cuando haya que especificar suites funcionales antes de ejecutar o automatizar.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar casos de prueba funcionales

## Propósito

Producir casos de prueba funcionales trazables, priorizados y técnicamente justificados para validar reglas de negocio y comportamientos del SUT.

## Entradas

- Historias / requisitos / criterios de aceptación.
- Reglas de negocio o flujos (opcionales).
- Controles regulatorios citados si afectan el comportamiento funcional (opcional).
- Alcance del release y restricciones de datos/entorno.

## Procedimiento

1. Inventaría requisitos verificables; lista huecos sin criterio de aceptación.
2. Clasifica cada regla: dato/rango, combinación de condiciones, ciclo de vida/estado, o flujo.
3. Elige técnica:
   - Partición de equivalencia → clases válidas/inválidas.
   - Valores límite → bordes de montos, plazos, contadores (incl. precisión monetaria si aplica).
   - Tabla de decisión → combinaciones de reglas de negocio.
   - Transición de estado → estados de cuenta/consentimiento/orden.
4. Redacta casos con: ID, precondiciones, pasos, datos, resultado esperado, técnica, prioridad preliminar, enlace a requisito.
5. Incluye al menos un negativo o borde por regla crítica.
6. Marca candidatos a automatización (sí/no/condicionado) sin implementar el framework.
7. Entrega suite + lista de requisitos sin cobertura.

## Salida

```md
## Suite funcional — [Alcance]

### Resumen
### Casos
| ID | Requisito | Técnica | Prioridad | Resultado esperado | Auto? |
### Datos de prueba (sintéticos)
### Huecos de requisito
### Notas de entorno
```

## Casos límite

- Criterios vagos (“debe ser seguro”) → no inventes oráculos; bloquea o pide refinamiento a Vivi/Usopp.
- Solo OpenAPI sin historias → deriva comportamiento observable; marca supuestos; ofrece handoff a Kalifa para contrato.
- Reglas mutuamente excluyentes → tabla de decisión obligatoria; no listas lineales.

## Validación

- Cada caso crítico cita requisito.
- Técnica indicada es coherente con el tipo de regla.
- No hay PII real en datos de ejemplo.

## Criterios de terminado

- Suite entregada con IDs estables.
- Huecos listados o inexistentes.
- Prioridad preliminar en todos los casos críticos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Historia con AC numéricos de límite | Casos BVA + equivalencia enlazados |
| Ambiguo | “Validar KYC correctamente” sin AC | Huecos + DELEGATION_REQUIRED/bloqueo parcial |
| Límite | Regla con 5 condiciones booleanas | Tabla de decisión, no 2 casos felices |

## Fuentes

- ISTQB CT-FT Syllabus v1.0 § Functional Testing — EP, BVA, decision tables, state transition en finanzas (2026-05-27; consultado 2026-08-04).
- ISTQB CTFL — black-box test techniques (consultado 2026-08-04).
