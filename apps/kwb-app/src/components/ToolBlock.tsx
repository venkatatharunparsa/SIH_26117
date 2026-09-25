import { useState } from "react";
import {
  AlertTriangle,
  CheckCircle2,
  ChevronRight,
  Info,
  Loader2,
  Wrench,
} from "lucide-react";
import type { StreamEntry } from "../lib/constants";

type ToolEntry = Extract<StreamEntry, { kind: "tool" }>;

type Props = {
  entry: ToolEntry;
};

function StatusIcon({ status }: { status: ToolEntry["status"] }) {
  if (status === "running")
    return <Loader2 size={12} className="spin" aria-hidden />;
  if (status === "ok")
    return <CheckCircle2 size={12} aria-hidden />;
  if (status === "deny")
    return <AlertTriangle size={12} aria-hidden />;
  return <Info size={12} aria-hidden />;
}

export function ToolBlock({ entry }: Props) {
  const [open, setOpen] = useState(
    entry.status === "deny" || entry.status === "running"
  );

  const phases = entry.phases || [];

  return (
    <div className={`tool-block${open ? " open" : ""}`}>
      <div
        className="tool-head"
        onClick={() => setOpen((o) => !o)}
        role="button"
        tabIndex={0}
        onKeyDown={(ev) => {
          if (ev.key === "Enter" || ev.key === " ") {
            ev.preventDefault();
            setOpen((o) => !o);
          }
        }}
      >
        <ChevronRight
          size={14}
          className={`tool-chevron${open ? " open" : ""}`}
          aria-hidden
        />
        <Wrench size={13} className="tool-wrench" aria-hidden />
        <span className="tool-name">{entry.name}</span>
        <span className="tool-path">{entry.path}</span>
        <span className={`tool-status ${entry.status}`}>
          <StatusIcon status={entry.status} />
          {entry.status === "running" ? "running" : entry.status}
        </span>
      </div>
      {phases.length > 0 ? (
        <div className="tool-phases" aria-live="polite">
          {phases.map((p, i) => (
            <span
              key={`${i}-${p.slice(0, 24)}`}
              className={`tool-phase${i === phases.length - 1 && entry.status === "running" ? " live" : ""}`}
            >
              {p}
            </span>
          ))}
        </div>
      ) : null}
      <div className="tool-body">
        {entry.summary && <div className="tool-summary">{entry.summary}</div>}
        {entry.errorCode && (
          <div className="tool-summary" style={{ color: "var(--deny)" }}>
            deny · {entry.errorCode}
          </div>
        )}
        {entry.request !== undefined && (
          <pre className="tool-json">
            {`→ ${JSON.stringify(entry.request, null, 2)}`}
          </pre>
        )}
        {entry.response !== undefined && (
          <pre className="tool-json">
            {`← ${JSON.stringify(entry.response, null, 2)}`}
          </pre>
        )}
      </div>
    </div>
  );
}
