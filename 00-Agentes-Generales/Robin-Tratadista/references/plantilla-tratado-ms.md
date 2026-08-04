# Plantilla — Tratado de microservicio / orquestación

Usa esta estructura como base. Omite secciones no aplicables y registra por qué.

```md
# Tratado — [Nombre]

## 1. Resumen
- Tipo: [microservicio | orquestación]
- Objetivo en una frase
- Dueño / célula sugerida

## 2. Contexto y motivadores
- Problema de negocio o técnico
- Drivers
- Enlaces a requisitos / ADRs

## 3. Límites del servicio
### Incluye
- [...]
### Excluye
- [...]
### Sistemas vecinos
- [...]

## 4. Capacidades y flujos
### Capacidad A
- Flujo feliz
- Alternativos / errores

## 5. Datos y ownership
- Entidades
- Fuente de verdad
- Retención / PII (si aplica)

## 6. Interfaces síncronas
- Resumen de recursos OpenAPI
- Path al contrato

## 7. Eventos / orquestación
- Resumen de channels AsyncAPI
- Path al contrato
- Compensaciones (si saga)

## 8. Trazabilidad BIAN
- Versión BIAN
- Service Domains (solo los del handoff)
- Operaciones / eventos trazados
- Huecos

## 9. NFR y restricciones
- Disponibilidad, latencia, volumen (si decididos)
- Seguridad
- Cumplimiento

## 10. Decisiones, supuestos, riesgos, pendientes
| Tipo | Descripción | Impacto |
```
