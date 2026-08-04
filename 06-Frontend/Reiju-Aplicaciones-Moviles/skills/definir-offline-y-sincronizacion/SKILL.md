---
name: definir-offline-y-sincronizacion
description: Define estrategia online-only u offline-first, colas, conflictos, caché y datos en dispositivo. Úsala cuando la app deba trabajar sin red o con sync diferido.
metadata:
  author: yzylabs
  version: "1.0"
---

# Definir offline y sincronización

## Propósito

Decidir y especificar cómo el cliente maneja conectividad intermitente sin corromper datos ni filtrar información sensible.

## Entradas

- Features que deben funcionar offline.
- Clasificación de datos (público, PII, financiero).
- SLAs de consistencia con backend.
- Límites de almacenamiento y batería.
- Stack y capas de persistencia disponibles.

## Procedimiento

1. Clasifica pantallas: online-only, read-cache, write-queue, full offline.
2. Elige modelo de consistencia (last-write-wins, merge, server-authoritative).
3. Diseña cola de mutaciones: idempotencia, reintentos, backoff, dead-letter.
4. Define invalidación de caché y TTL por tipo de dato.
5. Exige cifrado at-rest para datos sensibles en dispositivo.
6. Documenta UX de sync (indicadores, conflictos, resolución).
7. Lista pruebas: airplane mode, kill app mid-sync, conflicto concurrente.

## Salida

```md
## Alcance offline
## Modelo de consistencia
## Cola / reintentos
## Caché y TTL
## Almacenamiento y cifrado
## UX de sync
## Pruebas
## Riesgos
```

## Casos límite

- Datos financieros que no pueden divergir → online-only o server-authoritative estricto.
- Cola infinita offline → límites de tamaño y política de purga.
- Multi-dispositivo → documenta qué gana en conflicto.

## Validación

- Cada feature offline tiene dueño de conflicto.
- Datos sensibles cifrados o prohibidos en disco.
- Pruebas de kill mid-sync definidas.

## Criterios de terminado

- Implementación puede construir cola/caché sin improvisar reglas.
- Gaps de backend (endpoints de sync) listados para Robin/API owner.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Catálogo + favoritos | Read-cache + cola de favoritos |
| Ambiguo | “Que funcione sin internet” | Inventario de features + matriz online/offline |
| Límite | Transferencias bancarias offline | Rechazo offline para mutaciones + justificación |

## Fuentes

- OWASP MASVS storage/network categories — https://mas.owasp.org/MASVS/03-Using_the_MASVS/ (2026-08-04).
- Apple / Android persistence guidance vía docs oficiales de plataforma (SwiftData/Room según stack) (2026-08-04).
