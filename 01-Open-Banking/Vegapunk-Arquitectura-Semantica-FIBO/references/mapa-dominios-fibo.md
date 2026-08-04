# Mapa de dominios FIBO (referencia operativa)

Fuente primaria: [edmcouncil/fibo README](https://github.com/edmcouncil/fibo) y [FIBO Viewer](https://spec.edmcouncil.org/fibo/ontology). Consultar siempre el repo/Viewer por vigencia (releases trimestrales). Fecha de síntesis: 2026-08-04.

| Dominio | Código | Uso típico en Open Banking / banca |
|---|---|---|
| Foundations | FND | Contratos, parties, organizaciones, lugares, acuerdos — base de casi todo |
| Business Entities | BE | Entidades legales, gobierno, reporting de entidades |
| Financial Business and Commerce | FBC | Productos/servicios financieros, intermediarios, instrumentos generales, reguladores |
| Securities | SEC | Valores, equities, deuda negociable, identificación/emisión |
| Loans | LOAN | Contratos de préstamo, roles, crédito, colateral |
| Derivatives | DER | Opciones, futuros, swaps y derivados |
| Indices and Indicators | IND | Índices, tasas de referencia, benchmarks |
| Market Data | MD | Precios, yields, series temporales de mercado |
| Business Process | BP | Flujos de emisión/transacción cuando el concepto depende del proceso |
| Corporate Actions and Events | CAE | Eventos corporativos sobre valores |

## Notas de adopción

- FIBO es OWL (Description Logic), machine-readable y human-readable.
- Host: EDM Council; también estandarizado por OMG (`EDMC-FIBO`).
- Licencia del código en GitHub: MIT (verificar `LICENSE` en el repo).
- Commons Ontology Library (OMG) ha absorbido/deprecado partes de FND/FBC — revisar release notes antes de anclar a clases antiguas.

## Open Banking

FIBO cubre fuerte el vocabulario financiero de negocio; **no** es un estándar PSD2/consent API por sí solo. Conceptos como consentimiento de acceso a cuentas o roles TPP pueden requerir extensión local o puentes a ontologías Open Banking (evidencia secundaria: OBO / literatura). Nunca presentes esas extensiones como “FIBO core”.
