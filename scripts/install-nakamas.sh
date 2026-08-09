#!/usr/bin/env bash
# Instala/sincroniza Nakamas Agents en esta Mac desde el repo versionado.
# Uso (desde la raíz del repo):
#   ./scripts/install-nakamas.sh
#   ./scripts/install-nakamas.sh --symlink
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AGENTS_SRC="$REPO_ROOT/runtime-agents"
ODA_SRC="$REPO_ROOT/ODA/oda.mdc"
CURSOR_AGENTS="${HOME}/.cursor/agents"
CURSOR_RULES="${HOME}/.cursor/rules"
MODE="copy"

if [[ "${1:-}" == "--symlink" ]]; then
  MODE="symlink"
fi

if [[ ! -d "$AGENTS_SRC" ]]; then
  echo "ERROR: no existe $AGENTS_SRC" >&2
  exit 1
fi

mkdir -p "$CURSOR_AGENTS" "$CURSOR_RULES"

echo "==> Instalando subagentes en $CURSOR_AGENTS ($MODE)"
shopt -s nullglob
for src in "$AGENTS_SRC"/*.md; do
  name="$(basename "$src")"
  dest="$CURSOR_AGENTS/$name"
  if [[ "$MODE" == "symlink" ]]; then
    ln -sfn "$src" "$dest"
  else
    cp "$src" "$dest"
  fi
  echo "  $name"
done

if [[ -f "$ODA_SRC" ]]; then
  echo "==> Instalando rule Oda en $CURSOR_RULES/oda.mdc"
  cp "$ODA_SRC" "$CURSOR_RULES/oda.mdc"
else
  echo "WARN: falta $ODA_SRC" >&2
fi

echo
echo "Listo."
echo "Siguiente:"
echo "  1. Cursor Settings → Rules → User Rule «Oda — runtime raíz Nakamas»"
echo "     debe reflejar ODA/INSTRUCTIONS.md (o pedirle al agente que sincronice vía MCP)."
echo "  2. En el chat raíz, selecciona Grok 4.5 para Oda."
echo "  2b. Modelos: default barato + escalación — ver docs/MODELS.md"
echo "  3. Lanza un Task de prueba y confirma en el dashboard que Composer no corre como Fast"
echo "     (frontmatter usa composer-2.5[])."
echo "Detalle: docs/SETUP-OTRA-MAC.md"
