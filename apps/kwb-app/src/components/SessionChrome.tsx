import {
  Bot,
  ChevronDown,
  Cpu,
  Loader2,
  Radio,
  Shield,
} from "lucide-react";
import type { RouteInfo, TaskType } from "../lib/constants";

/** Expected routed tags when Auto is selected (honest floor from models.yaml). */
export const AUTO_MODELS: Record<TaskType, string> = {
  inspection: "llama3.2:3b",
  coding: "qwen2.5-coder:7b",
};

type Props = {
  taskType: TaskType;
  onTaskType: (t: TaskType) => void;
  /** "auto" or a station tag */
  modelChoice: string;
  onModelChoice: (v: string) => void;
  stationTags: string[];
  route: RouteInfo;
  busy: boolean;
  healthOk: boolean | null;
  inferenceLabel: string;
  grantId: string | null;
  pendingAsk: boolean;
};

export function SessionChrome({
  taskType,
  onTaskType,
  modelChoice,
  onModelChoice,
  stationTags,
  route,
  busy,
  healthOk,
  inferenceLabel,
  grantId,
  pendingAsk,
}: Props) {
  const local = inferenceLabel.toUpperCase().includes("LOCAL");

  function onPickModel(v: string) {
    onModelChoice(v);
    if (v === "auto") return;
    const lower = v.toLowerCase();
    if (lower.includes("coder") || lower.includes("qwen")) {
      onTaskType("coding");
    } else if (lower.includes("llama") || lower.includes("inspect")) {
      onTaskType("inspection");
    }
  }

  return (
    <div className="session-chrome" role="toolbar" aria-label="Agent controls">
      <div className="chrome-left">
        <span className="chrome-pill mode" title="Agent mode · maps to Pack card">
          <Bot size={13} strokeWidth={2} aria-hidden />
          <select
            className="chrome-select"
            value={taskType}
            disabled={busy || pendingAsk}
            aria-label="Agent mode"
            onChange={(e) => {
              const t = e.target.value as TaskType;
              onTaskType(t);
              if (modelChoice === "auto") return;
              onModelChoice("auto");
            }}
          >
            <option value="inspection">Agent · inspection</option>
            <option value="coding">Agent · coding</option>
          </select>
          <ChevronDown size={12} className="chrome-chevron" aria-hidden />
        </span>

        <span
          className="chrome-pill model"
          title="Model · Auto uses task→card route; tags from station /v1/models"
        >
          <Cpu size={13} strokeWidth={2} aria-hidden />
          <select
            className="chrome-select"
            value={modelChoice}
            disabled={busy}
            aria-label="Model"
            onChange={(e) => onPickModel(e.target.value)}
          >
            <option value="auto">Auto · {AUTO_MODELS[taskType]}</option>
            {modelChoice !== "auto" && !stationTags.includes(modelChoice) ? (
              <option value={modelChoice}>{modelChoice} (stale)</option>
            ) : null}
            {stationTags.map((t) => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
          </select>
          <ChevronDown size={12} className="chrome-chevron" aria-hidden />
        </span>

        <span className="chrome-model-live" title={route.card_id || "no grant yet"}>
          {busy ? (
            <Loader2 size={12} className="spin" aria-hidden />
          ) : (
            <span
              className={`dot sm ${healthOk ? "ok" : healthOk === false ? "bad" : ""}`}
            />
          )}
          {route.model_id ? (
            <span className="chrome-routed">routed · {route.model_id}</span>
          ) : (
            <span className="chrome-routed mute">awaiting route</span>
          )}
          {route.card_id ? (
            <span className="chrome-card">{route.card_id}</span>
          ) : null}
        </span>
      </div>

      <div className="chrome-right">
        {pendingAsk ? (
          <span className="chrome-flag ask">needs you</span>
        ) : null}
        {busy ? <span className="chrome-flag busy">running</span> : null}
        <span
          className={`chrome-flag peer${local ? " local" : ""}`}
          title={inferenceLabel}
        >
          <Radio size={11} strokeWidth={2} aria-hidden />
          {local ? "loopback" : "LAN peer"}
        </span>
        {grantId ? (
          <span className="chrome-flag grant" title={grantId}>
            <Shield size={11} strokeWidth={2} aria-hidden />
            grant
          </span>
        ) : (
          <span className="chrome-flag mute">no grant</span>
        )}
      </div>
    </div>
  );
}
