---
name: producir-handoff-seguridad
description: Empaqueta HANDOFF_SEGURIDAD con amenazas, controles, residuales y estado para Law/Robin. Úsala al cerrar una revisión de seguridad o cuando el director pida el handoff consumible.
metadata:
  author: yzylabs
  version: "1.0"
---

# Producir HANDOFF_SEGURIDAD

## Propósito

Consolidar el trabajo de seguridad técnica en el contrato Nakamas que Law y Robin pueden consumir sin reinterpretar riesgos.

## Entradas

- Salidas de `revisar-arquitectura-segura`, `modelar-amenazas`, `definir-controles-tecnicos`, `evaluar-confianza-cero` y/o `auditar-gobierno-seguridad` según la misión.
- Objetivo y alcance acordados.
- Fuentes y frameworks usados.

## Procedimiento

1. Abre `references/contrato-handoff-seguridad.md`.
2. Completa metadatos (fecha, productor, objetivo, frameworks, estado).
3. Transcribe supuestos, trust boundaries y amenazas con IDs.
4. Incluye controles solo con traza; omite o marca N/D si falta.
5. Lista residuales/excepciones con owner y caducidad sugerida.
6. Extrae requisitos contractuales mínimos para Robin (authn/authz, datos, errores/logging).
7. Asigna estado `completo` | `parcial` | `borrador` coherente con huecos.
8. Escribe el artefacto en la ruta de misión acordada (o bloque en el reporte a Law).
9. Verifica que Law pueda decidir y Robin pueda reflejar requisitos sin inventar controles.

## Salida

Bloque `## HANDOFF_SEGURIDAD` conforme al contrato.

## Casos límite

- Pedido de estado completo con amenazas sin controles → rechaza; usa `parcial`.
- Sin modelado previo → ejecuta skills previas o marca `borrador`.
- Conflicto Law vs. control crítico → documenta disenso en residuales/DECISIONS_REQUIRED.

## Validación

- Campos mínimos presentes.
- Cero controles sin traza.
- Estado coherente con pendientes.
- Sin secretos/PII reales.

## Criterios de terminado

- Handoff autocontenido entregado a `law-director-arquitectura`.
- Requisitos para Robin listados o N/A justificado.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Amenazas + controles completos del alcance | Estado completo |
| Ambiguo | Controles parciales | Estado parcial + fuera de cobertura |
| Límite | Sin amenazas ni diseño | Borrador o BLOCKED; no inventar filas |

## Fuentes

- `references/contrato-handoff-seguridad.md`
- NIST CSF 2.0 / ASVS 5.0 / NIST SP 800-207 — consultados 2026-08-04
