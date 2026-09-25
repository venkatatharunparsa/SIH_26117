import { useEffect, useState } from "react";
import { CheckCircle2, Circle, Loader2, Sparkles } from "lucide-react";
import { api } from "../lib/api";

export type SkillStep = {
  id: string;
  label: string;
  detail: string;
  skill_id?: string;
};

type Recommend = {
  ok?: boolean;
  reason?: string;
  empty?: boolean;
  skills?: Array<{ id: string; description?: string; score?: number }>;
  steps?: SkillStep[];
};

type Props = {
  taskType: "inspection" | "coding";
  /** Live composer text — skills re-score as the operator types */
  message: string;
  filename: string | null;
  phase: string | null;
  hasAttach: boolean;
  hasDraft: boolean;
  leaveReady: boolean;
  busy: boolean;
  pendingAsk: string | null;
};

/** Which skill step ids are already finished for the current orch phase. */
function doneIds(phase: string, flags: Props): Set<string> {
  const p = (phase || "idle").toLowerCase();
  const done = new Set<string>();
  if (flags.hasAttach || p !== "idle") done.add("ingest");
  if (
    p === "await_review_cites" ||
    p === "await_self_check" ||
    p === "await_export" ||
    p === "done" ||
    flags.hasDraft
  ) {
    done.add("confirm_extract");
    done.add("retrieve");
    done.add("read_request");
  }
  if (p === "await_self_check" || p === "await_export" || p === "done" || flags.hasDraft) {
    done.add("review_cites");
    done.add("draft_word");
    done.add("sandbox");
    done.add("observe");
  }
  if (p === "await_export" || p === "done" || flags.leaveReady) {
    done.add("self_check");
    done.add("accept");
  }
  if (p === "done" || flags.leaveReady) done.add("export");
  return done;
}

export function AgentPlan(props: Props) {
  const {
    taskType,
    message,
    filename,
    phase,
    busy,
    pendingAsk,
  } = props;
  const [plan, setPlan] = useState<Recommend | null>(null);

  useEffect(() => {
    const handle = window.setTimeout(() => {
      void api<Recommend>("/skills/recommend", {
        message: message || "",
        filename: filename || "",
        task_type: taskType,
      })
        .then(setPlan)
        .catch(() =>
          setPlan({
            ok: false,
            empty: true,
            reason: "Skill recommend unavailable · is the API up?",
            steps: [],
            skills: [],
          })
        );
    }, 280);
    return () => window.clearTimeout(handle);
  }, [message, filename, taskType]);

  const steps = plan?.steps || [];
  const finished = doneIds(phase || "idle", props);
  const activeId = steps.find((s) => !finished.has(s.id))?.id;

  return (
    <div className="agent-plan" aria-label="Skill plan">
      <div className="agent-plan-head">
        <Sparkles size={13} aria-hidden />
        <strong>Skill plan</strong>
        {(plan?.skills || []).map((s) => (
          <span key={s.id} className="agent-plan-mode" title={s.description || s.id}>
            {s.id}
          </span>
        ))}
        {pendingAsk ? (
          <span className="agent-plan-ask">needs you · {pendingAsk}</span>
        ) : null}
      </div>
      {steps.length === 0 ? (
        <p className="agent-plan-note">
          {plan?.reason ||
            "Type a task or attach a file. Matching skills will propose the steps — nothing is fixed until the input matches a skill."}
        </p>
      ) : (
        <ol className="agent-plan-list skill">
          {steps.map((s) => {
            const st = finished.has(s.id)
              ? "done"
              : s.id === activeId
                ? "active"
                : "todo";
            return (
              <li key={`${s.skill_id}-${s.id}`} className={`agent-plan-step ${st}`}>
                <span className="agent-plan-ico" aria-hidden>
                  {st === "done" ? (
                    <CheckCircle2 size={12} />
                  ) : st === "active" && busy ? (
                    <Loader2 size={12} className="spin" />
                  ) : (
                    <Circle size={12} />
                  )}
                </span>
                <span className="agent-plan-label">{s.label}</span>
                <span className="agent-plan-detail">
                  {s.skill_id ? `${s.skill_id} · ` : ""}
                  {s.detail}
                </span>
              </li>
            );
          })}
        </ol>
      )}
      <p className="agent-plan-note">
        {plan?.reason} Steps are written in <code>data/skills/*/SKILL.md</code>.
        The workbench runs the matched skill, then stops at a human gate — it does
        not invent a free-form plan.
      </p>
    </div>
  );
}
