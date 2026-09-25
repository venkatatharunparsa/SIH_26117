#!/usr/bin/env node
/** Hard-fail: kwb-desk is REJECTED. Primary product is apps/kwb-app. */
const msg = `
╔══════════════════════════════════════════════════════════════╗
║  REJECTED — do not demo apps/kwb-desk                        ║
║  Use:  cd apps/kwb-app && npm run electron:dev               ║
║  See:  apps/kwb-desk/LEGACY.md                               ║
╚══════════════════════════════════════════════════════════════╝
`;
console.error(msg);
process.exit(1);
