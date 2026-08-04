---
name: orquestar-activacion-partner
description: Orquesta la activación operativa del partner (portal/PRM, contactos, roles, certs mínimas, primer engagement). Úsala cuando haya que pasar de contrato firmado a partner usable en el canal.
metadata:
  author: yzylabs
  version: "1.0"
---

# Orquestar activación de partner

## Propósito

Eliminar fricción administrativa y de readiness para que el partner pueda operar: accesos, roles, certificaciones mínimas y primer engagement conjunto.

## Entradas

- Acuerdo firmado y tier.
- Lista de contactos y roles esperados.
- Estado de portal/PRM, CRM deal-reg, LMS.
- Certificaciones mínimas del programa.
- Dependencias técnicas (sandbox/API → Sabo) si aplica.

## Procedimiento

1. Checklist de provisioning: cuentas portal/PRM, permisos, deal registration, MDF (si aplica), canal de soporte.
2. Fija SLA time-to-portal (target &lt;48h) o documenta excepción manual con dueño.
3. Identifica RACI de contactos vendor↔partner (primary, technical, executive sponsor).
4. Define readiness mínima por rol (sales vs technical vs delivery) — JIT, no firehose.
5. Agenda kickoff + primer engagement conjunto (demo, opportunity review).
6. Registra blockers con owner y ETA; escala a Buggy si el blocker es comercial/capacidad.
7. Si el blocker es API/sandbox/portal developer → empaquetar requisitos para Sabo/Koala vía Buggy/Luffy.
8. Entrega runbook de activación + estado green/yellow/red.

## Salida

```md
## Estado de activación (RAG)
## Provisioning checklist
## Contactos / RACI
## Readiness mínima por rol
## Primer engagement
## Blockers + owners + ETA
## Escalamiento propuesto
```

## Casos límite

- Partner sin IT dedicado → path low-tech (PDF + calls) sin fingir self-service completo.
- Multi-brand partner → scopes de portal por brand/tier.
- Cert obligatoria larga → no bloquees deal-reg; paraleliza tracks.

## Validación

- Accesos críticos tienen estado y fecha.
- Hay primary contact bilateral.
- Blockers tienen owner; ninguno “en el aire”.
- No se produce contenido enablement (Mr. 3) ni se diseña OpenAPI (Sabo).

## Criterios de terminado

- Partner puede iniciar fase 1 del plan 30-60-90.
- RAG y blockers visibles para Buggy.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Firma + portal OK | Checklist verde + kickoff agendado |
| Ambiguo | “Actívalo” sin contactos | Bloqueo explícito + plantilla de contactos requerida |
| Límite | Sandbox API roto | Activación comercial parcial + handoff Sabo |

## Fuentes

- 76nord First 90 Days (portal &lt;48h) — https://76nord.com/blog/20250618-partner-onboarding-90-days/ (2026-08-04).
- Mindmatrix PRM & TTV — https://channelandsalesenablementblog.mindmatrix.net/using-prm-for-partner-onboarding-how-to-use-ai-and-automation-to-slash-time-to-value/ (2026-08-04).
- Pedowitz structured onboarding — https://www.pedowitzgroup.com/design-structured-partner-onboarding-program (2026-08-04).
