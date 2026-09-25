import { useCallback, useEffect, useRef, useState } from "react";
import {
  API_BASE,
  api,
  artifactUrl,
  leavePackUrl,
  type ApiError,
} from "./lib/api";
import {
  DEFAULT_FINDINGS,
  DEFAULT_QUERY,
  FX_EXTRACT,
  uid,
  type RouteInfo,
  type SessionMeta,
  type StreamEntry,
  type TaskType,
} from "./lib/constants";
import {
  askAcceptSandbox,
  askFromOrch,
  isAffirmative,
  type PendingAsk,
} from "./lib/conductor";

type OrchTurnResponse = {
  ok?: boolean;
  grant_id?: string;
  task_id?: string;
  route?: RouteInfo;
  phase?: string;
  orchestrator?: boolean;
  assistant?: { text?: string; model?: string } | null;
  tools?: Array<Record<string, unknown>>;
  ask?: {
    kind?: string;
    prompt?: string;
    context_preview?: string;
    confirm_action?: string;
  };
  draft?: {
    filename?: string;
    path?: string;
    artefact_version?: string | number;
    format?: string;
    download?: string;
  };
  extract_text?: string;
  extract_bullets?: string[];
  match_notes?: string[];
  cites?: unknown[];
  query?: string;
  leave_ready?: boolean;
  grant_revoked?: boolean;
  note?: string;
  error?: string;
  attached_name?: string;
  ingest_engine?: string;
  ingest_degraded?: boolean;
  live_ocr?: boolean;
  ingest_message?: string;
};
import { SessionList } from "./components/SessionList";
import { SessionChrome } from "./components/SessionChrome";
import { Transcript } from "./components/Transcript";
import { Composer } from "./components/Composer";
import { MonitorPanel } from "./components/MonitorPanel";
import { FilesPanel } from "./components/FilesPanel";
import { PreviewPane } from "./components/PreviewPane";
import { AgentPlan } from "./components/AgentPlan";
import { Activity, PanelRight } from "lucide-react";
import {
  loadDemoFixtures,
  readDemoFixture,
  snapshotFromDirectoryFiles,
} from "./lib/workspace";
import type { WorkspaceFile, WorkspaceSnapshot } from "./lib/workspaceTypes";

type SessionState = {
  meta: SessionMeta;
  entries: StreamEntry[];
  extract: string;
  query: string;
  findings: string;
  h1Acked: boolean;
  h7Acked: boolean;
  h2Ok: boolean;
  draftFilename: string | null;
  artefactVersion: number | string | null;
  monSession: string | null;
  leaveReady: boolean;
  lastDenies: string[];
  attachedName: string | null;
  retrieved: boolean;
  sandboxRan: boolean;
  h9Acked: boolean;
  pendingAsk: PendingAsk | null;
  /** "auto" or station tag — Auto = task→card route */
  modelChoice: string;
  /** Last orchestrator phase (industrial agent spine) */
  orchPhase: string | null;
};

function freshSession(taskType: TaskType = "inspection"): SessionState {
  const id = uid("sess");
  return {
    meta: {
      id,
      title: `${taskType} · untitled`,
      task_type: taskType,
      grant_id: null,
      task_id: null,
      route: {},
      createdAt: Date.now(),
      status: "idle",
    },
    entries: [
      {
        kind: "system",
        id: uid("sys"),
        ts: Date.now(),
        text: "Workspace ready · FastAPI 127.0.0.1:8080 · chat & attach go through Orchestrator (/orch/turn) · Pack→Gateway only for models",
      },
    ],
    extract: FX_EXTRACT,
    query: DEFAULT_QUERY,
    findings: DEFAULT_FINDINGS,
    h1Acked: false,
    h7Acked: false,
    h2Ok: false,
    draftFilename: null,
    artefactVersion: null,
    monSession: null,
    leaveReady: false,
    lastDenies: [],
    attachedName: null,
    retrieved: false,
    sandboxRan: false,
    h9Acked: false,
    pendingAsk: null,
    modelChoice: "auto",
    orchPhase: "idle",
  };
}

/** Last 10 user+assistant messages — mirrors server CHAT_HISTORY_WINDOW (bootstrap only; orch is SoT). */
const CHAT_HISTORY_WINDOW = 10;

function chatHistory(
  entries: StreamEntry[],
  latestUser: string
): { role: string; content: string }[] {
  const msgs: { role: string; content: string }[] = [];
  for (const e of entries) {
    if (e.kind === "user") msgs.push({ role: "user", content: e.text });
    if (e.kind === "assistant")
      msgs.push({ role: "assistant", content: e.text });
  }
  msgs.push({ role: "user", content: latestUser });
  return msgs.slice(-CHAT_HISTORY_WINDOW);
}

function canContinueSession(s: SessionState | undefined): boolean {
  if (!s || s.pendingAsk) return false;
  if (s.meta.status === "exported" || s.leaveReady) return false;
  return true;
}

export function App() {
  const [sessions, setSessions] = useState<SessionState[]>(() => {
    return [freshSession("inspection")];
  });
  const [activeId, setActiveId] = useState<string>("");
  const [busy, setBusy] = useState(false);
  const [healthOk, setHealthOk] = useState<boolean | null>(null);
  const [healthLine, setHealthLine] = useState("checking…");
  const [inferenceLabel, setInferenceLabel] = useState("…");
  const [inferenceUrl, setInferenceUrl] = useState("");
  const [inferenceTags, setInferenceTags] = useState<string[]>([]);
  const [liveLog, setLiveLog] = useState<string[]>([]);
  const [auditText, setAuditText] = useState("");
  const [auditVerify, setAuditVerify] = useState("");
  /** Monitor B closed by default — open on click (RT UX) */
  const [monitorOpen, setMonitorOpen] = useState(false);
  const [draftInput, setDraftInput] = useState("");
  const [filesOpen, setFilesOpen] = useState(true);
  const [workspace, setWorkspace] = useState<WorkspaceSnapshot | null>(null);
  const [workspaceSource, setWorkspaceSource] = useState<
    "none" | "electron" | "browser" | "fixtures"
  >("none");
  const [selectedPath, setSelectedPath] = useState<string | null>(null);
  const [preview, setPreview] = useState<WorkspaceFile | null>(null);
  const browserFileCache = useRef<Map<string, WorkspaceFile>>(new Map());
  const folderInputRef = useRef<HTMLInputElement>(null);
  const bottomRef = useRef<HTMLDivElement>(null);
  const sessionsRef = useRef(sessions);
  sessionsRef.current = sessions;

  const resolvedId = activeId || sessions[0]?.meta.id || "";
  const active =
    sessions.find((s) => s.meta.id === resolvedId) ?? sessions[0];

  useEffect(() => {
    if (!activeId && sessions[0]) setActiveId(sessions[0].meta.id);
  }, [activeId, sessions]);

  const patchActive = useCallback(
    (fn: (s: SessionState) => SessionState) => {
      const all = sessionsRef.current;
      const id = activeId || all[0]?.meta.id;
      const next = all.map((s) => (s.meta.id === id ? fn(s) : s));
      sessionsRef.current = next;
      setSessions(next);
    },
    [activeId]
  );

  const pushEntry = useCallback(
    (entry: StreamEntry) => {
      patchActive((s) => ({ ...s, entries: [...s.entries, entry] }));
    },
    [patchActive]
  );

  const updateTool = useCallback(
    (toolId: string, patch: Partial<Extract<StreamEntry, { kind: "tool" }>>) => {
      patchActive((s) => ({
        ...s,
        entries: s.entries.map((e) =>
          e.kind === "tool" && e.id === toolId ? { ...e, ...patch } : e
        ),
      }));
    },
    [patchActive]
  );

  const runTool = useCallback(
    async <T,>(
      name: string,
      path: string,
      body?: unknown
    ): Promise<T | null> => {
      const toolId = uid("tool");
      pushEntry({
        kind: "tool",
        id: toolId,
        ts: Date.now(),
        name,
        path,
        status: "running",
        request: body,
      });
      try {
        const data = await api<T>(path, body);
        const keys =
          data && typeof data === "object"
            ? Object.keys(data as object).slice(0, 10)
            : [];
        updateTool(toolId, {
          status: "ok",
          response: data,
          summary: `ok · keys [${keys.join(", ")}]`,
        });
        return data;
      } catch (e) {
        const err = e as ApiError;
        updateTool(toolId, {
          status: "deny",
          response: err.detail,
          errorCode: err.errorCode,
          summary: `denied · ${err.errorCode}`,
        });
        patchActive((s) => ({
          ...s,
          lastDenies: [err.errorCode, ...s.lastDenies].slice(0, 8),
          meta: { ...s.meta, status: "denied" },
        }));
        return null;
      }
    },
    [patchActive, pushEntry, updateTool]
  );

  const refreshInference = useCallback(async () => {
    try {
      const s = await api<{
        label?: string;
        llm_base_url?: string;
        tags_on_target?: string[];
        is_local?: boolean;
      }>("/inference/status");
      setInferenceLabel(s.label || "?");
      setInferenceUrl(s.llm_base_url || "");
      setInferenceTags(s.tags_on_target || []);
      setLiveLog((prev) =>
        [
          `${new Date().toISOString().slice(11, 19)} inference · ${s.label} · ${(s.tags_on_target || []).slice(0, 3).join(",")}`,
          ...prev,
        ].slice(0, 40)
      );
    } catch {
      setLiveLog((prev) =>
        [`${new Date().toISOString().slice(11, 19)} inference · refresh failed`, ...prev].slice(
          0,
          40
        )
      );
    }
  }, []);

  useEffect(() => {
    (async () => {
      try {
        const h = await api<{
          bind?: string;
          version?: string;
          llm_base_url?: string;
          inference_label?: string;
          inference_target?: { label?: string; llm_base_url?: string; is_local?: boolean };
          ollama_policy?: { adopted_chat_tags?: string[]; adopted_vision_tags?: string[] };
        }>("/health");
        setHealthOk(true);
        const label =
          h.inference_label ||
          h.inference_target?.label ||
          (h.llm_base_url?.includes("127.0.0.1") || h.llm_base_url?.includes("localhost")
            ? "LOCAL (Laptop-B)"
            : h.llm_base_url || "?");
        const url = h.inference_target?.llm_base_url || h.llm_base_url || "";
        setInferenceLabel(label);
        setInferenceUrl(url);
        setHealthLine(`${h.bind ?? "127.0.0.1:8080"} · ${label}`);
        const adopted = [
          ...(h.ollama_policy?.adopted_chat_tags || []),
          ...(h.ollama_policy?.adopted_vision_tags || []),
        ];
        if (adopted.length) {
          setInferenceTags((prev) => (prev.length ? prev : adopted));
        }
        await refreshInference();
      } catch {
        setHealthOk(false);
        setHealthLine("API offline");
        setInferenceLabel("offline");
        setInferenceUrl("");
      }
    })();
    const t = setInterval(() => {
      void refreshInference();
    }, 8000);
    return () => clearInterval(t);
  }, [refreshInference]);

  /* Audit + live log poll only while Monitor is open */
  useEffect(() => {
    if (!monitorOpen) return;
    let lastFp = "";
    const poll = async () => {
      try {
        const res = await fetch(`${API_BASE}/audit/recent?limit=24`);
        if (!res.ok) return;
        const data = (await res.json()) as {
          events?: Record<string, unknown>[];
          items?: Record<string, unknown>[];
        };
        const events = data.events || data.items || [];
        if (!Array.isArray(events) || !events.length) return;
        const fp = JSON.stringify(events[0]);
        if (fp === lastFp) return;
        lastFp = fp;
        const lines = events.slice(0, 16).map((e) => {
          const t = String(e.ts || e.time || "").slice(11, 19);
          const name = String(e.kind || e.event || e.type || e.action || "?");
          const model = e.model ? ` model=${e.model}` : "";
          const base = e.base_url ? ` @${String(e.base_url).replace("http://", "")}` : "";
          const host = e.inference_host ? ` host=${e.inference_host}` : "";
          const label = e.inference_label ? ` [${e.inference_label}]` : "";
          const err = String(
            e.error ||
              e.reason ||
              (e.detail &&
              typeof e.detail === "object" &&
              (e.detail as { error?: string }).error) ||
              ""
          );
          return `${t} ${name}${label}${model}${base}${host}${err ? " · " + err : ""}`;
        });
        setAuditText(lines.join("\n"));
        const interesting = events.filter((e) => {
          const n = String(e.kind || e.event || "");
          return (
            n.includes("gateway") ||
            n.includes("orch_") ||
            n.includes("orch_phase") ||
            n.includes("word") ||
            n.includes("router") ||
            n.includes("mcp")
          );
        });
        if (interesting.length) {
          setLiveLog(
            interesting.slice(0, 24).map((e) => {
              const t = String(e.ts || "").slice(11, 19);
              const n = String(e.kind || e.event || "?");
              const model = e.model ? ` → ${e.model}` : "";
              const base = e.base_url ? ` @ ${e.base_url}` : "";
              const lab = e.inference_label ? ` · ${e.inference_label}` : "";
              const phaseLab = e.label ? ` · ${e.label}` : "";
              return `${t} ${n}${model}${base}${lab}${phaseLab}`;
            })
          );
        }
      } catch {
        /* optional */
      }
    };
    const id = setInterval(poll, 2500);
    poll();
    void refreshInference();
    return () => clearInterval(id);
  }, [monitorOpen, refreshInference]);

  useEffect(() => {
    const el = document.querySelector(".transcript");
    if (el) el.scrollTop = el.scrollHeight;
  }, [active?.entries.length]);

  function newSession() {
    const s = freshSession(active?.meta.task_type ?? "inspection");
    setSessions((all) => {
      const next = [s, ...all];
      sessionsRef.current = next;
      return next;
    });
    setActiveId(s.meta.id);
    setDraftInput("");
  }

  function streamNote(text: string) {
    pushEntry({
      kind: "system",
      id: uid("sys"),
      ts: Date.now(),
      text,
    });
  }

  function openAsk(spec: Omit<PendingAsk, "id">) {
    const ask: PendingAsk = { ...spec, id: uid("ask") };
    patchActive((s) => ({
      ...s,
      pendingAsk: ask,
      entries: [
        ...s.entries,
        {
          kind: "ask",
          id: ask.id,
          ts: Date.now(),
          prompt: ask.prompt,
          contextPreview: ask.contextPreview,
          askKind: ask.kind,
        },
      ],
    }));
  }

  function clearAsk() {
    patchActive((s) => ({ ...s, pendingAsk: null }));
  }

  function readActive(): SessionState | undefined {
    const id = activeId || sessionsRef.current[0]?.meta.id;
    return sessionsRef.current.find((s) => s.meta.id === id);
  }

  /** Apply /orch/turn response onto session + transcript. */
  function applyOrchResult(data: OrchTurnResponse) {
    if (data.grant_id) {
      patchActive((cur) => ({
        ...cur,
        meta: {
          ...cur.meta,
          grant_id: data.grant_id ?? cur.meta.grant_id,
          task_id: data.task_id ?? cur.meta.task_id,
          route: data.route || cur.meta.route,
          title: data.task_id
            ? `${cur.meta.task_type} · ${String(data.task_id).slice(0, 8)}`
            : cur.meta.title,
          status:
            data.leave_ready || data.phase === "done"
              ? "exported"
              : cur.meta.status === "idle"
                ? "active"
                : cur.meta.status,
        },
        extract: data.extract_text ?? cur.extract,
        query: data.query ?? cur.query,
        findings: data.extract_text ?? cur.findings,
        attachedName: data.attached_name ?? cur.attachedName,
        draftFilename: data.draft?.filename ?? cur.draftFilename,
        artefactVersion:
          data.draft?.artefact_version ?? cur.artefactVersion,
        leaveReady: data.leave_ready ?? cur.leaveReady,
        h1Acked:
          data.phase === "await_review_cites" ||
          data.phase === "await_self_check" ||
          data.phase === "await_export" ||
          data.phase === "done" ||
          cur.h1Acked,
        h7Acked:
          data.phase === "await_self_check" ||
          data.phase === "await_export" ||
          data.phase === "done" ||
          cur.h7Acked,
        h2Ok:
          data.phase === "await_export" ||
          data.phase === "done" ||
          cur.h2Ok,
        retrieved: Boolean(data.cites?.length) || cur.retrieved,
        pendingAsk: null,
        orchPhase: data.phase ?? cur.orchPhase,
      }));
    } else if (data.phase) {
      patchActive((cur) => ({ ...cur, orchPhase: data.phase ?? cur.orchPhase }));
    }

    for (const t of data.tools || []) {
      const name = String(t.name || "orch.tool");
      const toolId = uid("tool");
      pushEntry({
        kind: "tool",
        id: toolId,
        ts: Date.now(),
        name,
        path: "/orch/turn",
        status: t.ok === false ? "deny" : "ok",
        response: t,
        summary:
          name === "pptx_draft" && t.filename
            ? `ok · PPTX ${String(t.filename)}`
            : name === "attach_extract"
              ? `ok · ${Array.isArray(t.extract_bullets) ? t.extract_bullets.length : 0} bullets · ${(t.cites as unknown[])?.length ?? 0} cites · engine=${String(t.ingest_engine || data.ingest_engine || "plain")}${t.live_ocr || data.live_ocr ? " · live OCR" : t.ingest_degraded || data.ingest_degraded ? " · fixture stub" : ""}`
              : `ok · orch`,
      });
    }

    if (data.ingest_message) {
      streamNote(
        `Ingest · ${data.ingest_engine || "plain"}${data.live_ocr ? " (live OCR)" : data.ingest_degraded ? " (NOT live OCR)" : ""} · ${data.ingest_message}`
      );
    }

    if (data.match_notes?.length) {
      streamNote(
        `Company docs · ${data.match_notes.slice(0, 3).join(" · ")}`
      );
    }

    if (data.draft?.filename) {
      const href = artifactUrl(data.draft.filename, data.grant_id);
      streamNote(
        `DRAFT ready · ${data.draft.filename} (${data.draft.format || "pptx"}) · ${href}`
      );
      setMonitorOpen(true);
    }

    if (data.assistant?.text) {
      pushEntry({
        kind: "assistant",
        id: uid("asst"),
        ts: Date.now(),
        text: data.assistant.text,
        model: data.assistant.model,
      });
    } else if (data.note === "no_assistant_text") {
      streamNote("Orch→Gateway returned no assistant text · check local LLM");
    }

    if (data.grant_revoked) {
      streamNote("Grant revoked on export leave · shelf closed");
    }

    if (data.ask) {
      openAsk(askFromOrch(data.ask));
    }

    if (data.note === "Ask cancelled") {
      streamNote("Ask cancelled");
    }
  }

  async function orchTurn(body: {
    message?: string;
    messages?: { role: string; content: string }[];
    attach_text?: string;
    attach_filename?: string;
    attach_b64?: string;
    attach_content_type?: string;
    intent?: string;
  }): Promise<OrchTurnResponse | null> {
    const s = readActive();
    if (!s) return null;
    const toolId = uid("tool");
    const phases: string[] = ["Packing turn…"];
    pushEntry({
      kind: "tool",
      id: toolId,
      ts: Date.now(),
      name: "orch.turn",
      path: "/orch/turn",
      status: "running",
      phases: [...phases],
      request: {
        intent: body.intent || "auto",
        has_attach: Boolean(body.attach_text || body.attach_b64),
        message_len: (body.message || "").length,
      },
    });

    const grantQ = s.meta.grant_id
      ? `?grant_id=${encodeURIComponent(s.meta.grant_id)}`
      : "";
    let es: EventSource | null = null;
    try {
      es = new EventSource(`${API_BASE}/orch/events${grantQ}`);
      es.onmessage = (ev) => {
        try {
          const data = JSON.parse(ev.data) as Record<string, unknown>;
          const kind = String(data.kind || "");
          if (kind === "orch_events_open") return;
          let label = "";
          if (kind === "orch_phase") {
            label = String(data.label || data.phase || "phase");
          } else if (kind === "gateway_chat_start") {
            label = `Calling ${data.model || "?"} · ${data.inference_label || ""}`;
          } else if (kind === "gateway_chat") {
            label = `Model reply · ${data.model || "?"} · ${data.ok ? "ok" : "fail"}`;
          } else if (kind.startsWith("orch_") || kind.startsWith("gateway")) {
            label = kind;
          }
          if (!label) return;
          phases.push(label);
          updateTool(toolId, {
            phases: [...phases],
            summary: label,
          });
        } catch {
          /* ignore bad SSE */
        }
      };
    } catch {
      es = null;
    }

    try {
      const data = await api<OrchTurnResponse>("/orch/turn", {
        grant_id: s.meta.grant_id,
        task_type: s.meta.task_type,
        user_id: "kwb-desktop",
        ...body,
      });
      phases.push(`Done · phase ${data.phase || "?"}`);
      updateTool(toolId, {
        status: "ok",
        phases: [...phases],
        response: {
          phase: data.phase,
          grant_id: data.grant_id,
          has_ask: Boolean(data.ask),
          has_assistant: Boolean(data.assistant?.text),
        },
        summary: `ok · phase ${data.phase || "?"} · orch`,
      });
      applyOrchResult(data);
      return data;
    } catch (e) {
      const err = e as ApiError;
      phases.push(`Denied · ${err.errorCode}`);
      updateTool(toolId, {
        status: "deny",
        phases: [...phases],
        response: err.detail,
        errorCode: err.errorCode,
        summary: `denied · ${err.errorCode}`,
      });
      patchActive((cur) => ({
        ...cur,
        lastDenies: [err.errorCode, ...cur.lastDenies].slice(0, 8),
        meta: { ...cur.meta, status: "denied" },
      }));
      return null;
    } finally {
      try {
        es?.close();
      } catch {
        /* ignore */
      }
    }
  }

  /** Open a grant for legacy More-menu tools (deny demos) — chat uses orch. */
  async function ensureGrantQuiet(
    s: SessionState
  ): Promise<{ grantId: string; session: SessionState } | null> {
    if (s.meta.grant_id) {
      return { grantId: s.meta.grant_id, session: s };
    }
    const data = await orchTurn({ intent: "continue", message: "" });
    if (!data?.grant_id) return null;
    const updated = readActive() ?? s;
    return { grantId: data.grant_id, session: updated };
  }

  async function sendChat(text: string) {
    const s0 = readActive();
    if (!s0) return;

    pushEntry({
      kind: "user",
      id: uid("user"),
      ts: Date.now(),
      text,
    });

    const messages = chatHistory(s0.entries, text);
    await orchTurn({
      intent: "message",
      message: text,
      messages,
    });
  }

  async function runAction(action: string): Promise<boolean> {
    const s = readActive();
    if (!s) return false;
    const grantId = s.meta.grant_id;

    switch (action) {
      case "start": {
        pushEntry({
          kind: "user",
          id: uid("user"),
          ts: Date.now(),
          text: `Start ${s.meta.task_type} task`,
        });
        const data = await orchTurn({ intent: "continue", message: "" });
        return Boolean(data?.grant_id);
      }
      case "h1": {
        if (!grantId) return false;
        const data = await orchTurn({ intent: "confirm", message: "" });
        return Boolean(data?.ok !== false);
      }
      case "retrieve": {
        if (!grantId) return false;
        const cur = readActive() ?? s;
        pushEntry({
          kind: "user",
          id: uid("user"),
          ts: Date.now(),
          text: `Retrieve: ${cur.query}`,
        });
        const ok = await runTool("task.retrieve", "/task/retrieve", {
          grant_id: grantId,
          query: cur.query,
          k: 5,
        });
        if (ok === null) return false;
        patchActive((x) => ({ ...x, retrieved: true }));
        return true;
      }
      case "h7": {
        if (!grantId) return false;
        const ok = await runTool("task.h7", "/task/h7-ack", {
          grant_id: grantId,
          h7_acked: true,
        });
        if (ok === null) return false;
        patchActive((x) => ({ ...x, h7Acked: true }));
        return true;
      }
      case "draft": {
        if (!grantId) return false;
        pushEntry({
          kind: "user",
          id: uid("user"),
          ts: Date.now(),
          text: "Generate PPTX DRAFT (orch)",
        });
        const data = await orchTurn({ intent: "confirm", message: "" });
        return Boolean(data?.draft?.filename || data?.ask);
      }
      case "draft-edit": {
        if (!grantId || !s.draftFilename) return false;
        pushEntry({
          kind: "user",
          id: uid("user"),
          ts: Date.now(),
          text: "Edit DRAFT findings (stale H2)",
        });
        const cur = readActive() ?? s;
        const data = await runTool<{
          artefact_version?: number | string;
          h2_stale?: boolean;
        }>("task.draft-edit", "/task/draft-edit", {
          grant_id: grantId,
          draft_filename: cur.draftFilename,
          findings: cur.findings,
          title: "Integrity briefing (DRAFT)",
        });
        if (!data) return false;
        patchActive((x) => ({
          ...x,
          artefactVersion: data.artefact_version ?? x.artefactVersion,
          h2Ok: false,
          leaveReady: false,
        }));
        return true;
      }
      case "h2": {
        if (!grantId || !s.draftFilename) return false;
        const data = await orchTurn({ intent: "confirm", message: "" });
        return Boolean(data);
      }
      case "export": {
        if (!grantId || !s.draftFilename) return false;
        const data = await orchTurn({ intent: "confirm", message: "" });
        if (data?.leave_ready) setMonitorOpen(true);
        return Boolean(data?.leave_ready);
      }
      case "sandbox-calc": {
        if (!grantId) return false;
        const ok = await runTool("sandbox.calc", "/sandbox/calc", {
          grant_id: grantId,
          expression: "8.0 - 7.6",
        });
        if (!ok) return false;
        patchActive((x) => ({ ...x, sandboxRan: true }));
        return true;
      }
      case "sandbox-red": {
        if (!grantId) return false;
        await runTool("sandbox.python", "/sandbox/python", {
          grant_id: grantId,
          source: "raise SystemExit(1)",
        });
        return true;
      }
      case "h9": {
        if (!grantId) return false;
        const ok = await runTool("task.h9", "/task/h9-ack", {
          grant_id: grantId,
          accept: true,
        });
        if (!ok) return false;
        patchActive((x) => ({ ...x, h9Acked: true }));
        return true;
      }
      case "mon-a-start": {
        const data = await runTool<{ session_id: string }>(
          "monitor-a.start",
          "/monitor-a/start",
          {}
        );
        if (!data) return false;
        patchActive((x) => ({ ...x, monSession: data.session_id }));
        return true;
      }
      case "mon-a-stop": {
        const sid = s.monSession || "";
        await runTool(
          "monitor-a.stop",
          `/monitor-a/stop?session_id=${encodeURIComponent(sid)}`,
          {}
        );
        return true;
      }
      case "g9": {
        await runTool("task.export-check", "/task/export-check", {
          text: "api_key=sk-abcdefghijklmnopqrstuvwxyz CONFIDENTIAL",
        });
        return true;
      }
      case "g8": {
        const ensured = await ensureGrantQuiet(s);
        if (!ensured) return false;
        await runTool("gateway.chat", "/gateway/chat", {
          grant_id: ensured.grantId,
          model: "gpt-4o",
          messages: [{ role: "user", content: "ping" }],
        });
        return true;
      }
      case "revoke": {
        if (!grantId) return false;
        await runTool("task.revoke", "/task/revoke", { grant_id: grantId });
        return true;
      }
      case "_monitor": {
        setMonitorOpen(true);
        return true;
      }
      default:
        return false;
    }
  }

  async function handleAction(action: string) {
    if (busy) return;
    setBusy(true);
    try {
      await runAction(action);
    } finally {
      setBusy(false);
    }
  }

  async function continueTask() {
    const s = readActive();
    if (!s || s.pendingAsk) return;

    if (s.meta.task_type === "coding") {
      if (!s.meta.grant_id) {
        const ok = await runAction("start");
        if (!ok) return;
      }
      if (!s.sandboxRan) {
        const ran = await runAction("sandbox-calc");
        if (ran) openAsk(askAcceptSandbox());
        return;
      }
      if (!s.h9Acked) {
        openAsk(askAcceptSandbox());
        return;
      }
      streamNote("Coding path uses sandbox HITL · inspection attach uses orch PPTX path");
      return;
    }

    // Inspection / attach ladder — orchestrator owns next step
    await orchTurn({ intent: "continue", message: "" });
  }

  async function resolveAsk(ask: PendingAsk, text: string) {
    const lower = text.trim().toLowerCase();
    if (
      ask.acceptTextAs === "none" &&
      (lower === "cancel" ||
        lower === "reject" ||
        lower === "no" ||
        lower === "stop")
    ) {
      await orchTurn({ intent: "cancel", message: "cancel" });
      return;
    }

    // Legacy sandbox ask still uses local h9 action
    if (ask.confirmAction === "h9") {
      clearAsk();
      pushEntry({
        kind: "user",
        id: uid("user"),
        ts: Date.now(),
        text: text.trim() || "Confirmed",
      });
      const ok = await runAction("h9");
      if (ok) streamNote("Sandbox observation accepted");
      return;
    }

    clearAsk();
    pushEntry({
      kind: "user",
      id: uid("user"),
      ts: Date.now(),
      text: text.trim() || "Confirmed",
    });

    await orchTurn({
      intent: "confirm",
      message: isAffirmative(text) ? "" : text.trim(),
    });
  }

  async function handleSubmit(text: string) {
    if (busy) return;
    const s = readActive();
    if (!s) return;

    const trimmed = text.trim();
    setDraftInput("");

    setBusy(true);
    try {
      if (s.pendingAsk) {
        await resolveAsk(s.pendingAsk, trimmed);
        return;
      }
      if (trimmed) {
        await sendChat(trimmed);
        return;
      }
      if (canContinueSession(s)) {
        await continueTask();
      }
    } finally {
      setBusy(false);
    }
  }

  async function onAttachText(text: string, name: string) {
    patchActive((s) => ({
      ...s,
      extract: text,
      attachedName: name,
    }));
    streamNote(`Context attached · ${name} → orchestrator extract`);
    setBusy(true);
    try {
      await orchTurn({
        intent: "attach",
        attach_text: text,
        attach_filename: name,
      });
    } finally {
      setBusy(false);
    }
  }

  async function onAttachBinary(
    b64: string,
    name: string,
    contentType: string
  ) {
    patchActive((s) => ({
      ...s,
      attachedName: name,
    }));
    streamNote(`Binary attached · ${name} → OCR/PDF ingest → Confirm extract`);
    setBusy(true);
    try {
      await orchTurn({
        intent: "attach",
        attach_b64: b64,
        attach_filename: name,
        attach_content_type: contentType || undefined,
      });
    } finally {
      setBusy(false);
    }
  }

  const isElectron = Boolean(window.kwbDesktop?.isElectron);
  const denyHint = active?.lastDenies[0];
  const canContinue = canContinueSession(active);

  useEffect(() => {
    const desk = window.kwbDesktop;
    if (!desk?.onWorkspaceChanged) return;
    const off = desk.onWorkspaceChanged((payload) => {
      setWorkspace(payload.root ? payload : null);
      setWorkspaceSource(payload.root ? "electron" : "none");
      setSelectedPath(null);
      setPreview(null);
      browserFileCache.current = new Map();
      if (payload.root) setFilesOpen(true);
    });
    const offFiles = desk.onFilesOpened?.((payload) => {
      const first = payload.files?.[0];
      if (!first) return;
      setPreview(first);
      setSelectedPath(first.path || first.name);
      setFilesOpen(true);
    });
    void desk.getWorkspace?.().then((snap) => {
      if (snap?.root) {
        setWorkspace(snap);
        setWorkspaceSource("electron");
        setFilesOpen(true);
      }
    });
    return () => {
      off?.();
      offFiles?.();
    };
  }, []);

  async function openFolder() {
    const desk = window.kwbDesktop;
    if (desk?.openFolder) {
      const snap = await desk.openFolder();
      if (snap?.ok && snap.root) {
        setWorkspace(snap);
        setWorkspaceSource("electron");
        setFilesOpen(true);
        browserFileCache.current = new Map();
      }
      return;
    }
    folderInputRef.current?.click();
  }

  async function onBrowserFolder(files: FileList | null) {
    if (!files?.length) return;
    const { snapshot, cache } = await snapshotFromDirectoryFiles(files);
    browserFileCache.current = cache;
    setWorkspace(snapshot);
    setWorkspaceSource("browser");
    setSelectedPath(null);
    setPreview(null);
    setFilesOpen(true);
  }

  async function openDemoFixtures() {
    try {
      const { snapshot, cache } = await loadDemoFixtures();
      browserFileCache.current = cache;
      setWorkspace(snapshot);
      setWorkspaceSource("fixtures");
      setSelectedPath(null);
      setPreview(null);
      setFilesOpen(true);
      streamNote("Opened demo fixtures · data/fixtures");
    } catch {
      streamNote("Demo fixtures unavailable · is API :8080 up?");
    }
  }

  async function selectWorkspaceFile(rel: string) {
    setSelectedPath(rel);
    const desk = window.kwbDesktop;
    if (workspaceSource === "electron" && desk?.readWorkspaceFile) {
      const file = await desk.readWorkspaceFile(rel);
      if (file && file.error == null) {
        setPreview(file);
        return;
      }
      streamNote(`Could not read · ${rel}`);
      return;
    }
    const cached = browserFileCache.current.get(rel);
    if (cached) {
      setPreview(cached);
      return;
    }
    try {
      const base = rel.split(/[/\\]/).pop() || rel;
      const file = await readDemoFixture(base);
      if (file) {
        browserFileCache.current.set(rel, file);
        setPreview(file);
      }
    } catch {
      streamNote(`Could not read · ${rel}`);
    }
  }

  async function attachPreviewFile(file: WorkspaceFile | null = preview) {
    if (!file || busy) return;
    if (file.kind === "text" && file.text != null) {
      await onAttachText(file.text, file.name);
      return;
    }
    if ((file.kind === "image" || file.kind === "pdf") && file.b64) {
      await onAttachBinary(
        file.b64,
        file.name,
        file.contentType ||
          (file.kind === "pdf" ? "application/pdf" : "image/png")
      );
      return;
    }
    streamNote(`Cannot attach · ${file.name} (${file.kind})`);
  }

  function closeFolder() {
    void window.kwbDesktop?.closeWorkspace?.();
    setWorkspace(null);
    setWorkspaceSource("none");
    setSelectedPath(null);
    setPreview(null);
    browserFileCache.current = new Map();
  }

  const shellClass = [
    "shell",
    monitorOpen ? "monitor-open" : "",
    filesOpen ? "files-open" : "",
    preview ? "preview-open" : "",
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <div className="app">
      <input
        ref={folderInputRef}
        type="file"
        multiple
        hidden
        {...({ webkitdirectory: "", directory: "" } as Record<string, string>)}
        onChange={(e) => {
          void onBrowserFolder(e.target.files);
          e.target.value = "";
        }}
      />
      <header className="titlebar">
        <div className="titlebar-brand">
          <span className="brand-mark" aria-hidden>
            KWB
          </span>
          <div className="brand-text">
            <strong>Knowledge Work Bench</strong>
            <span>
              {isElectron ? "desktop" : "renderer"} · agent workbench · private
              LAN
            </span>
          </div>
        </div>
        <div className="titlebar-meta">
          <span className={`dot ${healthOk ? "ok" : healthOk === false ? "bad" : ""}`} />
          <span>{healthLine}</span>
          {busy ? (
            <span className="badge badge-busy">
              <Activity size={10} className="spin" aria-hidden /> agent
            </span>
          ) : null}
          {denyHint ? (
            <span className="badge badge-deny" title={denyHint}>
              deny
            </span>
          ) : null}
          <span className="badge badge-not-cert">not CERT</span>
          <button
            type="button"
            className={`chip titlebar-mon${filesOpen ? " primary" : ""}`}
            aria-pressed={filesOpen}
            onClick={() => setFilesOpen((o) => !o)}
          >
            Files
          </button>
          <button
            type="button"
            className={`chip titlebar-mon${monitorOpen ? " primary" : ""}`}
            aria-pressed={monitorOpen}
            onClick={() => setMonitorOpen((o) => !o)}
          >
            <PanelRight size={12} aria-hidden />
            Monitor
          </button>
        </div>
      </header>

      <div className={shellClass}>
        <SessionList
          sessions={sessions.map((s) => s.meta)}
          activeId={resolvedId}
          onSelect={setActiveId}
          onNew={newSession}
        />

        {filesOpen ? (
          <FilesPanel
            snapshot={workspace}
            selectedPath={selectedPath}
            onSelect={(p) => void selectWorkspaceFile(p)}
            onOpenFolder={() => void openFolder()}
            onOpenDemoFixtures={() => void openDemoFixtures()}
            onCloseFolder={closeFolder}
            onAttachSelected={() => void attachPreviewFile()}
            canAttach={Boolean(
              preview &&
                (preview.kind === "text" ||
                  preview.kind === "image" ||
                  preview.kind === "pdf")
            )}
            isElectron={isElectron}
          />
        ) : null}

        <main className="workspace">
          <SessionChrome
            taskType={active?.meta.task_type ?? "inspection"}
            onTaskType={(t) =>
              patchActive((s) => ({
                ...s,
                meta: {
                  ...s.meta,
                  task_type: t,
                  title: s.meta.grant_id
                    ? s.meta.title
                    : `${t} · untitled`,
                },
              }))
            }
            modelChoice={active?.modelChoice ?? "auto"}
            onModelChoice={(v) =>
              patchActive((s) => ({ ...s, modelChoice: v }))
            }
            stationTags={inferenceTags}
            route={active?.meta.route ?? {}}
            busy={busy}
            healthOk={healthOk}
            inferenceLabel={inferenceLabel}
            grantId={active?.meta.grant_id ?? null}
            pendingAsk={Boolean(active?.pendingAsk)}
          />
          <AgentPlan
            taskType={active?.meta.task_type ?? "inspection"}
            message={draftInput}
            filename={active?.attachedName ?? null}
            phase={active?.orchPhase ?? "idle"}
            hasAttach={Boolean(active?.attachedName)}
            hasDraft={Boolean(active?.draftFilename)}
            leaveReady={Boolean(active?.leaveReady)}
            busy={busy}
            pendingAsk={active?.pendingAsk?.kind ?? null}
          />
          <Transcript entries={active?.entries ?? []} />
          <div ref={bottomRef} />
          <Composer
            taskType={active?.meta.task_type ?? "inspection"}
            busy={busy}
            pendingAsk={active?.pendingAsk ?? null}
            canContinue={canContinue}
            attachedName={active?.attachedName ?? null}
            onAttachedName={(name) =>
              patchActive((s) => ({ ...s, attachedName: name }))
            }
            onAttachText={onAttachText}
            onAttachBinary={onAttachBinary}
            onStreamNote={streamNote}
            onAction={handleAction}
            onSubmit={handleSubmit}
            draftInput={draftInput}
            onDraftInput={setDraftInput}
          />
        </main>

        {preview ? (
          <PreviewPane
            file={preview}
            onClose={() => {
              setPreview(null);
              setSelectedPath(null);
            }}
            onAttach={() => void attachPreviewFile()}
            canAttach={
              preview.kind === "text" ||
              preview.kind === "image" ||
              preview.kind === "pdf"
            }
          />
        ) : null}

        <MonitorPanel
          open={monitorOpen}
          onClose={() => setMonitorOpen(false)}
          healthOk={healthOk}
          healthLine={healthLine}
          inferenceLabel={inferenceLabel}
          inferenceUrl={inferenceUrl}
          inferenceTags={inferenceTags}
          grantId={active?.meta.grant_id ?? null}
          taskId={active?.meta.task_id ?? null}
          route={active?.meta.route ?? {}}
          artefactVersion={active?.artefactVersion ?? null}
          draftFilename={active?.draftFilename ?? null}
          h2Ok={active?.h2Ok ?? false}
          monSession={active?.monSession ?? null}
          leaveReady={active?.leaveReady ?? false}
          lastDenies={active?.lastDenies ?? []}
          auditText={auditText}
          liveLog={liveLog}
          auditVerify={auditVerify}
          onRefreshInference={() => void refreshInference()}
          onVerifyAudit={async () => {
            try {
              const v = await api<{
                ok?: boolean;
                tip?: string;
                entries?: number;
                not_cert?: boolean;
              }>("/audit/verify");
              const tip = v.tip ? String(v.tip).slice(0, 12) : "?";
              setAuditVerify(
                `${v.ok ? "chain OK" : "chain FAIL"} · ${v.entries ?? "?"} events · tip ${tip}… · not CERT`
              );
            } catch {
              setAuditVerify("verify failed · API error");
            }
          }}
          onDownloadDraft={() => {
            const fn = active?.draftFilename;
            const g = active?.meta.grant_id;
            if (!fn) return;
            const a = document.createElement("a");
            a.href = artifactUrl(fn, g);
            a.download = fn;
            a.rel = "noopener";
            document.body.appendChild(a);
            a.click();
            a.remove();
          }}
          onDownloadLeave={() => {
            const fn = active?.draftFilename;
            const g = active?.meta.grant_id;
            if (!fn || !g) return;
            window.open(leavePackUrl(g, fn), "_blank", "noopener");
          }}
        />
      </div>
    </div>
  );
}
