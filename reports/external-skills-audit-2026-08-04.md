# External Agent Skills — Security Audit & Install

**Date:** 2026-08-04  
**Auditor:** vegapunk-forjador-agentes  
**REPORT_TO:** luffy-coordinador  
**Gate:** fail-closed (remote code, secret exfil, untrusted binaries, prompt-injection/tool-abuse, unknown telemetry, incompatible license)

## Verdict table

| # | Skill / repo | Security | Target agent(s) | Installed paths | Blocked reason / limitations |
|---|---|---|---|---|---|
| 1 | oiloil-ui-ux-guide (`oil-oil/ui-ux-guide`; URL alias oiloil-ui-ux-guide) | **PASS** | Nami, Perona, Miss-Goldenweek | `07-UX-UI/{Nami,Perona,Miss-Goldenweek}/skills/oiloil-ui-ux-guide/`; `.cursor/skills/oiloil-ui-ux-guide/` | Apache-2.0; markdown-only. Reviewed `skills/oiloil-ui-ux-guide/SKILL.md`. |
| 2 | hashicorp/agent-skills (Terraform subset) | **PASS** | Haredas-IaC-Cloud | 7 skills under `03-DevOps-Plataforma/Haredas-IaC-Cloud/skills/` + mirrors; `terraform-search-import/scripts/list_resources.sh` | MPL-2.0. Packer/provider-dev skills not installed (out of Haredas primary scope). Local `terraform`/`jq` script inspected — no remote exec. |
| 3 | Ashutos1997/claude-design-auditor-skill | **FAIL** | — | — | **No license** declared (GitHub `license: null`). Fail-closed. |
| 4 | anthropics/skills `web-artifacts-builder` | **PASS_WITH_LIMITATIONS** | Cavendish | `06-Frontend/Cavendish-Arquitectura-Web/skills/web-artifacts-builder/` + mirrors | Skill `LICENSE.txt` Apache-2.0. Upstream scripts (`init-artifact.sh` does `npm install -g pnpm`, pulls many packages, extracts tarball) **not installed/executed**. Markdown guidance only. |
| 5 | JuliusBrussee/blueprint → redirects to **cavekit** | **PASS** | Luffy (+ Law for spec) | `cavekit-grill`, `cavekit-spec` on Luffy; `cavekit-spec-arquitectura` on Law | MIT. URL renamed to cavekit; planning skills grill/spec adapted. |
| 6 | hqhq1025/skill-optimizer | **PASS** | Vegapunk only | `skill-miner`, `skill-generalizer`, `skill-personalizer` + `scan_sessions.py` (local-only) | MIT. Python scanner uses local session paths only (no network). |
| 7 | obra/superpowers `brainstorming` | **PASS_WITH_LIMITATIONS** | Luffy | `00-Agentes-Generales/Luffy-Coordinador/skills/brainstorming/` | MIT. Companion `server.cjs` loads brand asset from `primeradiant.com` and runs local HTTP server — **scripts not installed**. Text-only adaptation. |
| 8 | glacierphonk/naming | **PASS_WITH_LIMITATIONS** | Shakky, Vivi | `…/Shakky…/skills/naming/`, `…/Vivi-Escritor/skills/naming/` | MIT. Public whois/curl availability checks (not secret exfil). |
| 9 | Astro-Han/karpathy-llm-wiki | **PASS** | Brook-Cronista ONLY | `00-Agentes-Generales/Brook-Cronista/skills/karpathy-llm-wiki/` + `scripts/check_evidence.py` | MIT. Evidence script local filesystem only. |
| 10 | plasma-ai/wiki `wiki/skills/wiki` | **FAIL** | — | — | Requires `pipx install plasma-wiki` (untrusted binary) + `wiki trust` authorizing `.wiki/wiki.py` hooks. Fail-closed. |
| 11 | test-fixing (claude-skills-marketplace) | **PASS** | Kuma (+ Usopp Rol pointer) | `08-QA/Kuma-Automatizacion-Pruebas/skills/test-fixing/` | Apache-2.0; markdown-only. |
| 12 | agamm/claude-code-owasp | **PASS** | Fujitora | `02-Arquitectura/Fujitora-Seguridad-Gobierno-Tecnico/skills/owasp-security/` | MIT; markdown under `.claude/skills/owasp-security/`. |
| 13 | openclaw/skills …/sanitize | **FAIL** | — | — | Repo/path **404** (`openclaw/skills` Not Found). Cannot audit. |
| 14 | Johell1NS/browser-search | **FAIL** | — | — | `setup.sh` runs `npm install` + downloads CloakBrowser Chromium binary; Camofox/SearXNG remote fetch stack. Untrusted binary + remote code surface. |
| 15 | coreyhaines31/marketingskills | **PASS** (curated) | Morgans + Carrot/Shakky/Bartolomeo/Vivi | curated skills + `marketingskills-index` | MIT. 13 installed + index; 36 listed optional (not dumped). |
| 16 | testdino-hq/playwright-skill | **PASS** | Kuma | `08-QA/Kuma-Automatizacion-Pruebas/skills/playwright-skill/` | MIT; markdown guides only (no binaries in tree). |

## Evidence (files reviewed)

- GitHub API trees + raw SKILL.md / scripts for each repo (2026-08-04).
- Grep for `curl|`, telemetry, `eval`, exfil, `child_process`, remote installs.
- Licenses via GitHub API + LICENSE files.
- `validate_agents.py` on touched agent parents: **0 ERRORS** (warnings only: missing ## Procedimiento/Salida/Validación on upstream-shaped skills).

## Not installed (by design)

- HashiCorp Packer / provider-development skills (not primary Haredas craft for this pass).
- Design auditor (no license).
- Plasma wiki CLI skill.
- Browser-search full stack.
- Sanitize (missing source).
- Marketing skills optional list (see `marketingskills-index`).
- Upstream install scripts (`npx skills add …`, companion servers, artifact init scripts).

## Activity MCP

`activity_start` → `unknown_agent: vegapunk-forjador-agentes` — badges skipped per mission.
