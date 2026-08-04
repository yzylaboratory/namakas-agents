---
name: terraform-policy
description: Write, test, or convert Terraform Policy files (.policy.hcl, .policytest.hcl, Sentinel→tfpolicy). Triggers: policy.hcl, policytest, convert sentinel, tfpolicy, write a policy. Use when Terraform/IaC work needs terraform-policy.
metadata:
  author: yzylabs
  version: "1.0"
  source: https://github.com/hashicorp/agent-skills (skill terraform-policy)
  license: MPL-2.0
  audited: 2026-08-04
---

# terraform-policy

**UTILITY SKILL** — INVOKES: [tfpolicy-author](references/tfpolicy-author.md) | [tfpolicy-test](references/tfpolicy-test.md)

## USE FOR:

- Writing a new `.policy.hcl` policy from a description or requirement
- Converting a `.sentinel` policy to Terraform Policy
- Writing or debugging a `.policytest.hcl` test file
- Migrating a Sentinel policy library to Terraform Policy

## DO NOT USE FOR:

- Writing `.tftest.hcl` files for Terraform modules — use `terraform-test`
- General Terraform HCL authoring — use `terraform-style-guide`

## Routing

| Task | Sub-skill |
|------|-----------|
| Write or convert a `.policy.hcl` policy | [tfpolicy-author](references/tfpolicy-author.md) |
| Write or debug a `.policytest.hcl` test | [tfpolicy-test](references/tfpolicy-test.md) |

## Examples

- "Block EC2 instances without encryption" → [tfpolicy-author](references/tfpolicy-author.md)
- "Convert this Sentinel policy to tfpolicy" → [tfpolicy-author](references/tfpolicy-author.md)
- "Write a policytest for my EBS policy" → [tfpolicy-test](references/tfpolicy-test.md)

## Troubleshooting

- **Wrong skill triggered?** Load the sub-skill directly from the routing table above.

```bash
npx skills add hashicorp/agent-skills/terraform/terraform-policy/skills/tfpolicy-author
npx skills add hashicorp/agent-skills/terraform/terraform-policy/skills/tfpolicy-test
```

## Fuentes / atribución

- Fuente: https://github.com/hashicorp/agent-skills (skill terraform-policy)
- Licencia: MPL-2.0
- Fecha de auditoría e instalación: 2026-08-04
- Security gate: PASS
- Adaptado para Nakamas Agents (Vegapunk). No ejecutar scripts de instalación remotos del upstream.

## Límites Nakamas

- REPORT_TO: `haredas-iac-cloud`
- Primary owner: `haredas-iac-cloud`. GitOps de apps → Capone Bege; CI → Paulie; SRE → Viola.
- Scripts locales (p.ej. list_resources.sh) solo tras inspección; no curl|bash remoto.
- FORBIDDEN: Tripulación `brd-*` / `yzy-*`, inventar BIAN/FIBO, Olvia/`brd-second-brain`.

