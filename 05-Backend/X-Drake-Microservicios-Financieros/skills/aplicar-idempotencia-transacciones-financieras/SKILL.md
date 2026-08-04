---
name: aplicar-idempotencia-transacciones-financieras
description: Diseña e implementa idempotencia para mutaciones financieras (Idempotency-Key, dedup, replay, conflictos). Úsala cuando el MS cree o altere cargos, reservas, transferencias u otras operaciones sensibles a reintentos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Aplicar idempotencia a transacciones financieras

## Propósito

Garantizar que reintentos de red/cliente no produzcan doble cobro ni doble side-effect: misma clave → mismo resultado observable.

## Entradas

- Operaciones mutantes del contrato.
- Modelo de tenancy (cuenta, cliente, tenant).
- Restricciones de store (DB/Redis) vía Pudding si aplica.
- Comportamiento de procesadores externos (si soportan idempotency keys).

## Procedimiento

1. Identifica todas las mutaciones que requieren clave de idempotencia.
2. Define header/campo (`Idempotency-Key` u homologo del contrato), longitud y entropía (p. ej. UUIDv4).
3. Define scope de la clave (tenant + operación + recurso) y retención mínima.
4. Especifica almacenamiento: dedup durable (constraint único) ± cache corta; no solo memoria de proceso.
5. Define fingerprint de body: mismo key + body distinto → conflicto (`422`/`409` según contrato), no silent overwrite.
6. Documenta replay: respuesta cacheada vs re-ejecución segura.
7. Para calls a PSPs: reenvía key si el proveedor la soporta; si no, query-back antes de retry; si ambiguo → estado `ambiguous` + reconciliación.
8. Añade tests: retry éxito, retry en vuelo, body mismatch, expiración de key.

## Salida

```md
## Operaciones cubiertas
## Semántica de clave (scope, TTL, header)
## Persistencia de dedup
## Conflictos / códigos
## Procesadores externos
## Tests
## Riesgos residuales
```

## Casos límite

- Timeout tras side-effect externo sin key del PSP → no reintentar authorize; marcar ambiguo.
- Key reutilizada con payload distinto → error de conflicto, no segundo cobro.
- GET/DELETE → no uses idempotency keys innecesarias (idempotentes por definición en HTTP).

## Validación

- Ninguna mutación financiera del alcance queda sin semántica de idempotencia.
- Hay estrategia ante ambigüedad (no “retry forever”).
- Fuentes de patrón citadas (Stripe / IETF draft cuando aplique).

## Criterios de terminado

- Un cliente puede reintentar con la misma key sin doble efecto.
- Casos de conflicto y ambiguo están documentados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | POST payment + UUIDv4 | Dedup + replay de respuesta |
| Ambiguo | Timeout de authorize sin query API | Estado ambiguous + reconciliación, no segundo authorize |
| Límite | Misma key, body distinto | 409/422 según contrato |

## Fuentes

- Stripe Idempotent requests — https://docs.stripe.com/api/idempotent_requests (2026-08-04).
- IETF draft-ietf-httpapi-idempotency-key-header — https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ (draft-07, 2025-10).
