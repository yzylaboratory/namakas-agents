---
name: auditar-integridad-indices
description: Audita integridad referencial, constraints, drift de schema e índices/consultas peligrosas. Úsala cuando se sospeche inconsistencia de datos, N+1, full scans o desalineación schema↔DB.
metadata:
  author: yzylabs
  version: "1.0"
---

# Auditar integridad e índices

## Propósito

Detectar huecos de integridad y riesgos de rendimiento en la capa de datos con evidencia accionable.

## Entradas

- Schema y migraciones.
- Código de consultas / includes.
- Métricas o EXPLAIN si existen.
- Reportes de datos huérfanos o duplicados.
- Entorno (solo lectura preferida para auditoría).

## Procedimiento

1. Inventaría constraints esperados vs presentes (PK, FK, UNIQUE, CHECK).
2. Busca FKs sin índice y predicados frecuentes sin soporte.
3. Detecta drift: schema ORM vs DB real / historial de migraciones.
4. Revisa patrones N+1, `SELECT *`, includes profundos y paginación ausente.
5. Señala soft-deletes sin filtros consistentes o unique parciales rotos.
6. Prioriza hallazgos por severidad (corrupción > pérdida > latencia).
7. Propón remediaciones (migración de constraints, índices, rewrite de query).
8. No apliques fixes destructivos en la misma pasada de auditoría sin mandato.

## Salida

```md
## Alcance auditado
## Hallazgos (severidad)
## Integridad / constraints
## Drift
## Índices / consultas
## Remediaciones propuestas
## Evidencia (rutas, EXPLAIN, counts)
```

## Casos límite

- Solo hay acceso a código sin DB → auditoría estática; marca límites.
- Hallazgo de PII en claro → escala a Corazón; no copies muestras reales al reporte.
- Índice sugerido sin predicado medido → márcalo como hipótesis.

## Validación

- Cada hallazgo tiene evidencia (ruta o métrica).
- Severidad asignada.
- Remediaciones separadas de la auditoría.
- Sin secretos/PII en el informe.

## Criterios de terminado

- Katakuri/X-Drake pueden priorizar fixes con lista ordenada.
- Drift y riesgos de integridad no quedan implícitos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | FK order_id sin índice | Hallazgo + índice propuesto |
| Ambiguo | “La API está lenta” | Hipótesis + plan de EXPLAIN / includes |
| Límite | Filas huérfanas por falta de FK | Severidad alta + migración de constraint + cleanup plan |

## Fuentes

- Prisma Best practices (indexes, query optimization) — https://www.prisma.io/docs/orm/more/best-practices (2026-08-04).
- PostgreSQL integrity / constraints (glossary) — https://www.postgresql.org/docs/current/glossary.html (2026-08-04).
