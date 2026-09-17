import datetime as dt
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "_meta" / "coverage" / "build_coverage.py"
SPEC = importlib.util.spec_from_file_location("build_coverage", MODULE_PATH)
coverage = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(coverage)

VALIDATOR_PATH = Path(__file__).resolve().parents[1] / "_meta" / "schema" / "validate_wiki.py"
VALIDATOR_SPEC = importlib.util.spec_from_file_location("validate_wiki", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(VALIDATOR_SPEC)
assert VALIDATOR_SPEC.loader is not None
VALIDATOR_SPEC.loader.exec_module(validator)


class BuildCoverageTests(unittest.TestCase):
    def test_stale_age_note_is_stable_across_display_boundaries(self):
        before_boundary = dt.date(2026, 9, 16)
        after_boundary = dt.date(2026, 10, 22)

        self.assertEqual(
            coverage.stale_age_note("2024-01-23", before_boundary),
            "**more than 2 years old**",
        )
        self.assertEqual(
            coverage.stale_age_note("2024-01-23", after_boundary),
            "**more than 2 years old**",
        )

    def test_stale_age_note_keeps_recent_dates_unflagged(self):
        self.assertIsNone(
            coverage.stale_age_note("2025-09-18", dt.date(2026, 9, 17))
        )

    def test_scan_file_recognises_abbreviated_article_anchors(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "L-TEST-2026.md"
            path.write_text(
                "---\n"
                "instrument_id: L-TEST-2026\n"
                "consolidation_date: 2026-01-01\n"
                "articole detectate: 2\n"
                "---\n\n"
                "## Art. 1. - Primul articol\n"
                "Text\n\n"
                "## Art. 2. - Al doilea articol\n"
                "Text\n",
                encoding="utf-8",
            )

            record = coverage.scan_file(path, "raw/papers/moldova-legal/L-TEST-2026.md")

        self.assertEqual(record["declared"], 2)
        self.assertEqual(record["anchors"], 2)


class TranslationScopeTests(unittest.TestCase):
    RULE = {
        "english_marker_min": 20,
        "english_marker_scope_roots": [
            "raw/papers/cnpf/",
            "raw/papers/moldova-legal/",
            "raw/papers/bnm/",
        ],
    }

    def test_english_original_outside_legal_corpus_is_not_a_translation_warning(self):
        self.assertFalse(
            validator.is_undeclared_translation(
                "legal-text",
                41,
                "raw/papers/mded-policy-2024/eu-reform-growth-facility-moldova-2024.md",
                "eu-reform-growth-facility-moldova-2024.md",
                self.RULE,
                (),
            )
        )

    def test_english_legal_text_in_bnm_scope_is_still_reported(self):
        self.assertTrue(
            validator.is_undeclared_translation(
                "legal-text",
                21,
                "raw/papers/bnm/legal/example.md",
                "example.md",
                self.RULE,
                (),
            )
        )


if __name__ == "__main__":
    unittest.main()
