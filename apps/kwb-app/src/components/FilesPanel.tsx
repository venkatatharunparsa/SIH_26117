import { useEffect, useState } from "react";
import {
  ChevronDown,
  ChevronRight,
  File,
  FileImage,
  FileText,
  Folder,
  FolderOpen,
  FolderPlus,
  Paperclip,
  X,
} from "lucide-react";
import type {
  WorkspaceFile,
  WorkspaceNode,
  WorkspaceSnapshot,
} from "../lib/workspaceTypes";

type Props = {
  snapshot: WorkspaceSnapshot | null;
  selectedPath: string | null;
  onSelect: (path: string) => void;
  onOpenFolder: () => void;
  onOpenDemoFixtures: () => void;
  onCloseFolder: () => void;
  onAttachSelected: () => void;
  canAttach: boolean;
  isElectron: boolean;
};

function FileIcon({ kind, open }: { kind: WorkspaceNode["kind"]; open?: boolean }) {
  if (kind === "dir")
    return open ? (
      <FolderOpen size={13} aria-hidden />
    ) : (
      <Folder size={13} aria-hidden />
    );
  if (kind === "image") return <FileImage size={13} aria-hidden />;
  if (kind === "pdf" || kind === "text") return <FileText size={13} aria-hidden />;
  return <File size={13} aria-hidden />;
}

function collectDirPaths(nodes: WorkspaceNode[], out: string[] = []): string[] {
  for (const n of nodes) {
    if (n.kind === "dir") {
      out.push(n.path);
      if (n.children?.length) collectDirPaths(n.children, out);
    }
  }
  return out;
}

function TreeNodes({
  nodes,
  selectedPath,
  onSelect,
  expanded,
  onToggle,
  depth = 0,
}: {
  nodes: WorkspaceNode[];
  selectedPath: string | null;
  onSelect: (path: string) => void;
  expanded: Set<string>;
  onToggle: (path: string) => void;
  depth?: number;
}) {
  return (
    <ul className="file-tree" style={{ paddingLeft: depth ? 10 : 0 }}>
      {nodes.map((n) => {
        const isDir = n.kind === "dir";
        const isOpen = isDir && expanded.has(n.path);
        const active = selectedPath === n.path;
        const hasKids = Boolean(n.children?.length);
        return (
          <li key={n.path}>
            <button
              type="button"
              className={`file-node${active ? " active" : ""}${isDir ? " dir" : ""}`}
              aria-expanded={isDir ? isOpen : undefined}
              title={n.path}
              onClick={() => {
                if (isDir) onToggle(n.path);
                else onSelect(n.path);
              }}
            >
              {isDir ? (
                <span className="file-chev-wrap" aria-hidden>
                  {isOpen ? (
                    <ChevronDown size={12} className="file-chev" />
                  ) : (
                    <ChevronRight size={12} className="file-chev" />
                  )}
                </span>
              ) : (
                <span className="file-chev-spacer" />
              )}
              <FileIcon kind={n.kind} open={isOpen} />
              <span className="file-name">{n.name}</span>
            </button>
            {isDir && isOpen && hasKids ? (
              <TreeNodes
                nodes={n.children || []}
                selectedPath={selectedPath}
                onSelect={onSelect}
                expanded={expanded}
                onToggle={onToggle}
                depth={depth + 1}
              />
            ) : null}
          </li>
        );
      })}
    </ul>
  );
}

export function FilesPanel({
  snapshot,
  selectedPath,
  onSelect,
  onOpenFolder,
  onOpenDemoFixtures,
  onCloseFolder,
  onAttachSelected,
  canAttach,
  isElectron,
}: Props) {
  const hasRoot = Boolean(snapshot?.root);
  const tree = snapshot?.tree || [];
  const [expanded, setExpanded] = useState<Set<string>>(() => new Set());

  useEffect(() => {
    // Default: expand all dirs one level when folder changes
    const rootKey = snapshot?.root || "";
    if (!rootKey) {
      setExpanded(new Set());
      return;
    }
    setExpanded(new Set(collectDirPaths(tree)));
  }, [snapshot?.root]);

  function toggle(path: string) {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(path)) next.delete(path);
      else next.add(path);
      return next;
    });
  }

  return (
    <aside className="files-panel" aria-label="Files">
      <div className="files-head">
        <h2>
          {hasRoot ? (
            <>
              <FolderOpen size={13} aria-hidden /> {snapshot?.rootName || "Folder"}
            </>
          ) : (
            <>
              <Folder size={13} aria-hidden /> Files
            </>
          )}
        </h2>
        {hasRoot ? (
          <button
            type="button"
            className="btn-icon"
            title="Close folder"
            aria-label="Close folder"
            onClick={onCloseFolder}
          >
            <X size={13} />
          </button>
        ) : null}
      </div>

      {!hasRoot ? (
        <div className="files-empty">
          <p>
            Open a project folder to browse scans, notes, and PDFs — then attach
            into the agent turn.
          </p>
          <button type="button" className="cc-mini primary" onClick={onOpenFolder}>
            <FolderPlus size={13} aria-hidden />{" "}
            {isElectron ? "Open Folder…" : "Choose Folder…"}
          </button>
          <button type="button" className="cc-mini" onClick={onOpenDemoFixtures}>
            Demo fixtures
          </button>
          {isElectron ? (
            <p className="files-hint">Menu · File → Open Folder (Ctrl+O)</p>
          ) : (
            <p className="files-hint">Browser · folder picker or demo fixtures</p>
          )}
        </div>
      ) : (
        <>
          <div className="files-body">
            {tree.length === 0 ? (
              <p className="files-hint">Empty folder</p>
            ) : (
              <TreeNodes
                nodes={tree}
                selectedPath={selectedPath}
                onSelect={onSelect}
                expanded={expanded}
                onToggle={toggle}
              />
            )}
          </div>
          <div className="files-foot">
            <button
              type="button"
              className="cc-mini primary"
              disabled={!canAttach}
              onClick={onAttachSelected}
              title="Send selected file into /orch/turn attach"
            >
              <Paperclip size={12} aria-hidden /> Attach to agent
            </button>
          </div>
        </>
      )}
    </aside>
  );
}

export type { WorkspaceFile, WorkspaceSnapshot };
