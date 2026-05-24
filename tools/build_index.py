#!/usr/bin/env python3
"""
Build the inspection-surface index from surface.yaml.

Outputs:
  - index.json           : machine-readable index
  - README.md (table)    : human-readable index, between markers

No claims are added here. This script only reflects surface.yaml.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from datetime import datetime, timezone

import yaml  # PyYAML

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "surface.yaml"
OUT_JSON = ROOT / "index.json"
README = ROOT / "README.md"
OWNER = "LalaSkye"

START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"


def load_surface() -> dict:
    with SRC.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def build_index(surface: dict) -> dict:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = []
    for repo in surface["repos"]:
        rows.append({
            "repo": repo["name"],
            "url": f"https://github.com/{OWNER}/{repo['name']}",
            "bounded_claim": " ".join(repo["bounded_claim"].split()),
            "proof_path": repo["proof_path"],
            "test_command": repo["test_command"],
            "release_tag": repo["release_tag"],
            "receipt_shape": repo["receipt_shape"],
        })
    return {
        "schema_version": surface.get("version", 1),
        "generated_at": now,
        "owner": OWNER,
        "rows": rows,
    }


def render_table(index: dict) -> str:
    header = (
        "| Repo | Bounded claim | Proof path | Test command | Tag | Receipt |\n"
        "|------|---------------|------------|--------------|-----|---------|"
    )
    lines = [header]
    for r in index["rows"]:
        lines.append(
            f"| [{r['repo']}]({r['url']}) "
            f"| {r['bounded_claim']} "
            f"| `{r['proof_path']}` "
            f"| `{r['test_command']}` "
            f"| `{r['release_tag']}` "
            f"| `{r['receipt_shape']}` |"
        )
    footer = f"\n\n_Generated {index['generated_at']} from `surface.yaml`._"
    return "\n".join(lines) + footer


def splice_readme(table_md: str) -> None:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(
            f"README.md must contain markers {START} and {END} "
            "where the index table will be written."
        )
    new = re.sub(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        f"{START}\n{table_md}\n{END}",
        text,
        flags=re.DOTALL,
    )
    README.write_text(new, encoding="utf-8")


def main() -> int:
    surface = load_surface()
    index = build_index(surface)
    OUT_JSON.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    splice_readme(render_table(index))
    print(f"wrote {OUT_JSON.relative_to(ROOT)} and updated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
