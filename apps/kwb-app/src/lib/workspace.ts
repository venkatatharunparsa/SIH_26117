import type { WorkspaceFile, WorkspaceNode, WorkspaceSnapshot } from "./workspaceTypes";
import { API_BASE, api } from "./api";

const TEXT_EXTS = [
  ".txt",
  ".md",
  ".csv",
  ".json",
  ".log",
  ".py",
  ".yaml",
  ".yml",
];
const IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".webp"];
const PDF_EXTS = [".pdf"];

function kindFor(name: string): WorkspaceNode["kind"] {
  const lower = name.toLowerCase();
  if (TEXT_EXTS.some((e) => lower.endsWith(e))) return "text";
  if (IMAGE_EXTS.some((e) => lower.endsWith(e))) return "image";
  if (PDF_EXTS.some((e) => lower.endsWith(e))) return "pdf";
  return "other";
}

function fileToBase64(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const result = String(reader.result || "");
      const comma = result.indexOf(",");
      resolve(comma >= 0 ? result.slice(comma + 1) : result);
    };
    reader.onerror = () => reject(reader.error || new Error("read failed"));
    reader.readAsDataURL(file);
  });
}

/** Browser: build a shallow tree from <input webkitdirectory>. */
export async function snapshotFromDirectoryFiles(
  fileList: FileList
): Promise<{ snapshot: WorkspaceSnapshot; cache: Map<string, WorkspaceFile> }> {
  const cache = new Map<string, WorkspaceFile>();
  const rootName =
    fileList[0]?.webkitRelativePath?.split(/[/\\]/)[0] || "folder";
  const top = new Map<string, WorkspaceNode>();

  for (const file of Array.from(fileList)) {
    const rel = file.webkitRelativePath || file.name;
    const parts = rel.split(/[/\\]/).filter(Boolean);
    if (parts.length < 2) continue;
    const name = parts[parts.length - 1];
    if (name.startsWith(".")) continue;
    const kind = kindFor(name);
    if (kind === "other") continue;
    // Flatten to top-level files + one-level dirs for simplicity
    if (parts.length === 2) {
      const node: WorkspaceNode = { name, path: name, kind };
      top.set(name, node);
      if (kind === "text") {
        cache.set(name, {
          name,
          path: name,
          kind: "text",
          text: await file.text(),
          size: file.size,
        });
      } else if (kind === "image" || kind === "pdf") {
        cache.set(name, {
          name,
          path: name,
          kind,
          b64: await fileToBase64(file),
          contentType: file.type || undefined,
          size: file.size,
        });
      }
    } else {
      const dir = parts[1];
      let dirNode = top.get(dir);
      if (!dirNode || dirNode.kind !== "dir") {
        dirNode = { name: dir, path: dir, kind: "dir", children: [] };
        top.set(dir, dirNode);
      }
      const childPath = parts.slice(1).join("/");
      dirNode.children = dirNode.children || [];
      if (!dirNode.children.some((c) => c.path === childPath)) {
        dirNode.children.push({ name, path: childPath, kind });
      }
      if (kind === "text") {
        cache.set(childPath, {
          name,
          path: childPath,
          kind: "text",
          text: await file.text(),
          size: file.size,
        });
      } else if (kind === "image" || kind === "pdf") {
        cache.set(childPath, {
          name,
          path: childPath,
          kind,
          b64: await fileToBase64(file),
          contentType: file.type || undefined,
          size: file.size,
        });
      }
    }
  }

  return {
    snapshot: {
      ok: true,
      root: rootName,
      rootName,
      tree: Array.from(top.values()).sort((a, b) =>
        a.kind === "dir" && b.kind !== "dir"
          ? -1
          : b.kind === "dir" && a.kind !== "dir"
            ? 1
            : a.name.localeCompare(b.name)
      ),
    },
    cache,
  };
}

export async function loadDemoFixtures(): Promise<{
  snapshot: WorkspaceSnapshot;
  cache: Map<string, WorkspaceFile>;
}> {
  const cat = await api<{
    ok?: boolean;
    root?: string;
    rootName?: string;
    tree?: Array<{ name: string; path: string; kind: string; size?: number }>;
  }>("/fixtures/catalog");
  const tree: WorkspaceNode[] = (cat.tree || []).map((t) => {
    const kind = (t.kind as WorkspaceNode["kind"]) || "other";
    const rawKids = (t as { children?: Array<{ name: string; path: string; kind: string }> })
      .children;
    const node: WorkspaceNode = {
      name: t.name,
      path: t.path,
      kind,
    };
    if (Array.isArray(rawKids) && rawKids.length) {
      node.children = rawKids.map((c) => ({
        name: c.name,
        path: c.path,
        kind: (c.kind as WorkspaceNode["kind"]) || "other",
      }));
    }
    return node;
  });
  return {
    snapshot: {
      ok: true,
      root: cat.root || `${API_BASE}/fixtures`,
      rootName: cat.rootName || "fixtures",
      tree,
    },
    cache: new Map(),
  };
}

export async function readDemoFixture(name: string): Promise<WorkspaceFile> {
  return api<WorkspaceFile>(`/fixtures/file/${encodeURIComponent(name)}`);
}
