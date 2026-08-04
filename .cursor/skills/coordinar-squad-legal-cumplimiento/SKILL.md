---
name: coordinar-squad-legal-cumplimiento
description: Coordina el squad Sengoku→Corazon (privacidad), Tsuru (regulación Open Finance) y Cobra (contratos) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa requiera alinear varias células legales o resolver choques entre privacidad, mandato OF y cláusulas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad Legal / Cumplimiento

## Propósito

Orquestar el trabajo departamental sin que Sengoku absorba DPIA, interpretación OF profunda ni redacción contractual, y sin que las células avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental.
- Estado de artefactos (privacidad, mapa regulatorio OF, contratos).
- Estado de forja de células (vivo / stub).
- Restricciones de plazo y dependencias (Jinbe, Robin, Law, Luffy).

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - Corazon: privacidad / datos personales.
   - Tsuru: regulación Open Finance / OB profunda.
   - Cobra: contratos / alianzas fintech.
3. Elabora RACI por entregable (Sengoku = Accountable).
4. Decide secuencia vs paralelo:
   - Paralelo temprano: exploración Corazon + Tsuru.
   - Gate de estabilización privacidad/OF antes de congelar términos vía Cobra.
5. Emite contratos de delegación autocontenidos.
6. Si célula es stub: no simules entrega; `DELEGATION_REQUIRED` a Vegapunk (forja) o `BLOCKED` con plan.
7. Al sincronizar: detecta contradicciones (base legal ≠ consentimiento OF ≠ cláusula DPA) y resuelve o escala.
8. Consolida reporte departamental a Luffy.

## Salida

```md
## Objetivo de la iniciativa
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas
## Stubs / bloqueos
## Contradicciones y resoluciones
## Listo para
```

## Casos límite

- Solo hay duda de producto OB sin issue legal: redirige a Jinbe; Sengoku no captura el roadmap.
- Robin necesita terms ya: exige mínimo de privacidad/OF o marca contrato como draft inestable.
- Tres células stub: coordina a nivel director (gates/memos) y lista forjas requeridas; no inventes Task `brd-*`.

## Validación

- Cada especialista tiene entregable distinto.
- Hay accountable (Sengoku) por iniciativa.
- Stubs no aparecen como “completados”.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones o bloqueos listos para el padre.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- Catálogo Nakamas Legal (`catalogo/agentes-one-piece.yaml`) — Corazon / Tsuru / Cobra
- Cadena de mando — `organization/organigrama.yaml` (direct_reports de Sengoku)
- Práctica de RACI en gobierno de cumplimiento — alineada a roles CMS ISO 37301 — consultado 2026-08-04
