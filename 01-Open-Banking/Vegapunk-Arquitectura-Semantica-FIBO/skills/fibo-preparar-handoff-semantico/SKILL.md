---
name: fibo-preparar-handoff-semantico
description: Empaqueta HANDOFF_FIBO con glosario canónico, mapeos, huecos, recomendaciones a APIs/datos y criterios de aceptación semánticos. Úsala al cerrar un trabajo de alineación o modelado para Robin, Lucci o implementación.
metadata:
  author: yzylabs
  version: "1.0"
---

# Preparar handoff semántico FIBO

## Propósito

Entregar un paquete autocontenido que el siguiente agente pueda consumir sin reinterpretar significados.

## Entradas

- Alineaciones, capa semántica, auditorías y/o extensiones del ciclo.
- Alcance y ancla FIBO usadas.
- Destinatario (Robin / Lucci / Law / implementación).

## Procedimiento

1. Reúne artefactos del ciclo y elimina duplicados.
2. Completa `references/contrato-handoff-fibo.md`.
3. Incluye solo términos del alcance; marca fuera de alcance.
4. Separa sección BIAN si hay solape de nombres (no sustituyas HANDOFF_BIAN).
5. Lista pendientes y bloqueos con dueño sugerido.
6. Añade rutas de archivos exactas en el repo.
7. Verifica: cero IRIs inventados; cada término material con categoría.

## Salida

Documento `HANDOFF_FIBO` completo según el contrato de referencia, más índice de archivos.

## Casos límite

- Ciclo incompleto → handoff parcial con BLOQUEOS explícitos.
- Destinatario Robin → enfatiza implicaciones en descriptions/schemas, no reescribas OpenAPI entero.
- Destinatario Lucci → enfatiza distinción capability vs ontology.

## Validación

- Metadatos, glosario, huecos y criterios de aceptación presentes.
- Distinción FIBO vs BIAN explícita cuando ambos aparezcan.

## Criterios de terminado

- Un tercero puede aplicar el vocabulario sin preguntar “qué significa X”.
- Checklist de aceptación semántica rellenado o con fallos listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 6 alineaciones + 1 extensión | HANDOFF_FIBO completo |
| Ambiguo | Mitad de términos sin categoría | Bloqueo / parcial |
| Límite | Mezcla pedidos BIAN+FIBO | Handoff FIBO + escalado BIAN a Lucci |

## Fuentes

- `references/contrato-handoff-fibo.md`
- https://spec.edmcouncil.org/fibo (2026-08-04)
- https://edmcouncil.org/frameworks/industry-models/fibo/ (2026-08-04)
