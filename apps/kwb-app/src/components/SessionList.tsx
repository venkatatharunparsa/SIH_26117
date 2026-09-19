import type { SessionMeta } from "../lib/constants";

type Props = {
  sessions: SessionMeta[];
  activeId: string | null;
  onSelect: (id: string) => void;
  onNew: () => void;
};

export function SessionList({ sessions, activeId, onSelect, onNew }: Props) {
  return (
    <aside className="rail" aria-label="Sessions">
      <div className="rail-head">
        <h2>Sessions</h2>
        <button type="button" className="btn-icon" onClick={onNew}>
          + new
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
              <span className="session-title">{s.title}</span>
              <span className="session-sub">
                {s.task_type} · {s.status}
                {s.task_id ? ` · ${s.task_id.slice(0, 8)}` : ""}
              </span>
            </button>
          </li>
        ))}
      </ul>
      <div className="rail-foot">KWB · desktop · not CERT</div>
    </aside>
  );
}
