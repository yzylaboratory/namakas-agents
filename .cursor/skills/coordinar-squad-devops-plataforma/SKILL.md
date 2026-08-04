---
name: coordinar-squad-devops-plataforma
description: Coordina el squad Franky→Capone Bege (GitOps), Viola (SRE), Haredas (IaC) y Paulie (CI/CD) con RACI, secuencia y contratos de delegación. Úsala cuando una iniciativa de plataforma requiera alinear varias células o resolver choques entre velocidad, confiabilidad e infraestructura.
metadata:
  author: yzylabs
  version: "1.0"
---

# Coordinar squad DevOps / Plataforma

## Propósito

Orquestar el trabajo departamental sin que Franky absorba GitOps, SRE, IaC ni pipelines, y sin que las células avancen en direcciones contradictorias.

## Entradas

- Iniciativa u objetivo departamental.
- Estado de artefactos (pipelines, manifests, módulos IaC, dashboards/SLOs).
- Restricciones de plazo y dependencias externas (Law, Fujitora, Backend, QA).

## Procedimiento

1. Define el resultado único de la iniciativa (una frase).
2. Parte el trabajo:
   - Capone Bege: GitOps / orquestación de sync y releases declarativos.
   - Viola: observabilidad, SLI/SLO, readiness operativa.
   - Haredas: IaC / cloud / provisionamiento.
   - Paulie: CI/CD / automatización y quality gates.
3. Elabora RACI por entregable (Franky Accountable de la iniciativa).
4. Decide secuencia vs paralelo:
   - Paralelo temprano: exploración Paulie + Viola de gates y telemetría.
   - Gate de congelación de entorno/IaC (Haredas) antes de GitOps estable (Capone).
5. Emite contratos de delegación autocontenidos.
6. Si la célula es stub: documenta plan y emite `DELEGATION_REQUIRED`; no inventes ejecución.
7. Al sincronizar: detecta contradicciones (pipeline ≠ GitOps ≠ módulo IaC ≠ alertas) y resuelve o escala.
8. Entrega consolidado departamental a Luffy.

## Salida

```md
## Objetivo de la iniciativa
## RACI del squad
| Entregable | R | A | C | I |
## Plan (secuencia / paralelo)
## Delegaciones emitidas
## Stubs / DELEGATION_REQUIRED
## Contradicciones y resoluciones
## Pendientes / bloqueos
## Listo para
```

## Casos límite

- Especialista sin demo Cursor (stub): planifica roster; no inventes Task `brd-*`.
- Choque Paulie vs Capone (“pipeline imperativo vs GitOps”): Franky decide path canónico o convivencia acotada documentada.
- Urgencia de negocio sin Haredas: MVP con escape hatch y deuda explícita; no fingir IaC completo.

## Validación

- Cada célula tiene un entregable distinto.
- Hay al menos un Accountable (Franky) por iniciativa.
- No hay dos dueños escribiendo el mismo artefacto crítico sin regla de merge.

## Criterios de terminado

- Plan y RACI claros.
- Delegaciones listas para Tasks cuando existan agentes forjados.
- Contradicciones materiales resueltas o escaladas.

## Fuentes

- DORA Platform engineering — extensibility, clear feedback, avoid ivory tower — https://dora.dev/capabilities/platform-engineering/ (consultado 2026-08-04)
- Organigrama Nakamas — `organization/organigrama.yaml` (squad DevOps)
