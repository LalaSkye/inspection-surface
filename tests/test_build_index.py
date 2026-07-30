import copy
import importlib.util
import sys
import types
import unittest
from pathlib import Path

sys.modules.setdefault("yaml", types.SimpleNamespace(safe_load=lambda _: None))

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "build_index.py"
spec = importlib.util.spec_from_file_location("build_index", MODULE_PATH)
build_index = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(build_index)


class BuildIndexTests(unittest.TestCase):
    def setUp(self):
        self.surface = {
            "version": 1,
            "generated_at": "2026-05-24T01:43:27+00:00",
            "repos": [{
                "name": "example",
                "bounded_claim": "A bounded\n claim.",
                "proof_path": "src/",
                "test_command": "python demo.py",
                "release_tag": "v0.1.0",
                "receipt_shape": "RECEIPT.md",
            }],
        }

    def test_same_surface_produces_same_index(self):
        first = build_index.build_index(copy.deepcopy(self.surface))
        second = build_index.build_index(copy.deepcopy(self.surface))
        self.assertEqual(first, second)

    def test_generated_at_is_source_controlled(self):
        index = build_index.build_index(self.surface)
        self.assertEqual(index["generated_at"], self.surface["generated_at"])

    def test_missing_generated_at_fails(self):
        del self.surface["generated_at"]
        with self.assertRaisesRegex(ValueError, "generated_at"):
            build_index.build_index(self.surface)

    def test_invalid_generated_at_fails(self):
        self.surface["generated_at"] = "not-a-timestamp"
        with self.assertRaisesRegex(ValueError, "ISO-8601"):
            build_index.build_index(self.surface)

    def test_naive_generated_at_fails(self):
        self.surface["generated_at"] = "2026-05-24T01:43:27"
        with self.assertRaisesRegex(ValueError, "UTC"):
            build_index.build_index(self.surface)

    def test_non_utc_generated_at_fails(self):
        self.surface["generated_at"] = "2026-05-24T02:43:27+01:00"
        with self.assertRaisesRegex(ValueError, "UTC"):
            build_index.build_index(self.surface)

    def test_duplicate_repository_fails(self):
        self.surface["repos"].append(copy.deepcopy(self.surface["repos"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            build_index.build_index(self.surface)

    def test_missing_repository_field_fails(self):
        del self.surface["repos"][0]["receipt_shape"]
        with self.assertRaisesRegex(ValueError, "missing fields"):
            build_index.build_index(self.surface)


if __name__ == "__main__":
    unittest.main()

