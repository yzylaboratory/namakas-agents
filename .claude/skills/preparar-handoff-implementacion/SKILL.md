---
name: preparar-handoff-implementacion
description: Empaqueta tratado, contratos y decisiones abiertas en un handoff listo para Backend, QA o DevOps. Úsala cuando la especificación deba transferirse a implementación o revisión sin reinterpretar el alcance.
metadata:
  author: yzylabs
  version: "1.0"
---

# Preparar handoff de implementación

## Propósito

Entregar un paquete autocontenido para que el siguiente agente o equipo implemente o pruebe sin depender de la conversación previa.

## Entradas

- Tratado MS/orch.
- OpenAPI y/o AsyncAPI.
- Consumo BIAN / trazabilidad (si aplica).
- Restricciones NFR, seguridad y entornos.
- Destinatario (Katakuri/X-Drake, Kalifa, Franky, etc.).

## Procedimiento

1. Identifica el destinatario y lo que necesita para empezar.
2. Lista rutas exactas de artefactos.
3. Resume en una página: propósito, límites, interfaces, eventos.
4. Adjunta checklist de implementación y de pruebas documentales.
5. Separa “listo para construir” vs “bloqueado”.
6. Incluye supuestos que el implementador no debe reinterpretar.
7. Define criterios de aceptación verificables (no vagos).
8. Indica validaciones sugeridas (lint OpenAPI, contract tests, mocks).
9. No incluyas secretos ni datos reales.

## Salida

```md
## HANDOFF_ESPECIFICACION — [Nombre]

### Destinatario
### Artefactos
- Tratado: path
- OpenAPI: path
- AsyncAPI: path
- BIAN: path / id handoff

### Listo para construir
- [...]

### Bloqueado
- [...]

### Criterios de aceptación
- [...]

### Riesgos y supuestos
- [...]

### Validación sugerida
- [...]
```

## Casos límite

- Destinatario QA → enfatiza contratos y casos negativos; menos detalle de deploy.
- Destinatario DevOps → enfatiza NFR, puertos, dependencias runtime; menos detalle de schema de negocio.
- Artefactos incompletos → handoff en estado BLOQUEADO; no digas “listo”.

## Validación

- Rutas existen o se crean en la misma entrega.
- Criterios de aceptación son verificables.
- Bloqueos visibles si faltan entradas materiales.

## Criterios de terminado

- Un tercero puede continuar sin pedir el chat completo.
- Estado listo/bloqueado explícito.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Tratado + OpenAPI coherentes | Handoff “listo” con checklist |
| Ambiguo | Tratado sin contratos | Handoff bloqueado + faltantes |
| Límite | Dos destinatarios (BE + QA) | Un handoff con secciones por rol |

## Fuentes

- Práctica contract-first: spec como fuente de verdad antes de implementar (2026-08-04).
- OpenAPI 3.1 / AsyncAPI como contratos machine-readable (2026-08-04).
