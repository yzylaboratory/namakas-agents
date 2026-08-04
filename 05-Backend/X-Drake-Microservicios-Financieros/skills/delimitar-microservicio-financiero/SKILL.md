---
name: delimitar-microservicio-financiero
description: Delimita el bounded context de un microservicio financiero (límites, invariantes, dependencias, no-objetivos). Úsala cuando haya que partir o acotar un MS de dominio financiero a partir de tratado/capacidades, antes de implementar.
metadata:
  author: yzylabs
  version: "1.0"
---

# Delimitar microservicio financiero

## Propósito

Convertir tratado/capacidades en un bounded context implementable: qué posee el MS, qué invariantes de dinero/estado protege y qué queda fuera.

## Entradas

- Tratado MS/orch y/o lista de capacidades.
- OpenAPI/AsyncAPI si existen.
- `HANDOFF_BIAN` / `HANDOFF_FIBO` (opcionales).
- Restricciones de Katakuri/Law (stack, SLAs).

## Procedimiento

1. Nombra el MS y el problema de dominio que resuelve (una oración).
2. Lista agregados/entidades de dominio que **posee** vs consulta.
3. Declara invariantes financieros (p. ej. saldo no negativo, reserva ≤ disponible, sumas de asientos = 0 si aplica ledger).
4. Define incluido / excluido (portal, core, reporting, KYC, etc.).
5. Mapea dependencias y dueños (Pudding, Apoo, identidad, core).
6. Si hay BIAN/FIBO: cita handoff; si falta y es material → gap/`DELEGATION_REQUIRED`.
7. Propón API interna de alto nivel (comandos/consultas) sin reinventar el OpenAPI de Robin.
8. Lista riesgos de acoplamiento y “MS dios”.

## Salida

```md
## Nombre / misión
## Posee / consulta
## Invariantes
## Incluido / Excluido
## Dependencias y dueños
## API interna (borrador)
## Gaps BIAN/FIBO/tratado
## Riesgos
```

## Casos límite

- Capacidad cruza dos ledgers → no fusiones; propone dos MS o orch con saga.
- Solo hay wishlist de negocio sin tratado → entrega borrador de límites + `BLOCKED` parcial para Robin.
- Nombre BIAN sugerido sin handoff → no adoptes el nombre; escala.

## Validación

- Invariantes son observables/testeables.
- Fuera de alcance explícito.
- Sin invención BIAN/FIBO.

## Criterios de terminado

- Katakuri/implementador entiende qué construye y qué no.
- Gaps tienen dueño.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Tratado “Account Holds” + OpenAPI | BC con invariantes de reserva y exclusiones |
| Ambiguo | “MS de pagos del banco” | Preguntas + 2–3 BC candidatos, no un omnibus |
| Límite | Capacidad con SD BIAN sin HANDOFF | Gap Lucci + límites sin inventar SD |

## Fuentes

- Chris Richardson — Microservice boundaries / domain decomposition (microservices.io) — consultado 2026-08-04.
- Contrato handoff Robin — `00-Agentes-Generales/Robin-Tratadista/skills/preparar-handoff-implementacion/SKILL.md`.
