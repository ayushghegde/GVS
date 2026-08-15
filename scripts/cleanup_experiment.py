#!/usr/bin/env python3
"""Remove disposable experiment artifacts while preserving reproducibility.

Usage:
    python scripts/cleanup_experiment.py experiments/<id>

The script deletes only known disposable patterns and never removes core source,
REPORT.md, manifest.json, compact CSV summaries, or explicitly named reference files.
"""
from __future__ import annotations

import sys
from pathlib import Path

DISPOSABLE_NAMES = {
    ".DS_Store",
}

DISPOSABLE_SUFFIXES = {
    ".raw",
    ".log",
    ".tmp",
    ".bak",
    ".swp",
    ".pyc",
}

DISPOSABLE_DIRS = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "tmp",
    "temp",
    "cache",
}

PRESERVE_NAMES = {
    "REPORT.md",
    "manifest.json",
    "README.md",
}


def remove_tree(path: Path) -> int:
    removed = 0
    for child in sorted(path.rglob("*"), reverse=True):
        if child.is_file() or child.is_symlink():
            child.unlink(missing_ok=True)
            removed += 1
        elif child.is_dir():
            try:
                child.rmdir()
            except OSError:
                pass
    try:
        path.rmdir()
    except OSError:
        pass
    return removed


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: cleanup_experiment.py experiments/<id>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.exists() or not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    removed = 0
    for path in sorted(root.rglob("*"), reverse=True):
        if not path.exists():
            continue
        if path.name in PRESERVE_NAMES:
            continue
        if path.is_dir() and path.name in DISPOSABLE_DIRS:
            removed += remove_tree(path)
            continue
        if path.is_file() and (path.name in DISPOSABLE_NAMES or path.suffix.lower() in DISPOSABLE_SUFFIXES):
            path.unlink()
            removed += 1

    print(f"cleanup complete: removed {removed} disposable entries from {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
