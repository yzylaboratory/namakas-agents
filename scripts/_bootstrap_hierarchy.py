#!/usr/bin/env python3
"""One-shot bootstrap for Nakamas hierarchy. Safe to re-run (idempotent sections)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MULTI_PERSONAJE = {
    "Capone-Bege": "Capone Bege",
    "Miss-Goldenweek": "Miss Goldenweek",
    "Mr-3": "Mr. 3",
    "X-Drake": "X Drake",
    "King-Riku": "King Riku",
    "Du-Feld": "Du Feld",
    "Bon-Clay": "Bon Clay",
    "Gild-Tesoro": "Gild Tesoro",
}

DEPT_NAMES = {
    "00-Agentes-Generales": "Agentes Generales",
    "01-Open-Banking": "Open Banking",
    "02-Arquitectura": "Arquitectura",
    "03-DevOps-Plataforma": "DevOps y Plataforma",
    "04-Sistemas-Core": "Sistemas Core",
    "05-Backend": "Backend",
    "06-Frontend": "Frontend",
    "07-UX-UI": "UX/UI",
    "08-QA": "QA",
    "09-Ventas-Alianzas": "Ventas y Alianzas",
    "10-Legal-Cumplimiento": "Legal y Cumplimiento",
    "11-Finanzas": "Finanzas",
    "12-Marketing-Growth": "Marketing y Growth",
}

LIVE_SLUGS = {
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

RESP_OVERRIDES = {
    "luffy-coordinador": [
        "Coordinar misiones multi-dominio",
        "Delegar a directores y agentes generales",
        "Consolidar reportes y entregar a Randy",
    ],
    "vegapunk-forjador-agentes": [
        "Forjar, auditar y validar agentes Nakamas",
        "Mantener jerarquía en plantillas y organigrama",
    ],
    "brook-cronista": [
        "Bitácoras de misión bajo reports/",
        "Registrar decisiones, delegaciones y ADR",
    ],
    "noland-explorador": [
        "Discovery y reconocimiento de sistemas",
        "Mapas de dependencias verificables",
    ],
    "vivi-escritor": [
        "Documentación de producto para humanos",
        "Historias de usuario y criterios de aceptación",
    ],
    "robin-tratadista": [
        "Tratados MS/orch y contratos OpenAPI/AsyncAPI",
        "Consumir HANDOFF_BIAN/FIBO sin inventar dominios",
    ],
    "jinbe-director-open-banking": [
        "Estrategia y gobierno Open Banking",
        "Coordinar Lucci, FIBO-Vegapunk y Sabo",
    ],
    "lucci-estandarizacion-procesos-bian": [
        "Mapear procesos a Service Domains BIAN",
        "Producir HANDOFF_BIAN",
    ],
    "vegapunk-arquitectura-semantica-fibo": [
        "Alinear semántica financiera a FIBO",
        "Producir HANDOFF_FIBO",
    ],
    "sabo-ecosistemas-abiertos-apis": [
        "DX, partner APIs, sandboxes y versionado externo",
    ],
}


def to_slug(folder: str) -> str:
    if folder in LIVE_SLUGS:
        return LIVE_SLUGS[folder]
    return folder.lower()


def personaje_from(folder: str) -> str:
    for prefix, name in MULTI_PERSONAJE.items():
        if folder.startswith(prefix + "-") or folder == prefix:
            return name
    return folder.split("-")[0]


def is_director(folder: str) -> bool:
    return "Director" in folder or "Directora" in folder


def scan_agents():
    agents = []
    for dept_dir in sorted(ROOT.glob("[0-9][0-9]-*")):
        dept_id = dept_dir.name
        dept_name = DEPT_NAMES.get(dept_id, dept_id)
        folders = sorted(p for p in dept_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
        directors = [p for p in folders if is_director(p.name)]
        director_slug = to_slug(directors[0].name) if directors else None

        for agent_dir in folders:
            folder = agent_dir.name
            slug = to_slug(folder)
            forged = any(
                (agent_dir / f).exists() and (agent_dir / f).stat().st_size > 0
                for f in ("Personalidad.md", "Rol.md")
            ) and (agent_dir / "skills").is_dir()

            if dept_id == "00-Agentes-Generales":
                if slug == "luffy-coordinador":
                    tipo = "coordinador"
                    reports_to = "Randy"
                else:
                    tipo = "agente-general"
                    reports_to = "luffy-coordinador"
            elif is_director(folder):
                tipo = "director"
                reports_to = "luffy-coordinador"
            else:
                tipo = "celula"
                reports_to = director_slug or "luffy-coordinador"

            role_words = folder
            for prefix in list(MULTI_PERSONAJE) + [personaje_from(folder).replace(" ", "-"), personaje_from(folder)]:
                if role_words.startswith(prefix.replace(" ", "-") + "-"):
                    role_words = role_words[len(prefix.replace(" ", "-")) + 1 :]
                    break
            role_label = role_words.replace("-", " ")
            responsabilidades = RESP_OVERRIDES.get(
                slug,
                [f"Ejecutar responsabilidades de {role_label} en {dept_name}", "Reportar al supervisor con evidencia"],
            )

            agents.append(
                {
                    "id": slug,
                    "nombre": folder,
                    "personaje": personaje_from(folder),
                    "tipo": tipo,
                    "reports_to": reports_to,
                    "direct_reports": [],
                    "departamento": dept_name,
                    "departamento_id": dept_id,
                    "path": str(agent_dir.relative_to(ROOT)),
                    "responsabilidades": responsabilidades,
                    "puede_delegar": tipo in ("coordinador", "director", "agente-general")
                    or (tipo == "celula" and forged),
                    "puede_responder_usuario": slug == "luffy-coordinador",
                    "forged": forged or slug in LIVE_SLUGS.values(),
                    "status": "live" if slug in LIVE_SLUGS.values() else ("forged" if forged else "stub"),
                }
            )
    by_id = {a["id"]: a for a in agents}
    for a in agents:
        if a["reports_to"] in by_id:
            by_id[a["reports_to"]]["direct_reports"].append(a["id"])
    for a in agents:
        a["direct_reports"] = sorted(a["direct_reports"])
    return agents


def yaml_escape(s: str) -> str:
    if any(c in s for c in ":#{}[],&*?|>!%@`'\""):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def write_organigrama(agents):
    lines = [
        "# Nakamas Agents — Organigrama canónico",
        "# Fuente de verdad de jerarquía. Vegapunk debe consultarlo antes de forjar agentes.",
        "version: 1",
        "owner: Randy",
        "coordinator: luffy-coordinador",
        "cadena:",
        "  - Randy",
        "  - luffy-coordinador",
        "  - director | agente-general",
        "  - celula",
        "  - especialista",
        "reglas:",
        "  solo_luffy_responde_usuario: true",
        "  reportes_suben_por_cadena: true",
        "  contratos:",
        "    task: organization/contratos/task-contract.md",
        "    report: organization/contratos/report-contract.md",
        "  protocolo: organization/protocolo-reportes.md",
        "agentes:",
    ]
    for a in agents:
        lines.append(f"  - id: {a['id']}")
        lines.append(f"    nombre: {yaml_escape(a['nombre'])}")
        lines.append(f"    personaje: {yaml_escape(a['personaje'])}")
        lines.append(f"    tipo: {a['tipo']}")
        lines.append(f"    reports_to: {a['reports_to']}")
        if a["direct_reports"]:
            lines.append("    direct_reports:")
            for d in a["direct_reports"]:
                lines.append(f"      - {d}")
        else:
            lines.append("    direct_reports: []")
        lines.append(f"    departamento: {yaml_escape(a['departamento'])}")
        lines.append(f"    departamento_id: {a['departamento_id']}")
        lines.append(f"    path: {a['path']}")
        lines.append("    responsabilidades:")
        for r in a["responsabilidades"]:
            lines.append(f"      - {yaml_escape(r)}")
        lines.append(f"    puede_delegar: {'true' if a['puede_delegar'] else 'false'}")
        lines.append(f"    puede_responder_usuario: {'true' if a['puede_responder_usuario'] else 'false'}")
        lines.append(f"    status: {a['status']}")
    out = ROOT / "organization" / "organigrama.yaml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


POS_MARKER = "## Posición organizacional"
HIER_MARKER = "## Jerarquía y reporte"
REPORT_MARKER = "REPORT_TO:"


def rol_section(a) -> str:
    subs = ", ".join(a["direct_reports"]) if a["direct_reports"] else "(ninguno)"
    return f"""## Posición organizacional

- Supervisor: `{a['reports_to']}`
- Subordinados directos: `{subs}`
- Departamento: {a['departamento']}
- Nivel jerárquico: `{a['tipo']}`
- Puede delegar: `{'sí' if a['puede_delegar'] else 'no'}`
- Puede responder al usuario: `{'sí' if a['puede_responder_usuario'] else 'no'}`
"""


def delegacion_section(a) -> str:
    can_delegate = ", ".join(f"`{x}`" for x in a["direct_reports"]) if a["direct_reports"] else "(ninguno registrado; usar DELEGATION_REQUIRED hacia Luffy si hace falta)"
    return f"""## Jerarquía y reporte

- A quién puede delegar: {can_delegate}
- A quién debe reportar (`REPORT_TO`): `{a['reports_to']}`
- Qué resultados debe validar: evidencia, criterios de aceptación y contrato `organization/contratos/report-contract.md`
- Cuándo debe escalar: bloqueos, contradicciones transversales, falta de autoridad o impacto fuera de su departamento
- Formato de reporte: campos `REPORT_*` de `organization/contratos/report-contract.md`

### Campos mínimos al reportar

```text
TASK_ID:
PARENT_TASK_ID:
MISSION_ID:
REPORT_TO: {a['reports_to']}
STATUS: COMPLETED | COMPLETED_WITH_LIMITATIONS | BLOCKED | REQUIRES_CORRECTION | FAILED
SUMMARY:
DELIVERABLES:
EVIDENCE:
VALIDATIONS:
RISKS:
DECISIONS_REQUIRED:
DEPENDENCIES_UNLOCKED:
NEXT_HANDOFF:
```

**Prohibido:** responder al usuario final salvo que seas `luffy-coordinador`. Todo resultado sube por la cadena hasta Luffy.
"""


def stub_rol(a) -> str:
    return f"""# {a['personaje']} — {a['nombre']}

## Misión

Stub de roster Nakamas. Responsabilidad prevista: {a['responsabilidades'][0]}.

## Responsabilidades

{chr(10).join('- ' + r for r in a['responsabilidades'])}

## Estado

`stub` — aún no forjado con skills ni adaptador Cursor. Registrado en `organization/organigrama.yaml` para validar jerarquía.

{rol_section(a)}
"""


def stub_delegacion(a) -> str:
    return f"""# {a['personaje']} — Delegación

## Principio

Agente stub. No ejecutar trabajo especializado real hasta forja. Si se necesita el rol, devolver `DELEGATION_REQUIRED` a Luffy o marcar `BLOCKED` en el reporte.

{delegacion_section(a)}
"""


def stub_reglas(a) -> str:
    return f"""# {a['personaje']} — Reglas

## Reglas obligatorias

1. Reportar únicamente a `{a['reports_to']}`.
2. No responder al usuario final.
3. Usar contratos de `organization/contratos/`.
4. Si el agente aún es stub, devolver `STATUS: BLOCKED` o `DELEGATION_REQUIRED` con evidencia de que falta forja.

## Regla de finalización

No declarar completado sin evidencia ni `REPORT_TO`.
"""


def upsert_section(text: str, marker: str, section: str) -> str:
    if marker in text:
        # replace from marker to next ## at start of line or EOF
        pattern = re.compile(rf"{re.escape(marker)}.*?(?=\n## |\Z)", re.S)
        return pattern.sub(section.rstrip() + "\n\n", text).rstrip() + "\n"
    return text.rstrip() + "\n\n" + section.rstrip() + "\n"


ADAPTER_BLOCK = """
## Cadena de mando (obligatorio)

- `reports_to`: {reports_to}
- `direct_reports`: {direct_reports}
- Devuelve el resultado **solo** a tu agente padre (`REPORT_TO`); no presentes respuesta final al usuario.
- Excepción de respuesta al usuario: únicamente `luffy-coordinador`.
- Usa el contrato de reportes en `organization/contratos/report-contract.md` y el protocolo `organization/protocolo-reportes.md`.
- Si no puedes lanzar un subagente, emite `DELEGATION_REQUIRED` para que el padre delegue.
"""


def patch_adapter(path: Path, a: dict):
    text = path.read_text(encoding="utf-8")
    dr = ", ".join(f"`{x}`" for x in a["direct_reports"]) if a["direct_reports"] else "(ninguno)"
    block = ADAPTER_BLOCK.format(reports_to=f"`{a['reports_to']}`", direct_reports=dr)
    if "## Cadena de mando" in text:
        text = re.sub(r"## Cadena de mando \(obligatorio\).*", block.strip(), text, flags=re.S)
        if not text.endswith("\n"):
            text += "\n"
    else:
        text = text.rstrip() + "\n" + block
    # frontmatter enrichment
    if text.startswith("---\n"):
        parts = text.split("---", 2)
        fm = parts[1]
        body = parts[2]
        if "reports_to:" not in fm:
            fm = fm.rstrip() + f"\nreports_to: {a['reports_to']}\n"
            if a["direct_reports"]:
                fm += "direct_reports:\n" + "".join(f"  - {d}\n" for d in a["direct_reports"])
            else:
                fm += "direct_reports: []\n"
            text = f"---{fm}---{body}"
            if not text.endswith("\n"):
                text += "\n"
    path.write_text(text, encoding="utf-8")


def patch_agent_docs(a: dict):
    agent_dir = ROOT / a["path"]
    rol = agent_dir / "Rol.md"
    deleg = agent_dir / "Delegacion.md"
    reglas = agent_dir / "Reglas.md"

    if a["status"] == "stub" and (not rol.exists() or rol.stat().st_size == 0):
        rol.write_text(stub_rol(a), encoding="utf-8")
    else:
        text = rol.read_text(encoding="utf-8") if rol.exists() else f"# {a['personaje']}\n"
        rol.write_text(upsert_section(text, POS_MARKER, rol_section(a)), encoding="utf-8")

    if a["status"] == "stub" and (not deleg.exists() or deleg.stat().st_size == 0):
        deleg.write_text(stub_delegacion(a), encoding="utf-8")
    else:
        text = deleg.read_text(encoding="utf-8") if deleg.exists() else f"# {a['personaje']} — Delegación\n"
        if REPORT_MARKER not in text or HIER_MARKER not in text:
            text = upsert_section(text, HIER_MARKER, delegacion_section(a))
        elif HIER_MARKER in text:
            text = upsert_section(text, HIER_MARKER, delegacion_section(a))
        deleg.write_text(text, encoding="utf-8")

    if a["status"] == "stub" and (not reglas.exists() or reglas.stat().st_size == 0):
        reglas.write_text(stub_reglas(a), encoding="utf-8")
    elif reglas.exists() and reglas.stat().st_size > 0:
        text = reglas.read_text(encoding="utf-8")
        extra = (
            "\n## Cadena de mando\n\n"
            f"- Reporta a `{a['reports_to']}`.\n"
            f"- `puede_responder_usuario`: {'true' if a['puede_responder_usuario'] else 'false'}.\n"
            "- Usa `organization/contratos/report-contract.md`.\n"
            "- No declares COMPLETED sin EVIDENCE.\n"
        )
        if "## Cadena de mando" not in text:
            reglas.write_text(text.rstrip() + "\n" + extra, encoding="utf-8")


def main():
    agents = scan_agents()
    write_organigrama(agents)
    by_id = {a["id"]: a for a in agents}
    for a in agents:
        patch_agent_docs(a)
    # adapters
    for adapter in (ROOT / ".cursor" / "agents").glob("*.md"):
        slug = adapter.stem
        if slug in by_id:
            patch_adapter(adapter, by_id[slug])
    for adapter in (ROOT / ".claude" / "agents").glob("*.md"):
        slug = adapter.stem
        if slug in by_id:
            patch_adapter(adapter, by_id[slug])
    print(f"agents={len(agents)}")
    print(f"live={sum(1 for a in agents if a['status']=='live')}")
    print(f"stubs={sum(1 for a in agents if a['status']=='stub')}")
    for a in agents:
        print(f"{a['id']}\t{a['tipo']}\t→{a['reports_to']}\t{a['status']}")


if __name__ == "__main__":
    main()
