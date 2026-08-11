#!/usr/bin/env python3
"""Convert Cursor Nakamas agent markdown → Claude / Codex / Antigravity formats."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


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


def toml_escape_multiline(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"""', '\\"""')


def to_claude(meta: dict[str, str], body: str) -> str:
    """Ad-hoc Claude convert (prefer SoT runtime/claude/agents/)."""
    lib_dir = Path(__file__).resolve().parent
    if str(lib_dir) not in sys.path:
        sys.path.insert(0, str(lib_dir))
    from generate_claude_agents import render_claude  # noqa: WPS433

    return render_claude(meta, body)


def to_codex_toml(meta: dict[str, str], body: str) -> str:
    name = meta.get("name") or "unnamed"
    description = meta.get("description") or name
    platform_note = (
        "## Runtime Codex\n\n"
        "Invocado como custom agent / sub-agent Codex (`name`). "
        "Slugs Cursor no se fijan aquí — hereda el modelo de la sesión salvo override explícito. "
        "Política SoT: `namakas-agents/docs/MODELS.md`.\n\n"
    )
    instructions = platform_note + body.rstrip() + "\n"
    parts = [
        f'name = "{name}"',
        f'description = "{description.replace(chr(34), chr(92)+chr(34))}"',
    ]
    if truthy(meta.get("readonly")):
        parts.append('sandbox_mode = "read-only"')
    # Capitanes / Grok-equivalent: hint high effort without inventing OpenAI model IDs
    if meta.get("model") == "cursor-grok-4.5-high":
        parts.append('model_reasoning_effort = "high"')
    parts.append(f'developer_instructions = """\n{toml_escape_multiline(instructions)}"""')
    return "\n".join(parts) + "\n"


def to_antigravity(meta: dict[str, str], body: str) -> str:
    """Antigravity: persona markdown (no native Cursor-style custom agent registry)."""
    name = meta.get("name") or "unnamed"
    description = meta.get("description") or name
    header = (
        f"# {name}\n\n"
        f"**description:** {description}\n\n"
        "> **Runtime Antigravity:** no hay registry de custom agents como Cursor. "
        "El agente raíz (Oda) lee este archivo y despacha trabajo vía `invoke_subagent` "
        "(tipos built-in `self` / `research`) con este prompt de persona, o adopta el rol "
        "en el turno cuando el nivel de routing lo permita. "
        "Slugs Cursor no aplican — usa el modelo de la sesión. "
        "SoT: `namakas-agents/docs/MODELS.md`.\n\n"
    )
    return header + body.rstrip() + "\n"


def mdc_to_plain_rule(text: str) -> str:
    """Strip Cursor .mdc alwaysApply frontmatter into a plain markdown rule body."""
    meta, body = parse_frontmatter(text)
    if not meta:
        return text if text.endswith("\n") else text + "\n"
    desc = meta.get("description", "")
    header = f"# {desc}\n\n" if desc else ""
    return header + body.rstrip() + "\n"


def convert_file(src: Path, fmt: str) -> str:
    text = src.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    if fmt == "claude":
        return to_claude(meta, body)
    if fmt == "codex":
        return to_codex_toml(meta, body)
    if fmt == "antigravity":
        return to_antigravity(meta, body)
    if fmt == "rule":
        return mdc_to_plain_rule(text)
    raise SystemExit(f"formato desconocido: {fmt}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=Path)
    parser.add_argument("--format", required=True, choices=("claude", "codex", "antigravity", "rule"))
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    out = convert_file(args.src, args.format)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
