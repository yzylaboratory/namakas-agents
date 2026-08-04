# Referencia rápida — pruebas funcionales y regulación

Última revisión: 2026-08-04. Apoyo a skills de Tashigi. No sustituye dictamen legal.

## Técnicas black-box (finanzas)

| Técnica | Uso típico |
|---|---|
| Partición de equivalencia | Clases de transacciones válidas/inválidas |
| Valores límite | Montos, precisión 0.01, umbrales just-below/at/above |
| Tabla de decisión | Combinaciones de reglas / tarifas / elegibilidad |
| Transición de estado | active/inactive/blocked, consentimientos, órdenes |

Fuente primaria: ISTQB CT-FT Syllabus v1.0 (2026/05/27).

## Auditabilidad mínima

1. Cita del mandato/control (fuente + versión/fecha).
2. Requisito funcional que lo implementa.
3. Caso(s) de prueba enlazados.
4. Evidencia de resultado (o NOT_EXECUTED explícito).
5. Defecto con enlace inverso al control cuando aplica.

## Separación QA Nakamas

| Célula | Foco |
|---|---|
| Tashigi | Funcional + cumplimiento funcional / trazabilidad |
| Kalifa | APIs y contratos |
| Kuma | Automatización |
| Kaido | Carga y rendimiento |

## Enlaces

- https://istqb.org/certifications/certified-tester-finance-testing-ct-ft/
- https://glossary.istqb.org/
- https://astqb.org/assets/documents/ISTQB-CT-FT-Syllabus-v1.0.pdf
