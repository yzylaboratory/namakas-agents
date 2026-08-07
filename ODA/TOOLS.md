# Tools — Oda (Custom Mode histórico → Agent actual)

## Hecho crítico

**Custom Modes fueron eliminados en Cursor 2.1.** No hay toggles de mode en la UI actual (Cursor 3.x).

Oda opera en **Agent** mode nativo, que ya incluye el stack completo de herramientas.

## Toggles históricos (pre-2.1) — referencia

Si algún día vuelven Custom Modes, Oda debería tener **todos** activados:

### Search
- [x] Read File
- [x] List Directory
- [x] Codebase
- [x] Grep
- [x] Search Files
- [x] Web
- [x] Fetch Rules

### Edit
- [x] Edit & Reapply
- [x] Delete File

### Run
- [x] Terminal

### MCP
- [x] MCP Servers

### Advanced (recomendado para raíz)
- [x] Auto-apply Edits — **opcional**; Oda debe preferir delegar edits a Implementer
- [ ] Auto-run sin guardrails — **no** por defecto; usar con criterio
- [x] Guardrails (allow/deny) según política del usuario
- [x] Auto-fix Errors — opcional

### Formulario del mode
- Name: `Oda`
- Icon: a elección
- Shortcut: opcional
- Custom instructions: contenido de `INSTRUCTIONS.md`

## Mapa actual (Cursor ≥ 2.1)

| Capacidad deseada | Cómo se obtiene hoy |
|-------------------|---------------------|
| Search / read repo | Agent mode |
| Edit | Agent mode (disciplina: delegar a Luffy cuando sea implementación) |
| Terminal | Agent mode |
| Skills | Agent + skills en `~/.cursor/skills*` |
| MCPs / Plugins | Config global MCP / plugins |
| Subagentes / Task | `~/.cursor/agents/` (Law, Luffy, crew) |
| Instructions persistentes de Oda | User Rule + `~/.cursor/rules/oda.mdc` |

## Fuentes

- Changelog 2.1: https://cursor.com/changelog/2-1
- Agent modes actuales: Agent / Ask / Plan / Debug
- Subagents: https://cursor.com/docs/subagents.md
