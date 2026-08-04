# Referencias — Persistencia (Pudding)

Notas operativas condensadas. Preferir siempre la documentación oficial del ORM/motor del repositorio objetivo.

## Prisma Migrate (resumen)

| Entorno | Comando típico | Notas |
|---|---|---|
| Dev local | `prisma migrate dev` | Genera y aplica; puede ser interactivo |
| CI / prod | `prisma migrate deploy` | Solo aplica migraciones committed |
| Prototipo local descartable | `prisma db push` | No usar en equipo/CI/prod |
| Reset local | `prisma migrate reset` | Destructivo; solo DB descartable |

Fuente: https://www.prisma.io/docs/orm/more/best-practices (2026-08-04).

## Expand-and-contract (patrón)

1. **Expand:** añadir columnas/tablas nuevas compatibles con lectores viejos.
2. **Migrate data / dual-write o dual-read** según caso.
3. **Contract:** eliminar columnas viejas cuando nadie las lea.

## ACID (PostgreSQL)

- Atomicity / Consistency / Isolation / Durability — ver glossary oficial.
- Default isolation típico: Read Committed; subir solo con justificación.

Fuentes:

- https://www.postgresql.org/docs/18/tutorial-transactions.html
- https://www.postgresql.org/docs/current/glossary.html
