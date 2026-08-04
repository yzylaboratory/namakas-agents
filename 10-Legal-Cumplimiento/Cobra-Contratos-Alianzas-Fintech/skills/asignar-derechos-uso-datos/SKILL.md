---
name: asignar-derechos-uso-datos
description: Categoriza datos de la alianza y asigna derechos de uso, portabilidad y obligaciones post-terminación. Úsala cuando el contrato hable de “ownership” genérico o cuando haya que separar uso comercial contractual de privacidad (Corazon).
metadata:
  author: yzylabs
  version: "1.0"
---

# Asignar derechos de uso de datos

## Propósito

Reemplazar “data ownership” vago por categorías de datos con use rights, restricciones, portabilidad, borrado y handoff de privacidad a Corazon cuando aplique.

## Entradas

- Cláusulas de datos del borrador.
- Flujos de datos conocidos (onboarding, transacciones, analytics, modelos).
- Jurisdicción / hints de privacidad (sin inventar base legal).
- Dependencias de ecosistema (sub-processors, otros partners).

## Procedimiento

1. Inventaría categorías: customer-provided, transactional, derived/analytics, operational logs, model training inputs/outputs.
2. Por categoría, asigna: quién puede usar, para qué Purpose, si es compartible con terceros del ecosistema.
3. Prohíbe uses no autorizados (reventa, profiling fuera de Purpose, entrenamiento de modelos sin licencia).
4. Define portabilidad y formato usable al terminar; plazos de devolución/borrado.
5. Separa obligaciones contractuales comerciales de DPA/DPIA/roles de controlador → escala a Corazon.
6. Señala tension entre “insights compartidos” y PII; propone anonimización/agregación como condición.
7. Documenta AI/ML si aplica: derechos sobre datasets vs algoritmos mejorados (sin joint ownership por defecto).
8. Lista gaps que bloquean firma.

## Salida

```md
## Categorías de datos
## Matriz de use rights
## Restricciones / prohibiciones
## Portabilidad y post-terminación
## AI/ML (si aplica)
## Handoff Corazon (DPA/DPIA/roles)
## Gaps y riesgos
```

## Casos límite

- Partner exige ownership exclusivo de derivados del cliente → red flag; propone licencia limitada.
- Solo hay cláusula GDPR genérica → no basta; exige use rights + escala DPA a Corazon.
- Datos de múltiples proveedores en plataforma → define reglas de compartición con salvaguardas.

## Validación

- No queda “ownership” genérico sin matriz de use rights.
- Todo PII tiene handoff a Corazon o justificación de por qué no aplica.
- Post-terminación tiene plazo y formato.

## Criterios de terminado

- Negociador puede defender la matriz categoría por categoría.
- Privacidad tiene dueño explícito.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Alianza con analytics compartidos | Matriz + anonimización + handoff Corazon |
| Ambiguo | “Compartimos todos los datos” | Preguntas + categorías candidatas + BLOCKED parcial |
| Límite | Training de modelos con PII del banco | Prohibición o licencia estrecha + escala |

## Fuentes

- Mayer Brown — Collaboration Agreements… (data buckets / use rights; avoid naive ownership) (2025-11-21) (2026-08-04).
- ABA — SaaS Agreements… (data ownership, retention, security) (2021-11) (2026-08-04).
