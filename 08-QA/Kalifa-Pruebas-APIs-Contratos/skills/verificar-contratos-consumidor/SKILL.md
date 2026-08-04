---
name: verificar-contratos-consumidor
description: Diseña o verifica contratos consumer-driven (Pact u equivalente) entre consumidores y provider. Úsala cuando haya consumidores conocidos y haya que proteger interacciones reales, no solo el OpenAPI global.
metadata:
  author: yzylabs
  version: "1.0"
---

# Verificar contratos consumer-driven

## Propósito

Asegurar que el provider satisface expectativas publicadas por consumidores (Pact/CDC), con provider states y verificación reproducible — complementario al schema-first.

## Entradas

- Pacts o especificación de interacciones consumidor→provider.
- Identidad de consumidores y versión del provider.
- Provider states / handlers disponibles.
- Broker o almacenamiento de pacts (si existe).
- OpenAPI (opcional, para contraste).

## Procedimiento

1. Inventaría consumidores e interacciones en alcance.
2. Confirma que cada `given`/provider state tiene handler o fixture; si no, marca flaky risk.
3. Ejecuta o documenta `pact verify` (o equivalente) contra el provider de test.
4. Si hay Pact Broker, documenta `can-i-deploy` / publicación de verification results.
5. Clasifica fallos: expectation del consumer incorrecta vs regresión del provider.
6. Contrasta con OpenAPI: campos usados por consumer vs spec; reporta gaps sin “arreglar” inventando.
7. Recomienda gate: no deploy si verify falla para consumidores críticos.

## Salida

- Matriz consumidor × interacción × resultado.
- Logs/rutas de verificación.
- Dueños: consumer team vs provider (backend) vs Robin si el contrato canónico diverge.

## Casos límite

- Sin pacts, solo OpenAPI → no fuerces CDC; usa schema-first y documenta.
- Pact sin broker en multi-equipo → limita valor; recomienda broker o almacén versionado.
- Polymorphic / oneOf no cubierto por consumer → residual risk explícito.

## Validación

- Resultados por interacción con evidencia.
- Provider states mapeados o gap listado.
- Separación clara CDC vs schema-first en el reporte.

## Criterios de terminado

- Verificación ejecutada o diseño bloqueado con gap explícito.
- Recomendación de gate para Usopp.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Pacts + provider test | Verify matrix + pass/fail |
| Ambiguo | “Haz Pact” sin consumidores | BLOCKED: lista consumidores requeridos |
| Límite | Fail por state ausente | FAILED/REQUIRES_CORRECTION + handler faltante |

## Fuentes

- Pact documentation — https://docs.pact.io/ (2026-08-04).
- Pact Broker / can-i-deploy — https://docs.pact.io/pact_broker (2026-08-04).
- QASkills Pact vs OpenAPI (secundaria) — https://qaskills.sh/blog/api-contract-testing-microservices (2026-08-04).
