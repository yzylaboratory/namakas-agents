---
name: auditar-calidad-mapeo-bian
description: Audita un mapeo o HANDOFF_BIAN contra reglas anti-invención, versión, fuentes, MECE y coherencia con Semantic APIs. Úsala antes de marcar un handoff completo o cuando Robin/Luffy duden de la calidad del mapeo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar calidad de mapeo BIAN

## Propósito

Detectar invención, ambigüedad, solapes, obsolescencia de versión y handoffs incompletos antes de liberar a Robin.

## Entradas

- `HANDOFF_BIAN` o matrices de mapeo.
- Fuentes citadas (o su ausencia).
- Versión BIAN declarada.
- Alcance original de la misión.

## Procedimiento

1. Verifica presencia de versión BIAN y al menos una fuente primaria.
2. Por cada Service Domain: ¿hay evidencia verificable? Si no → hallazgo crítico (invención o no citado).
3. Busca nombres “genéricos” no alineados al catálogo (p. ej. inventados en español sin equivalente BIAN).
4. Comprueba MECE: solapes no justificados entre SDs del mismo handoff.
5. Contrasta operaciones listadas con Semantic API/release cuando se afirme alineación API.
6. Revisa escenarios: ¿se usaron como prescritivos para crear SDs? → hallazgo.
7. Evalúa coherencia del estado (`completo` con huecos = fallo).
8. Emite veredicto y acciones correctivas (no corrijas invención inventando otra cosa).

## Salida

```md
## Auditoría mapeo BIAN
- Veredicto: [aprobado | aprobado con observaciones | requiere corrección | rechazado]
- Versión declarada:
- Hallazgos críticos:
- Hallazgos mayores:
- Observaciones:
- Acciones requeridas antes de Robin:
```

## Casos límite

- Fuentes detrás de formulario GDPR del portal → exigir evidencia alternativa (YAML oficial, release notes) o bajar estado.
- Dos versiones mezcladas en un handoff → requiere corrección.
- Handoff vacío con estado completo → rechazado.

## Validación

- Veredicto alineado a hallazgos (no “aprobado” con críticos abiertos).
- Acciones accionables.

## Criterios de terminado

- Informe de auditoría entregado.
- Si hay críticos, handoff no se recomienda como `completo`.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Handoff V14 con URLs y sin huecos | Aprobado |
| Ambiguo | SD sin URL pero “de memoria” | Requiere corrección |
| Límite | Escenario inventó un SD | Rechazado / crítico |

## Fuentes

- Reglas del agente (`Reglas.md`)
- BIAN Service Landscape + Release Notes V14 + `bian-official/public` — consultado 2026-08-04
- Practitioner’s Guide v8.1 (límites de scenarios) — 2024-12
