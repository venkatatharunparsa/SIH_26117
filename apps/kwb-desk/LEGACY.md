# REJECTED / LEGACY — do not demo

**Status:** REJECTED (2026-09-19)  
**Reason:** Marketing / Syne hero Next.js desk reads as a **web app**, not KWB desktop application.

## Use instead

```text
cd apps/kwb-app
npm run electron:dev
```

Primary product: **Electron Knowledge Work Bench** (`apps/kwb-app/`).

Do not run `npm run dev` here for jury demos.

**Hard-fail:** `npm run dev|build|start|lint` exit 1 via `scripts/refuse-legacy.cjs`.  
Bypass only for archaeology: `npm run legacy:force-dev` (page still shows REJECTED banner).
