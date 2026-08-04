---
name: coordinar-squad-qa
description: Coordina el squad Usopp→Tashigi (funcional/regulación), Kalifa (APIs/contratos), Kuma (automatización) y Kaido (carga/rendimiento) con RACI y contratos de delegación. Úsala cuando una misión QA requiera alinear varias células o resolver choques de prioridad entre tipos de prueba.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad QA

## Propósito

Orquestar el trabajo departamental sin que Usopp absorba ejecución especializada, y sin que las células avancen en direcciones contradictorias.

## Entradas

- Objetivo único de la misión QA / release.
- Estrategia o backlog RBT.
- Estado de artefactos (casos, contratos, automatización, baselines de perf).
- Restricciones de plazo y dependencias externas (Robin, Franky, Law, Legal).

## Procedimiento

1. Define el resultado único de la misión (una frase).
2. Parte el trabajo:
   - Tashigi: funcional / evidencia regulatoria de prueba.
   - Kalifa: APIs / contratos.
   - Kuma: automatización / estabilidad en pipeline.
   - Kaido: carga / rendimiento.
3. Elabora RACI por entregable (Usopp = Accountable de coherencia departamental).
4. Decide secuencia vs paralelo:
   - Paralelo temprano: inventario riesgos + contratos + candidatas a automatizar.
   - Gate: build candidato estable antes de carga (Kaido) y antes de firmar readiness.
5. Emite contratos de delegación autocontenidos.
6. Si células son stub: documenta plan roster + `DELEGATION_REQUIRED` a Luffy; no inventes `brd-*`.
7. Al sincronizar: detecta contradicciones (funcional pasa / contrato falla / perf rompe SLO) y resuelve o escala.
8. Entrega consolidado departamental a Luffy.

## Salida

```md
## Objetivo de la misión QA
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas / DELEGATION_REQUIRED
## Contradicciones y resoluciones
## Pendientes / bloqueos
## Listo para
```

## Casos límite

- Solo una célula relevante: RACI mínimo; no inventes trabajo para las demás.
- Kalifa bloqueada por OpenAPI incompleto: escala Robin vía Luffy; no rehagas el tratado.
- Presión de release vs suites rojas: Usopp propone go-with-risks o no-go; no oculta fallos.

## Validación

- Cada especialista tiene entregable distinto.
- Hay accountable (Usopp) por misión.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge.
- Identidad correcta: no se enruta a `brd-todologo`.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para Tasks cuando existan agentes vivos, o `DELEGATION_REQUIRED` explícito.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- ISTQB CTAL-TM v3.0 — Managing the Team / stakeholder coordination — https://istqb.org/certifications/certified-tester-advanced-level-test-management-ctal-tm-v3-0/ (2026-08-04)
- Catálogo Nakamas QA (Tashigi, Kalifa, Kuma, Kaido) — `organization/organigrama.yaml`
