---
name: gobernar-migraciones
description: Gobierna migraciones versionadas (dev vs deploy, SQL review, expand/contract). Úsala cuando se creen, revisen o apliquen cambios de schema en equipo/CI/producción.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar migraciones

## Propósito

Mantener el historial de schema reproducible, auditable y seguro entre entornos.

## Entradas

- Diff de schema o requisito de cambio.
- Carpeta de migraciones existente.
- Entorno objetivo (local, CI, prod).
- Restricciones de downtime y volumen de datos.
- Herramienta evidenciada (Prisma Migrate, Flyway, EF Migrations, etc.).

## Procedimiento

1. Confirma herramienta y comandos del repo (no inventes CLI).
2. En desarrollo: genera migración versionada (`migrate dev` o equivalente); revisa SQL.
3. En CI/prod: solo aplica migraciones committed (`migrate deploy` o equivalente).
4. Prohíbe `db push` / reset en entornos no descartables.
5. Si el cambio es destructivo o de alto riesgo: diseña expand-and-contract (add → dual-write/read → drop).
6. Nunca edites una migración ya desplegada; crea follow-up.
7. Exige commit de schema + carpeta `migrations/` completa (incl. lockfile si aplica).
8. Documenta rollback/forward-fix y riesgos de bloqueo/lock.

## Salida

```md
## Cambio
## Entorno y comando
## SQL revisado (resumen)
## Estrategia (directa | expand-contract)
## Archivos de migración
## Rollback / forward-fix
## Riesgos
```

## Casos límite

- Drift detectado (DB ≠ historial) → no “arreglar a mano” en silencio; plan de reconcile.
- Migración fallida a medias en prod → follow-up + estado `_migrations`; no reescribir historial.
- Equipo concurrente → incorpora migraciones remotas antes de generar las tuyas.

## Validación

- Comando correcto por entorno.
- SQL revisado para drops/renames.
- Historial versionado intacto.
- Expand/contract presente si hay datos/prod.

## Criterios de terminado

- Otro ingeniero puede aplicar el mismo cambio en CI sin prompts interactivos.
- Riesgos de datos listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Add column nullable | Migración + deploy path documentado |
| Ambiguo | “Actualiza la DB en prod” | Pregunta de change set + rechazo de push/reset |
| Límite | Rename columna usada en prod | Plan expand-contract en 2–3 pasos |

## Fuentes

- Prisma Migrate team schema changes — https://www.prisma.io/docs/guides/database/schema-changes (2026-08-04).
- Prisma Best practices (production migrations) — https://www.prisma.io/docs/orm/more/best-practices (2026-08-04).
