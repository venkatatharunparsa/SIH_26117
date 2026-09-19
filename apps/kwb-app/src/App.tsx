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
import { SessionList } from "./components/SessionList";
import { Transcript } from "./components/Transcript";
import { Composer } from "./components/Composer";
import { MonitorPanel } from "./components/MonitorPanel";

type SessionState = {
  meta: SessionMeta;
  entries: StreamEntry[];
  extract: string;
  query: string;
  findings: string;
  h7Acked: boolean;
  h2Ok: boolean;
  draftFilename: string | null;
  artefactVersion: number | string | null;
  monSession: string | null;
  leaveReady: boolean;
  lastDenies: string[];
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
        text: "Workspace ready · FastAPI 127.0.0.1:8080 · run task/start to open a grant",
      },
    ],
    extract: FX_EXTRACT,
    query: DEFAULT_QUERY,
    findings: DEFAULT_FINDINGS,
    h7Acked: false,
    h2Ok: false,
    draftFilename: null,
    artefactVersion: null,
    monSession: null,
    leaveReady: false,
    lastDenies: [],
  };
}

export function App() {
  const [sessions, setSessions] = useState<SessionState[]>(() => {
    return [freshSession("inspection")];
  });
  const [activeId, setActiveId] = useState<string>("");
  const [busy, setBusy] = useState(false);
  const [healthOk, setHealthOk] = useState<boolean | null>(null);
  const [healthLine, setHealthLine] = useState("checking…");
  const [auditText, setAuditText] = useState("");
  const bottomRef = useRef<HTMLDivElement>(null);

  const resolvedId = activeId || sessions[0]?.meta.id || "";
  const active =
    sessions.find((s) => s.meta.id === resolvedId) ?? sessions[0];

  useEffect(() => {
    if (!activeId && sessions[0]) setActiveId(sessions[0].meta.id);
  }, [activeId, sessions]);

  const patchActive = useCallback(
    (fn: (s: SessionState) => SessionState) => {
      setSessions((all) => {
        const id = activeId || all[0]?.meta.id;
        return all.map((s) => (s.meta.id === id ? fn(s) : s));
      });
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

  useEffect(() => {
    (async () => {
      try {
        const h = await api<{ bind?: string; version?: string }>("/health");
        setHealthOk(true);
        setHealthLine(
          `${h.bind ?? "127.0.0.1:8080"} · v${h.version ?? "?"}`
        );
      } catch {
        setHealthOk(false);
        setHealthLine("API offline");
      }
    })();
  }, []);

  useEffect(() => {
    let lastFp = "";
    const poll = async () => {
      try {
        const res = await fetch(`${API_BASE}/audit/recent?limit=12`);
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
        const lines = events.slice(0, 12).map((e) => {
          const t = String(e.ts || e.time || "");
          const name = String(e.event || e.type || e.action || "?");
          const err = String(
            e.error ||
              e.reason ||
              (e.detail &&
              typeof e.detail === "object" &&
              (e.detail as { error?: string }).error) ||
              ""
          );
          return `${t} ${name}${err ? " · " + err : ""}`;
        });
        setAuditText(lines.join("\n"));
      } catch {
        /* optional */
      }
    };
    const id = setInterval(poll, 4000);
    poll();
    return () => clearInterval(id);
  }, []);

  useEffect(() => {
    const el = document.querySelector(".transcript");
    if (el) el.scrollTop = el.scrollHeight;
  }, [active?.entries.length]);

  function newSession() {
    const s = freshSession(active?.meta.task_type ?? "inspection");
    setSessions((all) => [s, ...all]);
    setActiveId(s.meta.id);
  }

  async function handleAction(action: string) {
    if (!active) return;
    setBusy(true);
    try {
      const grantId = active.meta.grant_id;
      switch (action) {
        case "start": {
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: `Start ${active.meta.task_type} task`,
          });
          const data = await runTool<{
            grant_id: string;
            task_id: string;
            route: RouteInfo;
          }>("task.start", "/task/start", {
            task_type: active.meta.task_type,
            user_id: "kwb-desktop",
          });
          if (data) {
            patchActive((s) => ({
              ...s,
              meta: {
                ...s.meta,
                grant_id: data.grant_id,
                task_id: data.task_id,
                route: data.route || {},
                title: `${s.meta.task_type} · ${data.task_id.slice(0, 8)}`,
                status: "active",
              },
              leaveReady: false,
              h2Ok: false,
              draftFilename: null,
              artefactVersion: null,
            }));
          }
          break;
        }
        case "load-fx": {
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: "Load fixture FX-EXT-01",
          });
          const toolId = uid("tool");
          pushEntry({
            kind: "tool",
            id: toolId,
            ts: Date.now(),
            name: "fixture.load",
            path: "local://FX-EXT-01",
            status: "ok",
            summary: "Confidential synthetic extract loaded (client fixture).",
            response: { fixture: "FX-EXT-01", classification: "Confidential synthetic" },
          });
          patchActive((s) => ({ ...s, extract: FX_EXTRACT }));
          break;
        }
        case "h1": {
          if (!grantId) return;
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: "Confirm H1 (same-user extract ack)",
          });
          await runTool("task.h1", "/task/h1-confirm", {
            grant_id: grantId,
            extract_text: active.extract,
            h1_acked: true,
          });
          break;
        }
        case "retrieve": {
          if (!grantId) return;
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: `Retrieve: ${active.query}`,
          });
          await runTool("task.retrieve", "/task/retrieve", {
            grant_id: grantId,
            query: active.query,
            k: 5,
          });
          break;
        }
        case "h7": {
          if (!grantId) return;
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: "Ack H7 (cite review)",
          });
          const ok = await runTool("task.h7", "/task/h7-ack", {
            grant_id: grantId,
            h7_acked: true,
          });
          if (ok !== null) {
            patchActive((s) => ({ ...s, h7Acked: true }));
          } else {
            patchActive((s) => ({ ...s, h7Acked: true }));
          }
          break;
        }
        case "draft": {
          if (!grantId) return;
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: "Generate Word DRAFT",
          });
          const data = await runTool<{
            filename: string;
            artefact_version: number | string;
            cite_verdict?: string;
          }>("task.inspect-draft", "/task/inspect-draft", {
            grant_id: grantId,
            title: "Inspection thickness note (DRAFT)",
            findings: active.findings,
            query_for_cites: active.query,
            h7_acked: active.h7Acked,
          });
          if (data) {
            patchActive((s) => ({
              ...s,
              draftFilename: data.filename,
              artefactVersion: data.artefact_version,
              h2Ok: false,
              leaveReady: false,
            }));
          }
          break;
        }
        case "h2": {
          if (!grantId || !active.draftFilename) return;
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: "H2 self-check",
          });
          const data = await runTool("task.h2", "/task/h2-ack", {
            grant_id: grantId,
            draft_filename: active.draftFilename,
            artefact_version: active.artefactVersion,
          });
          if (data !== null) {
            patchActive((s) => ({ ...s, h2Ok: true }));
          }
          break;
        }
        case "export": {
          if (!grantId || !active.draftFilename) return;
          pushEntry({
            kind: "user",
            id: uid("user"),
            ts: Date.now(),
            text: "Export leave (soft copy · not CERT)",
          });
          const data = await runTool<{ filename?: string }>(
            "task.export",
            "/task/export",
            {
              grant_id: grantId,
              draft_filename: active.draftFilename,
              h2_acked: true,
              artefact_version: active.artefactVersion,
            }
          );
          if (data) {
            patchActive((s) => ({
              ...s,
              leaveReady: true,
              meta: { ...s.meta, status: "exported" },
            }));
          }
          break;
        }
        case "sandbox-calc": {
          if (!grantId) return;
          await runTool("sandbox.calc", "/sandbox/calc", {
            grant_id: grantId,
            expression: "8.0 - 7.6",
          });
          break;
        }
        case "sandbox-red": {
          if (!grantId) return;
          await runTool("sandbox.python", "/sandbox/python", {
            grant_id: grantId,
            source: "raise SystemExit(1)",
          });
          break;
        }
        case "h9": {
          if (!grantId) return;
          await runTool("task.h9", "/task/h9-ack", {
            grant_id: grantId,
            accept: true,
          });
          break;
        }
        case "mon-a-start": {
          const data = await runTool<{ session_id: string }>(
            "monitor-a.start",
            "/monitor-a/start",
            {}
          );
          if (data) {
            patchActive((s) => ({ ...s, monSession: data.session_id }));
          }
          break;
        }
        case "mon-a-stop": {
          const sid = active.monSession || "";
          await runTool(
            "monitor-a.stop",
            `/monitor-a/stop?session_id=${encodeURIComponent(sid)}`,
            {}
          );
          break;
        }
        case "g9": {
          await runTool("task.export-check", "/task/export-check", {
            text: "AKIAIOSFODNN7EXAMPLE secret_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
          });
          break;
        }
        case "g8": {
          if (!grantId) return;
          await runTool("gateway.chat", "/gateway/chat", {
            grant_id: grantId,
            model: "gpt-4o",
            messages: [{ role: "user", content: "ping" }],
          });
          break;
        }
        case "revoke": {
          if (!grantId) return;
          await runTool("task.revoke", "/task/revoke", { grant_id: grantId });
          break;
        }
        default:
          break;
      }
    } finally {
      setBusy(false);
    }
  }

  const isElectron = Boolean(window.kwbDesktop?.isElectron);

  return (
    <div className="app">
      <header className="titlebar">
        <div className="titlebar-brand">
          Knowledge Work Bench
          <span>
            {isElectron ? "desktop" : "renderer"} · agent workbench
          </span>
        </div>
        <div className="titlebar-meta">
          <span className={`dot ${healthOk ? "ok" : healthOk === false ? "bad" : ""}`} />
          <span>{healthLine}</span>
          <span className="badge badge-draft">DRAFT</span>
          <span className="badge badge-not-cert">not CERT</span>
        </div>
      </header>

      <div className="shell">
        <SessionList
          sessions={sessions.map((s) => s.meta)}
          activeId={resolvedId}
          onSelect={setActiveId}
          onNew={newSession}
        />

        <main className="workspace">
          <Transcript entries={active?.entries ?? []} />
          <div ref={bottomRef} />
          <Composer
            taskType={active?.meta.task_type ?? "inspection"}
            onTaskType={(t) =>
              patchActive((s) => ({
                ...s,
                meta: { ...s.meta, task_type: t },
              }))
            }
            extract={active?.extract ?? FX_EXTRACT}
            onExtract={(v) => patchActive((s) => ({ ...s, extract: v }))}
            query={active?.query ?? DEFAULT_QUERY}
            onQuery={(v) => patchActive((s) => ({ ...s, query: v }))}
            findings={active?.findings ?? DEFAULT_FINDINGS}
            onFindings={(v) => patchActive((s) => ({ ...s, findings: v }))}
            busy={busy}
            hasGrant={Boolean(active?.meta.grant_id)}
            onAction={handleAction}
          />
        </main>

        <MonitorPanel
          healthOk={healthOk}
          healthLine={healthLine}
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
