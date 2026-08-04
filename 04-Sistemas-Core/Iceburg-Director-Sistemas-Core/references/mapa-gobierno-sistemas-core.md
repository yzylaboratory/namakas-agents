# Mapa de gobierno — Sistemas Core

Referencia operativa para Iceburg. Consultada / sintetizada 2026-08-04. No sustituye estándares oficiales ni arquitectura de solución.

## Capas típicas

| Capa | Preocupación | Dueño preferido |
|---|---|---|
| System of record / ledger | Saldos, posting, auditoría | Kaku (+ Iceburg gates) |
| Productos / cuentas | Ciclo de vida de productos core | Iceburg + Backend según alcance |
| Integración / adapters | Anti-corruption, canónico interno | Tom |
| Legacy / batch | Coexistencia, strangler | Crocus |
| Rails / mensajería | ISO 20022, clearing, files | Tom/Kaku en borde; no core profundo |
| Exposición externa | APIs OB, consentimiento | Jinbe / Sabo (fuera de Core) |

## Gates de cutover (mínimos)

1. **Integridad**: dual-run parity o reconciliación con umbral de breaks aceptado.
2. **Idempotencia**: claves y semántica de reintento documentadas.
3. **Rollback**: procedimiento probado y ventana definida.
4. **Ownership**: interfaz y métricas con dueño nombrado.
5. **Observabilidad**: traces/métricas suficientes para descuadres.
6. **Comunicación**: consumidores internos notificados; deprecación calendarizada.

## ISO 20022 / CBPR+ (alto nivel)

- ISO 20022 es el estándar de mensajería financiera rico/estructurado (ISO / comunidad Swift).
- CBPR+ define market practice para pagos cross-border en Swift; coexistencia MT/MX de instrucciones de pago cerró Nov 2025 en el programa Swift.
- Implicación para Core: preservar datos ricos end-to-end; no truncar en el camino al ledger/compliance.
- Fuentes: https://www.swift.com/standards/iso-20022 — https://www.iso20022.org/

## Patrones preferidos

- **Modelo canónico interno** + codecs de borde (no acoplar servicios internos a MX/MT crudo).
- **Payment-intent / instrucción tipada** detrás de adapters de rail.
- **Strangler + dual-run** frente a big-bang.
- **DLQ / quarantine** para poison messages sin detener el pipeline crítico.

## Escalamiento rápido

| Señal | Escalar a |
|---|---|
| Conflicto multi-departamento | Luffy |
| Arquitectura de solución | Law |
| Seguridad estructural | Fujitora |
| Plataforma / SRE | Franky / Viola |
| API externa / OB | Jinbe |
| Célula stub sin worker | `DELEGATION_REQUIRED` → Luffy / Vegapunk |
