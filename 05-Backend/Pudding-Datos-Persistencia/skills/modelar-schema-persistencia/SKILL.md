---
name: modelar-schema-persistencia
description: Modela schemas de persistencia (entidades, relaciones, constraints e índices). Úsala cuando se pida diseñar o evolucionar el modelo de datos / Prisma schema / tablas, no la lógica de negocio del MS.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar schema de persistencia

## Propósito

Convertir requisitos de dominio en un modelo de almacenamiento durable, tipado y con integridad explícita.

## Entradas

- Objetivo de negocio o bounded context.
- Schema existente (si hay).
- Motor/ORM evidenciado (PostgreSQL, Prisma, etc.).
- Restricciones de multi-tenant, soft-delete, auditoría temporal.
- Sensibilidad de campos (PII).

## Procedimiento

1. Lista entidades/agregados y ownership por contexto.
2. Define cardinalidades y relaciones explícitas (1-1, 1-N, N-N con tabla puente).
3. Declara PK, FK, UNIQUE, CHECK y NOT NULL con nombres explícitos cuando el ORM lo permita.
4. Elige tipos (UUID vs serial, TEXT vs enums, JSONB solo si es flexible de verdad).
5. Propón índices para FKs y predicados `where`/`orderBy` frecuentes.
6. Separa columnas de proyección/cache de hechos de dominio.
7. Marca campos PII y requisitos de cifrado/enmascarado (escala a Corazón si legal).
8. Entrega diff o schema propuesto + justificación.

## Salida

```md
## Contexto / ownership
## Modelo (entidades y relaciones)
## Constraints
## Índices propuestos
## Campos sensibles
## Decisiones y alternativas descartadas
## Riesgos / pendientes
```

## Casos límite

- Dos bounded contexts quieren “la misma” tabla → no fusiones; propone boundary o vista.
- Solo hay DTOs de API sin dominio → modela mínimo viable y marca supuestos.
- JSONB para datos frecuentemente filtrados → recomienda columnas tipadas + índice.

## Validación

- Relaciones y cardinalidades explícitas.
- Constraints no dejados “solo en la app”.
- Índices alineados a predicados reales o marcados como hipótesis.
- ORM/motor citado con evidencia del repo o decisión documentada.

## Criterios de terminado

- Un implementador puede escribir el schema sin reinventar cardinalidades.
- Gaps legales/eventos/MS tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Cuentas y titulares 1-N | Schema con FK, índices, UNIQUE de negocio |
| Ambiguo | “Modela usuarios” | Preguntas de identidad vs perfil + borrador mínimo |
| Límite | Mezclar ledger y notificaciones en una tabla | Rechazo de fusión; dos modelos + ownership |

## Fuentes

- Prisma Best practices (schema design) — https://www.prisma.io/docs/orm/more/best-practices (2026-08-04).
- PostgreSQL Glossary / integrity — https://www.postgresql.org/docs/current/glossary.html (2026-08-04).
