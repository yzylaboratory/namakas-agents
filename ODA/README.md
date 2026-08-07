# Oda — agente raíz (Custom Mode / runtime)

**Oda NO es un subagente.** Es el agente raíz / runtime principal de Nakamas Agents en Cursor.

| Qué | Dónde |
|-----|--------|
| Identidad versionada | este directorio (`ODA/`) |
| Runtime Cursor (equivalente a Custom Mode) | User Rule + `~/.cursor/rules/oda.mdc` |
| Capitanes / tripulación | `~/.cursor/agents/*.md` |

## Estado de Custom Modes en Cursor

Desde **Cursor 2.1** (nov 2025), los **Custom Modes fueron eliminados**. No hay UI ni archivo oficial (`modes.json`) para crear un mode llamado "Oda".

Equivalente operativo actual:

1. Chat en **Agent** mode (herramientas completas).
2. Instructions de Oda como **User Rule** / rule global `alwaysApply`.
3. Capitanes como **subagentes** en `~/.cursor/agents/` (Law, Luffy, Lucci, tripulación).

No crear `~/.cursor/agents/oda.md` — eso lo convertiría en subagente y rompe la cadena Usuario → Oda → Capitán.

## Archivos

| Archivo | Uso |
|---------|-----|
| `INSTRUCTIONS.md` | Prompt completo de Oda (personalidad + routing 0–4 + **Nakamas Engineering Loop**; SoT para sync) |
| `TOOLS.md` | Toggles históricos de Custom Mode + mapa a Agent actual |

## Sync runtime

Fuentes en vivo (deben reflejar la misma personalidad + config funcional + Engineering Loop + política de modelos):

1. `~/.cursor/rules/oda.mdc` (`alwaysApply`) — espejo en repo: `ODA/oda.mdc`
2. User Rule **“Oda — runtime raíz Nakamas”** (Cursor Settings → Rules; también vía MCP `cursor-app-control` / `cursor_dialog`)
3. Este repo: `ODA/INSTRUCTIONS.md`

Tras editar personalidad/comunicación/loop/modelos (tabla definitiva) aquí, sincronizar (1) y (2). No crear `~/.cursor/agents/oda.md`.

Setup en otra Mac: [`../docs/SETUP-OTRA-MAC.md`](../docs/SETUP-OTRA-MAC.md).

## Cadena de mando

```
Usuario → Oda (raíz) → Capitán → Tripulación
```

Cadena base para **misiones de tripulación** (Niveles 3–4). En Niveles 1–2 Oda puede consultar/asignar a un especialista directo (reporta a Oda). En Nivel 3–4 no salta al capitán para asignar subordinados.

**Engineering Loop (Nivel 4 entre grupos):**

```
Usuario → Oda → Law → READY_FOR_IMPLEMENTATION → Oda → Luffy → READY_FOR_VERIFICATION → Oda → Lucci → VERIFIED → DONE
```

Detalle: `INSTRUCTIONS.md` → **Routing inteligente** + **Nakamas Engineering Loop**. Capitanes: Law, Luffy, Lucci (`rob-lucci` en `~/.cursor/agents/`).
