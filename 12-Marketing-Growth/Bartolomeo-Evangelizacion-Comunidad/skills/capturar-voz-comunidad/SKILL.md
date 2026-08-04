---
name: capturar-voz-comunidad
description: Sintetiza fricciones, pedidos y temas recurrentes de la comunidad en handoffs accionables. Úsala cuando haga falta cerrar el loop bidireccional advocate↔producto/docs/adopción sin quedarse en sentiment vago.
metadata:
  author: yzylabs
  version: "1.0"
---

# Capturar voz de la comunidad

## Propósito

Convertir conversaciones comunitarias en evidencia estructurada y handoffs que otros agentes (Carrot, Vivi, producto vía Morgans) puedan ejecutar — y planificar el cierre de loop hacia los miembros.

## Entradas

- Fuentes: hilos, office hours, issues, encuestas, tickets (con permiso).
- Ventana temporal del análisis.
- Preguntas de negocio (¿qué bloquea adopción? ¿qué confunde?).
- Restricciones de privacidad (anonimizar por defecto).

## Procedimiento

1. Recolecta evidencia en la ventana dada; no inventes citas.
2. Agrupa por tema (fricción, pedido de feature, docs, trust/compliance, love stories).
3. Cuenta frecuencia relativa y severidad percibida (con método explícito).
4. Separa hechos observados de interpretaciones.
5. Propón handoffs: Carrot (activación), Vivi (docs), Shakky (mensaje/posicionamiento), producto (Morgans→Luffy).
6. Redacta “lo que escuchamos / lo que haremos / lo que no haremos (aún)” para cierre de loop.
7. Anonimiza PII; marca material sensible/compliance.
8. Lista gaps de evidencia (sesgo de canal, sample pequeño).

## Salida

```md
# Voz de comunidad — [producto] ([ventana])

## Temas (ordenados por frecuencia/severidad)
| Tema | Frecuencia | Severidad | Evidencia (anon) | Interpretación |
|---|---|---|---|---|

## Handoffs accionables
- Destino: … | Pedido: … | Criterio de hecho: …

## Cierre de loop (mensaje a comunidad)
- Escuchamos: …
- Actuamos: …
- No (aún) / por qué: …

## Sesgos y límites
- …

## Riesgos
- …
```

## Casos límite

- Sample < 5 voces: etiqueta como anécdota; no declares “la comunidad quiere X”.
- Tema regulado (crédito, inversiones): escala compliance; no des consejos.
- Sentiment solo positivo de embajadores pagos: marca conflicto de interés.
- Pedidos contradictorios: presenta trade-off; no elijas roadmap solo.

## Validación

- Cada tema tiene evidencia o queda marcado como supuesto.
- Handoffs tienen destino y criterio.
- PII anonimizada.
- Cierre de loop borrador presente.

## Criterios de terminado

- Síntesis usable por Morgans y peers.
- Al menos un handoff accionable o declaración explícita de “sin señal fuerte”.
- Riesgos/sesgos documentados.

## Fuentes

- Gingiris Developer Advocate Guide 2026 — bidirectional feedback to product; consultado 2026-08-04.
- Stateshift CLG — community conversations feed onboarding/content loops (Nov 2025); consultado 2026-08-04.
