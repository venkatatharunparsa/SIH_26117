"""Smoke B3/B4/G10 — H2 stale + sandbox-red export deny. API on 127.0.0.1:8080."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:8080"


def post(path: str, body: dict) -> tuple[int, dict]:
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        BASE + path,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, {"raw": raw}


def main() -> int:
    st, start = post("/task/start", {"task_type": "inspection"})
    assert st == 200, start
    gid = start["grant_id"]

    st, h1 = post(
        "/task/h1-confirm",
        {"grant_id": gid, "extract_text": "V-101 7.6mm", "h1_acked": True},
    )
    assert st == 200, h1

    st, draft = post(
        "/task/inspect-draft",
        {
            "grant_id": gid,
            "title": "Thickness note",
            "findings": "Measured 7.6 mm below 8.0 mm min.",
        },
    )
    assert st == 200, draft
    fn = draft["filename"]
    ver = draft["artefact_version"]

    st, _ = post(
        "/task/h2-ack",
        {"grant_id": gid, "draft_filename": fn, "artefact_version": ver},
    )
    assert st == 200

    st, edit = post(
        "/task/draft-edit",
        {"grant_id": gid, "draft_filename": fn, "findings": "Edited — still 7.6 mm."},
    )
    assert st == 200 and edit.get("h2_stale") is True, edit

    st, denied = post(
        "/task/export",
        {"grant_id": gid, "draft_filename": fn, "h2_acked": True, "artefact_version": ver},
    )
    assert st == 400, denied
    detail = denied.get("detail") or denied
    assert "h2_stale" in str(detail), detail
    print("PASS stale export deny")

    new_v = edit["artefact_version"]
    st, _ = post(
        "/task/h2-ack",
        {"grant_id": gid, "draft_filename": fn, "artefact_version": new_v},
    )
    assert st == 200

    st, start2 = post("/task/start", {"task_type": "coding"})
    assert st == 200, start2
    gid2 = start2["grant_id"]
    st, bad = post("/sandbox/python", {"grant_id": gid2, "source": "raise SystemExit(1)"})
    assert st == 200 and bad.get("ok") is False, bad
    st, h9fail = post("/task/h9-ack", {"grant_id": gid2, "accept": True})
    assert st == 400, h9fail
    print("PASS sandbox-red H9 accept deny")

    # coding draft path minimal: make a draft under gid2 then export should hit G10
    st, d2 = post(
        "/task/inspect-draft",
        {"grant_id": gid2, "title": "Code note", "findings": "sandbox red walk"},
    )
    assert st == 200, d2
    st, _ = post(
        "/task/h2-ack",
        {
            "grant_id": gid2,
            "draft_filename": d2["filename"],
            "artefact_version": d2["artefact_version"],
        },
    )
    assert st == 200
    st, g10 = post(
        "/task/export",
        {
            "grant_id": gid2,
            "draft_filename": d2["filename"],
            "h2_acked": True,
            "artefact_version": d2["artefact_version"],
        },
    )
    assert st == 400, g10
    assert "sandbox_red" in str(g10), g10
    print("PASS G10 sandbox-red export deny")
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
