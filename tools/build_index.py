#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "surface.yaml"
OUT_JSON = ROOT / "index.json"
README = ROOT / "README.md"
OWNER = "LalaSkye"

START = "<!-- INDEX:START -->"
END = "<!-- INDEX:END -->"
REQUIRED_REPO_FIELDS = {
    "name",
    "bounded_claim",
    "proof_path",
    "test_command",
    "release_tag",
    "receipt_shape",
}


def load_surface() -> dict:
    with SRC.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def build_index(surface: dict) -> dict:
    generated_at = surface.get("generated_at")
    if not isinstance(generated_at, str) or not generated_at:
        raise ValueError("surface.generated_at must be a non-empty string")

    repos = surface.get("repos")
    if not isinstance(repos, list):
        raise ValueError("surface.repos must be a list")

    rows = []
    seen_names = set()
    for position, repo in enumerate(repos):
        if not isinstance(repo, dict):
            raise ValueError(f"surface.repos[{position}] must be an object")
        missing = REQUIRED_REPO_FIELDS - set(repo)
        if missing:
            raise ValueError(
                f"surface.repos[{position}] missing fields: {sorted(missing)}"
            )
        name = repo["name"]
        if not isinstance(name, str) or not name:
            raise ValueError(f"surface.repos[{position}].name must be non-empty")
        if name in seen_names:
            raise ValueError(f"duplicate repository name: {name}")
        seen_names.add(name)
        rows.append({
            "repo": name,
            "url": f"https://github.com/{OWNER}/{name}",
            "bounded_claim": " ".join(repo["bounded_claim"].split()),
            "proof_path": repo["proof_path"],
            "test_command": repo["test_command"],
            "release_tag": repo["release_tag"],
            "receipt_shape": repo["receipt_shape"],
        })
    return {
        "schema_version": surface.get("version", 1),
        "generated_at": generated_at,
        "owner": OWNER,
        "rows": rows,
    }


def render_table(index: dict) -> str:
    header = (
        "| Repo | Bounded claim | Proof path | Test command | Tag | Receipt |\n"
        "|------|---------------|------------|--------------|-----|---------|"
    )
    lines = [header]
    for row in index["rows"]:
        lines.append(
            f"| [{row['repo']}]({row['url']}) "
            f"| {row['bounded_claim']} "
            f"| `{row['proof_path']}` "
            f"| `{row['test_command']}` "
            f"| `{row['release_tag']}` "
            f"| `{row['receipt_shape']}` |"
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

