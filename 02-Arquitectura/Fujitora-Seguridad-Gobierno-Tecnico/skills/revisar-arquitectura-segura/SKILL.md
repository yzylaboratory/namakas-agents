---
name: revisar-arquitectura-segura
description: Revisa un diseño de MS/orch/API frente a principios de arquitectura segura y decisiones documentadas. Úsala cuando Law o la misión pidan revisión de seguridad de arquitectura o detectar anti-patrones de diseño.
metadata:
  author: yzylabs
  version: "1.0"
---

# Revisar arquitectura segura

## Propósito

Evaluar si el diseño aplica principios de ingeniería segura (menor privilegio, defensa en profundidad, fallar seguro, defaults seguros, segregación) y si las decisiones de seguridad están documentadas.

## Entradas

- Alcance del sistema o cambio.
- Diagramas, tratado, ADRs, OpenAPI/AsyncAPI o descripción de flujos.
- Clasificación de datos e identidades involucradas (si existen).
- Políticas o principios organizacionales (opcionales).

## Procedimiento

1. Fija alcance incluido/excluido y supuestos.
2. Inventaría componentes, trust boundaries y flujos de datos sensibles.
3. Contrasta el diseño con `references/principios-arquitectura-segura.md`.
4. Busca anti-patrones: trust por red, secretos en config, privilegios amplios, falta de authz por recurso, logging de datos sensibles.
5. Exige o registra Documented Security Decisions faltantes (ASVS 5.0).
6. Clasifica hallazgos por severidad (crítica / alta / media / baja / info).
7. Propón remediaciones concretas o marca hueco si falta información.
8. Resume riesgos residuales aceptables solo si hay owner sugerido.

## Salida

Informe con: alcance, principios evaluados, hallazgos priorizados, decisiones faltantes, remediaciones, residuales.

## Casos límite

- Solo hay un diagrama verbal → estado borrador; lista preguntas bloqueantes.
- Pedido de “aprobar arquitectura” sin Law → entrega juicio técnico; no usurpes decisión final de Law.
- Alcance incluye compliance legal → señala escalamiento; no certifiques.

## Validación

- Cada hallazgo cita evidencia del diseño o ausencia explícita.
- Principios no evaluados están justificados (fuera de alcance).
- No hay secretos reales en el informe.

## Criterios de terminado

- Informe priorizado entregado.
- Remediaciones o preguntas bloqueantes claras para Law.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Tratado + diagrama con authn/authz | Hallazgos trazables + remediaciones |
| Ambiguo | Solo README marketing | Borrador + preguntas bloqueantes |
| Límite | Pedido de sello ISO | Rechazo de certificación; juicio técnico solo |

## Fuentes

- `references/principios-arquitectura-segura.md`
- ISO/IEC 27001:2022 A.8.27 (síntesis) — consultado 2026-08-04
- OWASP ASVS 5.0 Preface — https://asvs.dev/v5.0.0/Preface/ — consultado 2026-08-04
