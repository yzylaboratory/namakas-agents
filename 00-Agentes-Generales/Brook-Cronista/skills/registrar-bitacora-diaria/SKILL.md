---
name: registrar-bitacora-diaria
description: Crea o actualiza la bitácora del día en memoria/diario/YYYY-MM-DD.md con hechos, decisiones, archivos y abiertos. Úsala cuando haya que dejar rastro cronológico de una misión o jornada Nakamas.
metadata:
  author: yzylabs
  version: "1.0"
---

# Registrar bitácora diaria

## Propósito

Conservar un diario fechado recuperable sin sobrescribir entradas previas del mismo día.

## Entradas

- Fecha (`YYYY-MM-DD`; por defecto la del turno).
- Resumen factual de lo ocurrido.
- Agentes involucrados.
- Archivos tocados (rutas).
- Decisiones y abiertos (si existen).
- Enlaces a decisiones/ADR relacionados (opcionales).

## Procedimiento

1. Resuelve la ruta `00-Agentes-Generales/Brook-Cronista/memoria/diario/YYYY-MM-DD.md`.
2. Si el archivo no existe, créalo con título `# Bitácora YYYY-MM-DD`.
3. Si existe, **añade** una nueva sección `## Turno — <hora o id breve>`; no borres secciones anteriores.
4. Dentro de la sección escribe: Hechos, Decisiones, Archivos tocados, Abiertos, Enlaces.
5. Redacta secretos como `[REDACTED]`.
6. Verifica que el archivo quedó en disco y reporta la ruta.

## Salida

```md
## Bitácora escrita

- Ruta: ...
- Acción: created | appended
- Secciones añadidas: ...
```

## Casos límite

- Mismo día, varios turnos → secciones distintas, no un merge destructivo.
- Sin hechos materiales → no crear archivo vacío; di por qué se omite.
- Fecha ambigua → pide confirmación o usa la fecha del contexto del sistema y declárala.

## Casos de evaluación

- Normal: un turno con 3 archivos tocados → append con secciones completas.
- Ambiguo: resumen narrativo sin fechas → pedir o fijar fecha explícita.
- Límite: archivo del día ya largo → append; no reescribir el día.

## Validación

- Archivo existe en la ruta declarada.
- Contenido previo del día (si había) sigue presente.
- Hay al menos hechos o decisión o abierto material.

## Criterios de terminado

- Ruta reportada.
- Entrada fechada y estructurada.
- Sin secretos en claro.

## Fuentes

- `references/estructura-memoria.md`
- Práctica de daily notes como captura de baja fricción (Second Brain / vaults Markdown) — 2026-08-04.
