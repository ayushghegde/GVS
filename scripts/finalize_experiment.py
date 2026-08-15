#!/usr/bin/env python3
"""Create a reproducibility manifest for a GVS experiment directory."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def command_version(command: list[str]) -> str | None:
    try:
        p = subprocess.run(command, check=False, capture_output=True, text=True, timeout=10)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    text = (p.stdout or p.stderr).strip().splitlines()
    return text[0] if text else None


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: finalize_experiment.py experiments/<id>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    files = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.name == "manifest.json":
            continue
        rel = p.relative_to(root).as_posix()
        files.append({"path": rel, "bytes": p.stat().st_size, "sha256": sha256(p)})

    manifest = {
        "schema": "gvs-experiment-manifest-v1",
        "experiment": root.name,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "host": {
            "platform": platform.platform(),
            "python": platform.python_version(),
        },
        "tools": {
            "ngspice": command_version(["ngspice", "--version"]),
            "magic": command_version(["magic", "--version"]),
            "klayout": command_version(["klayout", "-v"]),
        },
        "environment": {
            "PDK_ROOT": os.environ.get("PDK_ROOT"),
            "PDK": os.environ.get("PDK"),
        },
        "files": files,
        "required_review": [
            "Confirm REPORT.md states PASS/PARTIAL PASS/FAIL.",
            "Confirm exact run command/script is present.",
            "Confirm simulator/PDK/corner information is recorded.",
            "Confirm generated data is not mislabeled as historical or extracted data.",
        ],
    }

    out = root / "manifest.json"
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
