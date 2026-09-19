import type { TaskType } from "../lib/constants";

type Props = {
  taskType: TaskType;
  onTaskType: (t: TaskType) => void;
  extract: string;
  onExtract: (v: string) => void;
  query: string;
  onQuery: (v: string) => void;
  findings: string;
  onFindings: (v: string) => void;
  busy: boolean;
  hasGrant: boolean;
  onAction: (action: string) => void;
};

const ACTIONS: { id: string; label: string; needsGrant?: boolean; danger?: boolean; primary?: boolean }[] = [
  { id: "start", label: "task/start", primary: true },
  { id: "load-fx", label: "load FX-EXT-01", needsGrant: true },
  { id: "h1", label: "h1-confirm", needsGrant: true },
  { id: "retrieve", label: "retrieve", needsGrant: true },
  { id: "h7", label: "h7-ack", needsGrant: true },
  { id: "draft", label: "inspect-draft", needsGrant: true, primary: true },
  { id: "h2", label: "h2-ack", needsGrant: true },
  { id: "export", label: "export leave", needsGrant: true, primary: true },
  { id: "sandbox-calc", label: "sandbox/calc", needsGrant: true },
  { id: "sandbox-red", label: "sandbox/red", needsGrant: true },
  { id: "h9", label: "h9-ack", needsGrant: true },
  { id: "mon-a-start", label: "monitor-a/start" },
  { id: "mon-a-stop", label: "monitor-a/stop" },
  { id: "g9", label: "G9 secret inject", danger: true },
  { id: "g8", label: "G8 bad model", needsGrant: true, danger: true },
  { id: "revoke", label: "revoke grant", needsGrant: true, danger: true },
];

export function Composer({
  taskType,
  onTaskType,
  extract,
  onExtract,
  query,
  onQuery,
  findings,
  onFindings,
  busy,
  hasGrant,
  onAction,
}: Props) {
  return (
    <div className="composer">
      <div className="action-row">
        {ACTIONS.map((a) => (
          <button
            key={a.id}
            type="button"
            className={`chip${a.primary ? " primary" : ""}${a.danger ? " danger" : ""}`}
            disabled={busy || (a.needsGrant && !hasGrant) || (a.id === "start" && false)}
            onClick={() => onAction(a.id)}
          >
            {a.label}
          </button>
        ))}
      </div>

      <div className="composer-fields">
        <div className="field">
          <label htmlFor="taskType">Task type</label>
          <select
            id="taskType"
            value={taskType}
            onChange={(e) => onTaskType(e.target.value as TaskType)}
            disabled={busy}
          >
            <option value="inspection">inspection</option>
            <option value="coding">coding</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="query">Retrieve query</label>
          <input
            id="query"
            value={query}
            onChange={(e) => onQuery(e.target.value)}
            disabled={busy}
          />
        </div>
        <div className="field">
          <label htmlFor="extract">Extract (H1)</label>
          <textarea
            id="extract"
            value={extract}
            onChange={(e) => onExtract(e.target.value)}
            disabled={busy}
          />
        </div>
        <div className="field">
          <label htmlFor="findings">Findings (DRAFT body)</label>
          <textarea
            id="findings"
            value={findings}
            onChange={(e) => onFindings(e.target.value)}
            disabled={busy}
          />
        </div>
      </div>
      <div className="composer-hint">
        Composer · tool actions append to stream · same-user HITL · DRAFT ≠ CERT
      </div>
    </div>
  );
}
