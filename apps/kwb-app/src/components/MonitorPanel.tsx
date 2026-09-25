import { useMemo, useState } from "react";
import { Activity, Copy, RefreshCw, X } from "lucide-react";
import type { RouteInfo } from "../lib/constants";

type Props = {
  open: boolean;
  onClose: () => void;
  healthOk: boolean | null;
  healthLine: string;
  inferenceLabel: string;
  inferenceUrl: string;
  inferenceTags: string[];
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
  liveLog: string[];
  auditVerify: string;
  onVerifyAudit: () => void;
  onDownloadDraft: () => void;
  onDownloadLeave: () => void;
  onRefreshInference: () => void;
};

type Tab = "status" | "log" | "share";

export function MonitorPanel({
  open,
  onClose,
  healthOk,
  healthLine,
  inferenceLabel,
  inferenceUrl,
  inferenceTags,
  grantId,
  taskId,
  route,
  artefactVersion: _artefactVersion,
  draftFilename,
  h2Ok,
  monSession,
  leaveReady,
  lastDenies,
  auditText,
  liveLog,
  auditVerify,
  onVerifyAudit,
  onDownloadDraft,
  onDownloadLeave,
  onRefreshInference,
}: Props) {
  const [tab, setTab] = useState<Tab>("log");
  const [copied, setCopied] = useState(false);

  const local = inferenceLabel.toUpperCase().includes("LOCAL");

  const shareText = useMemo(() => {
    const lines = [
      "KWB Monitor share (not CERT)",
      `time_utc: ${new Date().toISOString()}`,
      `llm_where: ${inferenceLabel}`,
      `llm_url: ${inferenceUrl}`,
      `posture: ${local ? "loopback" : "private_LAN_peer"} · not_air_gap`,
      `sandbox: host-process`,
      `tags: ${(inferenceTags || []).join(", ") || "—"}`,
      `api: ${healthLine}`,
      `monitor_a: evidence_pack_not_CERT`,
      `grant: ${grantId || "—"}`,
      `task: ${taskId || "—"}`,
      `card: ${route.card_id || "—"}`,
      `model: ${route.model_id || "—"}`,
      `draft: ${draftFilename || "—"}`,
      `h2: ${h2Ok ? "fresh" : "pending/stale"}`,
      "--- live log (recent) ---",
      ...(liveLog.length ? liveLog.slice(0, 20) : ["(empty)"]),
      "--- denies ---",
      ...(lastDenies.length ? lastDenies : ["(none)"]),
    ];
    return lines.join("\n");
  }, [
    inferenceLabel,
    inferenceUrl,
    inferenceTags,
    healthLine,
    grantId,
    taskId,
    route.card_id,
    route.model_id,
    draftFilename,
    h2Ok,
    liveLog,
    lastDenies,
  ]);

  if (!open) return null;

  const copyShare = async () => {
    try {
      await navigator.clipboard.writeText(shareText);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  };

  return (
    <aside className="monitor" aria-label="Monitor B">
      <div className="monitor-head">
        <div>
          <h2>Monitor</h2>
          <p className="mon-note">LLM target · live log · share · ≠ CERT</p>
        </div>
        <button
          type="button"
          className="btn-icon"
          aria-label="Close Monitor"
          onClick={onClose}
        >
          <X size={14} strokeWidth={2} />
        </button>
      </div>

      <div className="mon-tabs" role="tablist">
        {(
          [
            ["log", "Live log"],
            ["status", "Status"],
            ["share", "Share"],
          ] as const
        ).map(([id, label]) => (
          <button
            key={id}
            type="button"
            role="tab"
            aria-selected={tab === id}
            className={`mon-tab${tab === id ? " on" : ""}`}
            onClick={() => setTab(id)}
          >
            {id === "log" ? <Activity size={12} aria-hidden /> : null}
            {label}
          </button>
        ))}
      </div>

      {tab === "log" ? (
        <div className="mon-tab-body">
          <div className="llm-banner" data-local={local ? "1" : "0"}>
            <strong>{inferenceLabel || "…"}</strong>
            <span>{inferenceUrl || "—"}</span>
          </div>
          <div className="download-row">
            <button type="button" className="dl-btn" onClick={onRefreshInference}>
              <RefreshCw size={12} aria-hidden /> Refresh target
            </button>
            <button type="button" className="dl-btn" onClick={onVerifyAudit}>
              Verify audit
            </button>
          </div>
          {auditVerify ? <p className="mon-note">{auditVerify}</p> : null}
          <h2>What just happened</h2>
          <div className="audit-log live-log">
            {liveLog.length === 0
              ? "Waiting for orch / gateway events…"
              : liveLog.join("\n")}
          </div>
          <h2>Raw audit (tail)</h2>
          <div className="audit-log">{auditText || "—"}</div>
        </div>
      ) : null}

      {tab === "status" ? (
        <div className="mon-tab-body">
          <div className="llm-banner" data-local={local ? "1" : "0"}>
            <strong>{local ? "LOCAL Laptop-B" : "LAPTOP-A"}</strong>
            <span>{inferenceLabel}</span>
          </div>
          <div className="stat-grid">
            <span className="k">api</span>
            <span className="v">{healthLine}</span>
            <span className="k">link</span>
            <span className="v">
              {healthOk === null ? "…" : healthOk ? "up" : "down"}
            </span>
            <span className="k">posture</span>
            <span className="v">
              {local
                ? "loopback · not air-gap"
                : "private LAN peer · not air-gap"}
            </span>
            <span className="k">sandbox</span>
            <span className="v">host-process · H9 gated</span>
            <span className="k">url</span>
            <span className="v" title={inferenceUrl}>
              {inferenceUrl || "—"}
            </span>
            <span className="k">tags</span>
            <span className="v" title={inferenceTags.join(", ")}>
              {inferenceTags.length
                ? inferenceTags.slice(0, 4).join(", ") +
                  (inferenceTags.length > 4 ? "…" : "")
                : "—"}
            </span>
            <span className="k">grant</span>
            <span className="v" title={grantId || undefined}>
              {grantId || "—"}
            </span>
            <span className="k">task</span>
            <span className="v">{taskId || "—"}</span>
            <span className="k">card</span>
            <span className="v">{route.card_id || "—"}</span>
            <span className="k">model</span>
            <span className="v">{route.model_id || "—"}</span>
            <span className="k">draft</span>
            <span className="v">{draftFilename || "—"}</span>
            <span className="k">H2</span>
            <span className="v">{h2Ok ? "fresh" : "pending/stale"}</span>
            <span className="k">MonA</span>
            <span className="v">{monSession || "— · ≠ CERT"}</span>
          </div>
          <p className="mon-note">
            Gateway allowlists local/RFC1918 only. Monitor A = evidence pack,
            not CERT / WAN=0 theatre. Air-gap = venue NIC evidence later.
          </p>
          <h2>Leave pack</h2>
          <div className="download-row">
            <button
              type="button"
              className="dl-btn"
              disabled={!draftFilename}
              onClick={onDownloadDraft}
            >
              Download DRAFT
            </button>
            <button
              type="button"
              className="dl-btn"
              disabled={
                !leaveReady ||
                !draftFilename ||
                !draftFilename.toLowerCase().endsWith(".docx")
              }
              onClick={onDownloadLeave}
            >
              Download leave pack
            </button>
          </div>
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
      ) : null}

      {tab === "share" ? (
        <div className="mon-tab-body">
          <p className="mon-note">
            Copy this block for teammates / jury notes. Soft evidence · not CERT.
          </p>
          <div className="download-row">
            <button type="button" className="dl-btn" onClick={copyShare}>
              <Copy size={12} aria-hidden /> {copied ? "Copied" : "Copy share text"}
            </button>
          </div>
          <pre className="share-block">{shareText}</pre>
        </div>
      ) : null}
    </aside>
  );
}
