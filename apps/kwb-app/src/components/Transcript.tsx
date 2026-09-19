import type { StreamEntry } from "../lib/constants";
import { ToolBlock } from "./ToolBlock";

type Props = {
  entries: StreamEntry[];
};

export function Transcript({ entries }: Props) {
  if (entries.length === 0) {
    return (
      <div className="transcript">
        <div className="empty-stream">
          <h3>Session workspace</h3>
          <p>
            Start a task from the left rail or press{" "}
            <kbd>New task</kbd>. Actions appear here as tool blocks — not a
            marketing wizard.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="transcript" role="log" aria-live="polite">
      {entries.map((e) => {
        if (e.kind === "system") {
          return (
            <div key={e.id} className="entry-system">
              {e.text}
            </div>
          );
        }
        if (e.kind === "user") {
          return (
            <div key={e.id} className="entry-user">
              <div className="label">You</div>
              {e.text}
            </div>
          );
        }
        return <ToolBlock key={e.id} entry={e} />;
      })}
    </div>
  );
}
