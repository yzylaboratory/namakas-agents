---
name: producir-handoff-bian
description: Produce el artefacto HANDOFF_BIAN para Robin-Tratadista con Service Domains evidenciados, huecos, riesgos y estado. Úsala al cerrar un mapeo BIAN o cuando Robin/Luffy pidan el handoff consumible.
metadata:
  author: yzylabs
  version: "1.0"
---

# Producir HANDOFF_BIAN

## Propósito

Empaquetar el mapeo BIAN en el contrato Nakamas que Robin consume sin reinterpretar ni inventar dominios.

## Entradas

- Matrices de `mapear-service-domains` (obligatorio).
- Salidas opcionales de escenarios, CR/BQ y alineación API.
- Objetivo MS/orch/proceso.
- Versión BIAN y fuentes usadas.

## Procedimiento

1. Abre la plantilla de `references/contrato-produccion-handoff-bian.md`.
2. Completa metadatos: fecha, agente `lucci-estandarizacion-procesos-bian`, versión, fuentes, objetivo.
3. Transcribe **solo** Service Domains con evidencia; incluye justificación y operaciones/eventos conocidos.
4. Añade CR/BQ si hay evidencia; si no, omite la celda o marca N/D.
5. Incluye escenario solo con disclaimer no prescritivo (opcional).
6. Lista fuera de mapeo y riesgos (renames, cobertura parcial, acceso limitado al portal, etc.).
7. Asigna estado:
   - `completo` — cobertura del alcance sin huecos materiales.
   - `parcial` — usable pero con huecos explícitos.
   - `borrador` — exploración inicial / evidencia insuficiente.
8. Escribe el archivo en la ruta acordada por la misión (si no hay ruta, entrega el bloque en la respuesta).
9. Verifica que Robin podría ejecutar `consumir-mapeo-bian` sin preguntas de naming.

## Salida

Bloque `## HANDOFF_BIAN` conforme al contrato (ver referencia).

## Casos límite

- Alcance cambió a mitad de misión → actualiza objetivo y estado; no dejes SDs huérfanos.
- Pedido de estado `completo` con huecos → rechaza; usa `parcial`.
- Naming `HANDOFF_HOSTOS` pedido por legado → mismo contenido; productor = Lucci.

## Validación

- Campos mínimos presentes.
- Cero SD sin justificación/evidencia.
- Estado coherente con huecos.

## Criterios de terminado

- Handoff autocontenido entregado.
- Listo para `robin-tratadista`.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Mapeo V14 completo del alcance | HANDOFF estado completo |
| Ambiguo | Mapeo con 2 huecos | Estado parcial + fuera de mapeo |
| Límite | Sin SDs evidenciados | Borrador o bloqueo; no inventar filas |

## Fuentes

- Contrato producción: `references/contrato-produccion-handoff-bian.md`
- Contrato consumo Robin: `00-Agentes-Generales/Robin-Tratadista/references/contrato-handoff-bian.md`
- https://bian.org/deliverables/service-landscape/ — consultado 2026-08-04
