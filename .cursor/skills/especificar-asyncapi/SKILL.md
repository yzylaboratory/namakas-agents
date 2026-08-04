---
name: especificar-asyncapi
description: Elabora o actualiza un contrato AsyncAPI para eventos, canales y orquestación asíncrona. Úsala cuando el MS/orch publique o consuma mensajes y el tratado requiera especificar flujos event-driven.
metadata:
  author: yzylabs
  version: "1.0"
---

# Especificar contrato AsyncAPI

## Propósito

Definir canales, mensajes y roles pub/sub (o request-reply asíncrono) de forma machine-readable, alineada al tratado y a patrones event-driven del dominio.

## Entradas

- Tratado del MS/orch con flujos asíncronos.
- Lista de eventos de dominio (nombres, productores, consumidores).
- Payloads y schemas acordados.
- Infra de mensajería conocida (Kafka, MQ, etc.) si está decidida.
- Mapeo BIAN / eventos de Service Domain cuando existan (p. ej. release AsyncAPI BIAN).
- Spec AsyncAPI existente, si hay.

## Procedimiento

1. Confirma que hay mensajería material; si solo hay HTTP, no inventes eventos.
2. Usa AsyncAPI 2.x o 3.x según toolchain del repo; declara la versión explícitamente.
3. Define `info`, servers/bindings conocidos y channels con nombres estables.
4. Separa mensajes de dominio de mensajes técnicos (notificaciones, DLQ) cuando aplique.
5. Documenta payload schemas (preferible `$ref` / components).
6. Declara quién publica y quién suscribe; evita channels huérfanos.
7. Documenta orden, idempotencia, claves de partición y retención solo si están decididos.
8. Si hay mapeo BIAN event-driven, traza channels a Service Domain/CR/BQ recibidos — no inventes.
9. Alinea nombres de eventos con el tratado OpenAPI/tratado MS.
10. Lista pending decisions (broker, schema registry, exactly-once, etc.).

## Salida

- Archivo AsyncAPI YAML.
- Matriz evento → productor → consumidores.
- Pendientes de infraestructura y semántica.

## Casos límite

- Orquestación tipo saga → documenta comandos/eventos por paso y compensaciones si están definidas.
- Mismo evento con dos nombres en equipos distintos → normaliza o registra alias; no dejes drift silencioso.
- Solo “emitiremos algo” sin payload → no completes; exige schema mínimo o marca bloqueo.

## Validación

- Versión AsyncAPI explícita.
- Cada channel tiene mensaje y al menos un rol productor o consumidor documentado.
- Schemas sin PII real ni secretos.
- Coherencia de nombres con el tratado.

## Criterios de terminado

- Spec usable para mocks/consumidores.
- Matriz de eventos completa para el alcance.
- Huecos de broker/semántica listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | 2 eventos de dominio con payload | AsyncAPI + matriz pub/sub |
| Ambiguo | “Usaremos eventos” sin lista | Bloqueo + preguntas; sin channels inventados |
| Límite | Saga con compensación indefinida | Documenta pasos conocidos y marca compensación pendiente |

## Fuentes

- AsyncAPI Specification — https://www.asyncapi.com/docs/reference/specification/latest (2026-08-04).
- bian-official/public AsyncAPI 3.x por Service Domain (release 14.x) — https://github.com/bian-official/public (2026-08-04).
