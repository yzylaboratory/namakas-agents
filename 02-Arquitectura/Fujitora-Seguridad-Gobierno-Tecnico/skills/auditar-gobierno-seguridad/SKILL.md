---
name: auditar-gobierno-seguridad
description: Audita gobierno técnico de seguridad del diseño o iniciativa (roles, política, oversight, excepciones, supply chain) alineado a NIST CSF 2.0 Govern. Úsala cuando Law pida gobierno, RACI de seguridad o revisión de excepciones/políticas aplicables.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar gobierno de seguridad

## Propósito

Verificar que el diseño/iniciativa tiene gobierno mínimo: dueños, políticas aplicables, oversight y manejo de excepciones — no sustituir un programa ISMS completo.

## Entradas

- Descripción de la iniciativa y stakeholders.
- Políticas/estándares citados como aplicables.
- Excepciones existentes o pedidas.
- Dependencias de terceros / supply chain técnico relevantes.

## Procedimiento

1. Identifica roles: quien acepta riesgo, quien implementa controles, quien verifica.
2. Lista políticas/estándares declarados aplicables al alcance.
3. Busca huecos: sin owner, sin oversight, excepción sin caducidad.
4. Revisa supply chain técnico (librerías críticas, SaaS, IdP, CI) en el alcance.
5. Alinea hallazgos a categorías Govern de NIST CSF 2.0 (contexto, estrategia de riesgo, roles, política, oversight, C-SCRM) solo donde apliquen.
6. Propón acciones de gobierno (no herramientas).
7. Separa “falta de gobierno” de “falta de control técnico”.

## Salida

Informe de gobierno: RACI mínimo, políticas aplicables, excepciones, gaps Govern, acciones.

## Casos límite

- Sin stakeholders nombrados → BLOCKED o borrador con DELEGATION_REQUIRED.
- Pedido de auditoría ISO 27001 completa → fuera de mandato; limita a gobierno del diseño.
- Excepción permanente sin owner → hallazgo crítico de gobierno.

## Validación

- Cada gap tiene impacto en decisión o riesgo.
- No inventa políticas organizacionales inexistentes.
- Distingue gobierno vs. control técnico.

## Criterios de terminado

- RACI o huecos de roles explícitos.
- Excepciones y oversight evaluados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Iniciativa API con owner Law + Dev | RACI + gaps menores |
| Ambiguo | “Gobierna esto” sin stakeholders | Preguntas bloqueantes |
| Límite | Pedido de certificación ISMS | Rechazo de alcance; gobierno técnico solo |

## Fuentes

- NIST CSF 2.0 Govern function — https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final — consultado 2026-08-04
- NIST news CSF 2.0 (governance emphasis) — https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework — consultado 2026-08-04
