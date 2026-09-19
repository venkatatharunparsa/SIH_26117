export const FX_EXTRACT = `Confidential synthetic — FX-EXT-01
Asset: V-101 shell course A
Measured thickness: 7.6 mm
Location: North quadrant, 1.2 m above grade
Raw notes: Pit indication near weld toe. Compare to SOP-THK-001 minimum 8.0 mm.`;

export const DEFAULT_FINDINGS =
  "Measured thickness 7.6 mm on V-101 shell course A is below SOP minimum 8.0 mm. Recommend reduced inspection interval. Confidential synthetic.";

export const DEFAULT_QUERY = "thickness vessel minimum";

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
    };

export function uid(prefix = "id"): string {
  return `${prefix}-${Math.random().toString(36).slice(2, 10)}`;
}
