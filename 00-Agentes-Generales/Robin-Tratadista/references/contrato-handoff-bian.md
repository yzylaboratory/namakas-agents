# Contrato — HANDOFF_BIAN (consumo por Robin)

Robin **consume** este handoff; no lo inventa. El especialista BIAN (Lucci u otro autorizado) lo produce.

## Campos mínimos esperados

```md
## HANDOFF_BIAN

- Fecha:
- Autor / agente:
- Versión BIAN:
- Fuentes: (portal BIAN, guía, repo oficial, release)
- MS / orch objetivo:

### Service Domains
| Service Domain | Justificación | Operaciones / eventos relevantes |
|---|---|---|

### Fuera de mapeo
- Capacidades del MS no cubiertas:

### Riesgos
- [...]

### Estado
- [completo | parcial | borrador]
```

## Reglas de consumo

1. Si falta este handoff en un MS/orch bancario nuevo → BLOQUEO.
2. Solo copia Service Domains listados aquí.
3. Si el estado es `parcial` o `borrador`, propaga esa etiqueta al tratado.
4. Naming legacy `HANDOFF_HOSTOS` se trata como sinónimo de entrada BIAN **solo como documento**; el agente ejecutor sigue siendo Robin Nakamas, nunca `brd-hostos`.
