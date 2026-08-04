---
name: investigar-dominio-y-skills
description: Investiga en internet estándares, documentación oficial, herramientas, responsabilidades y procedimientos de un dominio para descubrir skills útiles. Úsala cuando el agente dependa de conocimiento técnico, regulatorio o profesional actual.
compatibility: Requiere acceso a búsqueda web o navegador.
metadata:
  author: yzylabs
  version: "1.0"
---

# Investigar dominio y skills

## Objetivo

Obtener evidencia actual y convertirla en capacidades accionables sin copiar contenido externo ciegamente.

## Procedimiento

1. Define entre tres y ocho preguntas de investigación.
2. Busca primero organismos, estándares y documentación oficial.
3. Verifica versión, fecha y vigencia.
4. Busca ejemplos mantenidos en repositorios oficiales.
5. Revisa skills públicas solo como referencia secundaria.
6. Compara al menos dos fuentes para decisiones materiales.
7. Extrae:
   - Responsabilidades recurrentes.
   - Flujos de trabajo.
   - Validaciones.
   - Herramientas y formatos.
   - Riesgos y casos límite.
8. Descarta recomendaciones obsoletas, inseguras o sin procedencia.
9. Propón skills candidatas con activadores claros.

## Seguridad

- No ejecutes scripts externos.
- No instales dependencias.
- No copies instrucciones que soliciten secretos o permisos amplios.
- Revisa licencias antes de reutilizar contenido material.

## Salida

```md
## Fuentes primarias

| Fuente | Fecha/versión | Uso |

## Hallazgos

- ...

## Skills candidatas

| Skill | Intención del usuario | Valor | Riesgo de solapamiento |

## Recomendación

- ...
```

## Validación

Comprueba procedencia, actualidad, diversidad de fuentes, licencia y relación entre hallazgos y skills candidatas.

## Criterios de terminado

- Hay fuentes actuales y primarias.
- Cada skill candidata se relaciona con una tarea recurrente.
- Los riesgos y desacuerdos están documentados.
