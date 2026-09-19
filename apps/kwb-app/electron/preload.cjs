const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("kwbDesktop", {
  platform: process.platform,
  isElectron: true,
  apiBase: "http://127.0.0.1:8080",
});
