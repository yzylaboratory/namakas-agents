#!/usr/bin/env python3
"""Generate Claude Code native subagents from Cursor SoT (runtime/cursor/agents).

SoT Claude: runtime/claude/agents/*.md
Frontmatter: https://code.claude.com/docs/en/sub-agents
Model map: docs/MODELS-CLAUDE.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)

# Planner decision / Grok-equivalent → opus + high effort
# Imp/Ver captains+crew → haiku (docs/MODELS-CLAUDE.md)
OPUS_HIGH = frozenset(
    {
        "trafalgar-d-water-law",
        "vegapunk-edison",
    }
)

HAIKU_CREW = frozenset(
    {
        "monkey-d-luffy",
        "franky",
        "usopp",
        "sanji",
        "nami",
        "jinbe",
        "roronoa-zoro",
        "brook",
        "rob-lucci",
        "tashigi",
        "tony-tony-chopper",
        "stussy",
        "issho-fujitora",
        "sengoku",
        "kaku",
    }
)

PLANNER_CREW = (
    "mont-blanc-noland",
    "nico-robin",
    "vegapunk-edison",
    "donquixote-doflamingo",
    "benn-beckman",
    "profesor-clover",
    "iceburg",
)
IMPLEMENTER_CREW = (
    "franky",
    "usopp",
    "sanji",
    "nami",
    "jinbe",
    "roronoa-zoro",
    "brook",
)
VERIFIER_CREW = (
    "tashigi",
    "tony-tony-chopper",
    "stussy",
    "issho-fujitora",
    "sengoku",
    "kaku",
)

CAPTAIN_CREW: dict[str, tuple[str, ...]] = {
    "trafalgar-d-water-law": PLANNER_CREW,
    "monkey-d-luffy": IMPLEMENTER_CREW,
    "rob-lucci": VERIFIER_CREW,
}

# Read-heavy verifiers (no Edit/Write by default). Chopper may fix → full implementer-ish set.
READ_HEAVY = frozenset(
    {
        "tashigi",
        "stussy",
        "issho-fujitora",
        "sengoku",
        "kaku",
        # Planner specialists that are analysis-only (Cursor readonly)
        "mont-blanc-noland",
        "nico-robin",
        "vegapunk-edison",
        "donquixote-doflamingo",
        "benn-beckman",
        "trafalgar-d-water-law",
        "rob-lucci",
        "monkey-d-luffy",  # captain coordinates; does not implement
    }
)

# Chopper can edit when fixing; iceburg/clover write docs/openspec
COLORS = {
    "trafalgar-d-water-law": "yellow",
    "monkey-d-luffy": "red",
    "rob-lucci": "purple",
    "vegapunk-edison": "cyan",
    "sanji": "orange",
    "usopp": "green",
    "franky": "blue",
    "jinbe": "blue",
    "nami": "orange",
    "roronoa-zoro": "green",
    "brook": "pink",
    "tony-tony-chopper": "pink",
    "stussy": "purple",
    "tashigi": "cyan",
    "iceburg": "yellow",
}

CURSOR_MODEL_RE = re.compile(
    r"`?(composer-2\.5(?:\[[^\]]*\])?|cursor-grok-4\.5-high|claude-sonnet-5-thinking-high|"
    r"gpt-5\.6-sol-high|gpt-5\.3-codex-high|claude-opus-5-thinking-high)`?",
    re.IGNORECASE,
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, match.group(2).lstrip("\n")


def truthy(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower() in {"true", "1", "yes"}


def enrich_description(name: str, description: str) -> str:
    d = description.strip()
    lower = d.lower()
    if name in CAPTAIN_CREW:
        if "use when" not in lower and "usar cuando" not in lower:
            d = d.rstrip(".") + ". Use when Oda routes a mission to this captain; use proactively for crew coordination."
        elif "proactiv" not in lower:
            d = d.rstrip(".") + " Use proactively to coordinate your crew."
    elif "use when" not in lower and "usar cuando" not in lower:
        d = d.rstrip(".") + ". Use when the task matches this specialist's domain."
    return d


def tools_for(name: str, readonly: bool) -> str:
    if name in CAPTAIN_CREW:
        crew = ", ".join(CAPTAIN_CREW[name])
        # Captains: Agent allowlist + read/orchestration tools (no Edit for captains)
        return f"Agent({crew}), Read, Grep, Glob, Bash, WebFetch, WebSearch, TodoWrite"

    if name in READ_HEAVY or readonly:
        return "Read, Grep, Glob, Bash, WebFetch, WebSearch, TodoWrite"

    # Implementers + Chopper + writers (iceburg, clover, etc.)
    return "Read, Grep, Glob, Bash, Edit, Write, NotebookEdit, WebFetch, WebSearch, TodoWrite, Skill"


def model_fields(name: str) -> list[str]:
    if name in OPUS_HIGH:
        return ["model: opus", "effort: high"]
    if name in HAIKU_CREW:
        return ["model: haiku"]
    return ["model: sonnet"]


def clean_body(body: str, name: str) -> str:
    """Strip Cursor-only model slugs; retarget Task→Agent where it helps Claude."""
    text = body

    # Collapse duplicate leading --- separators left in some Cursor files
    text = re.sub(r"\A---\s*\n+", "", text)

    # Replace Modelo sections that cite Cursor slugs
    text = re.sub(
        r"(?m)^## Modelo\n\n.*?(?=\n## |\n# |\Z)",
        _modelo_section(name),
        text,
        count=1,
        flags=re.DOTALL,
    )

    # Inline slug replacements remaining in body
    def _slug_sub(m: re.Match[str]) -> str:
        raw = m.group(0).strip("`")
        if name in HAIKU_CREW:
            return "`haiku`"
        if "grok" in raw.lower() or "opus-5" in raw.lower():
            return "`opus` + `effort: high`"
        if "sonnet-5" in raw.lower():
            return "`sonnet`"
        if "composer" in raw.lower() or "codex" in raw.lower() or "sol" in raw.lower():
            return "`sonnet`"
        return "`sonnet`"

    text = CURSOR_MODEL_RE.sub(_slug_sub, text)

    # Soften Cursor Task tool wording without destroying meaning
    text = text.replace("Task tool", "Agent tool")
    text = text.replace("`Task`", "`Agent`")
    text = re.sub(r"\binvocar Task\b", "invocar Agent", text)
    text = re.sub(r"\binvocar Task\b", "invocar Agent", text, flags=re.IGNORECASE)

    note = (
        "> **Runtime Claude Code:** subagente en `~/.claude/agents/`. "
        "Invoca con la herramienta `Agent` por `name`. "
        "Modelos: ver `namakas-agents/docs/MODELS-CLAUDE.md` (no uses slugs Cursor).\n\n"
    )
    return note + text.rstrip() + "\n"


def _modelo_section(name: str) -> str:
    if name in OPUS_HIGH:
        detail = (
            "Frontmatter Claude: `model: opus` + `effort: high` "
            "(equivalente de decisión a Grok en Cursor).\n\n"
        )
    elif name in HAIKU_CREW:
        detail = "Frontmatter Claude: `model: haiku` (Implementer / Verifier).\n\n"
    else:
        detail = "Frontmatter Claude: `model: sonnet` (default de ejecución).\n\n"

    if name == "trafalgar-d-water-law":
        detail += (
            "Tripulación Planner: `sonnet` por defecto. Edison = `opus` + `effort: high`.\n"
            "Escalación L3+/L4: documentá override en consolidado (`docs/MODELS-CLAUDE.md`). "
            "No uses modelos caros en L0–L2 ni “por si acaso”.\n\n"
        )
    elif name == "monkey-d-luffy":
        detail += "Tripulación Implementer: `haiku`. Escalación puntual: `docs/MODELS-CLAUDE.md`.\n\n"
    elif name == "rob-lucci":
        detail += "Tripulación Verifier: `haiku`. Escalación RCA/security: `docs/MODELS-CLAUDE.md`.\n\n"

    return "## Modelo\n\n" + detail


def render_claude(meta: dict[str, str], body: str) -> str:
    name = meta.get("name") or "unnamed"
    description = enrich_description(name, meta.get("description") or name)
    readonly = truthy(meta.get("readonly"))

    lines = [
        "---",
        f"name: {name}",
        f"description: {description}",
        f"tools: {tools_for(name, readonly)}",
        *model_fields(name),
    ]
    if name in COLORS:
        lines.append(f"color: {COLORS[name]}")
    if truthy(meta.get("is_background")):
        lines.append("background: true")
    # Capitanes: plan/orchestration — prefer default permissions
    if name in CAPTAIN_CREW:
        lines.append("permissionMode: default")
    elif name in READ_HEAVY or readonly:
        lines.append("permissionMode: default")
    else:
        lines.append("permissionMode: acceptEdits")

    lines.extend(["---", ""])
    return "\n".join(lines) + clean_body(body, name)


# Claude-only hand-maintained agents (not generated from Cursor SoT).
# Never overwrite or delete these on --regenerate.
CLAUDE_ONLY_KEEP = frozenset({"oda.md"})


def generate(src_dir: Path, dest_dir: Path) -> list[str]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    for src in sorted(src_dir.glob("*.md")):
        if src.name in CLAUDE_ONLY_KEEP:
            print(f"SKIP (Claude-only): {src.name}", file=sys.stderr)
            continue
        meta, body = parse_frontmatter(src.read_text(encoding="utf-8"))
        if not meta.get("name"):
            print(f"WARN: sin name en {src.name}", file=sys.stderr)
            continue
        out = render_claude(meta, body)
        dest = dest_dir / src.name
        dest.write_text(out, encoding="utf-8")
        written.append(meta["name"])
    # Preserve Claude-only files already in dest (e.g. oda.md)
    for keep in sorted(CLAUDE_ONLY_KEEP):
        kept = dest_dir / keep
        if kept.is_file():
            print(f"KEEP Claude-only: {keep}")
        else:
            print(f"WARN: falta Claude-only {keep} en {dest_dir}", file=sys.stderr)
    return written


def validate(dest_dir: Path) -> None:
    allowed = {
        "name",
        "description",
        "tools",
        "disallowedTools",
        "model",
        "permissionMode",
        "maxTurns",
        "skills",
        "mcpServers",
        "hooks",
        "memory",
        "background",
        "effort",
        "isolation",
        "color",
        "initialPrompt",
    }
    names: set[str] = set()
    for path in sorted(dest_dir.glob("*.md")):
        meta, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        unknown = set(meta) - allowed
        if unknown:
            raise SystemExit(f"{path.name}: campos no soportados: {sorted(unknown)}")
        if "name" not in meta or "description" not in meta:
            raise SystemExit(f"{path.name}: faltan name/description")
        if meta["name"] in names:
            raise SystemExit(f"name duplicado: {meta['name']}")
        names.add(meta["name"])
        text = path.read_text(encoding="utf-8")
        if "composer-2.5" in text or "cursor-grok" in text:
            raise SystemExit(f"{path.name}: aún contiene slug Cursor")
        model = meta.get("model", "")
        if model not in {"sonnet", "opus", "haiku", "fable", "inherit"} and not model.startswith(
            "claude-"
        ):
            raise SystemExit(f"{path.name}: model inválido: {model}")


def main() -> int:
    repo = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src",
        type=Path,
        default=repo / "runtime" / "cursor" / "agents",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=repo / "runtime" / "claude" / "agents",
    )
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    if not args.validate_only:
        if not args.src.is_dir():
            print(f"ERROR: no existe {args.src}", file=sys.stderr)
            return 1
        written = generate(args.src, args.dest)
        print(f"Generados {len(written)} agentes Claude → {args.dest}")
        for n in written:
            print(f"  {n}")

    validate(args.dest)
    print("Validación OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
