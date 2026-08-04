---
name: escribir-guia-usuario
description: Escribe o reestructura una guía de usuario (tutorial o how-to) orientada a una tarea concreta. Úsala cuando el lector deba aprender o lograr un resultado paso a paso, no solo leer un README.
metadata:
  author: yzylabs
  version: "1.0"
---

# Escribir guía de usuario

## Propósito

Crear documentación accionable alineada a Diátaxis: tutorial (aprender) o how-to (resolver un problema), sin mezclar referencia densa ni ensayo conceptual salvo secciones explícitas.

## Entradas

- Objetivo del lector (“quiero lograr X”).
- Nivel (principiante vs. operador experimentado).
- Tipo deseado: tutorial o how-to (si no se indica, inferir y declarar).
- Prerrequisitos reales (herramientas, accesos, versiones).
- Evidencia del flujo (UI, CLI, API de producto).
- Ubicación del archivo de salida.

## Procedimiento

1. Declara el tipo:
   - **Tutorial**: recorrido guiado, éxito temprano, poca ramificación.
   - **How-to**: problema → pasos → resultado; asume competencia básica.
2. Escribe el resultado esperado al inicio.
3. Lista prerrequisitos verificables.
4. Numera pasos atómicos; un resultado observable por paso cuando sea posible.
5. Incluye un ejemplo mínimo realista (comando, pantalla o payload) respaldado por evidencia.
6. Añade “Qué hacer si falla” solo para fallos frecuentes conocidos.
7. Enlaza explicación o referencia en lugar de mezclar teoría larga.
8. Revisa que no se hayan colado promesas de features no confirmadas.

## Salida

```md
# [Título orientado a tarea]

## Resultado

[Qué logrará el lector]

## Tipo

[tutorial | how-to]

## Prerrequisitos

- […]

## Pasos

1. […]
2. […]

## Verificación

[Cómo saber que funcionó]

## Solución de problemas

- […]

## Ver también

- […]
```

## Casos límite

- Flujo con ramas de producto: documenta el camino feliz y señala variantes; no finjas un único camino si el producto tiene dos modos.
- Tutorial pedido pero audiencia experta: ofrece how-to y justifica.
- Sin acceso al producto: estructura + supuestos; no inventes UI.
- Guía que es en realidad referencia de API: redirige a Robin / tratado técnico.

## Validación

- El título refleja la tarea, no un tema vago.
- Pasos son accionables y ordenados.
- Tipo Diátaxis declarado y coherente con el cuerpo.
- Fallos inventados no aparecen como “conocidos”.

## Criterios de terminado

- Guía completa en el formato pedido.
- Resultado y verificación explícitos.
- Huecos marcados.
- Sin mezcla confusa de explicación larga y pasos.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | “Cómo rotar un token de API” con CLI real | How-to con pasos y verificación |
| Ambiguo | “Documenta el onboarding” | Elegir tutorial vs how-to; aclarar audiencia |
| Límite | Feature aún no mergeada | No publicar como vigente; draft + pendientes |

## Fuentes

- Diátaxis — https://diataxis.fr/ (2026-08-04)
- Google developer documentation style guide — https://developers.google.com/style (2026-08-04)
