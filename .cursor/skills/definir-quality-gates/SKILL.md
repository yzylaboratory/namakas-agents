---
name: definir-quality-gates
description: Define e integra quality gates en el pipeline (tests, cobertura, SAST/SCA, scans, política de flaky). Úsala cuando se pida umbrales de calidad, gates de merge/release o política de fallos; no inventes política de QA de producto — acuerda o escala.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir quality gates

## Propósito

Convertir criterios de calidad/seguridad acordados en gates automatizados que fallen de forma explícita y atribuible.

## Entradas

- Criterios de aceptación de calidad (de Franky/QA/Seguridad).
- Herramientas disponibles (test runners, coverage, SAST, SCA, container scan).
- Severidad mínima que bloquea merge vs release.
- Histórico de flaky si existe.

## Procedimiento

1. Inventaría gates candidatos por etapa (PR vs main vs release).
2. Asigna cada gate a un job con umbral y artefacto de reporte.
3. Diferencia “informativo” vs “bloqueante”; documenta ambos.
4. Define política flaky: cuarentena, ticket dueño, tiempo máximo en cuarentena.
5. Integra SAST/SCA/container scan con severidades acordadas — no inventes CVSS cutoffs.
6. Asegura que el fallo muestre mensaje accionable (qué falló, dónde, cómo reproducir).
7. Si faltan criterios de QA de producto, escala; no substitutes estrategia de pruebas.
8. Entrega configuración de gates + tabla umbrales + excepciones temporales con expiry.

## Salida

```md
## Gates por etapa
## Umbrales
## Flaky policy
## Reportes/artefactos
## Excepciones (expiry)
## Riesgos
```

## Casos límite

- Cobertura 0% legacy → gate incremental (no bajar) o baseline acordado; no 90% mágico.
- Scan ruidoso → severidad + allowlist versionada; no `continue-on-error` silencioso en release.
- Conflicto QA vs velocidad → opciones con trade-offs a Franky; no decidas solo.

## Validación

- Cada gate bloqueante tiene dueño y umbral.
- Flaky no se “skippea” sin cuarentena.
- Reportes persistidos como artefactos o enlaces.

## Criterios de terminado

- Merge/release falla solo por reglas documentadas.
- Excepciones tienen fecha de caducidad.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Unit + coverage 70% + SCA high | Jobs bloqueantes con umbral y reporte |
| Ambiguo | “Más calidad” | Preguntas + propuesta de gates mínimos PR/main |
| Límite | Suite 15% flaky | Política cuarentena + lista tests; no ignore global |

## Fuentes

- DORA — Change failure rate context — https://dora.dev/ (2026-08-04).
- OWASP — Dependency-Check / SCA practices (reference) — https://owasp.org/www-community/Component_Analysis (2026-08-04).
- GitHub Docs — About code scanning — https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning (2026-08-04).
