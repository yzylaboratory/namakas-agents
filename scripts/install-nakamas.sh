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
#
# No borra configs no-Nakamas. Solo escribe agentes/rules Nakamas y secciones marcadas.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AGENTS_SRC="$REPO_ROOT/runtime-agents"
ODA_MDC="$REPO_ROOT/ODA/oda.mdc"
ODA_INSTRUCTIONS="$REPO_ROOT/ODA/INSTRUCTIONS.md"
GRAPHIFY_RULE_SRC="$REPO_ROOT/rules/nakamas-graphify.mdc"
CRG_RULE_SRC="$REPO_ROOT/rules/nakamas-code-review-graph.mdc"
SERENA_RULE_SRC="$REPO_ROOT/rules/nakamas-serena.mdc"
CONVERT="$REPO_ROOT/scripts/lib/convert_agent.py"
UPSERT="$REPO_ROOT/scripts/lib/upsert_marked_section.py"

TARGET="cursor"
MODE="copy"

usage() {
  sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

for arg in "$@"; do
  case "$arg" in
    -h|--help) usage 0 ;;
    --symlink) MODE="symlink" ;;
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

if [[ ! -d "$AGENTS_SRC" ]]; then
  echo "ERROR: no existe $AGENTS_SRC" >&2
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
  local n=0
  local f
  for f in "$AGENTS_SRC"/*.md; do
    n=$((n + 1))
  done
  echo "$n"
}

install_cursor() {
  local CURSOR_AGENTS="${HOME}/.cursor/agents"
  local CURSOR_RULES="${HOME}/.cursor/rules"
  mkdir -p "$CURSOR_AGENTS" "$CURSOR_RULES"

  echo "==> [cursor] Subagentes → $CURSOR_AGENTS ($MODE)"
  local src name
  for src in "$AGENTS_SRC"/*.md; do
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

install_claude() {
  local CLAUDE_AGENTS="${HOME}/.claude/agents"
  local CLAUDE_RULES="${HOME}/.claude/rules"
  local CLAUDE_MD="${HOME}/.claude/CLAUDE.md"
  mkdir -p "$CLAUDE_AGENTS" "$CLAUDE_RULES"

  echo "==> [claude] Subagentes → $CLAUDE_AGENTS"
  local src name dest
  for src in "$AGENTS_SRC"/*.md; do
    name="$(basename "$src")"
    dest="$CLAUDE_AGENTS/$name"
    python3 "$CONVERT" "$src" --format claude -o "$dest"
    echo "  $name"
  done

  echo "==> [claude] Rule Oda → $CLAUDE_RULES/oda.md"
  {
    echo "# Oda — runtime raíz Nakamas (Claude Code)"
    echo
    echo "No eres un subagente. Capitanes/tripulación: \`~/.claude/agents/*.md\` (invoca con Agent/Task por \`name\`)."
    echo "En Claude, \`Task\`/\`Agent\` sustituye al Task tool de Cursor. No crees \`~/.claude/agents/oda.md\`."
    echo
    echo "Coexiste con rules legacy (p. ej. \`tripulacion.md\` / brd-*): para Engineering Loop Nakamas, esta rule manda."
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

- Raíz: rule `~/.claude/rules/oda.md` (Oda — no es subagente).
- Flota: `~/.claude/agents/*.md` (SoT: `namakas-agents/runtime-agents/`).
- Invocar: Agent/Task con `name` del frontmatter (ej. `trafalgar-d-water-law`, `monkey-d-luffy`, `rob-lucci`).
- Sync: `./scripts/install-nakamas.sh --target=claude` desde el repo.
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

  echo "==> [codex] Custom agents → $CODEX_AGENTS (*.toml)"
  local src stem dest
  for src in "$AGENTS_SRC"/*.md; do
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
  # Paths reales en esta Mac: ~/.antigravity/.agent/rules + GEMINI.md global
  local AGY_RULES="${HOME}/.antigravity/.agent/rules"
  local AGY_AGENTS="${HOME}/.antigravity/.agent/agents"
  local GEMINI_MD="${HOME}/.gemini/GEMINI.md"
  mkdir -p "$AGY_RULES" "$AGY_AGENTS"

  echo "==> [antigravity] Personas → $AGY_AGENTS"
  local src name dest
  for src in "$AGENTS_SRC"/*.md; do
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

  # Índice de flota (siempre útil para el modelo raíz)
  {
    echo "# Nakamas fleet index (Antigravity)"
    echo
    echo "Personas en \`~/.antigravity/.agent/agents/\`. Capitanes: \`trafalgar-d-water-law\`, \`monkey-d-luffy\`, \`rob-lucci\`."
    echo "Raíz: rule \`oda.md\`. Sync: \`./scripts/install-nakamas.sh --target=antigravity\`."
    echo
    echo "## Agentes"
    for src in "$AGENTS_SRC"/*.md; do
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
  local n
  n="$(count_agents)"
  echo
  echo "Flota SoT: $n agentes en runtime-agents/ (no incluye Editor Cursor-only: buggy/alvida/…)."
  echo "Detalle multi-IA: docs/SETUP-MULTI-IA.md"
  echo "Cursor-only: docs/SETUP-OTRA-MAC.md | Modelos: docs/MODELS.md"
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
