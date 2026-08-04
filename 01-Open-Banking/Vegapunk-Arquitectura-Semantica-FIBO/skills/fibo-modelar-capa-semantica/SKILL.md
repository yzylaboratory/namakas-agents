---
name: fibo-modelar-capa-semantica
description: Diseña una capa semántica o glosario canónico acotado alineado a FIBO, separando modelo conceptual, lógico/físico y contratos API. Úsala cuando se pida modelo semántico, knowledge layer o vocabulario canónico para Open Banking.
metadata:
  author: yzylabs
  version: "1.0"
---

# Modelar capa semántica FIBO

## Propósito

Construir un modelo semántico operativo (subset) anclado en FIBO para un producto o dominio OB, sin ontologizar el banco entero.

## Entradas

- Alcance del dominio/producto.
- Alineaciones existentes o lista de términos prioritarios.
- Artefactos de datos/API a cubrir (opcional).
- Ancla de release FIBO (opcional).

## Procedimiento

1. Delimita el bounded context semántico (qué entra / qué no).
2. Inventaría términos prioritarios (máx. razonable para la entrega; prioriza por interoperabilidad).
3. Asegura alineación FIBO por término (reutiliza skills de navegación/alineación).
4. Modela:
   - Entidades y roles
   - Relaciones materiales
   - Atributos de negocio (no columnas físicas)
5. Declara tres capas: conceptual FIBO | lógico/físico | API/evento.
6. Documenta extensiones locales en namespace propio.
7. Emite diagrama textual o tabla de relaciones + glosario.

## Salida

```md
## Capa semántica

- Alcance: [...]
- Ancla FIBO: [...]
- Glosario canónico (tabla)
- Relaciones (tabla o lista)
- Extensiones locales: [...]
- Fuera de alcance: [...]
- Supuestos: [...]
```

## Casos límite

- Alcance demasiado amplio → exige priorización o escala a Luffy/Jinbe.
- Solo hay schemas físicos → no los renombres como FIBO; mapea hacia arriba.
- Solape con BIAN → capa FIBO no redefine Service Domains.

## Validación

- Todo término material tiene alineación o extensión marcada.
- Capas conceptual/físico/API no están mezcladas en una sola lista confusa.
- Cero clases FIBO inventadas.

## Criterios de terminado

- Modelo usable como fuente de verdad semántica del alcance.
- Listo para alimentar `HANDOFF_FIBO`.

## Casos de evaluación

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Normal | Glosario de 8 términos de cuentas/pagos | Capa + alineaciones |
| Ambiguo | “modelar todo Open Banking” | Recorte de alcance o bloqueo parcial |
| Límite | Mezcla BIAN + FIBO en un solo diagrama | Separación explícita de estándares |

## Fuentes

- https://github.com/edmcouncil/fibo (2026-08-04)
- https://www.omg.org/spec/EDMC-FIBO/ (2026-08-04)
- https://www.w3.org/TR/owl2-overview/ (2026-08-04)
- `references/mapa-dominios-fibo.md`
