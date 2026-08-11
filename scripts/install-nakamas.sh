#!/usr/bin/env bash
# Instala/sincroniza Nakamas Agents desde este repo (SoT) a runtimes locales.
#
# Uso (desde la raíz del repo o vía path al script):
#   ./scripts/install-nakamas.sh                          # cursor (compat)
#   ./scripts/install-nakamas.sh --target=cursor
#   ./scripts/install-nakamas.sh --target=codex
#   ./scripts/install-nakamas.sh --target=claude
#   ./scripts/install-nakamas.sh --target=antigravity
#   ./scripts/install-nakamas.sh --target=all
#   ./scripts/install-nakamas.sh --target=cursor --symlink
#   ./scripts/install-nakamas.sh --target=claude --regenerate
#
# No borra configs no-Nakamas. Solo escribe agentes/rules Nakamas y secciones marcadas.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURSOR_AGENTS_SRC="$REPO_ROOT/runtime/cursor/agents"
CLAUDE_AGENTS_SRC="$REPO_ROOT/runtime/claude/agents"
# Compat: symlink runtime-agents → runtime/cursor/agents
AGENTS_SRC="$CURSOR_AGENTS_SRC"
ODA_MDC="$REPO_ROOT/ODA/oda.mdc"
ODA_INSTRUCTIONS="$REPO_ROOT/ODA/INSTRUCTIONS.md"
GRAPHIFY_RULE_SRC="$REPO_ROOT/rules/nakamas-graphify.mdc"
CRG_RULE_SRC="$REPO_ROOT/rules/nakamas-code-review-graph.mdc"
SERENA_RULE_SRC="$REPO_ROOT/rules/nakamas-serena.mdc"
CONVERT="$REPO_ROOT/scripts/lib/convert_agent.py"
GENERATE_CLAUDE="$REPO_ROOT/scripts/lib/generate_claude_agents.py"
UPSERT="$REPO_ROOT/scripts/lib/upsert_marked_section.py"

TARGET="cursor"
MODE="copy"
REGENERATE=0

usage() {
  sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

for arg in "$@"; do
  case "$arg" in
    -h|--help) usage 0 ;;
    --symlink) MODE="symlink" ;;
    --regenerate) REGENERATE=1 ;;
    --target=*) TARGET="${arg#--target=}" ;;
    --target)
      echo "ERROR: usa --target=cursor|codex|claude|antigravity|all" >&2
      exit 2
      ;;
    *)
      echo "ERROR: argumento desconocido: $arg" >&2
      usage 2
      ;;
  esac
done

if [[ ! -d "$CURSOR_AGENTS_SRC" ]]; then
  echo "ERROR: no existe $CURSOR_AGENTS_SRC" >&2
  exit 1
fi

if [[ ! -f "$CONVERT" || ! -f "$UPSERT" ]]; then
  echo "ERROR: faltan helpers en scripts/lib/" >&2
  exit 1
fi

shopt -s nullglob

install_file() {
  local src="$1" dest="$2"
  mkdir -p "$(dirname "$dest")"
  if [[ "$MODE" == "symlink" ]]; then
    ln -sfn "$src" "$dest"
  else
    cp "$src" "$dest"
  fi
}

count_agents() {
  local dir="$1"
  local n=0
  local f
  for f in "$dir"/*.md; do
    n=$((n + 1))
  done
  echo "$n"
}

install_cursor() {
  local CURSOR_AGENTS="${HOME}/.cursor/agents"
  local CURSOR_RULES="${HOME}/.cursor/rules"
  mkdir -p "$CURSOR_AGENTS" "$CURSOR_RULES"

  echo "==> [cursor] Subagentes → $CURSOR_AGENTS ($MODE) desde runtime/cursor/agents"
  local src name
  for src in "$CURSOR_AGENTS_SRC"/*.md; do
    name="$(basename "$src")"
    install_file "$src" "$CURSOR_AGENTS/$name"
    echo "  $name"
  done

  if [[ -f "$ODA_MDC" ]]; then
    echo "==> [cursor] Rule Oda → $CURSOR_RULES/oda.mdc"
    cp "$ODA_MDC" "$CURSOR_RULES/oda.mdc"
  else
    echo "WARN: falta $ODA_MDC" >&2
  fi

  for pair in \
    "$GRAPHIFY_RULE_SRC|$CURSOR_RULES/nakamas-graphify.mdc" \
    "$CRG_RULE_SRC|$CURSOR_RULES/nakamas-code-review-graph.mdc" \
    "$SERENA_RULE_SRC|$CURSOR_RULES/nakamas-serena.mdc"
  do
    local s="${pair%%|*}"
    local d="${pair##*|}"
    if [[ -f "$s" ]]; then
      echo "==> [cursor] $(basename "$d")"
      cp "$s" "$d"
    else
      echo "WARN: falta $s" >&2
    fi
  done

  echo "[cursor] Listo. User Rule Oda → reflejar ODA/INSTRUCTIONS.md (Settings → Rules)."
}

ensure_claude_sot() {
  if [[ "$REGENERATE" -eq 1 ]] || [[ ! -d "$CLAUDE_AGENTS_SRC" ]] || [[ -z "$(echo "$CLAUDE_AGENTS_SRC"/*.md)" ]]; then
    echo "==> [claude] Regenerando SoT runtime/claude/agents/ desde Cursor"
    python3 "$GENERATE_CLAUDE"
  else
    python3 "$GENERATE_CLAUDE" --validate-only
  fi
}

install_claude() {
  ensure_claude_sot

  local CLAUDE_AGENTS="${HOME}/.claude/agents"
  local CLAUDE_RULES="${HOME}/.claude/rules"
  local CLAUDE_MD="${HOME}/.claude/CLAUDE.md"
  mkdir -p "$CLAUDE_AGENTS" "$CLAUDE_RULES"

  echo "==> [claude] Subagentes → $CLAUDE_AGENTS ($MODE) desde runtime/claude/agents (frontmatter nativo)"
  local src name
  for src in "$CLAUDE_AGENTS_SRC"/*.md; do
    name="$(basename "$src")"
    install_file "$src" "$CLAUDE_AGENTS/$name"
    echo "  $name"
  done

  # Guardrail: solo flota SoT Claude (no extras locales / Editor Cursor-only)
  local bad=0
  for src in "$CLAUDE_AGENTS_SRC"/*.md; do
    name="$(basename "$src")"
    if rg -n 'composer-2\.5|cursor-grok' "$CLAUDE_AGENTS/$name" >/dev/null 2>&1; then
      echo "ERROR: slug Cursor en flota instalada: $name" >&2
      bad=1
    fi
  done
  if [[ "$bad" -ne 0 ]]; then
    exit 1
  fi

  # Limpiar leftovers Editor/Cursor mal copiados (no están en SoT Claude)
  local orphan
  for orphan in "$CLAUDE_AGENTS"/*.md; do
    name="$(basename "$orphan")"
    if [[ ! -f "$CLAUDE_AGENTS_SRC/$name" ]]; then
      if rg -q 'composer-2\.5|cursor-grok|^model: composer|^model: cursor-' "$orphan" 2>/dev/null; then
        echo "==> [claude] Quitando leftover Cursor-only: $name"
        rm -f "$orphan"
      fi
    fi
  done

  echo "==> [claude] Rule Oda (refuerzo) → $CLAUDE_RULES/oda.md"
  {
    echo "# Oda — runtime raíz Nakamas (Claude Code)"
    echo
    echo "**SoT invocable:** agent file \`~/.claude/agents/oda.md\` (\`claude --agent oda\` o @-mention)."
    echo "Esta rule es **refuerzo** del mismo prompt; el agent file manda para invocación explícita."
    echo "Capitanes/tripulación: \`~/.claude/agents/*.md\` (invoca con Agent por \`name\`)."
    echo "En Claude, \`Agent\` sustituye al Task tool de Cursor."
    echo "Modelos Claude: \`namakas-agents/docs/MODELS-CLAUDE.md\` (opus/sonnet/haiku — no Composer/Grok)."
    echo "Oda agent: \`model: opus\` + \`effort: high\` (equivalente Grok decisión)."
    echo
    echo "Coexiste con rules legacy (p. ej. \`tripulacion.md\` / brd-*): para Engineering Loop Nakamas, Oda (agent + esta rule) manda."
    echo
    cat "$ODA_INSTRUCTIONS"
  } > "$CLAUDE_RULES/oda.md"

  for pair in \
    "$GRAPHIFY_RULE_SRC|$CLAUDE_RULES/nakamas-graphify.md" \
    "$CRG_RULE_SRC|$CLAUDE_RULES/nakamas-code-review-graph.md" \
    "$SERENA_RULE_SRC|$CLAUDE_RULES/nakamas-serena.md"
  do
    local s="${pair%%|*}"
    local d="${pair##*|}"
    if [[ -f "$s" ]]; then
      echo "==> [claude] $(basename "$d")"
      python3 "$CONVERT" "$s" --format rule -o "$d"
    fi
  done

  local tmp
  tmp="$(mktemp)"
  cat > "$tmp" <<'EOF'
## Nakamas Agents (Claude)

- Raíz: agent `~/.claude/agents/oda.md` (SoT invocable: `claude --agent oda` / @oda) + rule `~/.claude/rules/oda.md` (refuerzo).
- Flota: `~/.claude/agents/*.md` (SoT: `namakas-agents/runtime/claude/agents/` — frontmatter nativo; incluye `oda.md`).
- Cursor SoT separado: `namakas-agents/runtime/cursor/agents/` (Oda **no** va ahí como subagente Cursor).
- Invocar: Agent con `name` del frontmatter (ej. `oda`, `trafalgar-d-water-law`, `monkey-d-luffy`, `rob-lucci`).
- Modelos: `docs/MODELS-CLAUDE.md` — no `composer-2.5[]` / `cursor-grok-*`.
- Sync: `./scripts/install-nakamas.sh --target=claude` (opcional `--regenerate`; no pisa `oda.md`).
- Docs: `namakas-agents/docs/SETUP-MULTI-IA.md`
EOF
  python3 "$UPSERT" "$CLAUDE_MD" \
    --begin "<!-- NAKAMAS:BEGIN -->" \
    --end "<!-- NAKAMAS:END -->" \
    --body-file "$tmp"
  rm -f "$tmp"
  echo "==> [claude] Sección marcada en $CLAUDE_MD"
  echo "[claude] Listo."
}

install_codex() {
  local CODEX_AGENTS="${HOME}/.codex/agents"
  local CODEX_AGENTS_MD="${HOME}/.codex/AGENTS.md"
  mkdir -p "$CODEX_AGENTS"

  echo "==> [codex] Custom agents → $CODEX_AGENTS (*.toml) desde runtime/cursor/agents"
  local src stem dest
  for src in "$CURSOR_AGENTS_SRC"/*.md; do
    stem="$(basename "$src" .md)"
    dest="$CODEX_AGENTS/${stem}.toml"
    python3 "$CONVERT" "$src" --format codex -o "$dest"
    echo "  ${stem}.toml"
  done

  local rules_dir="${HOME}/.codex/nakamas-rules"
  mkdir -p "$rules_dir"
  {
    echo "# Oda — runtime raíz Nakamas (Codex)"
    echo
    echo "No eres un subagente. Capitanes/tripulación: \`~/.codex/agents/*.toml\`."
    echo "Invoca custom/sub-agents Codex por \`name\`. No crees un agent TOML llamado oda."
    echo
    cat "$ODA_INSTRUCTIONS"
  } > "$rules_dir/oda.md"

  for pair in \
    "$GRAPHIFY_RULE_SRC|$rules_dir/nakamas-graphify.md" \
    "$CRG_RULE_SRC|$rules_dir/nakamas-code-review-graph.md" \
    "$SERENA_RULE_SRC|$rules_dir/nakamas-serena.md"
  do
    local s="${pair%%|*}"
    local d="${pair##*|}"
    if [[ -f "$s" ]]; then
      python3 "$CONVERT" "$s" --format rule -o "$d"
      echo "==> [codex] $(basename "$d")"
    fi
  done

  local tmp
  tmp="$(mktemp)"
  cat > "$tmp" <<EOF
## Nakamas Agents (Codex)

Eres **Oda** cuando actúas como agente raíz de este runtime. Instrucciones completas: \`~/.codex/nakamas-rules/oda.md\`.

- Flota (custom agents): \`~/.codex/agents/*.toml\` — invocar por \`name\` (Law / Luffy / Lucci + tripulación).
- Code intel: lee \`~/.codex/nakamas-rules/nakamas-graphify.md\` (y Serena / code-review-graph cuando aplique).
- Modelos Cursor no se fijan en los TOML; hereda el modelo de la sesión. SoT: namakas-agents/docs/MODELS.md.
- Sync: \`./scripts/install-nakamas.sh --target=codex\`
- Docs: namakas-agents/docs/SETUP-MULTI-IA.md

Cadena: Usuario → Oda → Capitán → Tripulación. No declares READY_FOR_* / VERIFIED tú mismo salvo el rol correspondiente.
EOF
  python3 "$UPSERT" "$CODEX_AGENTS_MD" \
    --begin "<!-- NAKAMAS:BEGIN -->" \
    --end "<!-- NAKAMAS:END -->" \
    --body-file "$tmp"
  rm -f "$tmp"
  echo "==> [codex] Sección marcada en $CODEX_AGENTS_MD (sin borrar el resto)"
  echo "[codex] Listo."
}

install_antigravity() {
  local AGY_RULES="${HOME}/.antigravity/.agent/rules"
  local AGY_AGENTS="${HOME}/.antigravity/.agent/agents"
  local GEMINI_MD="${HOME}/.gemini/GEMINI.md"
  mkdir -p "$AGY_RULES" "$AGY_AGENTS"

  echo "==> [antigravity] Personas → $AGY_AGENTS desde runtime/cursor/agents"
  local src name dest
  for src in "$CURSOR_AGENTS_SRC"/*.md; do
    name="$(basename "$src")"
    dest="$AGY_AGENTS/$name"
    python3 "$CONVERT" "$src" --format antigravity -o "$dest"
    echo "  $name"
  done

  echo "==> [antigravity] Rule Oda → $AGY_RULES/oda.md"
  {
    echo "# Oda — runtime raíz Nakamas (Antigravity)"
    echo
    echo "No eres un subagente. Antigravity no expone un registry de custom agents como Cursor."
    echo "Personas Nakamas: \`~/.antigravity/.agent/agents/<name>.md\`."
    echo "Para despachar trabajo especializado: \`invoke_subagent\` con tipo built-in (\`self\` / \`research\`)"
    echo "e incluye el contenido de la persona correspondiente en el prompt; o adopta el rol si el nivel 0–2 lo permite."
    echo
    cat "$ODA_INSTRUCTIONS"
  } > "$AGY_RULES/oda.md"

  for pair in \
    "$GRAPHIFY_RULE_SRC|$AGY_RULES/nakamas-graphify.md" \
    "$CRG_RULE_SRC|$AGY_RULES/nakamas-code-review-graph.md" \
    "$SERENA_RULE_SRC|$AGY_RULES/nakamas-serena.md"
  do
    local s="${pair%%|*}"
    local d="${pair##*|}"
    if [[ -f "$s" ]]; then
      python3 "$CONVERT" "$s" --format rule -o "$d"
      echo "==> [antigravity] $(basename "$d")"
    fi
  done

  {
    echo "# Nakamas fleet index (Antigravity)"
    echo
    echo "Personas en \`~/.antigravity/.agent/agents/\`. Capitanes: \`trafalgar-d-water-law\`, \`monkey-d-luffy\`, \`rob-lucci\`."
    echo "Raíz: rule \`oda.md\`. Sync: \`./scripts/install-nakamas.sh --target=antigravity\`."
    echo
    echo "## Agentes"
    for src in "$CURSOR_AGENTS_SRC"/*.md; do
      echo "- \`$(basename "$src" .md)\`"
    done
  } > "$AGY_RULES/nakamas-fleet.md"

  if [[ -f "$GEMINI_MD" ]]; then
    local tmp
    tmp="$(mktemp)"
    cat > "$tmp" <<'EOF'
## Nakamas Agents (Antigravity)

- Raíz: `~/.antigravity/.agent/rules/oda.md`
- Personas: `~/.antigravity/.agent/agents/*.md`
- Despacho: `invoke_subagent` (built-in `self`/`research`) + prompt de persona; no hay Task types Nakamas nativos.
- Sync: `./scripts/install-nakamas.sh --target=antigravity`
- Docs: `namakas-agents/docs/SETUP-MULTI-IA.md`
EOF
    python3 "$UPSERT" "$GEMINI_MD" \
      --begin "<!-- NAKAMAS:BEGIN -->" \
      --end "<!-- NAKAMAS:END -->" \
      --body-file "$tmp"
    rm -f "$tmp"
    echo "==> [antigravity] Sección marcada en $GEMINI_MD"
  else
    echo "WARN: no existe $GEMINI_MD — solo rules/agents bajo ~/.antigravity/.agent/" >&2
  fi
  echo "[antigravity] Listo."
}

print_footer() {
  local nc ncl
  nc="$(count_agents "$CURSOR_AGENTS_SRC")"
  ncl="$(count_agents "$CLAUDE_AGENTS_SRC")"
  echo
  echo "SoT Cursor: $nc agentes en runtime/cursor/agents/ (symlink: runtime-agents/)."
  echo "SoT Claude: $ncl agentes en runtime/claude/agents/ (frontmatter nativo)."
  echo "Detalle multi-IA: docs/SETUP-MULTI-IA.md | Modelos Claude: docs/MODELS-CLAUDE.md"
  echo "Cursor-only: docs/SETUP-OTRA-MAC.md | Modelos Cursor: docs/MODELS.md"
}

case "$TARGET" in
  cursor) install_cursor ;;
  claude) install_claude ;;
  codex) install_codex ;;
  antigravity) install_antigravity ;;
  all)
    install_cursor
    echo
    install_claude
    echo
    install_codex
    echo
    install_antigravity
    ;;
  *)
    echo "ERROR: --target debe ser cursor|codex|claude|antigravity|all (recibido: $TARGET)" >&2
    exit 2
    ;;
esac

print_footer
