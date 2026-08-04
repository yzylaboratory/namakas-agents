---
name: implementar-casos-uso-dominio-financiero
description: Implementa o especifica casos de uso de dominio financiero a partir del tratado y OpenAPI/AsyncAPI. Úsala cuando haya que traducir operaciones del contrato a comandos, estados, errores y código del microservicio.
metadata:
  author: yzylabs
  version: "1.0"
---

# Implementar casos de uso de dominio financiero

## Propósito

Materializar operaciones del contrato como casos de uso de dominio: entrada, invariantes, transiciones de estado, errores y puntos de integración — sin drift respecto al tratado.

## Entradas

- OpenAPI/AsyncAPI y tratado.
- Bounded context delimitado.
- Stack/target repo (si existe).
- Políticas de authz/scopes del contrato.

## Procedimiento

1. Inventaría operaciones mutantes vs consultas del contrato.
2. Por cada mutación: comando, precondiciones, postcondiciones, estados resultantes.
3. Alinea request/response/schemas al OpenAPI; no inventes campos “convenientes” sin actualizar contrato vía Robin.
4. Define códigos de error de dominio coherentes con el contrato.
5. Marca side-effects externos (procesador, core, fraude) y su semántica de fallo.
6. Implementa o especifica tests de aceptación por caso de uso (happy + unhappy material).
7. Registra drift detectado tratado↔código como gap para Robin o corrección.

## Salida

```md
## Casos de uso
| Op | Comando | Estados | Errores | Side-effects |
## Notas de implementación
## Tests de aceptación
## Drift / gaps
```

## Casos límite

- Contrato incompleto → implementa subset marcado `parcial` y lista paths bloqueados.
- Operación de solo lectura con side-effect oculto → rechaza; exige rediseño.
- Conflicto contrato vs invariante de dinero → escala a Katakuri/Robin; no silencies el invariante.

## Validación

- Cada mutación del alcance tiene caso de uso documentado.
- Errores y schemas trazables al OpenAPI.
- Sin campos inventados no reflejados en contrato o gap explícito.

## Criterios de terminado

- Un revisor puede probar el caso de uso contra el contrato.
- Gaps tienen dueño (Robin/Katakuri).

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | POST /holds con schema completo | Caso de uso + estados + errores + test |
| Ambiguo | “Implementa pagos” sin OpenAPI | `BLOCKED`/`DELEGATION_REQUIRED` a Robin |
| Límite | Path con side-effect no documentado | Rechazo + propuesta de cambio de contrato |

## Fuentes

- OpenAPI Specification 3.1 — https://spec.openapis.org/oas/v3.1.0 (consulta 2026-08-04).
- Robin — `especificar-openapi` / tratado MS Nakamas.
