---
name: evaluar-confianza-cero
description: Evalúa un diseño frente a principios de Zero Trust (NIST SP 800-207): trust implícito, authn/authz por recurso y enforcement. Úsala cuando la arquitectura asuma perímetro, redes “internas confiables” o se pida alineación ZTA.
metadata:
  author: yzylabs
  version: "1.0"
---

# Evaluar confianza cero

## Propósito

Detectar confianza implícita y proponer alineación a Zero Trust Architecture sin imponer un producto vendor.

## Entradas

- Diseño de acceso (usuarios, servicios, dispositivos, APIs).
- Diagrama de red/perímetro y puntos de enforcement.
- Mecanismos IdP, gateway, mTLS, políticas existentes (si hay).

## Procedimiento

1. Identifica dónde el diseño confía por ubicación, VPN, “red interna” u ownership.
2. Lista recursos protegidos (APIs, datos, admin planes, pipelines).
3. Verifica si authn y authz son discretos antes del acceso a cada recurso.
4. Localiza Policy Enforcement Points (explícitos o ausentes).
5. Evalúa políticas: estáticas vs. dinámicas; continuous verification.
6. Revisa identidad de workload (servicio-a-servicio) además de usuario humano.
7. Propón gaps priorizados alineados a NIST SP 800-207 (no roadmap eterno).
8. Si ZTA completo está fuera de alcance, documenta perfil mínimo viable para el cambio.

## Salida

Informe ZTA: trust implícito encontrado, PEPs, gaps, recomendaciones acotadas, fuera de alcance.

## Casos límite

- Monolito on-prem sin IdP → gaps estructurales; no finjas ZTA completo.
- Pedido de “Zero Trust” solo marketing → exige principios verificables.
- Multi-cloud sin identidad de workload → prioriza identidad de servicio.

## Validación

- Cada gap cita un tenet SP 800-207 o anti-patrón observado.
- No recomienda un vendor específico como requisito.
- Alcance ZTA acotado al cambio pedido.

## Criterios de terminado

- Trust implícito inventariado.
- Recomendaciones priorizadas y acotadas.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | API gateway + JWT usuario, sin authz servicio | Gaps s2s + recomendaciones |
| Ambiguo | “Somos Zero Trust” sin diagrama | Borrador + evidencia faltante |
| Límite | Solo cambio de color UI | Fuera de alcance ZTA; no fuerces evaluación |

## Fuentes

- NIST SP 800-207 — https://csrc.nist.gov/pubs/sp/800/207/final — consultado 2026-08-04
- OWASP Zero Trust Architecture Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Zero_Trust_Architecture_Cheat_Sheet.html — consultado 2026-08-04
