/**
 * Windows-friendly electron:dev launcher.
 * Starts Vite, waits for 127.0.0.1:5173, then opens Electron.
 */
import { spawn } from "node:child_process";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");

const children = [];

function spawnInherit(command, args, extraEnv = {}) {
  const child = spawn(command, args, {
    cwd: root,
    stdio: "inherit",
    shell: true,
    env: { ...process.env, ...extraEnv },
  });
  children.push(child);
  return child;
}

function waitForHttp(url, timeoutMs = 60000) {
  const start = Date.now();
  return new Promise((resolve, reject) => {
    const tick = () => {
      const req = http.get(url, (res) => {
        res.resume();
        resolve();
      });
      req.on("error", () => {
        if (Date.now() - start > timeoutMs) {
          reject(new Error(`Timeout waiting for ${url}`));
          return;
        }
        setTimeout(tick, 400);
      });
    };
    tick();
  });
}

function shutdown(code = 0) {
  for (const c of children) {
    try {
      c.kill();
    } catch {
      /* ignore */
    }
  }
  process.exit(code);
}

process.on("SIGINT", () => shutdown(0));
process.on("SIGTERM", () => shutdown(0));

const vite = spawnInherit("npx", [
  "vite",
  "--host",
  "127.0.0.1",
  "--port",
  "5173",
]);

vite.on("exit", (code) => {
  if (code && code !== 0) shutdown(code);
});

try {
  await waitForHttp("http://127.0.0.1:5173/");
  console.log("[kwb-app] Vite ready — launching Electron");
  const electron = spawnInherit("npx", ["electron", "."], {
    KWB_ELECTRON_DEV: "1",
  });
  electron.on("exit", (code) => shutdown(code ?? 0));
} catch (err) {
  console.error(err);
  shutdown(1);
}
