import hashlib
import json
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS_INDEX = ROOT / "docs" / "index.md"
SURFACE = ROOT / "surface.yaml"
INDEX = ROOT / "index.json"
RECEIPT_DOC = ROOT / "RECEIPT.md"
HISTORICAL_RECEIPT = ROOT / "receipts" / "verification-2026-08-30.json"
WORKFLOW = ROOT / ".github" / "workflows" / "index.yml"

HISTORICAL_RECEIPT_SHA256 = (
    "3cd04aefb973c002ed0d09e113ce750cc97d9d698cc0ff5879463d11f4c8ffdd"
)

STOP_MACHINE_URL = "https://github.com/LalaSkye/stop-machine"
START_HERE_URL = "https://github.com/LalaSkye/start-here"


class EntryRoutingTests(unittest.TestCase):
    def test_readme_primary_entry_points_to_stop_machine(self):
        text = README.read_text(encoding="utf-8")
        self.assertIn(
            f"**Primary entry point:** [stop-machine]({STOP_MACHINE_URL})",
            text,
        )
        self.assertNotIn(
            f"**Primary entry point:** [start-here]({START_HERE_URL})",
            text,
        )

    def test_docs_begin_here_points_to_stop_machine(self):
        text = DOCS_INDEX.read_text(encoding="utf-8")
        self.assertIn(
            f"**Begin here:** [LalaSkye/stop-machine]({STOP_MACHINE_URL})",
            text,
        )
        self.assertNotIn(
            f"**Begin here:** [LalaSkye/start-here]({START_HERE_URL})",
            text,
        )

    def test_start_here_is_marked_historical(self):
        for path in (README, DOCS_INDEX):
            text = path.read_text(encoding="utf-8")
            self.assertIn("superseded by `stop-machine`", text)
            self.assertIn("not the current entry point", text)
        self.assertIn(
            "does not transfer to `stop-machine`",
            DOCS_INDEX.read_text(encoding="utf-8"),
        )

    def test_surface_commentary_matches_route(self):
        text = SURFACE.read_text(encoding="utf-8")
        self.assertIn("`stop-machine` is the canonical public entry route", text)
        self.assertNotIn("Only the three current public inspection objects", text)

    def test_historical_receipt_is_unchanged(self):
        digest = hashlib.sha256(HISTORICAL_RECEIPT.read_bytes()).hexdigest()
        self.assertEqual(digest, HISTORICAL_RECEIPT_SHA256)

    def test_current_receipt_is_fresh_and_binds_surface(self):
        index = json.loads(INDEX.read_text(encoding="utf-8"))
        receipt_path = ROOT / index["verification_receipt"]
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        self.assertEqual(
            receipt["surface_sha256"],
            hashlib.sha256(SURFACE.read_bytes()).hexdigest(),
        )
        self.assertEqual(receipt["verified_at_utc"], index["generated_at"])
        self.assertEqual(
            {repo["verified_at_utc"] for repo in index["rows"]},
            {receipt["verified_at_utc"]},
        )
        observed_at = datetime.fromisoformat(receipt["verified_at_utc"])
        self.assertLessEqual(observed_at, datetime.now(timezone.utc))
        self.assertNotIn(
            "stop-machine",
            {entry["repository"] for entry in receipt["entries"]},
        )
        self.assertIn("historical evidence identity", receipt["claim_limit"])
        self.assertIn("Evidence does not transfer", receipt["claim_limit"])

    def test_workflow_follows_surface_receipt_pointer(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('["verification_receipt"]', text)
        self.assertNotIn(
            "verify_evidence_receipt.py receipts/verification-2026-08-30.json",
            text,
        )

    def test_receipt_document_preserves_claim_ceiling(self):
        text = RECEIPT_DOC.read_text(encoding="utf-8")
        self.assertIn("verification-2026-09-03.json", text)
        self.assertIn("historical evidence identities", text)
        self.assertIn("does not transfer to `stop-machine`", text)


if __name__ == "__main__":
    unittest.main()
