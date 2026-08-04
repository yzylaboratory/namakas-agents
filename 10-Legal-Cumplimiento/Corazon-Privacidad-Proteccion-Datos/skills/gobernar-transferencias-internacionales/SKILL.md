---
name: gobernar-transferencias-internacionales
description: Mapea y gobierna transferencias internacionales de datos personales y encargos de tratamiento. Úsala cuando datos salen de la jurisdicción, hay SaaS/cloud extranjero o partners procesan PII.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gobernar transferencias internacionales

## Propósito

Visibilizar flujos transfronterizos y bases de transferencia/encargo, con gaps accionables hacia contratos (Cobra) y seguridad (Fujitora) — sin inventar decisiones de adecuación.

## Entradas

- Mapa de sistemas y regiones de hosting.
- Lista de vendors/SaaS/partners con acceso a PII.
- Contratos DPA / cláusulas existentes.
- Jurisdicción de origen (RD, UE, UK, etc.).
- Finalidades que motivan la transferencia.

## Procedimiento

1. Inventaría destinatarios fuera de la jurisdicción y ubicación de almacenamiento/procesamiento.
2. Clasifica cada flujo: transferencia internacional vs acceso remoto vs encargado local.
3. Para cada transferencia, documenta base candidata (consentimiento, contrato, excepción legal) citando la norma aplicable.
4. Revisa existencia de DPA: instrucciones, seguridad, subencargados, auditoría, borrado al término.
5. Señala vendors sin DPA o con subencargados opacos como gap bloqueante.
6. Coordina requisitos contractuales a Cobra y controles técnicos a Fujitora.
7. No declares “país adecuado” sin fuente oficial vigente; marca “requiere revisión legal humana” si aplica.
8. Produce matriz de transferencias + plan de remediación priorizado.

## Salida

```md
## Matriz de transferencias
## Bases documentadas / gaps
## Estado DPA por vendor
## Subencargados conocidos
## Requisitos a Cobra / Fujitora
## Riesgos a titulares
## Fuentes
```

## Casos límite

- CDN/analytics “solo cookies” con IDs → sigue siendo transferencia potencial; no trivialices.
- Multi-región active-active sin residencia forzada → documenta riesgo y opciones.
- Open Banking TPP en otra jurisdicción → separa mandato regulatorio OB (Tsuru) de transferencia PII.

## Validación

- Cada destino tiene país/región y categoría de datos.
- Gaps contractuales no se ocultan con “uso habitual del sector”.
- Fuentes: Ley 172-13 transferencias / GDPR Capítulo V según aplique.

## Criterios de terminado

- Legal y seguridad pueden actuar sobre una lista priorizada.
- Ninguna transferencia material queda “desconocida”.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | CRM SaaS en US + clientes RD | Matriz + gap DPA/consentimiento |
| Ambiguo | “Está en AWS” | Preguntas de región/cuentas + mapa |
| Límite | Subencargados no listados en DPA | Bloqueo + requisitos a Cobra |

## Fuentes

- Ley 172-13 — transferencias internacionales (PDF Presidencia, 2013-12-13).
- GDPR Capítulo V (Arts. 44–49) — https://eur-lex.europa.eu/eli/reg/2016/679/oj (consultado 2026-08-04).
- ISO/IEC 27701:2025 — controles PII controller/processor — https://www.iso.org/standard/27701 (2025-10).
