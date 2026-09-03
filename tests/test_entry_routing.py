import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS_INDEX = ROOT / "docs" / "index.md"
SURFACE = ROOT / "surface.yaml"

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


if __name__ == "__main__":
    unittest.main()
