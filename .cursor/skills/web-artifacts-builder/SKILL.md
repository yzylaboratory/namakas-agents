---
name: web-artifacts-builder
description: Guide for building shareable web artifacts (HTML/React). Úsala cuando se pida un artefacto web empaquetado o demo interactiva frontend.
metadata:
  author: yzylabs
  version: "1.0"
  source: https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder
  license: Apache-2.0
  audited: 2026-08-04
---

# Web Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `(scripts upstream NO instalados — scaffold manual)/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `(scripts upstream NO instalados — scaffold manual)/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash (scripts upstream NO instalados — scaffold manual)/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash (scripts upstream NO instalados — scaffold manual)/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components

## Nakamas adaptation

Do **not** run upstream `init-artifact.sh` / `bundle-artifact.sh` or `npm install -g`. Scaffold with project-approved tooling after human review of dependencies.

## Fuentes / atribución

- Fuente: https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder
- Licencia: Apache-2.0
- Fecha de auditoría e instalación: 2026-08-04
- Security gate: PASS_WITH_LIMITATIONS
- Adaptado para Nakamas Agents (Vegapunk). No ejecutar scripts de instalación remotos del upstream.

## Límites Nakamas

- REPORT_TO: `cavendish-arquitectura-web`
- Multi-canal gov → `sanji-director-frontend`. Portal DX UI → Koala.
- FORBIDDEN: Tripulación `brd-*` / `yzy-*`, inventar BIAN/FIBO, Olvia/`brd-second-brain`.

- LIMITACIÓN: no se instalan ni ejecutan scripts/binarios del upstream; solo procedimiento en markdown adaptado.

