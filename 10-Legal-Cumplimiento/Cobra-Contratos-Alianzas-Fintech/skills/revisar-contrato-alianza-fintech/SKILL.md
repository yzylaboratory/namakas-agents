---
name: revisar-contrato-alianza-fintech
description: Revisa MSA, partnership o collaboration agreements fintech y produce gaps, riesgos y remediaciones. Úsala cuando haya un borrador o term sheet de alianza bancaria/fintech que deba auditarse antes de negociar o firmar.
metadata:
  author: yzylabs
  version: "1.0"
---

# Revisar contrato de alianza fintech

## Propósito

Convertir un borrador o term sheet de alianza fintech en un informe accionable: cláusulas presentes/faltantes, asimetrías, red flags y remediaciones priorizadas.

## Entradas

- Borrador contractual, term sheet o lista de posiciones.
- Partes, tipo de alianza (BaaS, API partnership, white-label, marketplace, plataforma).
- Jurisdicción conocida (si existe).
- Dependencias operativas (API, datos, marca, clientes).
- Restricciones de Sengoku / negocio.

## Procedimiento

1. Clasifica el instrumento (MSA + schedules, collaboration agreement, API framework, SOW).
2. Inventaría secciones: alcance, fees, API, SLA, datos, IP, confidentiality, audit, compliance, liability, indemnification, term/termination, exit, governance, change control.
3. Marca cada sección: OK / gap / ambiguo / asimétrico.
4. Extrae red flags (caps unilaterales, exclusividad abusiva, cambio sin aviso, audit nulo, exit vacío).
5. Propón remediación por gap (texto sugerido o ask negociador).
6. Asigna criticidad y dueño (Cobra / Corazon / Tsuru / Sabo / Du-Feld / Fujitora / Sengoku).
7. Declara explícitamente que el output es borrador de análisis, no dictamen vinculante.

## Salida

```md
## Instrumento y partes
## Resumen ejecutivo (top riesgos)
## Matriz de cláusulas (OK/gap/asimétrico)
## Red flags
## Remediaciones priorizadas
## Dueños y handoffs
## Ask / fallback / walk-away
## Pendientes / supuestos
```

## Casos límite

- Solo hay deck comercial sin cláusulas → produce checklist mínimo de MSA + preguntas bloqueantes.
- Jurisdicción desconocida → no inventes ley aplicable; bloquea firma y escala a Sengoku.
- Conflicto con producto Sabo ya publicado → documenta drift y escala.

## Validación

- Toda remediación apunta a una cláusula o sección.
- Privacidad/regulación no se “resuelven” inventando texto normativo.
- Hay al menos una posición walk-away si hay red flag crítico.

## Criterios de terminado

- Sengoku puede priorizar negociación sin releer el contrato completo.
- Gaps críticos tienen dueño y ask.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | MSA BaaS con API schedule incompleto | Matriz + gaps API/SLA/exit + remediaciones |
| Ambiguo | “Revisa el partnership” sin adjunto | Lista de artefactos mínimos + BLOCKED parcial |
| Límite | Cap de liability que excluye data breach del partner | Red flag crítico + walk-away sugerido |

## Fuentes

- Mayer Brown — Collaboration Agreements for Customer-Facing Platforms (2025-11-21) — https://www.mayerbrown.com/en/insights/publications/2025/11/collaboration-agreements-for-customer-facing-platforms (2026-08-04).
- ABA — SaaS Agreements: Key Contractual Provisions (2021-11) — https://www.americanbar.org/groups/business_law/resources/business-law-today/2021-november/saas-agreements-key-contractual-provisions/ (2026-08-04).
