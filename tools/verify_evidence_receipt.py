#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SURFACE = ROOT / "surface.yaml"


class EvidenceReceiptError(ValueError):
    pass


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def compute_receipt_hash(receipt: dict[str, Any]) -> str:
    payload = dict(receipt)
    payload.pop("receipt_hash", None)
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def _require_utc(value: object, field: str) -> None:
    if not isinstance(value, str):
        raise EvidenceReceiptError(f"{field} must be a string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EvidenceReceiptError(f"{field} must be ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise EvidenceReceiptError(f"{field} must use UTC")


def validate_receipt(
    surface: dict[str, Any],
    surface_bytes: bytes,
    receipt: dict[str, Any],
) -> None:
    if receipt.get("schema_version") != 1:
        raise EvidenceReceiptError("unsupported receipt schema_version")
    if receipt.get("surface_version") != surface.get("version"):
        raise EvidenceReceiptError("surface version mismatch")
    _require_utc(receipt.get("verified_at_utc"), "verified_at_utc")

    expected_surface_hash = hashlib.sha256(surface_bytes).hexdigest()
    if receipt.get("surface_sha256") != expected_surface_hash:
        raise EvidenceReceiptError("surface SHA-256 mismatch")
    if receipt.get("receipt_hash") != compute_receipt_hash(receipt):
        raise EvidenceReceiptError("receipt hash mismatch")

    receipt_entries = receipt.get("entries")
    if not isinstance(receipt_entries, list):
        raise EvidenceReceiptError("entries must be a list")
    by_name = {entry.get("repository"): entry for entry in receipt_entries}
    if len(by_name) != len(receipt_entries):
        raise EvidenceReceiptError("duplicate receipt repository")

    surface_repos = surface.get("repos")
    if not isinstance(surface_repos, list) or set(by_name) != {
        repo.get("name") for repo in surface_repos
    }:
        raise EvidenceReceiptError("receipt repositories do not match surface")

    for repo in surface_repos:
        entry = by_name[repo["name"]]
        for field in (
            "repository_resolves",
            "proof_path_resolves",
            "receipt_path_resolves",
        ):
            if not isinstance(entry.get(field), bool):
                raise EvidenceReceiptError(
                    f"{repo['name']}.{field} must be boolean"
                )
        for field in ("commit_sha", "release_ref", "replay_status"):
            if entry.get(field) != repo.get(field):
                raise EvidenceReceiptError(
                    f"{repo['name']}.{field} does not match surface"
                )

    claim_limit = receipt.get("claim_limit")
    if not isinstance(claim_limit, str) or not claim_limit:
        raise EvidenceReceiptError("claim_limit must be non-empty")


def load_inputs(receipt_path: Path) -> tuple[dict[str, Any], bytes, dict[str, Any]]:
    surface_bytes = SURFACE.read_bytes()
    surface = yaml.safe_load(surface_bytes)
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if not isinstance(surface, dict) or not isinstance(receipt, dict):
        raise EvidenceReceiptError("surface and receipt roots must be objects")
    return surface, surface_bytes, receipt


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: verify_evidence_receipt.py RECEIPT.json", file=sys.stderr)
        return 2
    try:
        surface, surface_bytes, receipt = load_inputs(Path(argv[1]))
        validate_receipt(surface, surface_bytes, receipt)
    except (EvidenceReceiptError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: evidence receipt is structurally consistent with surface.yaml")
    print("BOUNDARY: downstream claims and replay commands are not proven")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
