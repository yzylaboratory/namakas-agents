---
name: inventariar-tratamientos-datos
description: Inventaría y documenta tratamientos de datos personales (RoPA / registro Art. 30 / Ley 172-13). Úsala cuando se pida mapear qué datos se procesan, con qué finalidad, por quién y con qué retención.
metadata:
  author: yzylabs
  version: "1.0"
---

# Inventariar tratamientos de datos

## Propósito

Construir o actualizar el registro de actividades de tratamiento con accountability verificable: finalidades, categorías, destinatarios, retención, transferencias y medidas.

## Entradas

- Nombre del sistema/producto/proceso.
- Jurisdicción(es) aplicables.
- Roles (responsable / encargado).
- Fuentes de datos (formularios, APIs, partners, logs).
- Políticas o RoPA existentes (si hay).

## Procedimiento

1. Identifica cada actividad de tratamiento (no mezcles nómina con analytics sin separar entradas).
2. Declara responsable, encargado y subencargados conocidos.
3. Lista finalidades y base(s) de legitimación candidatas (sin inventar excepciones).
4. Clasifica categorías de datos y de titulares (clientes, empleados, TPP users, etc.).
5. Mapea destinatarios internos/externos y transferencias internacionales.
6. Define o pregunta retención operativa y de archivo; marca gaps.
7. Describe medidas de seguridad a alto nivel; escala detalle técnico a Fujitora.
8. Etiqueta sensibilidad (datos especiales/sensibles) y necesidad potencial de DPIA.
9. Produce entrada RoPA lista para consolidar en el registro maestro.

## Salida

```md
## Tratamiento
## Roles
## Finalidades / bases
## Categorías de datos y titulares
## Destinatarios / transferencias
## Retención
## Medidas (alto nivel)
## Gaps / dueños
## Fuentes normativas
```

## Casos límite

- “Todo el data lake” sin finalidades → no inventaríes un solo bloque; exige segmentación.
- Seudonimización presentada como anonimato → reclasifica y documenta riesgo de reidentificación.
- Encargado sin contrato → gap bloqueante hacia Cobra/Sengoku.

## Validación

- Una finalidad por entrada (o finalidades explícitamente listadas).
- Roles y jurisdicción claros.
- Transferencias fuera de jurisdicción señaladas.
- Normas citadas (Ley 172-13 / GDPR Art. 30 según aplique).

## Criterios de terminado

- Un auditor puede entender qué se trata, para qué y quién recibe los datos.
- Gaps tienen dueño y no están ocultos.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Onboarding KYC bancario | Entrada RoPA con categorías, retención, destinatarios |
| Ambiguo | “Usamos HubSpot y el core” | Preguntas + borrador de 2+ tratamientos separados |
| Límite | Logs con PII sin política de retención | Gap bloqueante + dueño Viola/Fujitora |

## Fuentes

- EDPB SME guide — records of processing / Art. 30 — https://www.edpb.europa.eu/sme-data-protection-guide/be-compliant_en (2026-08-04).
- GDPR Art. 30 — https://eur-lex.europa.eu/eli/reg/2016/679/oj (consultado 2026-08-04).
- Ley 172-13 RD — https://www.presidencia.gob.do/sites/default/files/statics/transparencia/marco-legal/leyes/Ley-172-13.pdf (2013-12-13).
