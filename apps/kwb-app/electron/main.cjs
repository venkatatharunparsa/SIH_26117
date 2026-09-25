const {
  app,
  BrowserWindow,
  shell,
  Menu,
  dialog,
  ipcMain,
} = require("electron");
const fs = require("fs");
const fsp = require("fs/promises");
const path = require("path");

const DEV = process.env.KWB_ELECTRON_DEV === "1";
const RENDERER_URL = process.env.KWB_RENDERER_URL || "http://127.0.0.1:5173";
const API_ORIGIN = "http://127.0.0.1:8080";

/** @type {BrowserWindow | null} */
let mainWindow = null;

/** Sandboxed workspace root chosen via Open Folder (absolute path). */
let workspaceRoot = null;

const TEXT_EXTS = new Set([
  ".txt",
  ".md",
  ".csv",
  ".json",
  ".log",
  ".py",
  ".ts",
  ".tsx",
  ".js",
  ".cjs",
  ".mjs",
  ".yaml",
  ".yml",
  ".toml",
  ".xml",
  ".html",
  ".css",
]);
const IMAGE_EXTS = new Set([".png", ".jpg", ".jpeg", ".webp", ".gif"]);
const PDF_EXTS = new Set([".pdf"]);

function isAllowedNav(url) {
  try {
    const u = new URL(url);
    if (u.protocol === "file:") return true;
    if (u.origin === new URL(RENDERER_URL).origin) return true;
    if (u.origin === API_ORIGIN) return true;
    return false;
  } catch {
    return false;
  }
}

function sendToRenderer(channel, payload) {
  if (mainWindow && !mainWindow.isDestroyed()) {
    mainWindow.webContents.send(channel, payload);
  }
}

function resolveUnderRoot(rel) {
  if (!workspaceRoot) {
    throw new Error("no_workspace");
  }
  const root = path.resolve(workspaceRoot);
  const cleaned = String(rel || ".")
    .replace(/\\/g, "/")
    .replace(/^\/+/, "");
  if (cleaned.includes("\0") || cleaned.split("/").includes("..")) {
    throw new Error("path_traversal");
  }
  const abs = path.resolve(root, cleaned);
  const relCheck = path.relative(root, abs);
  if (relCheck.startsWith("..") || path.isAbsolute(relCheck)) {
    throw new Error("path_traversal");
  }
  return { root, abs, rel: cleaned === "" ? "." : cleaned.replace(/\\/g, "/") };
}

function kindFor(name) {
  const ext = path.extname(name).toLowerCase();
  if (TEXT_EXTS.has(ext)) return "text";
  if (IMAGE_EXTS.has(ext)) return "image";
  if (PDF_EXTS.has(ext)) return "pdf";
  return "other";
}

async function listTree(rel = ".", depth = 0, maxDepth = 3) {
  const { abs, rel: safeRel } = resolveUnderRoot(rel === "." ? "" : rel);
  const entries = [];
  let names;
  try {
    names = await fsp.readdir(abs, { withFileTypes: true });
  } catch {
    return entries;
  }
  names.sort((a, b) => {
    if (a.isDirectory() !== b.isDirectory()) return a.isDirectory() ? -1 : 1;
    return a.name.localeCompare(b.name);
  });
  for (const ent of names) {
    if (ent.name.startsWith(".")) continue;
    const childRel =
      safeRel === "." ? ent.name : `${safeRel}/${ent.name}`.replace(/^\.\//, "");
    if (ent.isDirectory()) {
      const node = {
        name: ent.name,
        path: childRel,
        kind: "dir",
        children: depth < maxDepth ? await listTree(childRel, depth + 1, maxDepth) : [],
      };
      entries.push(node);
    } else if (ent.isFile()) {
      entries.push({
        name: ent.name,
        path: childRel,
        kind: kindFor(ent.name),
      });
    }
  }
  return entries;
}

async function readWorkspaceFile(rel) {
  const { abs } = resolveUnderRoot(rel);
  const st = await fsp.stat(abs);
  if (!st.isFile()) throw new Error("not_a_file");
  if (st.size > 8 * 1024 * 1024) throw new Error("file_too_large");
  const name = path.basename(abs);
  const kind = kindFor(name);
  if (kind === "text") {
    const text = await fsp.readFile(abs, "utf8");
    return { ok: true, name, path: rel, kind, text, size: st.size };
  }
  if (kind === "image" || kind === "pdf") {
    const buf = await fsp.readFile(abs);
    const ext = path.extname(name).toLowerCase();
    const types = {
      ".png": "image/png",
      ".jpg": "image/jpeg",
      ".jpeg": "image/jpeg",
      ".webp": "image/webp",
      ".gif": "image/gif",
      ".pdf": "application/pdf",
    };
    return {
      ok: true,
      name,
      path: rel,
      kind,
      b64: buf.toString("base64"),
      contentType: types[ext] || "application/octet-stream",
      size: st.size,
    };
  }
  return {
    ok: true,
    name,
    path: rel,
    kind: "other",
    size: st.size,
    note: "Preview not supported · attach may still work for known types",
  };
}

async function openFolderDialog() {
  const result = await dialog.showOpenDialog(mainWindow, {
    title: "Open folder — Knowledge Work Bench",
    properties: ["openDirectory"],
  });
  if (result.canceled || !result.filePaths[0]) {
    return { ok: false, canceled: true };
  }
  workspaceRoot = result.filePaths[0];
  const tree = await listTree(".");
  const payload = {
    ok: true,
    root: workspaceRoot,
    rootName: path.basename(workspaceRoot),
    tree,
  };
  sendToRenderer("workspace:changed", payload);
  return payload;
}

async function openFilesDialog() {
  const result = await dialog.showOpenDialog(mainWindow, {
    title: "Open files — Knowledge Work Bench",
    properties: ["openFile", "multiSelections"],
    filters: [
      { name: "Workbench", extensions: ["txt", "md", "csv", "json", "log", "png", "jpg", "jpeg", "webp", "pdf"] },
      { name: "All", extensions: ["*"] },
    ],
  });
  if (result.canceled || !result.filePaths.length) {
    return { ok: false, canceled: true };
  }
  const files = [];
  for (const fp of result.filePaths) {
    const name = path.basename(fp);
    const kind = kindFor(name);
    const st = await fsp.stat(fp);
    if (st.size > 8 * 1024 * 1024) continue;
    if (kind === "text") {
      files.push({
        name,
        path: name,
        kind,
        text: await fsp.readFile(fp, "utf8"),
        size: st.size,
      });
    } else if (kind === "image" || kind === "pdf") {
      const ext = path.extname(name).toLowerCase();
      const types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".pdf": "application/pdf",
      };
      files.push({
        name,
        path: name,
        kind,
        b64: (await fsp.readFile(fp)).toString("base64"),
        contentType: types[ext] || "application/octet-stream",
        size: st.size,
      });
    }
  }
  sendToRenderer("workspace:files-opened", { ok: true, files });
  return { ok: true, files };
}

function buildMenu() {
  const isMac = process.platform === "darwin";
  /** @type {Electron.MenuItemConstructorOptions[]} */
  const template = [
    ...(isMac
      ? [
          {
            label: app.name,
            submenu: [
              { role: "about" },
              { type: "separator" },
              { role: "services" },
              { type: "separator" },
              { role: "hide" },
              { role: "hideOthers" },
              { role: "unhide" },
              { type: "separator" },
              { role: "quit" },
            ],
          },
        ]
      : []),
    {
      label: "File",
      submenu: [
        {
          label: "Open Folder…",
          accelerator: "CmdOrCtrl+O",
          click: () => {
            void openFolderDialog();
          },
        },
        {
          label: "Open Files…",
          accelerator: "CmdOrCtrl+Shift+O",
          click: () => {
            void openFilesDialog();
          },
        },
        {
          label: "Close Folder",
          click: () => {
            workspaceRoot = null;
            sendToRenderer("workspace:changed", {
              ok: true,
              root: null,
              rootName: null,
              tree: [],
            });
          },
        },
        { type: "separator" },
        isMac ? { role: "close" } : { role: "quit", label: "Exit" },
      ],
    },
    {
      label: "Edit",
      submenu: [
        { role: "undo" },
        { role: "redo" },
        { type: "separator" },
        { role: "cut" },
        { role: "copy" },
        { role: "paste" },
        { role: "selectAll" },
      ],
    },
    {
      label: "View",
      submenu: [
        { role: "reload" },
        { role: "forceReload" },
        { role: "toggleDevTools" },
        { type: "separator" },
        { role: "resetZoom" },
        { role: "zoomIn" },
        { role: "zoomOut" },
        { type: "separator" },
        { role: "togglefullscreen" },
      ],
    },
    {
      label: "Window",
      submenu: [{ role: "minimize" }, { role: "close" }],
    },
  ];
  Menu.setApplicationMenu(Menu.buildFromTemplate(template));
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1440,
    height: 900,
    minWidth: 1100,
    minHeight: 700,
    title: "Knowledge Work Bench",
    backgroundColor: "#0e1116",
    show: false,
    webPreferences: {
      preload: path.join(__dirname, "preload.cjs"),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      webSecurity: true,
    },
  });

  mainWindow.once("ready-to-show", () => {
    mainWindow?.show();
  });

  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    if (url.startsWith(API_ORIGIN)) {
      return { action: "allow" };
    }
    shell.openExternal(url);
    return { action: "deny" };
  });

  mainWindow.webContents.on("will-navigate", (event, url) => {
    if (!isAllowedNav(url)) {
      event.preventDefault();
      shell.openExternal(url);
    }
  });

  if (DEV) {
    mainWindow.webContents.openDevTools({ mode: "detach" });
    mainWindow.webContents.on("did-fail-load", (_e, code, desc, url) => {
      console.error("[kwb-app] did-fail-load", code, desc, url);
    });
    mainWindow.loadURL(RENDERER_URL).catch((err) => {
      console.error("[kwb-app] loadURL failed", err);
    });
  } else {
    mainWindow.loadFile(path.join(__dirname, "..", "dist", "index.html"));
  }

  mainWindow.on("closed", () => {
    mainWindow = null;
  });
}

function registerIpc() {
  ipcMain.handle("workspace:openFolder", async () => openFolderDialog());
  ipcMain.handle("workspace:openFiles", async () => openFilesDialog());
  ipcMain.handle("workspace:get", async () => {
    if (!workspaceRoot) {
      return { ok: true, root: null, rootName: null, tree: [] };
    }
    return {
      ok: true,
      root: workspaceRoot,
      rootName: path.basename(workspaceRoot),
      tree: await listTree("."),
    };
  });
  ipcMain.handle("workspace:list", async (_e, rel) => {
    try {
      return { ok: true, tree: await listTree(rel || ".") };
    } catch (err) {
      return { ok: false, error: String(err?.message || err) };
    }
  });
  ipcMain.handle("workspace:read", async (_e, rel) => {
    try {
      return await readWorkspaceFile(rel);
    } catch (err) {
      return { ok: false, error: String(err?.message || err) };
    }
  });
  ipcMain.handle("workspace:close", async () => {
    workspaceRoot = null;
    return { ok: true };
  });
}

app.whenReady().then(() => {
  buildMenu();
  registerIpc();
  createWindow();
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});
