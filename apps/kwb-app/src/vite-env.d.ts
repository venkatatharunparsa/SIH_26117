/// <reference types="vite/client" />

interface KwbDesktop {
  platform: string;
  isElectron: boolean;
  apiBase: string;
}

interface Window {
  kwbDesktop?: KwbDesktop;
}
