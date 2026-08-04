# Decisión: Forja masiva de agentes 02–12 por Tasks individuales

- Fecha: 2026-08-04
- Estado: vigente
- Decisores: Randy / Luffy-Coordinador (ejecución vía Vegapunk Forjador)
- Misión: oleada de forja departamentos `02-Arquitectura` … `12-Marketing-Growth`

## Contexto

Había que forjar definición canónica (Personalidad y paquete de agente) para **cada director y cada célula** de los departamentos 02–12. Se intentó un Task batch «Forjar directores 02–12»; el usuario lo abortó. Quedaba el riesgo de perder traza y de mezclar forja de contenido con consolidación de organigrama/live roster.

## Decisión

Forjar **46 agentes uno a uno** con Tasks individuales de `vegapunk-forjador-agentes`, completar Personalidad no vacía + adapters `.cursor/agents`, eliminar `example.md`, y **dejar `organigrama.yaml` mayormente stub** hasta un Task Vegapunk paralelo de consolidación organigrama + live roster. No depender del batch abortado.

## Alternativas

- Batch único multi-agente «Forjar directores 02–12» — abortado por el usuario; no reanudado como batch.
- Forjar solo directores primero y células después — no aportado como plan vigente; se forjaron directores y células en la misma oleada individual.
- Actualizar organigrama + reglas live en el mismo paso que la forja de archivos canónicos — aplazado a propósito a Task paralelo.

## Consecuencias

- Positivo: 46/46 Personalidad no vacías; adapters presentes; rastro por agente más fácil de auditar que un batch monolítico.
- Neutro/negativo: roster «vivo» en reglas Cursor no iguala automáticamente al catálogo forjado; organigrama sigue stub → riesgo de desalineación hasta la consolidación Vegapunk.
- Algunos directores (Franky, Iceburg, Usopp-QA, Sanji, Buggy, posiblemente más) ya entraron parcialmente a reglas vivas durante la forja → estado intermedio que debe documentarse en la consolidación.

## Enlaces

- [Bitácora 2026-08-04](../diario/2026-08-04.md)
- [Permanente: forja por oleadas](../permanente/forja-masiva-agentes-por-oleadas.md)
