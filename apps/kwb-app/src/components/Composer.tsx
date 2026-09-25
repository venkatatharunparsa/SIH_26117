import { useEffect, useRef, useState, type KeyboardEvent } from "react";
import {
  ArrowUp,
  Check,
  Loader2,
  MoreHorizontal,
  Paperclip,
} from "lucide-react";
import type { TaskType } from "../lib/constants";
import { FIXTURES, type FixtureId } from "../lib/constants";
import type { PendingAsk } from "../lib/conductor";

type Props = {
  taskType: TaskType;
  busy: boolean;
  pendingAsk: PendingAsk | null;
  /** True when agent can advance without an open ask */
  canContinue: boolean;
  attachedName: string | null;
  onAttachedName: (name: string | null) => void;
  onAttachText: (text: string, name: string) => void;
  onAttachBinary: (b64: string, name: string, contentType: string) => void;
  onStreamNote: (text: string) => void;
  onAction: (action: string) => void;
  /** Claude Code: empty continue / typed reply */
  onSubmit: (text: string) => void;
  draftInput: string;
  onDraftInput: (v: string) => void;
};

const TEXT_EXTS = [".txt", ".md", ".csv", ".json", ".log"];
const BINARY_EXTS = [".png", ".jpg", ".jpeg", ".webp", ".pdf"];

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

const MORE: { id: string; label: string; danger?: boolean }[] = [
  { id: "draft-edit", label: "Edit draft (stale self-check)" },
  { id: "sandbox-calc", label: "Sandbox calc" },
  { id: "sandbox-red", label: "Sandbox red (fail demo)" },
  { id: "mon-a-start", label: "Evidence pack start" },
  { id: "mon-a-stop", label: "Evidence pack stop" },
  { id: "g9", label: "Inject secret (deny demo)", danger: true },
  { id: "g8", label: "Bad model (deny demo)", danger: true },
  { id: "revoke", label: "Revoke grant", danger: true },
];

export function Composer({
  taskType,
  busy,
  pendingAsk,
  canContinue,
  attachedName,
  onAttachedName,
  onAttachText,
  onAttachBinary,
  onStreamNote,
  onAction,
  onSubmit,
  draftInput,
  onDraftInput,
}: Props) {
  const fileRef = useRef<HTMLInputElement>(null);
  const [attachOpen, setAttachOpen] = useState(false);
  const [moreOpen, setMoreOpen] = useState(false);
  const [fixtureId, setFixtureId] = useState<FixtureId>("FX-EXT-01");
  const wrapRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function onDoc(e: MouseEvent) {
      if (!wrapRef.current?.contains(e.target as Node)) {
        setAttachOpen(false);
        setMoreOpen(false);
      }
    }
    document.addEventListener("mousedown", onDoc);
    return () => document.removeEventListener("mousedown", onDoc);
  }, []);

  async function onFile(file: File | null) {
    if (!file) return;
    const lower = file.name.toLowerCase();
    const isText = TEXT_EXTS.some((e) => lower.endsWith(e));
    const isBinary = BINARY_EXTS.some((e) => lower.endsWith(e));
    if (!isText && !isBinary) {
      onStreamNote(
        `Attach refused · use .txt/.md/.csv or .png/.jpg/.pdf (OCR/PDF ingest)`
      );
      return;
    }
    try {
      if (isBinary) {
        const b64 = await fileToBase64(file);
        onAttachBinary(b64, file.name, file.type || "");
      } else {
        const text = await file.text();
        onAttachText(text, file.name);
      }
      setAttachOpen(false);
    } catch {
      onStreamNote(`Attach failed · ${file.name}`);
    }
  }

  function loadFixture() {
    const fx = FIXTURES.find((f) => f.id === fixtureId);
    if (!fx) return;
    onAttachText(fx.body, fx.id);
    setAttachOpen(false);
  }

  function onKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      onSubmit(draftInput);
    }
  }

  const placeholder = pendingAsk
    ? "Reply to the ask above · Enter to confirm · Shift+Enter newline"
    : canContinue
      ? "Message the agent… · empty Enter continues when a step is ready"
      : "Message the workbench…";

  const hasText = Boolean(draftInput.trim());
  const sendTitle = busy
    ? "Working…"
    : hasText
      ? "Send"
      : pendingAsk
        ? "Confirm"
        : canContinue
          ? "Continue"
          : "Send";

  return (
    <div className="composer cc" ref={wrapRef}>
      <div className="cc-bar">
        <div className="cc-meta">
          <span className="cc-mode-tag">{taskType}</span>
          {attachedName ? (
            <span className="cc-attach-pill" title={attachedName}>
              <Paperclip size={11} strokeWidth={2} aria-hidden />
              {attachedName}
            </span>
          ) : (
            <span className="cc-next-hint">context in background</span>
          )}
          {pendingAsk ? (
            <span className="cc-ask-pill">waiting for you</span>
          ) : canContinue ? (
            <span className="cc-next-hint">ready to continue</span>
          ) : null}
        </div>

        <div className="cc-input-row">
          <div className="cc-tools">
            <button
              type="button"
              className={`cc-icon${attachOpen ? " on" : ""}`}
              disabled={busy}
              title="Add context (file / fixture)"
              aria-label="Attach context"
              onClick={() => {
                setMoreOpen(false);
                setAttachOpen((o) => !o);
              }}
            >
              <Paperclip size={16} strokeWidth={1.75} />
            </button>
            <button
              type="button"
              className={`cc-icon${moreOpen ? " on" : ""}`}
              disabled={busy}
              title="More tools"
              aria-label="More tools"
              onClick={() => {
                setAttachOpen(false);
                setMoreOpen((o) => !o);
              }}
            >
              <MoreHorizontal size={16} strokeWidth={1.75} />
            </button>
          </div>

          <textarea
            className="cc-prompt"
            rows={2}
            disabled={busy}
            placeholder={placeholder}
            value={draftInput}
            onChange={(e) => onDraftInput(e.target.value)}
            onKeyDown={onKeyDown}
          />

          <button
            type="button"
            className={`cc-send${hasText || pendingAsk || canContinue ? " ready" : ""}`}
            disabled={busy}
            title={sendTitle}
            aria-label={sendTitle}
            onClick={() => onSubmit(draftInput)}
          >
            {busy ? (
              <Loader2 size={16} className="spin" aria-hidden />
            ) : pendingAsk && !hasText ? (
              <Check size={16} strokeWidth={2.25} aria-hidden />
            ) : (
              <ArrowUp size={16} strokeWidth={2.25} aria-hidden />
            )}
          </button>
        </div>
      </div>

      {attachOpen && (
        <div className="cc-popover" role="dialog" aria-label="Add context">
          <p className="cc-pop-title">Add context</p>
          <p className="cc-pop-help">
            Text · Markdown · PNG/JPG (OCR) · PDF → orchestrator extract → company
            docs → Confirm extract → Word DRAFT (.docx). Chat uses /orch/turn →
            Pack → Gateway (up to 10 messages). Missing Tesseract → fixture stub,
            labeled NOT live OCR.
          </p>
          <div className="cc-pop-actions">
            <input
              ref={fileRef}
              type="file"
              accept=".txt,.md,.csv,.json,.log,.png,.jpg,.jpeg,.webp,.pdf,text/plain,image/png,image/jpeg,application/pdf"
              hidden
              onChange={(e) => {
                void onFile(e.target.files?.[0] ?? null);
                e.target.value = "";
              }}
            />
            <button
              type="button"
              className="cc-mini"
              disabled={busy}
              onClick={() => fileRef.current?.click()}
            >
              Document…
            </button>
            <select
              className="cc-select"
              value={fixtureId}
              disabled={busy}
              onChange={(e) => setFixtureId(e.target.value as FixtureId)}
            >
              {FIXTURES.map((f) => (
                <option key={f.id} value={f.id}>
                  {f.id}
                </option>
              ))}
            </select>
            <button
              type="button"
              className="cc-mini primary"
              disabled={busy}
              onClick={loadFixture}
            >
              Load fixture
            </button>
            {attachedName ? (
              <button
                type="button"
                className="cc-mini"
                disabled={busy}
                onClick={() => {
                  onAttachedName(null);
                  onStreamNote("Cleared attach label · extract context kept");
                }}
              >
                Clear label
              </button>
            ) : null}
          </div>
        </div>
      )}

      {moreOpen && (
        <div className="cc-popover more" role="menu">
          <p className="cc-pop-title">More</p>
          {MORE.map((m) => (
            <button
              key={m.id}
              type="button"
              className={`cc-menu-item${m.danger ? " danger" : ""}`}
              disabled={busy}
              onClick={() => {
                setMoreOpen(false);
                onAction(m.id);
              }}
            >
              {m.label}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
