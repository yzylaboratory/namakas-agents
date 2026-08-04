# Contrato — producción de HANDOFF_BIAN (Lucci)

Lucci **produce** este handoff. Robin lo **consume** sin inventar Service Domains.

Espejo de consumo: `00-Agentes-Generales/Robin-Tratadista/references/contrato-handoff-bian.md`.

## Plantilla obligatoria

```md
## HANDOFF_BIAN

- Fecha:
- Autor / agente: lucci-estandarizacion-procesos-bian
- Versión BIAN:
- Fuentes: (portal BIAN, release notes, Semantic API repo/path, guía)
- MS / orch / proceso objetivo:

### Service Domains
| Service Domain | Justificación (evidencia) | Operaciones / eventos relevantes | Control Record / BQ (si evidencia) |
|---|---|---|---|

### Business Scenarios / wireframes (opcional)
- Referencia BIAN o adaptación local:
- Disclaimer: ilustrativo, no prescritivo

### Fuera de mapeo
- Capacidades no cubiertas / sin evidencia:

### Riesgos
- [...]

### Estado
- [completo | parcial | borrador]
```

## Reglas de producción

1. Ninguna fila de Service Domain sin columna de justificación con fuente.
2. Si solo hay evidencia parcial → estado `parcial` o `borrador`, nunca `completo`.
3. Renames V13→V14: usa el nombre de la versión de trabajo y anota el alias previo en riesgos o justificación.
4. No rellenes operaciones “por costumbre” (Initiate/Retrieve) sin evidencia del SD o Semantic API.
5. Naming legacy `HANDOFF_HOSTOS` puede usarse como **sinónimo documental** de entrada BIAN; el productor sigue siendo Lucci Nakamas, nunca `brd-bian` / Hostos.

## Criterios de aceptación del handoff

- Robin puede copiar Service Domains tal cual.
- Versión BIAN explícita.
- Huecos listados o cobertura justificada.
- Estado coherente con la evidencia.
