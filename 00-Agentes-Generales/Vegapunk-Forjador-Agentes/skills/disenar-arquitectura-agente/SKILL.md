---
name: disenar-arquitectura-agente
description: Convierte investigación y requisitos en la arquitectura de un agente: personalidad, rol, reglas, delegación y conjunto de skills. Úsala después de analizar e investigar y antes de generar archivos.
metadata:
  author: yzylabs
  version: "1.0"
---

# Diseñar arquitectura del agente

## Procedimiento

1. Define la misión y responsabilidad exclusiva.
2. Separa contenido por capa:
   - Personalidad: comportamiento y comunicación.
   - Rol: misión, entradas, salidas y autoridad.
   - Reglas: políticas permanentes y límites.
   - Delegación: relaciones y contratos de handoff.
   - Skills: procedimientos bajo demanda.
3. Agrupa procedimientos en unidades coherentes.
4. Elimina skills redundantes o demasiado genéricas.
5. Define para cada skill:
   - Intención que la activa.
   - Entradas.
   - Procedimiento.
   - Salida.
   - Validación.
   - Casos límite.
6. Decide herramientas y permisos mínimos.
7. Diseña el adaptador de Cursor y Claude Code.
8. Prepara una matriz de cobertura.

## Salida

- Diseño de los cuatro archivos canónicos.
- Lista de skills con activadores y contratos.
- Matriz de cobertura.
- Permisos y adaptadores propuestos.

## Matriz de cobertura

```md
| Responsabilidad | Archivo o skill que la cubre | Validación |
```

## Validación

Revisa cobertura, solapamientos, coherencia de autoridad y separación entre reglas y procedimientos.

## Criterios de terminado

- Cada responsabilidad está cubierta una vez.
- Las reglas no contienen procedimientos largos.
- Las skills no contienen personalidad redundante.
- La delegación no contradice la autoridad.
