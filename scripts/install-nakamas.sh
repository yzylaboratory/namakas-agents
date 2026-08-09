#!/usr/bin/env bash
# Instala/sincroniza Nakamas Agents en esta Mac desde el repo versionado.
# Uso (desde la raíz del repo):
#   ./scripts/install-nakamas.sh
#   ./scripts/install-nakamas.sh --symlink
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AGENTS_SRC="$REPO_ROOT/runtime-agents"
ODA_SRC="$REPO_ROOT/ODA/oda.mdc"
GRAPHIFY_RULE_SRC="$REPO_ROOT/rules/nakamas-graphify.mdc"
CRG_RULE_SRC="$REPO_ROOT/rules/nakamas-code-review-graph.mdc"
SERENA_RULE_SRC="$REPO_ROOT/rules/nakamas-serena.mdc"
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

if [[ -f "$GRAPHIFY_RULE_SRC" ]]; then
  echo "==> Instalando rule Graphify en $CURSOR_RULES/nakamas-graphify.mdc"
  cp "$GRAPHIFY_RULE_SRC" "$CURSOR_RULES/nakamas-graphify.mdc"
else
  echo "WARN: falta $GRAPHIFY_RULE_SRC" >&2
fi

if [[ -f "$CRG_RULE_SRC" ]]; then
  echo "==> Instalando rule code-review-graph (requestable) en $CURSOR_RULES/nakamas-code-review-graph.mdc"
  cp "$CRG_RULE_SRC" "$CURSOR_RULES/nakamas-code-review-graph.mdc"
else
  echo "WARN: falta $CRG_RULE_SRC" >&2
fi

if [[ -f "$SERENA_RULE_SRC" ]]; then
  echo "==> Instalando rule Serena (requestable) en $CURSOR_RULES/nakamas-serena.mdc"
  cp "$SERENA_RULE_SRC" "$CURSOR_RULES/nakamas-serena.mdc"
else
  echo "WARN: falta $SERENA_RULE_SRC" >&2
fi

echo
echo "Listo."
echo "Siguiente:"
echo "  1. Cursor Settings → Rules → User Rule «Oda — runtime raíz Nakamas»"
echo "     debe reflejar ODA/INSTRUCTIONS.md (o pedirle al agente que sincronice vía MCP)."
echo "  2. En el chat raíz, selecciona Grok 4.5 para Oda."
echo "  2b. Modelos: default barato + escalación — ver docs/MODELS.md"
echo "  2c. Code intel (3 capas): docs/CODE-INTEL.md"
echo "      Graphify: docs/GRAPHIFY.md + nakamas-graphify.mdc (uv tool install graphifyy)"
echo "      code-review-graph: docs/CODE-REVIEW-GRAPH.md + nakamas-code-review-graph.mdc"
echo "        (uv tool install code-review-graph; MCP: uvx code-review-graph serve)"
echo "      Serena: docs/SERENA.md + nakamas-serena.mdc"
echo "        (uv tool install -p 3.13 serena-agent && serena init;"
echo "         MCP: serena start-mcp-server --context ide)"
echo "  3. Lanza un Task de prueba y confirma en el dashboard que Composer no corre como Fast"
echo "     (frontmatter usa composer-2.5[])."
echo "Detalle: docs/SETUP-OTRA-MAC.md"
