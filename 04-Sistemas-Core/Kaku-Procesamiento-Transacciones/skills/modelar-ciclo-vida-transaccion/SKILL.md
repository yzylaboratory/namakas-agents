---
name: modelar-ciclo-vida-transaccion
description: Modela estados, eventos, transiciones e identificadores de correlación del ciclo de vida de una transacción core (incl. relación con pain/pacs/camt cuando aplique). Úsala cuando haya que definir o auditar el state machine de pagos/transferencias/ajustes antes de posteo o integración.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar ciclo de vida de transacción

## Propósito

Producir un modelo de ciclo de vida verificable: estados, eventos, terminales, timeouts e IDs de correlación — alineado a mensajería estándar cuando exista evidencia, sin inventar mensajes.

## Entradas

- Tipo de transacción y resultado de negocio esperado.
- Sistemas origen/destino conocidos.
- Requisitos de status reporting / timeouts.
- Evidencia ISO 20022 u otros formatos (si aplica).
- Restricciones de producto (auth vs capture, on-us vs clearing).

## Procedimiento

1. Nombra el objeto de negocio (p. ej. credit transfer, book transfer, adjustment).
2. Lista estados propuestos y clasifícalos: inicial, intermedio, terminal éxito, terminal fallo, hold.
3. Define eventos que disparan transiciones (aceptación, clearing ack, settlement, reject, timeout).
4. Fija identificadores: `MsgId` (mensaje), `EndToEndIdentification` (negocio), UETR u local IDs — y quién los genera/persiste.
5. Si hay ISO 20022, mapea hitos a familias conocidas (`pain` initiation/status, `pacs` clearing/settlement/status/return, `camt` reporting) **solo con evidencia** del catálogo.
6. Documenta timeouts y compensaciones disparadas por tiempo.
7. Entrega tabla de estados + diagrama textual + pendientes.

## Salida

```md
# Ciclo de vida — [Nombre transacción]

## Estados
| Estado | Tipo | Descripción |
## Transiciones
| Desde | Evento | Hacia | Condición |
## Correlación
| ID | Alcance | Generador | Persistencia |
## Mapeo mensajería (si aplica)
| Hito | Familia/mensaje | Fuente |
## Timeouts / excepciones
## Pendientes
```

## Casos límite

- Solo hay nombre comercial sin flujo → esqueleto + `borrador`; no inventes mensajes ISO.
- Auth y capture separados → dos fases con estados y claves distintas o jerárquicas.
- Retry de red vs retry de negocio → no compartan el mismo `MsgId` si son envíos lógicos distintos.

## Validación

- Todo estado no terminal tiene al menos una salida.
- Terminales explícitos.
- IDs de correlación definidos.
- Sin mensajes ISO inventados.

## Criterios de terminado

- Tabla de estados usable por implementador.
- Correlación documentada.
- Huecos listados.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Transferencia crédito con status | Ciclo completo + correlación EndToEnd |
| Ambiguo | “Procesar pago” sin canal | Esqueleto + bloqueos; sin inventar pacs.* |
| Límite | Timeout en clearing con return | Transición a reverse/return correlacionada |

## Fuentes

- ISO 20022 catalogue / Business Areas (pain, pacs, camt) — consulta 2026-08-04
- Intro ISO 20022 PDF — modelo de mensajes
