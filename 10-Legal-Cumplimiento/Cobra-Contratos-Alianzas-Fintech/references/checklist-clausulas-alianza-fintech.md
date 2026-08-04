# Checklist de cláusulas — alianzas fintech

Referencia operativa para Cobra. Fuentes: Mayer Brown (2025-11), ABA SaaS provisions (2021-11), API Framework Agreement (Ulster Bank Open Banking, ejemplo de industria). Consultado 2026-08-04.

## Instrumento

- [ ] Partes y capacidad contractual
- [ ] Jurisdicción / ley aplicable (sin inventar)
- [ ] Tipo: MSA + schedules / collaboration / BaaS / white-label / marketplace

## Comercial y gobernanza

- [ ] Alcance y exclusiones
- [ ] Fees / payment (deep pricing → Du-Feld)
- [ ] Change control / approval rights en cambios customer-facing o compliance
- [ ] Governance / escalation committees
- [ ] Audit / information rights (especialmente si hay entidad regulada)

## API e integración

- [ ] Licencia API (scope, Purpose, no sublicencia)
- [ ] Credenciales y seguridad de acceso
- [ ] Sandbox vs producción
- [ ] Responsabilidad por fallos de llamada / downtime / mapping
- [ ] Rate limits / suspension por abuso
- [ ] Referencia a OpenAPI / API Materials (owner Sabo/Robin)

## SLA y riesgo

- [ ] Métricas medibles + método
- [ ] Remedios (credits, terminate, RCA)
- [ ] Cap de liability + carve-outs (data/security, IP, confidentiality, gross negligence)
- [ ] Indemnidades por lado
- [ ] Mutual SLAs si la colaboración es bidireccional

## Datos e IP

- [ ] Categorías de datos + use rights (no ownership genérico)
- [ ] Portabilidad / borrado post-terminación
- [ ] Handoff Corazon (DPA/DPIA/roles)
- [ ] Background IP + foreground IP (evitar joint ownership por defecto)
- [ ] Escrow si dependencia crítica

## Salida

- [ ] Triggers de terminación
- [ ] Transition assistance con duración y scope
- [ ] Data return en formato usable
- [ ] Disengagement customer-facing si aplica
- [ ] Survival clauses

## Red flags típicos

- Cap unilateral que excluye data breach del partner
- Exclusividad perpetua sin reciprocidad
- Cambio unilateral de producto sin notice/approval
- Audit rights nulos hacia entidad regulada
- Terminación inmediata sin wind-down en servicio crítico
- “Ownership” de todos los derivados del cliente
