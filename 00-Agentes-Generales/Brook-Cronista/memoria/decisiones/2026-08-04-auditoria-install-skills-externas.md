# Decisión: Auditoría fail-closed e install selectivo de skills externas

- Fecha: 2026-08-04
- Estado: vigente
- Decisores: Vegapunk-Forjador-Agentes (ejecución); Luffy-Coordinador (misión / REPORT_TO)
- Misión: `audit-install-external-skills` (informe `reports/external-skills-audit-2026-08-04.md`)

## Contexto

Había que incorporar skills de terceros al roster Nakamas sin abrir superficie de ejecución remota, exfiltración, binarios no auditados, telemetría desconocida o licencias incompatibles/ausentes. El gate declarado fue **fail-closed**.

## Decisión

1. **No instalar** skills con FAIL: sin licencia (`design-auditor`), CLI/hooks no confiables (`plasma-wiki`), fuente 404 (`sanitize`), binarios/remoto de setup (`browser-search`).
2. **Instalar** solo PASS / PASS_WITH_LIMITATIONS, mapeadas a agentes destino (Nami/Perona/Miss-Goldenweek, Haredas Terraform×7, Cavendish web-artifacts sin scripts upstream, Luffy+Law cavekit, Vegapunk skill-optimizer, Luffy brainstorming sin `server.cjs`, Shakky+Vivi naming, Brook karpathy-llm-wiki, Kuma test-fixing+playwright, Fujitora owasp, Morgans squad marketingskills curado 13 + index).
3. Excluir por diseño scripts companion peligrosos (`npm install -g`, servers HTTP con asset remoto, stacks Chromium/SearXNG, etc.) aunque el markdown de la skill pase.
4. Tratar como diferido (no bloqueo del gate): Packer HashiCorp opcional; marketing restante; re-audit de sanitize/plasma si hay fuente.

## Alternativas

- Instalar todo el catálogo solicitado y mitigar después — descartado (fail-closed).
- Rechazar también PASS_WITH_LIMITATIONS — descartado; se aceptó markdown con exclusiones de scripts.
- Dump completo de marketingskills (36 opcionales) — no aplicado; curado 13 + index.

## Consecuencias

- Positivo: traza auditada en `reports/external-skills-audit-2026-08-04.md`; `validate_agents` 0 ERRORS en agentes tocados; superficie de ejecución reducida.
- Neutro/negativo: huecos conscientes (Packer, marketing restante, sanitize/plasma) hasta nueva fuente o prioridad de Luffy/Vegapunk.
- Brook conserva karpathy-llm-wiki bajo su árbol de skills; no implica adoptar plasma-wiki.

## Enlaces

- [Bitácora 2026-08-04 — turno audit-install-external-skills](../diario/2026-08-04.md)
- Informe: `reports/external-skills-audit-2026-08-04.md`
