# PLANNER — Los Piratas de Heart

Grupo técnico `PLANNER/`. Identidad de flota: **Los Piratas de Heart**.

Capitán y orquestador: **Trafalgar D. Water Law**.

## Runtime

La fuente de lectura/runtime de Cursor es `~/.cursor/agents/`.  
Este directorio solo **versiona** las definiciones; no las sustituye en runtime.

## Árbol

```
PLANNER/                              ← Los Piratas de Heart
├── captain/                          ← Capitán / orquestador
│   └── trafalgar-d-water-law.md
├── requirements-discovery/           ← Especialista
├── analista-de-sistemas/
├── arquitecto-de-software/
├── arquitecto-de-integraciones/
├── technical-planner/
└── documentador-tecnico/
```

## Cadena de mando

Todos los especialistas reportan a Law. Law delega, revisa, coordina y consolida el paquete para `IMPLEMENTER/`. No implementa código.

| Rol | Carpeta | Responsabilidad |
|-----|---------|-----------------|
| Capitán | `captain/` | Orquestar el proceso completo de planificación |
| Requirements Discovery | `requirements-discovery/` | Pregunta, aclara y descubre lo que realmente se necesita |
| Analista de sistemas | `analista-de-sistemas/` | Analiza el sistema actual, reglas, flujos y dependencias |
| Arquitecto de software | `arquitecto-de-software/` | Toma los requisitos aprobados y diseña el SDD |
| Arquitecto de integraciones | `arquitecto-de-integraciones/` | Diseña APIs, eventos, contratos y alineación con BIAN |
| Technical Planner | `technical-planner/` | Convierte el diseño en un plan de implementación ordenado |
| Documentador técnico | `documentador-tecnico/` | Normaliza, organiza y mantiene la documentación final |

## Agentes Cursor existentes

En `~/.cursor/agents/` solo está instalado hoy `trafalgar-d-water-law.md` (capitán).  
Los demás roles tienen estructura + README placeholder; no hay agentes `.md` completos versionados hasta que existan en Cursor o se autoricen.
