---
name: especificar-control-records
description: Especifica Control Records, Behavior Qualifiers y functional patterns de Service Domains BIAN ya mapeados. Úsala cuando necesites el artefacto operativo (CR/BQ) y operaciones asociadas con evidencia.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar Control Records

## Propósito

Documentar el Control Record y, si aplica, Behavior Qualifiers y functional pattern de cada Service Domain mapeado, como base para operaciones y handoff.

## Entradas

- Lista de Service Domains evidenciada.
- Versión BIAN.
- Acceso a release notes / Semantic API / guía de practitioners / BOM-CR si disponible.

## Procedimiento

1. Por cada Service Domain, identifica asset type y functional pattern desde fuente primaria.
2. Deriva o confirma el Control Record (combinación asset + generic artifact del functional pattern).
3. Lista Behavior Qualifiers documentados; no inventes particiones.
4. Relaciona service operations / action terms al CR y a cada BQ.
5. Separa claramente operaciones CR vs BQ (BQ requiere instancia CR padre).
6. Si la fuente no publica CR/BQ para ese SD en la versión de trabajo → marca `desconocido` / hueco.
7. Resume implicaciones para información intercambiada (alto nivel; sin inventar atributos BOM).

## Salida

```md
## Control Records
- Versión BIAN:

| Service Domain | Functional Pattern | Control Record | Behavior Qualifiers | Operaciones (CR/BQ) | Evidencia |
|---|---|---|---|---|---|

### Huecos
- ...
```

## Casos límite

- Solo Semantic API sin diagrama CR → documenta operaciones observadas; CR como `parcial/inferido` etiquetado.
- BQ mencionado en news/release pero no en YAML del SD → no inventes; cita release y marca verificación pendiente.
- SD deprecado/renombrado en V14 → usa definición de la versión de trabajo.

## Validación

- Ningún CR/BQ inventado.
- Inferencias etiquetadas.
- Operaciones ligadas a evidencia.

## Criterios de terminado

- Tabla CR usable por `alinear-apis-semanticas-bian` y `producir-handoff-bian`.
- Huecos explícitos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | SD con CR en guía/YAML | CR + BQ + ops citadas |
| Ambiguo | SD sin BOM público | Hueco / parcial etiquetado |
| Límite | Pedido de atributos BOM inventados | Rechazo; solo evidencia |

## Fuentes

- BIAN Semantic API Practitioner’s Guide v8.1 §§ Control Records, BQ, Action Terms — 2024-12.
- BIAN v14.0 Release Notes §§ Control Record Models, Behavior Qualifiers — 2026-02.
- https://github.com/bian-official/public
- `references/metamodelo-bian-operativo.md`
