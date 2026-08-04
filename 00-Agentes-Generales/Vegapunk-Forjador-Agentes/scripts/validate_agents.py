#!/usr/bin/env python3
from pathlib import Path
import argparse
import re
import sys

REQUIRED = {"Personalidad.md", "Rol.md", "Reglas.md", "Delegacion.md"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return {}, "missing YAML frontmatter"
    try:
        _, block, _ = text.split("---", 2)
    except ValueError:
        return {}, "invalid YAML frontmatter delimiters"
    data = {}
    for line in block.strip().splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data, None


def validate_agent(agent: Path):
    errors, warnings = [], []
    files = {p.name for p in agent.iterdir() if p.is_file()}
    missing = REQUIRED - files
    if missing:
        errors.append(f"missing canonical files: {sorted(missing)}")

    skills_dir = agent / "skills"
    if not skills_dir.is_dir():
        errors.append("missing skills directory")
        return errors, warnings

    skill_dirs = [p for p in skills_dir.iterdir() if p.is_dir()]
    if not skill_dirs:
        warnings.append("agent has no skills")

    descriptions = {}
    for skill in skill_dirs:
        path = skill / "SKILL.md"
        if not path.exists():
            errors.append(f"{skill.name}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        fm, err = parse_frontmatter(text)
        if err:
            errors.append(f"{skill.name}: {err}")
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if name != skill.name:
            errors.append(f"{skill.name}: frontmatter name '{name}' must match directory")
        if not NAME_RE.fullmatch(name):
            errors.append(f"{skill.name}: invalid skill name")
        if not desc:
            errors.append(f"{skill.name}: missing description")
        elif len(desc) > 1024:
            errors.append(f"{skill.name}: description exceeds 1024 characters")
        elif not any(token in desc.lower() for token in ("cuando", "use", "úsala", "usala", "úsalo", "usalo")):
            warnings.append(f"{skill.name}: description may not explain when to use it")
        for section in ["## Procedimiento", "## Salida", "## Validación"]:
            if section not in text:
                warnings.append(f"{skill.name}: missing recommended section {section}")
        normalized = re.sub(r"\W+", " ", desc.lower()).strip()
        if normalized in descriptions:
            warnings.append(f"{skill.name}: description duplicates {descriptions[normalized]}")
        descriptions[normalized] = skill.name

    return errors, warnings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default="agents")
    args = parser.parse_args()
    root = Path(args.root)
    if not root.exists():
        print(f"ERROR: root not found: {root}")
        return 2

    total_errors = 0
    agent_dirs = [p for p in root.iterdir() if p.is_dir()]
    for agent in sorted(agent_dirs):
        errors, warnings = validate_agent(agent)
        if errors or warnings:
            print(f"\n[{agent.name}]")
        for item in errors:
            print(f"  ERROR: {item}")
        for item in warnings:
            print(f"  WARN: {item}")
        total_errors += len(errors)

    print(f"\nValidated {len(agent_dirs)} agent(s). Errors: {total_errors}")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
