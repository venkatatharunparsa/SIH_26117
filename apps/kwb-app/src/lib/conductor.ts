/** Claude Code–style conductor: background context + ask only when human input is required.
 * Ask payloads are produced by the backend orchestrator (/orch/turn); these helpers map them for UI.
 */

export type AskKind =
  | "confirm_extract"
  | "review_cites"
  | "self_check_draft"
  | "accept_sandbox"
  | "confirm_export"
  | "goal";

export type PendingAsk = {
  id: string;
  kind: AskKind;
  /** Shown in stream — what we need from the human */
  prompt: string;
  /** Background context the agent already has (not a form) */
  contextPreview?: string;
  /** Tool action / orch confirm_action */
  confirmAction: string;
  /** If human types free text, where it goes before confirm */
  acceptTextAs?: "extract" | "query" | "findings" | "none";
};

export function isAffirmative(text: string): boolean {
  const t = text.trim().toLowerCase();
  return (
    t === "" ||
    t === "y" ||
    t === "yes" ||
    t === "ok" ||
    t === "okay" ||
    t === "confirm" ||
    t === "continue" ||
    t === "proceed" ||
    t === "lgtm" ||
    t === "ack"
  );
}

export function askFromOrch(ask: {
  kind?: string;
  prompt?: string;
  context_preview?: string;
  confirm_action?: string;
}): Omit<PendingAsk, "id"> {
  const kind = (ask.kind || "goal") as AskKind;
  const action = ask.confirm_action || "confirm";
  let acceptTextAs: PendingAsk["acceptTextAs"] = "none";
  if (action === "confirm_extract") acceptTextAs = "extract";
  else if (action === "confirm_cites") acceptTextAs = "findings";
  else if (action === "confirm_self_check") acceptTextAs = "findings";
  return {
    kind,
    prompt: ask.prompt || "Confirm to continue.",
    contextPreview: ask.context_preview,
    confirmAction: action,
    acceptTextAs,
  };
}

export function askConfirmExtract(extract: string): Omit<PendingAsk, "id"> {
  const preview =
    extract.length > 420 ? `${extract.slice(0, 420)}…` : extract;
  return {
    kind: "confirm_extract",
    prompt:
      "Confirm extract before we treat it as input. Enter to accept background context, or paste a corrected extract.",
    contextPreview: preview,
    confirmAction: "confirm_extract",
    acceptTextAs: "extract",
  };
}

export function askReviewCites(): Omit<PendingAsk, "id"> {
  return {
    kind: "review_cites",
    prompt:
      "Review citations vs company docs. Enter to proceed to DRAFT PowerPoint, or type notes to fold into findings.",
    confirmAction: "confirm_cites",
    acceptTextAs: "findings",
  };
}

export function askSelfCheckDraft(
  filename: string | null
): Omit<PendingAsk, "id"> {
  return {
    kind: "self_check_draft",
    prompt: `Self-check DRAFT${filename ? ` (${filename})` : ""} before export leave. Enter to confirm, or type corrections for findings then we re-check.`,
    confirmAction: "confirm_self_check",
    acceptTextAs: "findings",
  };
}

export function askAcceptSandbox(): Omit<PendingAsk, "id"> {
  return {
    kind: "accept_sandbox",
    prompt:
      "Sandbox finished. Enter to accept the observation, or type reject to stop the leave path.",
    confirmAction: "h9",
    acceptTextAs: "none",
  };
}

export function askConfirmExport(): Omit<PendingAsk, "id"> {
  return {
    kind: "confirm_export",
    prompt:
      "Export leave — soft-copy DRAFT (not CERT). Enter to export, or type cancel.",
    confirmAction: "confirm_export",
    acceptTextAs: "none",
  };
}
