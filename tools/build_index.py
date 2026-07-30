#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
import sys
from datetime import datetime, timezone

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
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
    "receipt_shape",
    "lifecycle_status",
    "evidence_status",
    "release_ref",
    "commit_sha",
    "verified_at_utc",
    "replay_status",
}
LIFECYCLE_STATUSES = {"UNRELEASED", "RELEASED"}
EVIDENCE_STATUSES = {
    "UNRELEASED",
    "REF_RESOLVES",
    "PATHS_RESOLVE",
    "REPLAY_VERIFIED",
    "REPLAY_FAILED",
    "STALE",
    "INVALID",
}
REPLAY_STATUSES = {"NOT_RUN", "PASSED", "FAILED"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def load_surface() -> dict:
    with SRC.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _validate_utc(value: object, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field} must be a non-empty string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field} must be a valid ISO-8601 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise ValueError(f"{field} must use UTC")
    return value


def build_index(surface: dict) -> dict:
    generated_at = _validate_utc(surface.get("generated_at"), "surface.generated_at")
    verification_receipt = surface.get("verification_receipt")
    if not isinstance(verification_receipt, str) or not verification_receipt:
        raise ValueError("surface.verification_receipt must be a non-empty string")

    repos = surface.get("repos")
    if not isinstance(repos, list):
        raise ValueError("surface.repos must be a list")

    rows = []
    seen_names = set()
    for position, repo in enumerate(repos):
        prefix = f"surface.repos[{position}]"
        if not isinstance(repo, dict):
            raise ValueError(f"{prefix} must be an object")
        missing = REQUIRED_REPO_FIELDS - set(repo)
        if missing:
            raise ValueError(f"{prefix} missing fields: {sorted(missing)}")
        name = repo["name"]
        if not isinstance(name, str) or not name:
            raise ValueError(f"{prefix}.name must be non-empty")
        if name in seen_names:
            raise ValueError(f"duplicate repository name: {name}")
        seen_names.add(name)

        lifecycle = repo["lifecycle_status"]
        evidence = repo["evidence_status"]
        replay = repo["replay_status"]
        release_ref = repo["release_ref"]
        commit_sha = repo["commit_sha"]
        if lifecycle not in LIFECYCLE_STATUSES:
            raise ValueError(f"{prefix}.lifecycle_status is invalid")
        if evidence not in EVIDENCE_STATUSES:
            raise ValueError(f"{prefix}.evidence_status is invalid")
        if replay not in REPLAY_STATUSES:
            raise ValueError(f"{prefix}.replay_status is invalid")
        if not isinstance(commit_sha, str) or not SHA40.fullmatch(commit_sha):
            raise ValueError(f"{prefix}.commit_sha must be a lowercase 40-character SHA")
        if lifecycle == "RELEASED" and (
            not isinstance(release_ref, str) or not release_ref
        ):
            raise ValueError(f"{prefix}.release_ref is required when RELEASED")
        if lifecycle == "UNRELEASED" and release_ref is not None:
            raise ValueError(f"{prefix}.release_ref must be null when UNRELEASED")
        verified_at = _validate_utc(repo["verified_at_utc"], f"{prefix}.verified_at_utc")

        rows.append({
            "repo": name,
            "url": f"https://github.com/{OWNER}/{name}",
            "bounded_claim": " ".join(repo["bounded_claim"].split()),
            "lifecycle_status": lifecycle,
            "evidence_status": evidence,
            "release_ref": release_ref,
            "commit_sha": commit_sha,
            "verified_at_utc": verified_at,
            "replay_status": replay,
            "proof_path": repo["proof_path"],
            "test_command": repo["test_command"],
            "receipt_shape": repo["receipt_shape"],
        })
    return {
        "schema_version": surface.get("version", 2),
        "generated_at": generated_at,
        "verification_receipt": verification_receipt,
        "owner": OWNER,
        "rows": rows,
    }

def render_table(index: dict) -> str:
    header = (
        "| Repo | Evidence | Lifecycle | Ref | Commit | Replay | Proof | Receipt |\n"
        "|------|----------|-----------|-----|--------|--------|-------|---------|"
    )
    lines = [header]
    for row in index["rows"]:
        release_ref = row["release_ref"] or "—"
        lines.append(
            f"| [{row['repo']}]({row['url']}) "
            f"| `{row['evidence_status']}` "
            f"| `{row['lifecycle_status']}` "
            f"| `{release_ref}` "
            f"| [`{row['commit_sha'][:7]}`]({row['url']}/commit/{row['commit_sha']}) "
            f"| `{row['replay_status']}` "
            f"| `{row['proof_path']}` "
            f"| `{row['receipt_shape']}` |"
        )
    footer = (
        f"\n\n_Generated {index['generated_at']} from `surface.yaml`. "
        f"Verification receipt: [{index['verification_receipt']}]"
        f"({index['verification_receipt']})._"
    )
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

