/** Knowledge Work Bench — API client (FastAPI 127.0.0.1:8080) */

export const API_BASE =
  process.env.NEXT_PUBLIC_KWB_API?.replace(/\/$/, "") ||
  "http://127.0.0.1:8080";

export type ApiError = {
  detail?: unknown;
  status: number;
  errorCode: string;
};

function extractErrorCode(detail: unknown, status: number): string {
  if (detail && typeof detail === "object") {
    const d = detail as Record<string, unknown>;
    const nested = d.detail;
    if (nested && typeof nested === "object") {
      const n = nested as Record<string, unknown>;
      const c = n.error || n.message || n.reason;
      if (typeof c === "string") return c;
    }
    const c = d.error || d.message || d.reason;
    if (typeof c === "string") return c;
  }
  return `http_${status}`;
}

export async function api<T = Record<string, unknown>>(
  path: string,
  body?: unknown
): Promise<T> {
  const opt: RequestInit =
    body === undefined
      ? { method: "GET" }
      : {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        };
  const res = await fetch(`${API_BASE}${path}`, opt);
  let data: Record<string, unknown> = {};
  try {
    data = (await res.json()) as Record<string, unknown>;
  } catch {
    /* empty */
  }
  if (!res.ok) {
    const detail = data.detail ?? data;
    const errorCode = extractErrorCode(
      typeof detail === "object" ? { detail, ...data } : data,
      res.status
    );
    const err = new Error("api") as Error & ApiError;
    err.detail = detail;
    err.status = res.status;
    err.errorCode = errorCode;
    throw err;
  }
  return data as T;
}

export function artifactUrl(filename: string, grantId?: string | null): string {
  const q = grantId ? `?grant_id=${encodeURIComponent(grantId)}` : "";
  return `${API_BASE}/artifacts/${encodeURIComponent(filename)}${q}`;
}

export function leavePackUrl(grantId: string, draftFilename: string): string {
  return (
    `${API_BASE}/task/leave-pack?grant_id=${encodeURIComponent(grantId)}` +
    `&draft_filename=${encodeURIComponent(draftFilename)}`
  );
}
