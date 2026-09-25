export const FX_EXTRACT = `Confidential synthetic — FX-EXT-01
Asset: V-101 shell course A
Measured thickness: 7.6 mm
Location: North quadrant, 1.2 m above grade
Raw notes: Pit indication near weld toe. Compare to SOP-THK-001 minimum 8.0 mm.`;

export const DEFAULT_FINDINGS =
  "Measured thickness 7.6 mm on V-101 shell course A is below SOP minimum 8.0 mm. Recommend reduced inspection interval. Confidential synthetic.";

export const DEFAULT_QUERY = "thickness vessel minimum";

/** Bundled demo fixtures (Confidential synthetic) — picker for Files screen */
export const FIXTURES = [
  {
    id: "FX-EXT-01",
    label: "Vessel thickness extract (H1)",
    body: FX_EXTRACT,
  },
  {
    id: "FX-SCAN-01",
    label: "Scan stub notes",
    body: `Confidential synthetic — FX-SCAN-01 scan stub
Vessel V-101 north quadrant OCR stub.
Thickness candidate: 7.6 mm. Use under H1 confirm (not live OCR).`,
  },
  {
    id: "FX-SOP-THK",
    label: "SOP thickness excerpt",
    body: `Confidential synthetic — SOP-THK-001 excerpt
Minimum allowable thickness for V-101 shell course A: 8.0 mm.
Cite via retrieve under grant; do not invent.`,
  },
  {
    id: "FX-README",
    label: "Attach README demo",
    body: `# README — Vessel thickness desk note (attach demo)

Confidential synthetic — SIH26 Knowledge Work Bench demo file.

## Asset
- Tag: **V-101** shell course A
- Location: North quadrant, ~1.2 m above grade

## Measurement
- Measured thickness: **7.6 mm**
- Compare to SOP-THK-001 minimum: **8.0 mm**

## Notes
Pit indication near weld toe. Recommend reduced inspection interval.
After Confirm extract, generate a Word DRAFT (.docx).`,
  },
] as const;

export type FixtureId = (typeof FIXTURES)[number]["id"];

export type RouteInfo = {
  card_id?: string;
  model_id?: string;
};

export type TaskType = "inspection" | "coding";

export type SessionMeta = {
  id: string;
  title: string;
  task_type: TaskType;
  grant_id: string | null;
  task_id: string | null;
  route: RouteInfo;
  createdAt: number;
  status: "idle" | "active" | "denied" | "exported";
};

export type ToolStatus = "running" | "ok" | "deny" | "info";

export type StreamEntry =
  | {
      kind: "system";
      id: string;
      ts: number;
      text: string;
    }
  | {
      kind: "user";
      id: string;
      ts: number;
      text: string;
    }
  | {
      kind: "assistant";
      id: string;
      ts: number;
      text: string;
      model?: string;
    }
  | {
      kind: "ask";
      id: string;
      ts: number;
      prompt: string;
      contextPreview?: string;
      askKind: string;
    }
  | {
      kind: "tool";
      id: string;
      ts: number;
      name: string;
      path: string;
      status: ToolStatus;
      request?: unknown;
      response?: unknown;
      summary?: string;
      errorCode?: string;
      phases?: string[];
    };

export function uid(prefix = "id"): string {
  return `${prefix}-${Math.random().toString(36).slice(2, 10)}`;
}
