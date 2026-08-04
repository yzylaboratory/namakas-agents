---
name: definir-guardrails-iac
description: Define guardrails cloud y policy-as-code (SCP/policies, tflint/tfsec/Checkov/OPA) para IaC. Úsala cuando se pidan baselines de seguridad, denies organizacionales o gates estáticos pre-apply.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir guardrails IaC

## Propósito

Codificar límites preventivos (organización + análisis estático) para que el error humano no abra regiones, identidades o exposiciones peligrosas.

## Entradas

- Cloud y alcance (org/OU/cuenta).
- Controles CIS / Well-Architected aplicables.
- Toolchain IaC y CI disponible (Paulie).
- Excepciones conocidas (si existen; no las inventes).

## Procedimiento

1. Lista amenazas prioritarias (leave-org, root misuse, regiones no aprobadas, público accidental).
2. Traduce a políticas org (SCP/Azure Policy/Org Policy) con herencia por OU.
3. Define checks estáticos en repo: `fmt`, `validate`, tflint, tfsec/Checkov, OPA/Conftest.
4. Separa fail-closed (bloquea merge/apply) vs warn (deuda registrada).
5. Documenta ownership: Haredas (definición IaC), Fujitora (excepción seguridad), Paulie (wire en CI).
6. Prohíbe secrets en código; exige scanners de secretos en el gate.
7. Entrega matriz control → evidencia → severidad → dueño.

## Salida

```md
## Amenazas cubiertas
## Políticas organizacionales
## Gates estáticos
## Fail-closed vs warn
## Matriz de evidencia
## Excepciones / escalamiento
```

## Casos límite

- “Apaga el deny para un hotfix” → no apruebes; escala Fujitora/Franky con ventana.
- Solo checklist manual → insuficiente; exige al menos un gate automatizable.
- False positives masivos → afina reglas; no desactives el pack entero.

## Validación

- Al menos un deny org-level material documentado.
- Gates estáticos nombrados y accionables en CI.
- Sin aprobación de excepciones de compliance por Haredas.

## Criterios de terminado

- Pack de guardrails listo para wire por Paulie.
- Riesgos residuales y dueños listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | AWS OU Workloads | SCP región + Checkov fail en público + matriz |
| Ambiguo | “Pon seguridad en Terraform” | Preguntas amenazas + set mínimo de gates |
| Límite | Bypass prod sin ticket | BLOCKED + escalamiento Fujitora |

## Fuentes

- CIS Benchmarks — https://www.cisecurity.org/cis-benchmarks (2026-08-04).
- AWS Well-Architected Security Pillar — https://docs.aws.amazon.com/wellarchitected/ (2026-08-04).
- OpenTofu/Terraform validate + community linters (tflint, tfsec/Checkov) — docs oficiales de cada herramienta (2026-08-04).
