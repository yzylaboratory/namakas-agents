# Contrato de producción — HANDOFF_TX

Paquete de handoff de **Kaku-Procesamiento-Transacciones** hacia Iceburg, Tom, Robin u otros consumidores.

## Campos mínimos

```text
HANDOFF_TX_ID:
MISSION_ID / TASK_ID:
PRODUCED_BY: kaku-procesamiento-transacciones
REPORT_TO: iceburg-director-sistemas-core
CONSUMER: tom-integracion-core | robin-tratadista | iceburg-director-sistemas-core | <otro>
STATUS: completo | parcial | borrador
TRANSACTION_TYPE:
SCOPE_IN:
SCOPE_OUT:
LIFECYCLE_SUMMARY:          # estados / terminales / timeouts
CORRELATION_IDS:            # MsgId, EndToEndIdentification, UETR, locales
IDEMPOTENCY:                # claves, TTL, replay, conflictos
LEDGER_POSTING_RULES:       # asiento D/C, ACID, locks, hold/capture
COMPENSATION_REVERSAL:      # matriz escenarios
INTEGRITY_AUDIT:            # veredicto PASS | PASS_WITH_LIMITATIONS | FAIL
MESSAGING_MAP:              # pain/pacs/camt u otros — solo con fuente
RISKS:
OPEN_DECISIONS:
DEPENDENCIES:               # Tom / Crocus / Lucci / Robin / …
ARTIFACT_PATHS:
EVIDENCE:
NEXT_HANDOFF:
```

## Reglas

1. `STATUS: completo` solo si auditoría no tiene bloqueantes críticos (doble posteo, desbalance, correlación rota).
2. No inventar mensajes ISO 20022 ni Service Domains BIAN.
3. Ejemplos sintéticos únicamente — cero PII/PAN.
4. Toda afirmación de mensajería estándar cita fuente o se marca supuesto.

## Relación con otros handoffs

| Handoff | Rol |
|---|---|
| `HANDOFF_BIAN` (Lucci) | Semántica de Service Domains — Kaku consume, no inventa |
| `HANDOFF_FIBO` | Términos semánticos — opcional |
| Tratado / OpenAPI (Robin) | Contratos de producto — Kaku no los sustituye |
| Adapters (Tom) | Transporte/integración — Kaku define semántica TX |
