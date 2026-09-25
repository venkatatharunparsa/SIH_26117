import { Eye, Paperclip, X } from "lucide-react";
import type { WorkspaceFile } from "../lib/workspaceTypes";

type Props = {
  file: WorkspaceFile | null;
  onClose: () => void;
  onAttach: () => void;
  canAttach: boolean;
};

export function PreviewPane({ file, onClose, onAttach, canAttach }: Props) {
  if (!file) return null;

  const dataUrl =
    file.b64 && file.contentType
      ? `data:${file.contentType};base64,${file.b64}`
      : null;

  return (
    <aside className="preview-pane" aria-label="File preview">
      <div className="preview-head">
        <h2>
          <Eye size={13} aria-hidden /> {file.name}
        </h2>
        <div className="preview-actions">
          <button
            type="button"
            className="cc-mini primary"
            disabled={!canAttach}
            onClick={onAttach}
          >
            <Paperclip size={12} aria-hidden /> Attach
          </button>
          <button
            type="button"
            className="btn-icon"
            aria-label="Close preview"
            onClick={onClose}
          >
            <X size={13} />
          </button>
        </div>
      </div>
      <div className="preview-meta">
        {file.kind}
        {file.size != null ? ` · ${file.size} B` : ""}
        {file.path ? ` · ${file.path}` : ""}
      </div>
      <div className="preview-body">
        {file.kind === "text" && file.text != null ? (
          <pre className="preview-text">{file.text}</pre>
        ) : null}
        {file.kind === "image" && dataUrl ? (
          <img className="preview-img" src={dataUrl} alt={file.name} />
        ) : null}
        {file.kind === "pdf" && dataUrl ? (
          <iframe
            className="preview-pdf"
            title={file.name}
            src={dataUrl}
          />
        ) : null}
        {file.kind === "other" || file.error ? (
          <p className="preview-note">
            {file.error || file.note || "No preview for this type"}
          </p>
        ) : null}
      </div>
    </aside>
  );
}
