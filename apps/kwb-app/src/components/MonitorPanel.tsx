import type { RouteInfo, TaskType } from "../lib/constants";

type Props = {
  healthOk: boolean | null;
  healthLine: string;
  grantId: string | null;
  taskId: string | null;
  route: RouteInfo;
  artefactVersion: number | string | null;
  draftFilename: string | null;
  h2Ok: boolean;
  monSession: string | null;
  leaveReady: boolean;
  lastDenies: string[];
  auditText: string;
  onDownloadDraft: () => void;
  onDownloadLeave: () => void;
};

export function MonitorPanel({
  healthOk,
  healthLine,
  grantId,
  taskId,
  route,
  artefactVersion,
  draftFilename,
  h2Ok,
  monSession,
  leaveReady,
  lastDenies,
  auditText,
  onDownloadDraft,
  onDownloadLeave,
}: Props) {
  return (
    <aside className="monitor" aria-label="Monitor B">
      <div>
        <h2>Monitor B</h2>
        <p className="mon-note">
          Own task · live status · evidence ≠ CERT
        </p>
        <div className="stat-grid">
          <span className="k">api</span>
          <span className="v">{healthLine}</span>
          <span className="k">link</span>
          <span className="v">
            {healthOk === null ? "…" : healthOk ? "up" : "down"}
          </span>
          <span className="k">grant</span>
          <span className="v" title={grantId || undefined}>
            {grantId || "—"}
          </span>
          <span className="k">task</span>
          <span className="v" title={taskId || undefined}>
            {taskId || "—"}
          </span>
          <span className="k">card</span>
          <span className="v">{route.card_id || "—"}</span>
          <span className="k">model</span>
          <span className="v">{route.model_id || "—"}</span>
          <span className="k">version</span>
          <span className="v">{artefactVersion ?? "—"}</span>
          <span className="k">draft</span>
          <span className="v" title={draftFilename || undefined}>
            {draftFilename || "—"}
          </span>
          <span className="k">H2</span>
          <span className="v">{h2Ok ? "fresh" : "pending/stale"}</span>
          <span className="k">MonA</span>
          <span className="v">{monSession || "—"}</span>
        </div>
      </div>

      <div>
        <h2>Leave pack</h2>
        <div className="download-row">
          <button
            type="button"
            className="dl-btn"
            disabled={!leaveReady || !draftFilename}
            onClick={onDownloadDraft}
          >
            Download DRAFT (.docx)
          </button>
          <button
            type="button"
            className="dl-btn"
            disabled={!leaveReady || !draftFilename}
            onClick={onDownloadLeave}
          >
            Download leave pack
          </button>
        </div>
        <p className="mon-note" style={{ marginTop: 6 }}>
          Soft copy · export leave · no Approver · not CERT
        </p>
      </div>

      <div>
        <h2>Last denies</h2>
        <div className="deny-list">
          {lastDenies.length === 0 ? (
            <div className="deny-chip empty">No denies yet</div>
          ) : (
            lastDenies.map((d) => (
              <div className="deny-chip" key={d}>
                {d}
              </div>
            ))
          )}
        </div>
      </div>

      <div>
        <h2>Audit trail</h2>
        <div className="audit-log">{auditText || "—"}</div>
      </div>
    </aside>
  );
}

export type { TaskType };
