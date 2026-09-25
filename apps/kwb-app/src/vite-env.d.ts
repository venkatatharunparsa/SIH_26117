/// <reference types="vite/client" />

import type {
  WorkspaceFile,
  WorkspaceNode,
  WorkspaceSnapshot,
} from "./lib/workspaceTypes";

declare global {
  interface KwbDesktop {
    platform: string;
    isElectron: boolean;
    apiBase: string;
    openFolder?: () => Promise<WorkspaceSnapshot>;
    openFiles?: () => Promise<{
      ok: boolean;
      canceled?: boolean;
      files?: WorkspaceFile[];
    }>;
    getWorkspace?: () => Promise<WorkspaceSnapshot>;
    listWorkspace?: (
      rel?: string
    ) => Promise<{ ok: boolean; tree?: WorkspaceNode[]; error?: string }>;
    readWorkspaceFile?: (rel: string) => Promise<WorkspaceFile>;
    closeWorkspace?: () => Promise<{ ok: boolean }>;
    onWorkspaceChanged?: (
      cb: (payload: WorkspaceSnapshot) => void
    ) => () => void;
    onFilesOpened?: (
      cb: (payload: { ok: boolean; files?: WorkspaceFile[] }) => void
    ) => () => void;
  }

  interface Window {
    kwbDesktop?: KwbDesktop;
  }
}

export {};
