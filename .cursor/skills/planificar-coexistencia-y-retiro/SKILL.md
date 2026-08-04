---
name: planificar-coexistencia-y-retiro
description: Planifica dual-run, sincronización de datos, cutover, rollback y decommission del host/façade. Úsala cuando la modernización entre en coexistencia o haya que retirar el legado con criterios medibles.
metadata:
  author: yzylabs
  version: "1.0"
---

# Planificar coexistencia y retiro

## Propósito

Definir cómo legado y moderno conviven sin corrupción de datos, cómo se corta y cuándo el host (y la façade) pueden morir.

## Entradas

- Plan de modernización incremental / etapas.
- Diseño ACL (si aplica).
- Inventario de datos compartidos y consumidores.
- Ventanas de cambio y requisitos de rollback.

## Procedimiento

1. Declara el estado de coexistencia por etapa (quién es SoR de cada dominio).
2. Diseña sync si hace falta: carga inicial (ETL) + CDC/replicación; criterios de consistencia.
3. Define dual-run / shadow / canary según riesgo (qué porcentaje, qué métricas).
4. Escribe checklist de cutover: validaciones, freeze, conmutación de lectura/escritura.
5. Documenta rollback hasta el punto de no retorno; marca qué pasos son irreversibles.
6. Lista dependencias que deben llegar a cero antes del decommission del host.
7. Criterios de retiro del host (sin tráfico, sin jobs, sin consumidores, datos migrados/archivados).
8. Plan de retiro de la façade (o conservación como adapter de clientes legacy — decisión explícita).
9. Asigna owners de cada puerta de corte; escala gaps a Iceburg.

## Salida

```md
## Modelo de coexistencia por etapa
## Sync de datos (ETL/CDC) y SoR
## Dual-run / canary
## Checklist de cutover
## Rollback y punto de no retorno
## Criterios de decommission del host
## Retiro o retención de façade
## Owners y evidencias requeridas
## Riesgos residuales
```

## Casos límite

- Sin CDC posible: documenta ventana batch y riesgo de divergencia.
- Consumidor fantasma descubierto tarde: bloquea retiro; reabre caracterización.
- Retiro político (“apagar ya”): exige checklist; no firmes COMPLETED sin evidencias.

## Validación

- SoR único por dominio en cada fase post-cutover.
- Rollback usable hasta el punto declarado.
- Criterios de retiro son observables (métricas/logs), no opiniones.

## Criterios de terminado

- Iceburg puede autorizar cutover/retiro con checklist.
- Dependencias a cero listadas o marcadas abiertas.
- HANDOFF_LEGACY incluye siguiente agente de ejecución (Tom/DevOps/etc.).

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Dominio Orders extraído con CDC | Plan dual-run → cutover → retiro tablas |
| Ambiguo | “Apagar el legacy el viernes” | Checklist + BLOCKED sin evidencias |
| Límite | Façade aún usada por clientes batch | Retener façade; retiro host parcial |

## Fuentes

- Microsoft Learn — Strangler Fig (fases de DB, ETL/CDC, rollback) (consultado 2026-08-04).
- AWS Strangler fig — coexistencia y decommission (consultado 2026-08-04).
- `references/patrones-modernizacion-legacy.md`
