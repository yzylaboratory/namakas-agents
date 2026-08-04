---
name: disenar-capa-acceso-datos
description: Diseña la capa de acceso a datos (repositorio, Unit of Work, client tipado). Úsala cuando se pida abstraer persistencia, límites de SaveChanges o evitar filtrar el ORM a otras capas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar capa de acceso a datos

## Propósito

Definir cómo el Backend lee/escribe almacenamiento con límites claros, sin ceremonias inútiles ni fugas del ORM.

## Entradas

- Casos de uso de lectura/escritura.
- ORM/client existente (Prisma Client, DbContext, etc.).
- Necesidad de testear sin DB real (sí/no).
- Aggregates / ownership.
- Requisitos de transacciones multi-repositorio.

## Procedimiento

1. Decide si hace falta repositorio explícito o basta el client tipado del ORM (justifica).
2. Si hay repositorio: modela por aggregate root, no por cada tabla.
3. No expongas `IQueryable`/builders crudos fuera de la capa de persistencia.
4. Coloca `Save`/`commit` en Unit of Work o servicio de aplicación, no en cada método CRUD suelto.
5. Prefiere APIs async y retornos concretos (`Entity`, DTO, página), no streams infinitos sin límite.
6. Define scoping (request/scoped) para compartir contexto/transacción.
7. Documenta qué queda fuera (caché, bus de eventos → Apoo).
8. Entrega interfaces + responsabilidades + ejemplo de flujo write.

## Salida

```md
## Decisión (client directo | repository | UoW)
## Justificación
## Interfaces / límites
## Flujo de escritura (quién hace Save)
## Lecturas (contratos de retorno)
## Testing strategy
## Riesgos / anti-patrones evitados
```

## Casos límite

- Microservicio CRUD simple → puede bastar Prisma/EF client; no fuerces repositorio vacío.
- Testing sin DB → repositorio que no retorna `IQueryable` (Microsoft EF guidance).
- Multi-DB en un caso de uso → UoW explícito o saga; escala complejidad a Katakuri/Law.

## Validación

- Justificación presente (no “siempre repository”).
- Save ownership claro.
- Sin fuga de queryables.
- Handoff a eventos/MS marcado si aplica.

## Criterios de terminado

- Un desarrollador sabe dónde escribir queries y dónde hacer commit.
- Anti-patrones (Save en cada Add, God repository) documentados como rechazados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Pedidos con líneas | Repo de aggregate Order + UoW/commit único |
| Ambiguo | “Pon repository en todo” | Decisión selectiva por bounded context |
| Límite | Tests unitarios sin DB | Interfaces sin IQueryable + estrategia de mock |

## Fuentes

- Microsoft Learn — Infrastructure persistence layer design — https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design (2026-08-04).
- Microsoft Learn — EF Core testing without the database — https://learn.microsoft.com/en-us/ef/core/testing/testing-without-the-database (2026-08-04).
