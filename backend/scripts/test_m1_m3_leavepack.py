"""M1–M3 leave-with integration — artefact download + leave-pack zip.

Requires API on 127.0.0.1:8080 with latest code.
Run: python scripts/test_m1_m3_leavepack.py
"""

from __future__ import annotations

import io
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile

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


def get_bytes(path: str) -> tuple[int, bytes, dict[str, str]]:
    req = urllib.request.Request(BASE + path, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return resp.status, resp.read(), headers
    except urllib.error.HTTPError as e:
        headers = {k.lower(): v for k, v in e.headers.items()} if e.headers else {}
        return e.code, e.read(), headers


def main() -> int:
    print("=== M1–M3 leave-pack integration ===")

    st, start = post("/task/start", {"task_type": "inspection", "user_id": "m1m3-test"})
    assert st == 200, start
    gid = start["grant_id"]
    print(f"OK start grant={gid}")

    st, h1 = post(
        "/task/h1-confirm",
        {"grant_id": gid, "extract_text": "V-101 7.6mm FX-EXT-01", "h1_acked": True},
    )
    assert st == 200, h1
    print("OK h1")

    st, draft = post(
        "/task/inspect-draft",
        {
            "grant_id": gid,
            "title": "M1–M3 leave pack note (DRAFT)",
            "findings": "Measured 7.6 mm below 8.0 mm min. Confidential synthetic.",
        },
    )
    assert st == 200, draft
    filename = draft["filename"]
    ver = draft["artefact_version"]
    print(f"OK draft {filename} ver={ver}")

    st, h2 = post(
        "/task/h2-ack",
        {"grant_id": gid, "draft_filename": filename, "artefact_version": ver},
    )
    assert st == 200, h2
    print("OK h2")

    st, exp = post(
        "/task/export",
        {
            "grant_id": gid,
            "draft_filename": filename,
            "h2_acked": True,
            "artefact_version": ver,
        },
    )
    assert st == 200 and exp.get("ok"), exp
    print(f"OK export {exp.get('filename')}")

    # M1 — GET /artifacts/{filename}
    q = urllib.parse.urlencode({"grant_id": gid})
    st, body, headers = get_bytes(f"/artifacts/{urllib.parse.quote(filename)}?{q}")
    assert st == 200, (st, body[:200])
    ctype = headers.get("content-type", "")
    assert "officedocument" in ctype or "octet-stream" in ctype or "word" in ctype, ctype
    assert body[:2] == b"PK", "docx is a zip (PK header)"
    assert len(body) > 100, len(body)
    print(f"PASS M1 artifact GET 200 bytes={len(body)} content-type={ctype}")

    # traversal / bad type smoke
    st_bad, _, _ = get_bytes("/artifacts/../secrets.txt")
    assert st_bad in (400, 404), st_bad
    st_ext, _, _ = get_bytes("/artifacts/not-a-docx.exe")
    assert st_ext in (400, 404), st_ext
    print("PASS M1 path/type guards")

    # M2 — leave-pack zip
    pack_q = urllib.parse.urlencode(
        {"grant_id": gid, "draft_filename": filename}
    )
    st, zbytes, zheaders = get_bytes(f"/task/leave-pack?{pack_q}")
    assert st == 200, (st, zbytes[:300])
    zctype = zheaders.get("content-type", "")
    assert "zip" in zctype or "octet-stream" in zctype, zctype
    assert zbytes[:2] == b"PK", "leave-pack must be zip"
    with zipfile.ZipFile(io.BytesIO(zbytes)) as zf:
        names = set(zf.namelist())
        assert filename in names, names
        assert "manifest.json" in names, names
        assert "audit-slice.json" in names, names
        manifest = json.loads(zf.read("manifest.json").decode("utf-8"))
        assert manifest.get("grant_id") == gid, manifest
        assert manifest.get("draft") == filename, manifest
        assert "exported_at" in manifest, manifest
        note = manifest.get("note") or ""
        assert "export leave" in note and "not CERT" in note, note
        assert "no forward-accept" in note, note
        docx_in_zip = zf.read(filename)
        assert docx_in_zip[:2] == b"PK"
    print(
        f"PASS M2 leave-pack 200 zip_bytes={len(zbytes)} members={sorted(names)} "
        f"note={manifest.get('note')!r}"
    )

    print("PASS M1+M2+M3 (API) — desk buttons are manual UI; endpoints wired.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as e:
        print("FAIL", e, file=sys.stderr)
        raise SystemExit(1)
    except urllib.error.URLError as e:
        print("FAIL API unreachable — start uvicorn on 127.0.0.1:8080:", e, file=sys.stderr)
        raise SystemExit(2)
