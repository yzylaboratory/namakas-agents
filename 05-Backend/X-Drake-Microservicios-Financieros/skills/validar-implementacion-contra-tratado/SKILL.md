---
name: validar-implementacion-contra-tratado
description: Audita coherencia entre implementación del MS financiero y el tratado/OpenAPI/AsyncAPI (drift, gaps, riesgos). Úsala antes de marcar COMPLETED o al recibir handoff de Robin para verificar que el código respeta el contrato.
metadata:
  author: yzylabs
  version: "1.0"
---

# Validar implementación contra tratado

## Propósito

Detectar drift entre lo especificado (tratado + contratos) y lo implementado: paths, schemas, errores, idempotencia, eventos y fuera de alcance.

## Entradas

- Tratado y OpenAPI/AsyncAPI.
- Código o diseño de implementación.
- Skills previas (idempotencia, saga, outbox) aplicadas.
- HANDOFF_BIAN/FIBO si el tratado los referencia.

## Procedimiento

1. Construye checklist: operaciones del contrato vs handlers/implementaciones.
2. Compara schemas request/response y códigos de error.
3. Verifica mutaciones: idempotencia presente y testeada.
4. Verifica side-effects: outbox/saga según diseño acordado.
5. Busca features en código no documentadas (scope creep) y docs sin código (hollow specs).
6. Si hay BIAN/FIBO en el tratado: confirma que no se inventaron nombres en código/comentarios.
7. Clasifica hallazgos: bloqueante / mayor / menor.
8. Emite veredicto: `alineado` | `parcial` | `desalineado` con evidencias.

## Salida

```md
## Veredicto
## Matriz contrato ↔ implementación
## Hallazgos (severidad)
## Riesgos (doble cobro / drift / seguridad)
## Acciones / dueños
```

## Casos límite

- Sin tratado → no inventes baseline; `BLOCKED` o valida solo contra OpenAPI existente.
- Implementación por encima del contrato “por pragmatismo” → drift mayor; exige sync con Robin.
- Tests ausentes en mutaciones financieras → hallazgo bloqueante.

## Validación

- Toda operación del alcance aparece en la matriz.
- Hallazgos bloqueantes impiden `COMPLETED`.
- Evidencia cita archivos/paths concretos.

## Criterios de terminado

- Katakuri puede aceptar o devolver con lista accionable.
- Veredicto explícito con severidades.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | OpenAPI + handlers 1:1 | Veredicto alineado |
| Ambiguo | Extra endpoint no documentado | Drift mayor + dueño Robin |
| Límite | Mutación sin idempotencia | Bloqueante |

## Fuentes

- OpenAPI 3.1 Spec — https://spec.openapis.org/oas/v3.1.0 (2026-08-04).
- Robin — auditar-coherencia-contratos / preparar-handoff-implementacion (Nakamas).
