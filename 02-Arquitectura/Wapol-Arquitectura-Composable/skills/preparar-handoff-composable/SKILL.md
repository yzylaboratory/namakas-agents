---
name: preparar-handoff-composable
description: Empaqueta el handoff de arquitectura composable (PBCs, MACH, composición, swap, orquestación) para Law u otros especialistas. Úsala al cerrar un diseño o auditoría composable antes de implementación o ADR.
metadata:
  author: yzylabs
  version: "1.0"
---

# Preparar handoff composable

## Propósito

Consolidar artefactos de arquitectura composable en un paquete accionable para Law, Robin, Enel, Fujitora, Backend o Frontend — con gaps y dueños explícitos.

## Entradas

- Scorecard MACH, catálogo PBC, blueprint, auditoría de swap, spec de orquestación (los que existan).
- Decisiones abiertas y restricciones de Law.
- Destinatario del handoff.

## Procedimiento

1. Identifica destinatario primario (Law por defecto) y secundarios.
2. Resume objetivo, alcance y no-objetivos en ≤10 líneas.
3. Adjunta o referencia artefactos producidos (rutas de archivos).
4. Lista decisiones que solo Law puede cerrar (ADRs).
5. Lista handoffs especializados (Enel/Fujitora/Robin/Noland/Sabo) con trigger.
6. Enumera criterios de aceptación verificables para “composable-ready”.
7. Separa `listo para implementar` vs `bloqueado`.
8. Cierra con riesgos, fuentes y `REPORT_TO` hacia Law.

## Salida

```md
## HANDOFF_COMPOSABLE
### Destinatario
### Resumen ejecutivo
### Artefactos (rutas)
### Decisiones para Law (ADR)
### Handoffs especializados
### Criterios composable-ready
### Listo / Bloqueado
### Riesgos
### Fuentes
### REPORT_TO: law-director-arquitectura
```

## Casos límite

- Faltan artefactos clave → `COMPLETED_WITH_LIMITATIONS` o `BLOCKED`, no inventes.
- Conflicto entre especialistas → documenta y escala a Law; no arbitres en silencio.
- Destinatario pide OpenAPI formal → incluye trigger a Robin, no sustituyas.

## Validación

- Destinatario y criterios explícitos.
- Gaps con dueño.
- Sin respuesta al usuario final.

## Criterios de terminado

- El destinatario puede actuar o pedir corrección sin reabrir el discovery completo.
- El reporte cumple contrato `organization/contratos/report-contract.md`.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | MACH+PBC+blueprint completos | Handoff listo a Law |
| Ambiguo | Solo notas sueltas | Exige consolidar o BLOCKED |
| Límite | Swap not-swappable sin remedio | Handoff con DECISIONS_REQUIRED |

## Fuentes

- Contratos Nakamas — `organization/contratos/report-contract.md`.
- Protocolo — `organization/protocolo-reportes.md`.
- Principios composable/MACH citados en Rol.md de Wapol (2026-08-04).
