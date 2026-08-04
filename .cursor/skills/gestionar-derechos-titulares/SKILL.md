---
name: gestionar-derechos-titulares
description: Diseña o audita procedimientos para derechos de titulares (ARCO / acceso, rectificación, cancelación, oposición, portabilidad). Úsala cuando se pida atender solicitudes de privacidad o hábeas data operativo.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gestionar derechos de titulares

## Propósito

Definir un procedimiento operable para recibir, verificar, cumplir y registrar solicitudes de titulares — con plazos, excepciones y dueños — alineado a Ley 172-13 y/o GDPR según jurisdicción.

## Entradas

- Canal(es) de solicitud (web, sucursal, email DPO).
- Sistemas que almacenan datos del titular.
- Jurisdicción y plazos legales conocidos.
- Excepciones candidatas (legal hold, fraude, secreto profesional).
- Capacidad técnica actual (export, borrado, rectificación).

## Procedimiento

1. Lista derechos aplicables (acceso, rectificación, cancelación/supresión, oposición, limitación, portabilidad, hábeas data).
2. Define intake: identidad del solicitante, alcance, canal y acuse de recibo.
3. Define verificación de identidad proporcional (evitar phishing y over-collection).
4. Mapea sistemas a consultar/borrar/exportar por tipo de derecho.
5. Establece plazos objetivo y escalamiento si hay terceros encargados.
6. Documenta excepciones con base legal; no inventes negativas genéricas.
7. Define registro de solicitudes (fecha, tipo, resultado, evidencia).
8. Señala gaps técnicos (no se puede borrar en backup X) con dueño y mitigación.

## Salida

```md
## Derechos aplicables
## Intake y verificación
## Flujos por derecho
## Plazos y SLAs internos
## Excepciones documentadas
## Registro / evidencia
## Gaps técnicos y dueños
## Fuentes
```

## Casos límite

- Solicitud de tercero sobre datos de otra persona → rechazo o mandato/poder; no filtrar.
- Borrado vs retención legal (AML/KYC) → oposición parcial / bloqueo documentado; escala Sengoku.
- Portabilidad pedida donde no aplica el derecho → explica límite con fuente; ofrece acceso.

## Validación

- Cada derecho tiene flujo y dueño operativo.
- Excepciones citan base; no “política interna” sola.
- Registro permite demostrar accountability.
- Jurisdicción explícita (172-13 / GDPR).

## Criterios de terminado

- Ops puede ejecutar una solicitud sin improvisar.
- Gaps de sistemas tienen plan o bloqueo explícito.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Acceso a datos de cliente retail | Flujo + sistemas + plazo |
| Ambiguo | “Cumplir ARCO” sin canales | Diseño de intake + RACI |
| Límite | Supresión vs retención AML | Excepción documentada + escala legal |

## Fuentes

- Ley 172-13 RD — derechos de acceso/rectificación/oposición/hábeas data — PDF Presidencia (2013-12-13).
- GDPR Arts. 12–22 — https://eur-lex.europa.eu/eli/reg/2016/679/oj (consultado 2026-08-04).
- ICO — DPO contact point for data subjects — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/data-protection-officers/ (2026-08-04).
