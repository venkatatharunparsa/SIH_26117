"use client";

import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import {
  API_BASE,
  api,
  artifactUrl,
  leavePackUrl,
  type ApiError,
} from "@/lib/api";
import {
  DEFAULT_FINDINGS,
  FX_EXTRACT,
  STEPS,
  saveWalkSession,
  type RouteInfo,
  type WalkSession,
} from "@/lib/constants";

type BannerKind = "ok" | "bad" | "warn" | null;

type Props = {
  session: WalkSession;
};

export function Workbench({ session }: Props) {
  const [grantId] = useState(session.grant_id);
  const [taskId] = useState(session.task_id);
  const [route] = useState<RouteInfo>(session.route);
  const [taskType, setTaskType] = useState<"inspection" | "coding">(
    session.task_type
  );

  const [step, setStep] = useState(1);
  const [maxStep, setMaxStep] = useState(1);
  const [banner, setBanner] = useState(
    "Select a step action. Deny banners appear here — fail-closed."
  );
  const [bannerKind, setBannerKind] = useState<BannerKind>(null);
  const [logText, setLogText] = useState("");
  const [lastDenies, setLastDenies] = useState<string[]>([]);
  const [healthLine, setHealthLine] = useState("—");

  const [extract, setExtract] = useState(FX_EXTRACT);
  const [query, setQuery] = useState("thickness vessel minimum");
  const [findings, setFindings] = useState(DEFAULT_FINDINGS);
  const [citesText, setCitesText] = useState("Cites appear here.");
  const [filesStatus, setFilesStatus] = useState("No fixture loaded yet.");
  const [fixtureLoaded, setFixtureLoaded] = useState(false);
  const [draftFilename, setDraftFilename] = useState<string | null>(null);
  const [artefactVersion, setArtefactVersion] = useState<number | null>(null);
  const [draftMeta, setDraftMeta] = useState("No DRAFT yet.");
  const [h7Acked, setH7Acked] = useState(false);
  const [h2Ok, setH2Ok] = useState(false);
  const [monSession, setMonSession] = useState<string | null>(null);
  const [leaveReady, setLeaveReady] = useState(false);

  const log = useCallback((msg: string, obj?: unknown) => {
    const line =
      typeof obj === "undefined" ? msg : `${msg} ${JSON.stringify(obj)}`;
    setLogText((prev) => (prev ? `${prev}\n${line}` : line));
  }, []);

  const pushDeny = useCallback((code: string) => {
    if (!code) return;
    setLastDenies((prev) => [String(code), ...prev].slice(0, 6));
  }, []);

  const showBanner = useCallback((text: string, kind: BannerKind = null) => {
    setBanner(text);
    setBannerKind(kind);
  }, []);

  const callApi = useCallback(
    async <T,>(path: string, body?: unknown): Promise<T> => {
      try {
        const data = await api<T>(path, body);
        const keys =
          data && typeof data === "object"
            ? Object.keys(data as object).slice(0, 8)
            : [];
        log(`OK ${path}`, { ok: true, keys });
        return data;
      } catch (e) {
        const err = e as ApiError;
        log(`DENY ${path}`, err.detail);
        pushDeny(err.errorCode);
        showBanner(`Denied: ${err.errorCode}`, "bad");
        throw e;
      }
    },
    [log, pushDeny, showBanner]
  );

  const advanceTo = (i: number) => {
    setMaxStep((m) => Math.max(m, i));
    setStep(i);
  };

  useEffect(() => {
    document.body.classList.add("is-working");
    return () => {
      document.body.classList.remove("is-working");
    };
  }, []);

  useEffect(() => {
    (async () => {
      try {
        const h = await api<{ bind?: string; version?: string }>("/health");
        setHealthLine(
          `${h.bind ?? "127.0.0.1:8080"} · v${h.version ?? "?"} · Ollama inference-only`
        );
        showBanner(
          `Task loaded · card ${route.card_id ?? "—"}${
            route.model_id
              ? ` · model ${route.model_id} (G1 floor may share model_id)`
              : ""
          }`,
          "ok"
        );
      } catch {
        setHealthLine("API offline");
      }
    })();
  }, [route, showBanner]);

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
        const denyCodes: string[] = [];
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
          if (err) denyCodes.push(err);
          return `${t} ${name}${err ? " · " + err : ""}`;
        });
        if (denyCodes.length) {
          setLastDenies((prev) =>
            [...new Set([...denyCodes, ...prev])].slice(0, 6)
          );
        }
        setLogText((prev) => {
          const kept = prev
            .split("\n")
            .filter((l) => l.startsWith("OK ") || l.startsWith("DENY "));
          return (
            kept.join("\n") +
            (kept.length ? "\n" : "") +
            "--- audit ---\n" +
            lines.join("\n")
          ).trim();
        });
      } catch {
        /* optional */
      }
    };
    const id = setInterval(poll, 4000);
    return () => clearInterval(id);
  }, []);

  async function restartTask() {
    const data = await callApi<{
      grant_id: string;
      task_id: string;
      route: RouteInfo;
    }>("/task/start", { task_type: taskType, user_id: "desk-operator" });
    saveWalkSession({
      grant_id: data.grant_id,
      task_id: data.task_id,
      route: data.route,
      task_type: taskType,
    });
    window.location.href = `/walk/${encodeURIComponent(data.task_id)}`;
  }

  return (
    <div className="workbench" id="workbench" aria-live="polite">
      <div className="wb-top">
        <div className="wb-brand">
          Knowledge Work Bench
          <span>Self-HITL · same-user gates · soft copy leave</span>
        </div>
        <div className="wb-health">
          {healthLine}
          <div style={{ marginTop: "0.35rem" }}>
            <Link href="/" className="ghost" style={{ fontSize: "0.75rem" }}>
              ← Home
            </Link>
          </div>
        </div>
      </div>

      <nav className="step-rail" aria-label="Walk steps">
        <h2>Walk</h2>
        <ul className="step-list">
          {STEPS.map((s, i) => {
            let cls = "step-item";
            if (i < step) cls += " done";
            if (i === step) cls += " current";
            return (
              <li key={s.id}>
                <button
                  type="button"
                  className={cls}
                  disabled={i > maxStep}
                  onClick={() => i <= maxStep && setStep(i)}
                >
                  <span className="idx">{String(i + 1).padStart(2, "0")}</span>
                  <span className="label-full">{s.label}</span>
                </button>
              </li>
            );
          })}
        </ul>
      </nav>

      <main className="stage">
        <div
          className={
            "banner" +
            (bannerKind === "ok"
              ? " ok"
              : bannerKind === "bad"
                ? " bad"
                : bannerKind === "warn"
                  ? " warn"
                  : "")
          }
        >
          {banner}
        </div>

        {step === 0 && (
          <section className="stage-panel active">
            <p className="stage-kicker">Step A · Intent</p>
            <h2 className="stage-title">Start a personal assist task</h2>
            <p className="stage-lead">
              No org chart. No Approver picker. Task type routes the Model Card;
              you own every gate.
            </p>
            <div className="field">
              <label htmlFor="taskType">Task type</label>
              <select
                id="taskType"
                value={taskType}
                onChange={(e) =>
                  setTaskType(e.target.value as "inspection" | "coding")
                }
              >
                <option value="inspection">Inspection</option>
                <option value="coding">Coding</option>
              </select>
            </div>
            <div className="actions">
              <button type="button" className="primary" onClick={restartTask}>
                Restart task
              </button>
              <button
                type="button"
                className="secondary"
                onClick={async () => {
                  const data = await callApi<{ session_id: string }>(
                    "/monitor-a/start",
                    {}
                  );
                  setMonSession(data.session_id);
                  showBanner(
                    "Monitor A start snapshot — evidence pack, not CERT.",
                    "ok"
                  );
                }}
              >
                Monitor A start
              </button>
              <button
                type="button"
                className="secondary"
                onClick={async () => {
                  const data = await callApi<{
                    pack?: { sha256?: string };
                  }>(
                    `/monitor-a/stop?session_id=${encodeURIComponent(monSession || "")}`,
                    {}
                  );
                  showBanner(
                    `Monitor A stop · sha256 ${(data.pack?.sha256 || "").slice(0, 12)}… — not CERT.`,
                    "ok"
                  );
                }}
              >
                Monitor A stop
              </button>
            </div>
            <p className="note-inline">
              Monitor A = evidence pack on workbench + Ollama loopback —{" "}
              <strong>not CERT</strong>.
            </p>
          </section>
        )}

        {step === 1 && (
          <section className="stage-panel active">
            <p className="stage-kicker">Step B · Files</p>
            <h2 className="stage-title">Load inputs</h2>
            <p className="stage-lead">
              Fixture extract only — no live plant browse. Confidential
              synthetic.
            </p>
            <div className="actions">
              <button
                type="button"
                className="primary"
                onClick={() => {
                  setExtract(FX_EXTRACT);
                  setFixtureLoaded(true);
                  setFilesStatus(
                    "FX-EXT-01 loaded (Confidential synthetic)."
                  );
                  showBanner("Fixture FX-EXT-01 loaded.", "ok");
                  setMaxStep((m) => Math.max(m, 2));
                }}
              >
                Load FX-EXT-01
              </button>
              <button
                type="button"
                className="secondary"
                onClick={() => {
                  if (!fixtureLoaded) {
                    setExtract(FX_EXTRACT);
                    setFixtureLoaded(true);
                  }
                  advanceTo(2);
                  showBanner("Review extract, then confirm H1.");
                }}
              >
                Continue to extract
              </button>
            </div>
            <p className="note-inline">{filesStatus}</p>
          </section>
        )}

        {step === 2 && (
          <section className="stage-panel active">
            <p className="stage-kicker">Step C · Extract + H1</p>
            <h2 className="stage-title">Confirm the extract</h2>
            <p className="stage-lead">
              You review the text. H1 is same-user acknowledge — not plant
              approval.
            </p>
            <div className="field">
              <label htmlFor="extract">
                Fixture extract{" "}
                <span className="hint">Confidential synthetic</span>
              </label>
              <textarea
                id="extract"
                value={extract}
                onChange={(e) => setExtract(e.target.value)}
              />
            </div>
            <div className="actions">
              <button
                type="button"
                className="primary"
                onClick={async () => {
                  await callApi("/task/h1-confirm", {
                    grant_id: grantId,
                    extract_text: extract,
                    h1_acked: true,
                  });
                  advanceTo(3);
                  showBanner(
                    "H1 confirmed — extract accepted by same user.",
                    "ok"
                  );
                }}
              >
                Confirm H1
              </button>
            </div>
          </section>
        )}

        {step === 3 && (
          <section className="stage-panel active">
            <p className="stage-kicker">Step D · Knowledge</p>
            <h2 className="stage-title">Retrieve with cite-or-abstain</h2>
            <p className="stage-lead">
              Honest NOT FOUND is success. Ack H7 before drafting when cites
              return.
            </p>
            <div className="field">
              <label htmlFor="query">Retrieve query</label>
              <input
                id="query"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              />
            </div>
            <div className="actions">
              <button
                type="button"
                className="primary"
                onClick={async () => {
                  const data = await callApi<{
                    cites?: { path: string; snippet: string }[];
                    verdict?: string;
                  }>("/task/retrieve", {
                    grant_id: grantId,
                    query,
                    k: 5,
                  });
                  const cites =
                    (data.cites || [])
                      .map((c) => `${c.path}: ${c.snippet}`)
                      .join("\n") ||
                    data.verdict ||
                    "NOT FOUND";
                  setCitesText(cites);
                  setMaxStep((m) => Math.max(m, 3));
                  showBanner(
                    data.verdict === "NOT FOUND"
                      ? "Retrieve: NOT FOUND (honest)."
                      : "Cites returned — ack H7 before draft.",
                    data.verdict === "NOT FOUND" ? "warn" : "ok"
                  );
                }}
              >
                Retrieve
              </button>
              <button
                type="button"
                className="secondary"
                onClick={async () => {
                  setH7Acked(true);
                  try {
                    await callApi("/task/h7-ack", {
                      grant_id: grantId,
                      h7_acked: true,
                    });
                  } catch {
                    /* client flag kept */
                  }
                  advanceTo(4);
                  showBanner(
                    "H7 acknowledged (own-work cite review).",
                    "ok"
                  );
                }}
              >
                Ack H7 (cites)
              </button>
            </div>
            <div className="cites-box">{citesText}</div>
          </section>
        )}

        {step === 4 && (
          <section className="stage-panel active">
            <p className="stage-kicker">Step E · DRAFT</p>
            <h2 className="stage-title">Generate Word DRAFT</h2>
            <p className="stage-lead">
              Artefact is a <strong>DRAFT</strong> — not a plant system of
              record. Version stamps for stale detection.
            </p>
            <div className="field">
              <label htmlFor="findings">Findings (DRAFT body)</label>
              <textarea
                id="findings"
                value={findings}
                onChange={(e) => setFindings(e.target.value)}
              />
            </div>
            <div className="actions">
              <button
                type="button"
                className="primary"
                onClick={async () => {
                  const data = await callApi<{
                    filename: string;
                    artefact_version: number;
                    cite_verdict?: string;
                  }>("/task/inspect-draft", {
                    grant_id: grantId,
                    title: "Inspection thickness note (DRAFT)",
                    findings,
                    query_for_cites: query,
                    h7_acked: h7Acked,
                  });
                  setDraftFilename(data.filename);
                  setArtefactVersion(data.artefact_version);
                  setH2Ok(false);
                  setDraftMeta(
                    `${data.filename} · v${data.artefact_version} · ${data.cite_verdict || ""}`
                  );
                  advanceTo(5);
                  showBanner(
                    `DRAFT ready · artefact_version ${data.artefact_version}`,
                    "ok"
                  );
                }}
              >
                Generate Word DRAFT
              </button>
              <button
                type="button"
                className="secondary"
                onClick={async () => {
                  const next = findings + " [edited]";
                  setFindings(next);
                  const data = await callApi<{ artefact_version: number }>(
                    "/task/draft-edit",
                    {
                      grant_id: grantId,
                      draft_filename: draftFilename,
                      findings: next,
                    }
                  );
                  setArtefactVersion(data.artefact_version);
                  setH2Ok(false);
                  showBanner(
                    "Material edit — H2 stale. Re-check before export leave.",
                    "warn"
                  );
                }}
              >
                Edit → stale H2
              </button>
            </div>
            <p className="note-inline">{draftMeta}</p>
          </section>
        )}

        {step === 5 && (
          <section className="stage-panel active">
            <p className="stage-kicker">Step F · Gates</p>
            <h2 className="stage-title">Own-work self-check</h2>
            <p className="stage-lead">
              H2 binds to artefact_version. Coding path needs sandbox + H9.
              Fail-closed injects prove deny.
            </p>
            <div className="actions">
              <button
                type="button"
                className="primary"
                onClick={async () => {
                  await callApi("/task/h2-ack", {
                    grant_id: grantId,
                    draft_filename: draftFilename,
                    artefact_version: artefactVersion,
                  });
                  setH2Ok(true);
                  advanceTo(6);
                  showBanner(
                    "H2 self-check fresh for current artefact_version.",
                    "ok"
                  );
                }}
              >
                H2 self-check
              </button>
            </div>
            <hr className="divider" />
            <p className="subhead">Coding branch</p>
            <div className="actions">
              <button
                type="button"
                className="secondary"
                onClick={async () => {
                  await callApi("/sandbox/calc", {
                    grant_id: grantId,
                    expression: "8.0 - 7.6",
                  });
                  showBanner(
                    "Sandbox calc recorded — H9 required before export if continuing coding path.",
                    "ok"
                  );
                }}
              >
                Sandbox calc
              </button>
              <button
                type="button"
                className="secondary"
                onClick={async () => {
                  await callApi("/sandbox/python", {
                    grant_id: grantId,
                    source: "raise SystemExit(1)",
                  });
                  showBanner(
                    "Sandbox red recorded — export leave must deny (G10).",
                    "warn"
                  );
                }}
              >
                Sandbox red
              </button>
              <button
                type="button"
                className="secondary"
                onClick={async () => {
                  await callApi("/task/h9-ack", {
                    grant_id: grantId,
                    accept: true,
                  });
                  showBanner("H9 accepted.", "ok");
                }}
              >
                H9 accept
              </button>
            </div>
            <hr className="divider" />
            <p className="subhead">Fail-closed injects</p>
            <div className="actions">
              <button
                type="button"
                className="danger"
                onClick={async () => {
                  try {
                    const data = await callApi<{
                      ok?: boolean;
                      error?: string;
                    }>("/task/export-check", {
                      text: "AKIAIOSFODNN7EXAMPLE secret_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                    });
                    if (data.ok === false) {
                      pushDeny(data.error || "secret_in_draft");
                      showBanner(
                        `G9 inject: ${data.error || "secret_in_draft"} — export would deny.`,
                        "bad"
                      );
                    } else {
                      showBanner(
                        "export-check clean (unexpected for inject).",
                        "warn"
                      );
                    }
                  } catch {
                    /* banner set */
                  }
                }}
              >
                G9 · secret → export-check
              </button>
              <button
                type="button"
                className="danger"
                onClick={async () => {
                  try {
                    await callApi("/gateway/chat", {
                      grant_id: grantId,
                      model: "gpt-4o",
                      messages: [{ role: "user", content: "ping" }],
                    });
                  } catch {
                    /* banner set */
                  }
                }}
              >
                G8 · bad model → gateway
              </button>
              <button
                type="button"
                className="danger"
                onClick={async () => {
                  await callApi("/task/revoke", { grant_id: grantId });
                  showBanner(
                    "Grant revoked — further tools must deny (G7).",
                    "warn"
                  );
                  try {
                    await callApi("/task/retrieve", {
                      grant_id: grantId,
                      query: "x",
                    });
                  } catch {
                    /* expected */
                  }
                }}
              >
                Revoke grant
              </button>
            </div>
          </section>
        )}

        {step === 6 && (
          <section className="stage-panel active">
            <p className="stage-kicker">Step G · Export leave</p>
            <h2 className="stage-title">Soft copy off the box</h2>
            <p className="stage-lead">
              Leave-with pack only. No forward-accept into plant SoR. Not CERT.
            </p>
            <div className="actions">
              <button
                type="button"
                className="primary"
                onClick={async () => {
                  const data = await callApi<{ filename?: string }>(
                    "/task/export",
                    {
                      grant_id: grantId,
                      draft_filename: draftFilename,
                      h2_acked: true,
                      artefact_version: artefactVersion,
                    }
                  );
                  setLeaveReady(true);
                  showBanner(
                    `Export leave OK — ${data.filename}. Download DRAFT / leave pack (not CERT · no forward-accept).`,
                    "ok"
                  );
                }}
              >
                Export leave
              </button>
            </div>
            <div className={`success-card${leaveReady ? " show" : ""}`}>
              <h3>Leave pack ready</h3>
              <p>
                Download DRAFT Word and the audit leave pack. Soft copy · not
                CERT · no forward-accept.
              </p>
              <div className="actions">
                <button
                  type="button"
                  className="primary"
                  disabled={!leaveReady || !draftFilename}
                  onClick={() => {
                    if (!draftFilename) return;
                    const a = document.createElement("a");
                    a.href = artifactUrl(draftFilename, grantId);
                    a.download = draftFilename;
                    a.rel = "noopener";
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                  }}
                >
                  Download DRAFT
                </button>
                <button
                  type="button"
                  className="primary"
                  disabled={!leaveReady || !draftFilename}
                  onClick={() => {
                    if (!draftFilename) return;
                    window.open(
                      leavePackUrl(grantId, draftFilename),
                      "_blank",
                      "noopener"
                    );
                  }}
                >
                  Download leave pack
                </button>
              </div>
            </div>
          </section>
        )}
      </main>

      <aside className="monitor" aria-label="Monitor B">
        <div>
          <h2>Monitor B</h2>
          <p className="mon-note">Own task only · live audit · not CERT</p>
        </div>
        <div className="stat-grid">
          <span className="k">grant</span>
          <span className="v">{grantId || "—"}</span>
          <span className="k">task</span>
          <span className="v">{taskId || "—"}</span>
          <span className="k">card</span>
          <span className="v">{route.card_id || "—"}</span>
          <span className="k">model</span>
          <span className="v">{route.model_id || "—"}</span>
          <span className="k">version</span>
          <span className="v">{artefactVersion ?? "—"}</span>
          <span className="k">draft</span>
          <span className="v">{draftFilename || "—"}</span>
          <span className="k">H2</span>
          <span className="v">{h2Ok ? "fresh" : "pending/stale"}</span>
          <span className="k">MonA</span>
          <span className="v">{monSession || "—"}</span>
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
          <div className="audit-log">{logText}</div>
        </div>
      </aside>
    </div>
  );
}
