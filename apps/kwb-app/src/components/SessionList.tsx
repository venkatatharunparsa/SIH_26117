import { MessageSquare, Plus } from "lucide-react";
import type { SessionMeta } from "../lib/constants";

type Props = {
  sessions: SessionMeta[];
  activeId: string | null;
  onSelect: (id: string) => void;
  onNew: () => void;
};

function statusDot(status: SessionMeta["status"]): string {
  if (status === "active") return "ok";
  if (status === "denied") return "bad";
  if (status === "exported") return "mute";
  return "";
}

export function SessionList({ sessions, activeId, onSelect, onNew }: Props) {
  return (
    <aside className="rail" aria-label="Sessions">
      <div className="rail-head">
        <h2>Sessions</h2>
        <button
          type="button"
          className="btn-icon"
          onClick={onNew}
          title="New session"
          aria-label="New session"
        >
          <Plus size={14} strokeWidth={2} aria-hidden />
          <span>New</span>
        </button>
      </div>
      <ul className="session-list">
        {sessions.length === 0 && (
          <li>
            <div className="session-sub" style={{ padding: 8 }}>
              No sessions yet
            </div>
          </li>
        )}
        {sessions.map((s) => (
          <li key={s.id}>
            <button
              type="button"
              className={`session-item${s.id === activeId ? " active" : ""}`}
              onClick={() => onSelect(s.id)}
            >
              <span className="session-row">
                <MessageSquare size={14} strokeWidth={1.75} className="session-ico" aria-hidden />
                <span className="session-title">{s.title}</span>
                <span className={`dot sm ${statusDot(s.status)}`} />
              </span>
              <span className="session-sub">
                {s.task_type} · {s.status}
                {s.route?.model_id ? ` · ${s.route.model_id}` : ""}
              </span>
            </button>
          </li>
        ))}
      </ul>
      <div className="rail-foot">desktop · not CERT</div>
    </aside>
  );
}
