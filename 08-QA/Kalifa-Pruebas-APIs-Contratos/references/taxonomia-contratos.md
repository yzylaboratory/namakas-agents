# Referencia — Taxonomía de pruebas de contratos (Kalifa)

Consulta 2026-08-04. Sintesis para el agente; no sustituye docs oficiales.

## Modos

| Modo | Fuente de verdad | Dirección | Herramientas típicas |
|---|---|---|---|
| Schema-first | OpenAPI / AsyncAPI del provider | Implementación ↔ spec | Spectral, Schemathesis, validators |
| Consumer-driven | Expectativas del consumer (Pact) | Provider verifica pacts | Pact, Pact Broker, can-i-deploy |
| Breaking-change | Diff spec vs baseline | Compatibilidad temporal | oasdiff / openapi-diff |
| Anti-drift | Varias fuentes | Spec ↔ runtime ↔ portal ↔ pacts | Matrices de coherencia |

## Orden recomendado

1. Auditar calidad del contrato (lint + completeness).
2. Schema-first si hay OpenAPI + entorno.
3. CDC si hay consumidores/Pacts.
4. Breaking-change si hay baseline.
5. Matriz de drift.
6. Reporte a Usopp.

## Límites vs peers

- **Robin**: autoría del contrato/tratado.
- **Sabo**: producto externo / DX / portal.
- **Kuma**: automatización genérica no centrada en contratos API.
- **Kaido**: carga/rendimiento.
- **Tashigi**: funcional/regulación.
- **Usopp**: priorización y gates.

## Fuentes oficiales / primarias

- https://spec.openapis.org/oas/v3.1
- https://stoplight.io/open-source/spectral
- https://meta.stoplight.io/docs/spectral
- https://docs.pact.io/
- https://schemathesis.readthedocs.io/
- https://www.asyncapi.com/docs/reference
