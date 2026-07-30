import copy
import hashlib
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "verify_evidence_receipt.py"
spec = importlib.util.spec_from_file_location("verify_evidence_receipt", MODULE_PATH)
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = verify
spec.loader.exec_module(verify)


class EvidenceReceiptTests(unittest.TestCase):
    def setUp(self):
        self.surface_bytes = b"version: 2\n"
        self.surface = {
            "version": 2,
            "repos": [{
                "name": "example",
                "commit_sha": "a" * 40,
                "release_ref": None,
                "replay_status": "NOT_RUN",
            }],
        }
        self.receipt = {
            "schema_version": 1,
            "verified_at_utc": "2026-07-30T07:55:00+00:00",
            "surface_version": 2,
            "surface_sha256": hashlib.sha256(self.surface_bytes).hexdigest(),
            "entries": [{
                "repository": "example",
                "commit_sha": "a" * 40,
                "release_ref": None,
                "repository_resolves": True,
                "proof_path_resolves": True,
                "receipt_path_resolves": True,
                "replay_status": "NOT_RUN",
            }],
            "claim_limit": "Structural consistency only.",
        }
        self.receipt["receipt_hash"] = verify.compute_receipt_hash(self.receipt)

    def test_valid_receipt_passes(self):
        verify.validate_receipt(
            self.surface, self.surface_bytes, self.receipt
        )

    def test_surface_tamper_fails(self):
        with self.assertRaisesRegex(verify.EvidenceReceiptError, "surface SHA"):
            verify.validate_receipt(
                self.surface, b"version: 3\n", self.receipt
            )

    def test_receipt_tamper_fails(self):
        broken = copy.deepcopy(self.receipt)
        broken["claim_limit"] = "Changed after hashing."
        with self.assertRaisesRegex(verify.EvidenceReceiptError, "receipt hash"):
            verify.validate_receipt(
                self.surface, self.surface_bytes, broken
            )

    def test_entry_mismatch_fails(self):
        broken = copy.deepcopy(self.receipt)
        broken["entries"][0]["commit_sha"] = "b" * 40
        broken["receipt_hash"] = verify.compute_receipt_hash(broken)
        with self.assertRaisesRegex(verify.EvidenceReceiptError, "commit_sha"):
            verify.validate_receipt(
                self.surface, self.surface_bytes, broken
            )


if __name__ == "__main__":
    unittest.main()
