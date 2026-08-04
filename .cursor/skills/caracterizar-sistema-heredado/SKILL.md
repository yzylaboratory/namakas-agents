---
name: caracterizar-sistema-heredado
description: Inventaria y caracteriza un sistema heredado (stack, owners, interfaces, datos, hotspots) con evidencia. Úsala cuando haya que entender qué es el legado antes de modernizar o cambiarlo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Caracterizar sistema heredado

## Propósito

Producir una ficha verificable del legado: qué es, cómo vive, con qué habla y dónde duele.

## Entradas

- Nombre/ID del sistema heredado.
- Rutas de repos, entornos o docs disponibles.
- Owners conocidos (si existen).
- Restricciones de acceso y tiempo.
- `HANDOFF_EXPLORADOR` de Noland (opcional).

## Procedimiento

1. Delimita el perímetro del host (qué entra / qué queda fuera).
2. Inventaria manifiestos y runtime (lenguaje, frameworks, jobs, batch, mainframes/host adapters).
3. Lista entry points: APIs, pantallas, colas, archivos, RPC, pantallas verdes, etc.
4. Identifica stores de datos (DB, archivos, VSAM-like, caches) y ownership observado.
5. Mapea interfaces externas (consumidores/productores) con evidencia.
6. Anota hotspots: god modules, código muerto sospechoso, libs EOLd, secretos en claro (solo ubicación).
7. Contrasta docs vs runtime; marca conflictos.
8. Declara lo no revisado.

## Salida

```md
## Identidad del legado
## Stack y runtime
## Entry points
## Datos y stores
## Interfaces / consumidores
## Owners y entornos
## Hotspots y deuda visible
## Conflictos doc↔runtime
## No revisado
## Evidencia clave
```

## Casos límite

- Solo binarios sin fuente: caracteriza interfaces y runtime observados; marca código interno como desconocido.
- Monolito multi-dominio: ficha por bounded context prioritario, no “todo el universo”.
- Owner ausente: documenta vacío y escala a Iceburg.

## Validación

- Cada afirmación material cita ruta, manifiesto o evidencia de runtime.
- No se inventan servicios fantasma.
- Perímetro y no-revisado explícitos.

## Criterios de terminado

- Un lector entiende qué es el host y dónde mirar después.
- Hotspots materiales señalados.
- Lista de vacíos accionables.

## Casos de evaluación

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Repo COBOL/Java + DB compartida | Ficha con entry points, stores e interfaces |
| Ambiguo | Solo hostname de prod | Bloqueo parcial + preguntas; sin invención |
| Límite | Monolito 20 años multi-dominio | Ficha del perímetro pedido + mapa de dominios sospechados |

## Fuentes

- Síntesis de discovery legacy + strangler prerequisites (Fowler Strangler Fig; Azure Strangler Fig) — consultado 2026-08-04.
- `references/patrones-modernizacion-legacy.md`
