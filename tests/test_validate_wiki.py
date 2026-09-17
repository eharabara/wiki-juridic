import importlib.util
import unittest
from pathlib import Path


VALIDATOR_PATH = Path(__file__).resolve().parents[1] / "_meta" / "schema" / "validate_wiki.py"
SPEC = importlib.util.spec_from_file_location("validate_wiki", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)

CITATION_RULES = {
    "raw_page_locator_required_roots": [
        "raw/papers/cnpf/",
        "raw/papers/moldova-legal/",
        "raw/papers/bnm/",
    ]
}


def raw_page_level_warning_count(text):
    report = validator.Report()
    validator.check_raw_page_level_refs(
        "entities/example.md", text, report, CITATION_RULES
    )
    return len(report.items[("warn", "citation.raw-page-level")])


class RawPageCitationTests(unittest.TestCase):
    def test_source_inventory_is_not_treated_as_a_substantive_citation(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "- **surse:** [raw/papers/moldova-legal/L-100-2017.md]\n"
            ),
            0,
        )

    def test_substantive_claim_without_locator_remains_a_warning(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "Legea stabilește cadrul aplicabil. [raw/papers/moldova-legal/L-100-2017.md]\n"
            ),
            1,
        )

    def test_substantive_claim_with_locator_is_not_a_warning(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "Legea stabilește cadrul aplicabil. [raw/papers/moldova-legal/L-100-2017.md art. 1]\n"
            ),
            0,
        )

    def test_multi_digit_article_locator_is_not_a_warning(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "Legea stabilește cadrul aplicabil. "
                "[raw/papers/moldova-legal/L-100-2017.md art. 62]\n"
            ),
            0,
        )

    def test_suffixed_article_locator_is_not_a_warning(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "Legea stabilește cadrul aplicabil. "
                "[raw/papers/moldova-legal/L-100-2017.md art. 3a]\n"
            ),
            0,
        )

    def test_source_structural_locator_is_not_a_warning(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "Fișierul păstrează versiunea indicată. "
                "[raw/papers/moldova-legal/L-100-2017.md antet]\n"
            ),
            0,
        )

    def test_stable_raw_line_locator_is_not_a_warning(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "Declarația este în textul neancorat. "
                "[raw/papers/moldova-legal/L-100-2017.md l. 137]\n"
            ),
            0,
        )

    def test_policy_source_without_legal_locator_is_not_a_warning(self):
        self.assertEqual(
            raw_page_level_warning_count(
                "Documentul de politici stabilește cadrul strategic. "
                "[raw/papers/moldova-policy/HG-361-2024-pnd-2025-2027.md]\n"
            ),
            0,
        )

    def test_source_inventory_path_is_not_a_warning(self):
        rules = {
            **CITATION_RULES,
            "raw_page_locator_exempt_paths": [
                "raw/papers/bnm/BNM_LEGISLATION_INVENTORY.md"
            ],
        }
        report = validator.Report()
        validator.check_raw_page_level_refs(
            "entities/example.md",
            "Registrul grupează actele. "
            "[raw/papers/bnm/BNM_LEGISLATION_INVENTORY.md]\n",
            report,
            rules,
        )
        self.assertEqual(len(report.items[("warn", "citation.raw-page-level")]), 0)


if __name__ == "__main__":
    unittest.main()
