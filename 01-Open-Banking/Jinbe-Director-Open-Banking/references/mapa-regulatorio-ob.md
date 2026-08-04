# Referencia — Mapas regulatorios Open Banking / Open Finance (alto nivel)

Última revisión: 2026-08-04. Uso: apoyo a la skill `alinear-regulacion-ob-alto-nivel`. No sustituye asesoría legal.

## Comparativa rápida

| Jurisdicción | Marco | Artefacto técnico típico | Notas de vigencia |
|---|---|---|---|
| Unión Europea | PSD2 (+ evolución PSD3/openFinance) | Berlin Group NextGenPSD2; openFinance Framework | NextGenPSD2 maduro; extensiones Open Finance en curso |
| Brasil | Open Finance (BCB / estructura de gobernanza) | Manual de APIs; Manual de Escopo; specs del portal OFB | Manual APIs v7.0 (IN BCB 615/2025); ecosistema mandatory-phase |
| Australia | Consumer Data Right (CDR) | Consumer Data Standards; seguridad alineada a FAPI | Prescriptivo; acreditación ACCC |
| Estados Unidos | CFPA §1033 / regla CFPB PFDR | Principios + estándares de mercado (p. ej. FDX); FAPI vía industria | Regla final oct 2024; implementación/litigio/reconsideración — verificar estado |
| Seguridad transversal | — | OpenID FAPI 1.0 / FAPI 2.0 | FAPI 2.0 Final 2025-02-19; no define modelo de datos de negocio |

## Distinciones críticas

1. **Regulación** impone derechos/obligaciones (consentimiento, acceso, conducta).
2. **Estándar de API de ecosistema** define recursos/payloads (NextGenPSD2, CDS, OFB).
3. **FAPI** endurece OAuth/OIDC para APIs de alto valor; es ortogonal al modelo de datos.
4. **Open Banking** suele centrarse en cuentas/pagos; **Open Finance** amplía productos (seguros, inversiones, etc.) según el mercado.

## Enlaces primarios

- https://openid.net/wg/fapi/
- https://www.berlin-group.org/psd2-access-to-bank-accounts
- https://www.consumerfinance.gov/personal-financial-data-rights/
- https://consumerdatastandardsaustralia.github.io/standards/
- Portal Open Finance Brasil / página BCB Open Finance (manuales vigentes)

## Fuentes secundarias (contraste)

- Ozone API — LatAm Open Finance status 2025
- Mastercard Insights — Open banking in Latin America
- Congress CRS IF13117 — Access to Consumer Financial Data
