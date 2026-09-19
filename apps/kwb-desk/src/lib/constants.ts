export const STEPS = [
  { id: "intent", label: "Intent" },
  { id: "files", label: "Files" },
  { id: "h1", label: "H1" },
  { id: "knowledge", label: "Knowledge" },
  { id: "draft", label: "DRAFT" },
  { id: "gates", label: "Gates" },
  { id: "export", label: "Export" },
] as const;

export const FX_EXTRACT = `Confidential synthetic — FX-EXT-01
Asset: V-101 shell course A
Measured thickness: 7.6 mm
Location: North quadrant, 1.2 m above grade
Raw notes: Pit indication near weld toe. Compare to SOP-THK-001 minimum 8.0 mm.`;

export const DEFAULT_FINDINGS =
  "Measured thickness 7.6 mm on V-101 shell course A is below SOP minimum 8.0 mm. Recommend reduced inspection interval. Confidential synthetic.";

export type RouteInfo = {
  card_id?: string;
  model_id?: string;
};

export type WalkSession = {
  grant_id: string;
  task_id: string;
  route: RouteInfo;
  task_type: "inspection" | "coding";
};

const STORAGE_KEY = "kwb-walk-session";

export function saveWalkSession(s: WalkSession): void {
  if (typeof window === "undefined") return;
  sessionStorage.setItem(STORAGE_KEY, JSON.stringify(s));
}

export function loadWalkSession(taskId: string): WalkSession | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = sessionStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const s = JSON.parse(raw) as WalkSession;
    if (s.task_id !== taskId) return null;
    return s;
  } catch {
    return null;
  }
}
