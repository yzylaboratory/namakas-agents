---
name: consultar-cores-bancarios-sql
description: "Protocolo compartido live SQL de cores Banreservas en Nakamas. Úsala antes de conectar a Cadencie/Way4/Cortex/ACard/Siebel (schema-first, VPN, read-only, redact PII)."
metadata:
  author: yzylabs
  version: "1.0"
---

# Consultar cores bancarios SQL (protocolo compartido)

## Propósito

Establecer el protocolo obligatorio de live SQL para las células core bajo Iceburg.
No sustituye la skill específica del core ni el schema durable del agente.

## Entradas

- Core objetivo (way4 / cadencie / cortex / acard / siebel).
- Objetivo de consulta (inventario códigos, muestreo, validar SP, lookup CRM).
- Confirmación de VPN / red si el host es privado.

## Procedimiento

1. Identifica el core y el experto dueño (`kuzan-core-way4`, `kizaru-core-cadencie`, `akainu-core-cortex`, `greenbull-core-acard`, `smoker-core-siebel`).
2. **Schema-first:** lee `references/<core>.md` (+ `.index.json`) del experto **antes** de meta-queries.
3. Resuelve credenciales fuera del repo (IAC/project secrets). **Nunca** imprimas passwords.
4. Conecta con cliente preferido (`sqlplus` / `sqlcmd` / Python). Timeouts cortos en primer connect.
5. Si VPN/red falla: reporta inalcanzable y **detén**. No inventes filas ni fallbacks.
6. SQL **read-only** por defecto (`SELECT` / `DESCRIBE` / `EXPLAIN`). DML/DDL solo con mandato explícito.
7. Redacta PAN (`BIN********LAST4`) y PII en toda salida. No dumps a vault.
8. Devuelve: core+entorno, SQL usado, counts, samples enmascarados, artefactos, nota VPN si aplica.

## Mapa de dominio

| Dominio | Core | Experto |
|---------|------|---------|
| TC crédito issuing | Way4 | `kuzan-core-way4` |
| TC crédito issuing | Cadencie | `kizaru-core-cadencie` |
| TD débito / PCI | Cortex | `akainu-core-cortex` |
| TC delivery/emboss | ACard | `greenbull-core-acard` |
| CRM / clientes | Siebel | `smoker-core-siebel` |

## Conexiones

Ver `04-Sistemas-Core/Iceburg-Director-Sistemas-Core/references/connections.md` (hosts como placeholders; secretos externos).

## Salida

```md
## Core + entorno
## SQL usado
## Counts / samples (masked)
## Artefactos
## Connectivity
```

## Validación

- Schema leído antes de `ALL_TAB_*` / `INFORMATION_SCHEMA` innecesarios.
- Sin passwords ni PAN/PII completos en salida.
- Sin resultados inventados ante fallo de red.
- Ownership del core correcto (no cruzar a otro experto sin escalar).

## Criterios de terminado

- Protocolo aplicado y evidencia SQL (o BLOCKED por VPN/credenciales).
- Reporte a Iceburg con `EVIDENCE`.

## Fuentes

| Fuente | Fecha | Uso |
|--------|-------|-----|
| Banreservas core-databases SKILL (adaptado, sanitizado) | 2026-07-29 / forja 2026-08-04 | Protocolo schema-first + safety |
| organization/organigrama.yaml | vigente | Jerarquía Iceburg |
