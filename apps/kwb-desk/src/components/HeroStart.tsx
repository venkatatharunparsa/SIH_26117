"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";
import { saveWalkSession } from "@/lib/constants";

type Health = {
  product?: string;
  bind?: string;
  version?: string;
  ok?: boolean;
};

export function HeroStart() {
  const router = useRouter();
  const [healthLine, setHealthLine] = useState("connecting…");
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const h = await api<Health>("/health");
        if (cancelled) return;
        setHealthLine(
          `${h.product ?? "KWB"} · ${h.bind ?? "127.0.0.1:8080"} · v${h.version ?? "?"}\nOllama inference-only · no pull`
        );
      } catch {
        if (!cancelled) {
          setHealthLine("API offline — start uvicorn on :8080");
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  async function startTask(taskType: "inspection" | "coding") {
    setBusy(true);
    try {
      const data = await api<{
        grant_id: string;
        task_id: string;
        route: { card_id?: string; model_id?: string };
      }>("/task/start", { task_type: taskType, user_id: "desk-operator" });
      saveWalkSession({
        grant_id: data.grant_id,
        task_id: data.task_id,
        route: data.route,
        task_type: taskType,
      });
      router.push(`/walk/${encodeURIComponent(data.task_id)}`);
    } catch {
      setHealthLine("Start failed — is API on 127.0.0.1:8080?");
      setBusy(false);
    }
  }

  return (
    <div className="shell-hero" id="shellHero">
      <div className="hero-atmosphere" aria-hidden="true" />
      <header className="hero">
        <h1 className="hero-mark">Knowledge Work Bench</h1>
        <p className="hero-line">
          Assist → <em>self-check</em> → export leave
        </p>
        <div className="hero-actions">
          <button
            type="button"
            className="primary btn-xl"
            disabled={busy}
            onClick={() => startTask("inspection")}
          >
            Start inspection walk
          </button>
          <button
            type="button"
            className="secondary"
            disabled={busy}
            onClick={() => startTask("coding")}
          >
            Coding path
          </button>
        </div>
        <p className="hero-meta" style={{ whiteSpace: "pre-line" }}>
          {healthLine}
        </p>
      </header>
    </div>
  );
}
