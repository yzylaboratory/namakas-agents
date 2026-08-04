---
name: preparar-seeds-datos-sinteticos
description: Prepara seeds y fixtures sintéticos por entorno sin PII real. Úsala cuando se necesiten datos de desarrollo, demos o pruebas reproducibles.
metadata:
  author: yzylabs
  version: "1.0"
---

# Preparar seeds de datos sintéticos

## Propósito

Proveer datos iniciales reproducibles y seguros que no contaminen entornos con información personal real.

## Entradas

- Schema / modelos.
- Entorno objetivo (dev, test, demo).
- Casos de uso a cubrir (happy / unhappy paths).
- Restricciones de volúmenes y referential order.
- Política de reset del entorno.

## Procedimiento

1. Confirma que el entorno es descartable o admite seed controlado.
2. Diseña dataset mínimo que ejercite constraints y relaciones críticas.
3. Usa solo datos sintéticos o enmascarados; nunca PII/prod dumps.
4. Ordena inserts por dependencias FK; documenta idempotencia (`upsert` vs fail-on-exists).
5. Separa seeds por entorno (dev ≠ demo ≠ integration).
6. Documenta comando de seed y si requiere migrate previo.
7. Incluye al menos un unhappy path de datos (duplicado rechazado, FK inválida) si el objetivo es QA.
8. Lista datos que **no** deben seedearse (secretos, tokens, claves reales).

## Salida

```md
## Entorno
## Dataset (entidades y volúmenes)
## Orden / idempotencia
## Comando
## Unhappy paths cubiertos
## Prohibiciones (PII/secretos)
## Riesgos
```

## Casos límite

- Pedido de “copia de prod anonimizada” → exige pipeline de anonimización; no copies raw.
- Seed en staging compartido → requiere aprobación Katakuri y estrategia no destructiva.
- Soft-delete / unique parcial → seeds deben respetar constraints reales.

## Validación

- Cero PII/secretos en archivos.
- Orden FK correcto.
- Comando reproducible.
- Entorno explícito.

## Criterios de terminado

- Otro dev puede seedear en frío tras migraciones.
- QA entiende qué escenarios cubre el dataset.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Dev local de catálogo | Seed mínimo con FKs + comando |
| Ambiguo | “Pon datos de prueba” | Preguntas de entorno + borrador sintético |
| Límite | Dump prod con emails reales | Rechazo; plan sintético/anonimizado |

## Fuentes

- Prisma Best practices (test database / seed workflow) — https://www.prisma.io/docs/orm/more/best-practices (2026-08-04).
- Política interna Nakamas: no PII en fixtures (alineada a reglas de ecosistema Sabo / Legal).
