# Decisión: Forja de 5 expertos live-SQL Banreservas bajo Iceburg

- Fecha: 2026-08-04
- Estado: vigente
- Decisores: Randy / Luffy-Coordinador (ejecución vía Vegapunk Forjador)
- Misión: `task:vegapunk-forge-core-db-experts` — células live-SQL de Sistemas Core

## Contexto

Hacía falta asientos vivos para consulta SQL a cores Banreservas (Way4, Cadencie, Cortex, ACard, Siebel) bajo el director Iceburg, sin confundir Siebel CRM con Fujitora (seguridad) ni mezclar secretos de conexión en el vault de agentes.

## Decisión

Forjar **cinco** Custom Agents live-SQL con ids `kuzan-core-way4`, `kizaru-core-cadencie`, `akainu-core-cortex`, `greenbull-core-acard`, `smoker-core-siebel`; paths en `04-Sistemas-Core/*`; organigrama **live**; ampliar routing live **56 → 61**; schemas sanitizados; skill compartida `consultar-cores-bancarios-sql`; conexiones solo como **placeholders**. Validate OK.

## Alternativas

- Reutilizar Fujitora u otro asiento de seguridad para Siebel — descartado: Siebel CRM ≠ gobierno técnico/seguridad.
- Un solo agente genérico «core SQL» — no aportado como plan vigente; se eligió un experto por plataforma.
- Guardar connection strings reales en el repo de agentes — rechazado; placeholders únicamente.

## Consecuencias

- Positivo: roster live 61; Iceburg tiene células SQL por core; naming `*-core-*` alineado con routing Nakamas.
- Neutro: conexiones reales quedan fuera de este vault hasta configuración operativa.
- Riesgo: Activity MCP aún no reconoce `brook-cronista` (`unknown_agent`); sin impacto en la forja de los cinco.

## Enlaces

- [Bitácora 2026-08-04 — turno forja-expertos-live-sql-cores](../diario/2026-08-04.md)
- Relacionada: [forja masiva 02–12](./2026-08-04-forja-masiva-agentes-02-12.md) (oleada previa; organigrama entonces stub)
