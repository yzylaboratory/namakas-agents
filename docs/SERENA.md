# Serena — edición / lectura por símbolo (Nakamas)

SoT para que agentes que **tocan código** usen [Serena](https://github.com/oraios/serena) (MCP + language servers) y lean/editen **símbolos** (funciones, clases, referencias) en lugar de archivos enteros.

Docs oficiales: https://oraios.github.io/serena/ · Tools: https://oraios.github.io/serena/01-about/035_tools.html

## Quién lo usa (scope)

| Rol | Uso |
|-----|-----|
| Implementer: Sanji, Usopp, Zoro, Franky, Nami, Brook, Jinbe | Principal — lectura + edición simbólica |
| Luffy | Nota corta: pedir a la tripulación Graphify→Serena→edit mínimo |
| Robin / Edison (y Law si analiza código) | Opcional, **read-only** / búsqueda de símbolos |
| Verifier (Lucci, Stussy, etc.) | Opcional **solo lectura** de símbolos si ayuda a un finding; **code-review-graph** sigue siendo el primario en reviews |
| Planner discovery genérico / chats triviales | **No** forzar Serena |
| Iceburg | Menos habitual (OpenSpec); no cablear como default |

No `alwaysApply` agresivo: rule requestable + párrafos en agentes. SoT de capas: `docs/CODE-INTEL.md`.

## Pipeline (con Graphify)

```
Graphify          →  ¿dónde está / qué depende?
Serena            →  dame solo ClassX.methodY (+ refs)
Cursor / agente   →  modifica únicamente ese símbolo
```

1. Orientación de sistema: Graphify (`docs/GRAPHIFY.md`).
2. Símbolo preciso: Serena (`find_symbol`, `get_symbols_overview`, `find_referencing_symbols`, …).
3. Edit mínimo: `replace_symbol_body` / `insert_after_symbol` / `insert_before_symbol` / `rename_symbol` / `safe_delete_symbol`.

Reviews / blast radius del diff → **code-review-graph**, no Serena. Ver `docs/CODE-REVIEW-GRAPH.md`.

## Install (máquina)

Requisito: [uv](https://docs.astral.sh/uv/). No instales Serena desde marketplaces MCP desactualizados (aviso upstream).

```bash
uv tool install -p 3.13 serena-agent
serena init                          # backend language servers (default)
# serena init -b JetBrains           # solo si usas el plugin JetBrains
uv tool upgrade serena-agent         # actualizar
```

Tras el install, el comando `serena` debe estar en PATH. Indexar un proyecto grande (recomendado upstream):

```bash
cd /ruta/al/proyecto
serena project index                 # si el CLI lo expone en tu versión; si no, seguir onboarding vía MCP
```

## MCP en Cursor

Servidor típico: **`serena`**. En IDEs (Cursor, etc.) usar contexto **`ide`** para reducir duplicación de tools con el cliente.

Entrada en `~/.cursor/mcp.json` (global) o `<repo>/.cursor/mcp.json`:

```json
"serena": {
  "command": "serena",
  "args": [
    "start-mcp-server",
    "--context", "ide"
  ]
}
```

- Config **global**: al inicio de sesión, activar proyecto con `activate_project` (o pedir “Activate the current dir as project using serena”).
- Config **por workspace**: preferible `--project <abs-path>` o `--project-from-cwd` si tu versión de Serena lo soporta.
- Si el cliente no encuentra `serena` en PATH, usa la ruta absoluta del binario (`which serena`).
- Reiniciar Cursor / recargar MCP tras añadir la entrada.

Si el MCP **no** está instalado: no inventar tools; leer/editar con acotación manual y mencionarlo en el consolidado.

## Tools clave (reales, docs upstream)

Solo documentar tools publicados. En la mayoría de configs solo un subconjunto está activo.

### Símbolos (LSP — núcleo Nakamas)

| Tool | Uso |
|------|-----|
| `find_symbol` | Búsqueda global/local de símbolo |
| `get_symbols_overview` | Outline de símbolos top-level de un archivo |
| `find_referencing_symbols` | Quién referencia el símbolo |
| `find_declaration` | Declaración/definición |
| `find_implementations` | Implementaciones (según language server) |
| `replace_symbol_body` | Reemplazar definición completa del símbolo |
| `insert_after_symbol` / `insert_before_symbol` | Insertar alrededor del símbolo |
| `rename_symbol` | Rename vía language server |
| `safe_delete_symbol` | Borrado seguro |
| `get_diagnostics_for_file` | Diagnósticos por archivo |
| `get_diagnostics_for_symbol` | (opcional) diagnósticos por símbolo |
| `restart_language_server` | (opcional) reiniciar LS |

### Proyecto / workflow

| Tool | Uso |
|------|-----|
| `activate_project` | Activar proyecto (configs MCP globales) |
| `get_current_config` | Config / tools / modos activos |
| `initial_instructions` | Manual de uso Serena si el cliente no lo inyectó |
| `onboarding` | Estructura del proyecto / tareas esenciales |

### Archivo / shell (suelen solaparse con Cursor — contexto `ide` los reduce)

`read_file`, `create_text_file`, `list_dir`, `find_file`, `search_for_pattern`, `replace_content`, `replace_in_files`, `execute_shell_command`, memories (`write_memory`, `read_memory`, …). Preferir **symbol_tools** sobre abrir archivos completos.

Tools JetBrains (`jet_brains_*`) solo si el backend es JetBrains — no asumirlos con LSP default.

## TypeScript / NestJS

- TypeScript está en el soporte LSP de Serena; NestJS = TS + decoradores/módulos — trabajar por **clase / método / provider**, no por carpeta entera.
- Flujo típico Sanji: Graphify → módulo/capa → `find_symbol` (`OrdersService.create`) → `find_referencing_symbols` → `replace_symbol_body` en el método → tests.
- Si el language server no indexó aún: esperar / `restart_language_server` / re-activar proyecto; no volcar el monorepo al contexto.
- Dependencias externas: `find_declaration` en deps puede fallar (limitación upstream).

## Rule / install Nakamas

- Rule requestable: `rules/nakamas-serena.mdc` (`alwaysApply: false`).
- `scripts/install-nakamas.sh` la copia a `~/.cursor/rules/`.
- Instrucciones en agentes Implementer + nota en Luffy / Lucci / Robin / Edison / Law.

## No hacer

- No inventar nombres de tools MCP.
- No alwaysApply Serena a chats triviales o Planner discovery “por si acaso”.
- No usar Serena como sustituto de code-review-graph en reviews.
- No reemplazar Graphify ni el Engineering Loop.
- No meter secretos MCP en el repo.
