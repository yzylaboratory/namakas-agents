---
name: definir-controles-tecnicos
description: Mapea amenazas o requisitos a controles técnicos verificables (ASVS/CSF/ISO) con evidencia de verificación. Úsala después de modelar amenazas o cuando Law pida un plan de controles trazable.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir controles técnicos

## Propósito

Traducir amenazas/requisitos en controles preventivos, detective o correctivos con criterio de verificación — sin checklist genérico.

## Entradas

- Modelo de amenazas (`modelar-amenazas`) o requisitos de seguridad explícitos.
- Nivel de rigor pedido (p. ej. ASVS L1/L2) si aplica.
- Restricciones de plataforma (cloud, gateway, IdP).

## Procedimiento

1. Toma cada amenaza/requisito priorizado.
2. Propón 1–N controles; etiqueta tipo P/D/C.
3. Cita referencia cuando ayude (capítulo ASVS 5.0, outcome CSF Protect/Identify, control Annex A).
4. Define evidencia de verificación (test, config, review, monitor).
5. Marca controles ya existentes vs. a implementar.
6. Calcula residual tras controles propuestos (cualitativo).
7. Evita controles duplicados o que se debiliten entre sí.
8. Prepara filas listas para `HANDOFF_SEGURIDAD`.

## Salida

Matriz amenaza/requisito → control → tipo → referencia → evidencia → residual.

## Casos límite

- Amenaza sin control viable en alcance → residual explícito + escalamiento.
- Pedido de “implementar WAF y listo” sin traza → rechaza como único control; exige modelo.
- Conflicto costo vs. riesgo → documenta opciones; Law decide.

## Validación

- Cero controles huérfanos (sin traza).
- Cada control tiene evidencia de verificación.
- Referencias de framework no inventadas.

## Criterios de terminado

- Matriz completa para amenazas en alcance (o huecos marcados).
- Residual documentado.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | T-01..T-05 priorizados | Matriz con P/D/C y evidencia |
| Ambiguo | “Pon ASVS completo” sin alcance | Exige nivel + capítulos aplicables |
| Límite | Amenaza física fuera de IT | Fuera de alcance; no inventes control cloud |

## Fuentes

- OWASP ASVS 5.0 — https://asvs.dev/v5.0.0/Preface/ — consultado 2026-08-04
- NIST CSF 2.0 — https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final — consultado 2026-08-04
- ISO/IEC 27001:2022 Annex A (p. ej. A.8.27 y controles tecnológicos relacionados) — consultado 2026-08-04
