#!/usr/bin/env python3
"""Insert or replace a marked section in a text file without touching the rest."""

from __future__ import annotations

import argparse
from pathlib import Path


def upsert(path: Path, begin: str, end: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    section = f"{begin}\n{body.rstrip()}\n{end}\n"
    if path.exists():
        text = path.read_text(encoding="utf-8")
    else:
        text = ""

    if begin in text and end in text:
        pre, rest = text.split(begin, 1)
        _, post = rest.split(end, 1)
        # drop a single leading newline from post if present
        if post.startswith("\n"):
            post = post[1:]
        new_text = pre.rstrip() + "\n\n" + section + ("\n" + post.lstrip("\n") if post.strip() else "")
        if not new_text.endswith("\n"):
            new_text += "\n"
        path.write_text(new_text, encoding="utf-8")
        return

    if text and not text.endswith("\n"):
        text += "\n"
    if text:
        text += "\n"
    path.write_text(text + section, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--begin", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--body-file", type=Path, required=True)
    args = parser.parse_args()
    upsert(args.path, args.begin, args.end, args.body_file.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
