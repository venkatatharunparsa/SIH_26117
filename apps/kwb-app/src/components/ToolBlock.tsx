import { useState } from "react";
import type { StreamEntry } from "../lib/constants";

type ToolEntry = Extract<StreamEntry, { kind: "tool" }>;

type Props = {
  entry: ToolEntry;
};

export function ToolBlock({ entry }: Props) {
  const [open, setOpen] = useState(
    entry.status === "deny" || entry.status === "running"
  );

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
        <span className="tool-name">{entry.name}</span>
        <span className="tool-path">{entry.path}</span>
        <span className={`tool-status ${entry.status}`}>{entry.status}</span>
      </div>
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
