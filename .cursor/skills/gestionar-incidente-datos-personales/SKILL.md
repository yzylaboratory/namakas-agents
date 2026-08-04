---
name: gestionar-incidente-datos-personales
description: Clasifica y gestiona la dimensión de privacidad de incidentes que afectan datos personales (notificación, alcance de titulares, evidencia). Úsala tras brechas, exposiciones o accesos indebidos a PII; no sustituye respuesta técnica de seguridad.
metadata:
  author: yzylabs
  version: "1.0"
---

# Gestionar incidente de datos personales

## Propósito

Evaluar si un incidente compromete datos personales, estimar impacto a titulares y definir obligaciones de notificación/comunicación según jurisdicción — coordinando contención con Fujitora y decisión legal con Sengoku.

## Entradas

- Descripción del incidente y línea de tiempo.
- Sistemas y datasets afectados.
- Categorías de datos y estimación de titulares.
- Controles existentes y estado de contención.
- Jurisdicción(es) y contactos DPO/legal.
- Evidencia forense disponible (alto nivel).

## Procedimiento

1. Confirma si hay datos personales afectados (vs solo indisponibilidad sin PII).
2. Clasifica impacto: confidencialidad, integridad, disponibilidad; sensibilidad de categorías.
3. Estima alcance (titulares, geografía, periodos) con rangos si hay incertidumbre.
4. Coordina con Fujitora contención, preservación de evidencia y erradicación (no dupliques IR técnico).
5. Evalúa probabilidad de riesgo a derechos de titulares (GDPR Arts. 33–34 / marco local).
6. Recomienda notificación a autoridad y/o titulares con justificación; no inventes plazos exactos sin fuente.
7. Define mensajes mínimos (qué pasó, qué datos, qué hacer el titular) para aprobación Sengoku.
8. Exige post-mortem: causa, alcance final, medidas correctivas, owners y fecha de cierre.

## Salida

```md
## Resumen del incidente (PII)
## Categorías y alcance estimado
## Riesgo a titulares
## Acciones privacidad (notificar / no notificar / por qué)
## Coordinación Fujitora / Sengoku
## Comunicación propuesta
## Evidencia y pendientes
## Fuentes
```

## Casos límite

- Ransomware con cifrado pero sin exfiltración confirmada → documenta incertidumbre; no asumas “sin riesgo”.
- Exposición pública breve de IDs → puede requerir notificación; evalúa riesgo real.
- Partner/encargado causa el incidente → activa DPA y flujo de notificación conjunta.

## Validación

- Separación clara privacidad vs IR técnico.
- Alcance y categorías no inventados; incertidumbre etiquetada.
- Recomendación de notificación justificada con fuente.
- Dueños y próximos pasos explícitos.

## Criterios de terminado

- Sengoku tiene un paquete accionable para decidir notificación.
- Fujitora tiene requisitos de evidencia/contención desde privacidad.
- Post-mortem tiene checklist de cierre.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | DB de clientes expuesta 2h | Alcance + riesgo + recomendación notificación |
| Ambiguo | “Hubo un incident en prod” | Preguntas de PII/alcance + triage |
| Límite | Encargado cloud sin detalles | Escalamiento DPA + supuestos documentados |

## Fuentes

- GDPR Arts. 33–34 (notification of personal data breach) — https://eur-lex.europa.eu/eli/reg/2016/679/oj (consultado 2026-08-04).
- ICO / EDPB accountability guidance (DPO cooperation with authority) — ICO DPO page (2026-08-04).
- Ley 172-13 — seguridad y deberes del responsable (PDF oficial, 2013-12-13).
- ISO/IEC 27701:2025 — privacy incident handling within PIMS — https://www.iso.org/standard/27701 (2025-10).
