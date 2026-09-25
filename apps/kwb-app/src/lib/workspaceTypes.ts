export type WorkspaceNode = {
  name: string;
  path: string;
  kind: "dir" | "text" | "image" | "pdf" | "other";
  children?: WorkspaceNode[];
};

export type WorkspaceSnapshot = {
  ok: boolean;
  root: string | null;
  rootName: string | null;
  tree: WorkspaceNode[];
  canceled?: boolean;
  error?: string;
};

export type WorkspaceFile = {
  ok?: boolean;
  name: string;
  path: string;
  kind: "text" | "image" | "pdf" | "other";
  text?: string;
  b64?: string;
  contentType?: string;
  size?: number;
  note?: string;
  error?: string;
};
