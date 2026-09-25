const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("kwbDesktop", {
  platform: process.platform,
  isElectron: true,
  apiBase: "http://127.0.0.1:8080",
  openFolder: () => ipcRenderer.invoke("workspace:openFolder"),
  openFiles: () => ipcRenderer.invoke("workspace:openFiles"),
  getWorkspace: () => ipcRenderer.invoke("workspace:get"),
  listWorkspace: (rel) => ipcRenderer.invoke("workspace:list", rel),
  readWorkspaceFile: (rel) => ipcRenderer.invoke("workspace:read", rel),
  closeWorkspace: () => ipcRenderer.invoke("workspace:close"),
  onWorkspaceChanged: (cb) => {
    const handler = (_event, payload) => cb(payload);
    ipcRenderer.on("workspace:changed", handler);
    return () => ipcRenderer.removeListener("workspace:changed", handler);
  },
  onFilesOpened: (cb) => {
    const handler = (_event, payload) => cb(payload);
    ipcRenderer.on("workspace:files-opened", handler);
    return () => ipcRenderer.removeListener("workspace:files-opened", handler);
  },
});
