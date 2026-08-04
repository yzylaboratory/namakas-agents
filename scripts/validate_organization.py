#!/usr/bin/env python3
"""Validate Nakamas organizational hierarchy, contracts, and adapters."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
ORG = ROOT / "organization" / "organigrama.yaml"
TASK_C = ROOT / "organization" / "contratos" / "task-contract.md"
REPORT_C = ROOT / "organization" / "contratos" / "report-contract.md"
PROTO = ROOT / "organization" / "protocolo-reportes.md"
RULE = ROOT / ".cursor" / "rules" / "cadena-de-mando.mdc"
ADAPTERS = ROOT / ".cursor" / "agents"

REQUIRED_TASK_FIELDS = [
    "TASK_ID",
    "PARENT_TASK_ID",
    "MISSION_ID",
    "ASSIGNED_BY",
    "ASSIGNED_TO",
    "REPORT_TO",
    "OBJECTIVE",
    "CONTEXT",
    "SCOPE",
    "OUT_OF_SCOPE",
    "INPUTS",
    "CONSTRAINTS",
    "EXPECTED_DELIVERABLE",
    "ACCEPTANCE_CRITERIA",
    "VALIDATION_REQUIRED",
]

REQUIRED_REPORT_FIELDS = [
    "TASK_ID",
    "PARENT_TASK_ID",
    "MISSION_ID",
    "REPORT_TO",
    "STATUS",
    "SUMMARY",
    "DELIVERABLES",
    "EVIDENCE",
    "VALIDATIONS",
    "RISKS",
    "DECISIONS_REQUIRED",
    "DEPENDENCIES_UNLOCKED",
    "NEXT_HANDOFF",
]

STATUS_ENUM = {
    "COMPLETED",
    "COMPLETED_WITH_LIMITATIONS",
    "BLOCKED",
    "REQUIRES_CORRECTION",
    "FAILED",
}

ADAPTER_MARKERS = [
    "reports_to",
    "REPORT_TO",
    "cadena de mando",
    "report-contract",
]


def parse_simple_yaml(text: str) -> dict:
    """Minimal YAML subset parser for organigrama if PyYAML missing."""
    agents = []
    current = None
    list_key = None
    for raw in text.splitlines():
        if raw.strip().startswith("#") or not raw.strip():
            continue
        if raw.startswith("agentes:"):
            continue
        if raw.startswith("  - id:"):
            if current:
                agents.append(current)
            current = {
                "id": raw.split(":", 1)[1].strip(),
                "direct_reports": [],
                "responsabilidades": [],
            }
            list_key = None
            continue
        if current is None:
            continue
        if raw.startswith("    ") and ":" in raw and not raw.startswith("      -"):
            key, val = raw.strip().split(":", 1)
            val = val.strip().strip('"')
            if val in ("[]",):
                current[key] = []
                list_key = None
            elif val == "":
                list_key = key
                if key == "direct_reports":
                    current["direct_reports"] = []
                elif key == "responsabilidades":
                    current["responsabilidades"] = []
            else:
                if val in ("true", "false"):
                    current[key] = val == "true"
                else:
                    current[key] = val
                list_key = None
        elif raw.startswith("      - ") and list_key:
            current.setdefault(list_key, []).append(raw.strip()[2:].strip().strip('"'))
    if current:
        agents.append(current)
    return {"agentes": agents}


def load_org() -> list[dict]:
    text = ORG.read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text)
        agents = data.get("agentes") or []
    else:
        agents = parse_simple_yaml(text).get("agentes") or []
    for a in agents:
        dr = a.get("direct_reports")
        if dr is None or dr == "[]" or dr == []:
            a["direct_reports"] = []
        elif isinstance(dr, str):
            # tolerate comma-separated accidental strings
            a["direct_reports"] = [x.strip() for x in dr.split(",") if x.strip() and x.strip() not in "[]"]
        resp = a.get("responsabilidades")
        if resp is None or resp == "[]":
            a["responsabilidades"] = []
    return agents


def discover_agent_dirs() -> dict[str, Path]:
    found = {}
    for dept in ROOT.glob("[0-9][0-9]-*"):
        for agent in dept.iterdir():
            if not agent.is_dir() or agent.name.startswith("."):
                continue
            # derive slug like bootstrap
            slug = agent.name.lower()
            live = {
                "Luffy-Coordinador": "luffy-coordinador",
                "Vegapunk-Forjador-Agentes": "vegapunk-forjador-agentes",
                "Brook-Cronista": "brook-cronista",
                "Noland-Explorador": "noland-explorador",
                "Vivi-Escritor": "vivi-escritor",
                "Robin-Tratadista": "robin-tratadista",
                "Jinbe-Director-Open-Banking": "jinbe-director-open-banking",
                "Lucci-Estandarizacion-Procesos-BIAN": "lucci-estandarizacion-procesos-bian",
                "Vegapunk-Arquitectura-Semantica-FIBO": "vegapunk-arquitectura-semantica-fibo",
                "Sabo-Ecosistemas-Abiertos-APIs": "sabo-ecosistemas-abiertos-apis",
            }
            slug = live.get(agent.name, slug)
            found[slug] = agent
    return found


def has_cycle(agents: dict[str, dict]) -> list[str]:
    errors = []
    for start in agents:
        seen = set()
        cur = start
        while cur and cur != "Randy":
            if cur in seen:
                errors.append(f"cycle involving {start} via {cur}")
                break
            seen.add(cur)
            nxt = agents.get(cur, {}).get("reports_to")
            if nxt == cur:
                errors.append(f"self-report {cur}")
                break
            cur = nxt
            if cur not in agents and cur != "Randy":
                break
    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not ORG.exists():
        errors.append(f"missing {ORG.relative_to(ROOT)}")
        print_results(errors, warnings)
        return 1
    for path in (TASK_C, REPORT_C, PROTO, RULE):
        if not path.exists():
            errors.append(f"missing required file {path.relative_to(ROOT)}")

    agents_list = load_org()
    if not agents_list:
        errors.append("organigrama.yaml has no agents")
        print_results(errors, warnings)
        return 1

    by_id = {a["id"]: a for a in agents_list}
    disk = discover_agent_dirs()

    # All disk agents registered
    for slug in disk:
        if slug not in by_id:
            errors.append(f"agent on disk not in organigrama: {slug}")

    # All org agents exist on disk
    for slug, meta in by_id.items():
        if slug not in disk:
            errors.append(f"organigrama agent missing on disk: {slug}")

    # Luffy rules
    luffy = by_id.get("luffy-coordinador")
    if not luffy:
        errors.append("luffy-coordinador missing from organigrama")
    else:
        if luffy.get("reports_to") != "Randy":
            errors.append("luffy-coordinador must report to Randy")
        if not luffy.get("puede_responder_usuario"):
            errors.append("luffy-coordinador must have puede_responder_usuario: true")

    for aid, meta in by_id.items():
        if aid != "luffy-coordinador" and meta.get("puede_responder_usuario"):
            errors.append(f"{aid}: only Luffy may set puede_responder_usuario true")
        if aid != "luffy-coordinador" and not meta.get("reports_to"):
            errors.append(f"{aid}: missing supervisor (reports_to)")
        rt = meta.get("reports_to")
        if rt and rt != "Randy" and rt not in by_id:
            errors.append(f"{aid}: reports_to '{rt}' does not exist")

        tipo = meta.get("tipo")
        if tipo == "celula" and rt:
            parent = by_id.get(rt, {})
            if parent.get("tipo") != "director":
                errors.append(f"{aid}: célula must report to a director (got {rt})")
        if tipo == "director" and rt != "luffy-coordinador":
            errors.append(f"{aid}: director must report to luffy-coordinador")
        if tipo == "agente-general" and rt != "luffy-coordinador":
            errors.append(f"{aid}: agente-general must report to luffy-coordinador")

        # direct_reports consistency
        for child in meta.get("direct_reports") or []:
            if child not in by_id:
                errors.append(f"{aid}: direct_report '{child}' missing")
            elif by_id[child].get("reports_to") != aid:
                errors.append(f"{aid}: child {child} does not report back")

        # inverse: if A reports to B, B should list A
        if rt in by_id:
            parent_reports = by_id[rt].get("direct_reports") or []
            if aid not in parent_reports:
                errors.append(f"{aid}: parent {rt} missing this id in direct_reports")

    errors.extend(has_cycle(by_id))

    # Contracts field presence
    if TASK_C.exists():
        task_txt = TASK_C.read_text(encoding="utf-8")
        for field in REQUIRED_TASK_FIELDS:
            if field not in task_txt:
                errors.append(f"task-contract.md missing field {field}")
    if REPORT_C.exists():
        report_txt = REPORT_C.read_text(encoding="utf-8")
        for field in REQUIRED_REPORT_FIELDS:
            if field not in report_txt:
                errors.append(f"report-contract.md missing field {field}")
        for st in STATUS_ENUM:
            if st not in report_txt:
                errors.append(f"report-contract.md missing STATUS {st}")
        if "EVIDENCE" not in report_txt:
            errors.append("report-contract.md missing EVIDENCE")

    # Delegation REPORT_TO on disk
    for slug, path in disk.items():
        deleg = path / "Delegacion.md"
        if not deleg.exists() or deleg.stat().st_size == 0:
            errors.append(f"{slug}: Delegacion.md missing or empty")
        else:
            txt = deleg.read_text(encoding="utf-8")
            if "REPORT_TO" not in txt:
                errors.append(f"{slug}: Delegacion.md missing REPORT_TO")
        rol = path / "Rol.md"
        if rol.exists() and rol.stat().st_size > 0:
            rtxt = rol.read_text(encoding="utf-8")
            if "## Posición organizacional" not in rtxt:
                errors.append(f"{slug}: Rol.md missing ## Posición organizacional")

    # Adapters
    if ADAPTERS.is_dir():
        for adapter in ADAPTERS.glob("*.md"):
            txt = adapter.read_text(encoding="utf-8").lower()
            for marker in ADAPTER_MARKERS:
                if marker.lower() not in txt:
                    errors.append(f"adapter {adapter.name}: missing protocol marker '{marker}'")
                    break
            # must forbid final user answer except Luffy
            if adapter.stem != "luffy-coordinador":
                if "usuario" not in txt and "user" not in txt:
                    warnings.append(f"adapter {adapter.name}: weak user-response prohibition wording")

    # Vegapunk must reference organigrama
    veg_reglas = ROOT / "00-Agentes-Generales" / "Vegapunk-Forjador-Agentes" / "Reglas.md"
    if veg_reglas.exists():
        vtxt = veg_reglas.read_text(encoding="utf-8")
        if "organigrama.yaml" not in vtxt:
            errors.append("Vegapunk Reglas.md must require consulting organigrama.yaml")

    print_results(errors, warnings)
    return 1 if errors else 0


def print_results(errors: list[str], warnings: list[str]) -> None:
    print("=== validate_organization.py ===")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARN: {w}")
    if not errors:
        print("OK: organization hierarchy valid")


if __name__ == "__main__":
    sys.exit(main())
