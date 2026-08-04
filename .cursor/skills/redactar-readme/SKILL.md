---
name: redactar-readme
description: Redacta o actualiza un README.md de producto o paquete con propósito, estado, uso y enlaces. Úsala cuando el usuario pida un README, landing de directorio o página de orientación para nuevos lectores.
metadata:
  author: yzylabs
  version: "1.0"
---

# Redactar README

## Propósito

Producir un `README.md` que oriente a un lector nuevo: qué es, para qué sirve, estado, cómo usarlo y dónde profundizar.

## Entradas

- Ruta del directorio o repositorio objetivo.
- Descripción del producto o paquete (hechos confirmados).
- Audiencia (dev interno, consumidor externo, ambos).
- Estado (estable, experimental, deprecado) si se conoce.
- Enlaces a docs detalladas, issues o contactos.
- README existente, si hay que actualizar.

## Procedimiento

1. Confirma la ubicación: `README.md` en la raíz del paquete o directorio de código (no enterrado solo en `docs/` como único landing).
2. Resume en una oración qué es y para quién.
3. Incluye o apunta a, como mínimo:
   - Propósito / contenido del paquete.
   - Estado (si aplica).
   - Cómo usarlo (comandos o ejemplo mínimo copiable).
   - Enlaces a documentación más detallada.
   - Punto de contacto o ownership cuando exista.
4. Mantén el README corto; mueve profundidad a guías enlazadas.
5. Elimina o reescribe secciones obsoletas; no dejes instrucciones rotas.
6. Verifica que los ejemplos reflejen el comportamiento actual disponible.
7. Marca supuestos si falta evidencia.

## Salida

```md
# [Nombre]

[Propósito en 1–3 oraciones]

## Estado

[estable | experimental | deprecado | …]

## Uso rápido

[comandos o ejemplo mínimo]

## Documentación

- [enlace]

## Ownership / contacto

[si aplica]

## Notas

- Supuestos: […]
- Pendientes: […]
```

Ajusta secciones al contexto; no inventes badges ni demos inexistentes.

## Casos límite

- Paquete interno sin release pública: prioriza propósito, ownership y enlace a docs internas.
- README existente largo y podrido: preferir recorte + enlaces sobre reescritura ornamental.
- Multi-paquete: un README por directorio de paquete, no un monolito engañoso.
- Sin evidencia de uso: documenta instalación desconocida como pendiente; no inventes comandos.

## Validación

- El archivo se llama `README.md`.
- Un lector nuevo entiende qué es y el siguiente paso.
- No hay promesas sin evidencia.
- Los comandos/ejemplos son coherentes con lo disponible o están marcados como pendientes.

## Criterios de terminado

- README entregado o actualizado en la ruta pedida.
- Contenido mínimo de orientación cubierto o explícitamente N/A con motivo.
- Riesgos y huecos listados.
- Sin secretos ni PII.

## Evaluación sugerida

| Caso | Entrada | Esperado |
|---|---|---|
| Normal | Repo con scripts de start conocidos | README con propósito + uso copiable |
| Ambiguo | “Haz un README bonito” sin producto claro | Preguntas/supuestos; no inventar features |
| Límite | Paquete deprecado | Estado deprecado visible; sin guiar a uso productivo como vigente |

## Fuentes

- Google docguide READMEs — https://google.github.io/styleguide/docguide/READMEs.html (2026-08-04)
- Google documentation best practices — https://github.com/google/styleguide/blob/HEAD/docguide/best_practices.md (2026-08-04)
