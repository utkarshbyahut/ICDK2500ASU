import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


class ConfigurationFileTests(unittest.TestCase):
    def test_model_context_windows_respect_cap(self) -> None:
        models = json.loads((REPO_ROOT / "config" / "models.json").read_text(encoding="utf-8"))
        self.assertTrue(models)
        self.assertTrue(all(model["context_window"] <= 4096 for model in models))

    def test_continue_template_has_dual_model_setup(self) -> None:
        template = json.loads(
            (REPO_ROOT / "templates" / "continue_config_template.json").read_text(encoding="utf-8")
        )
        self.assertIn("tabAutocompleteModel", template)
        self.assertTrue(template["models"])
        self.assertEqual(template["tabAutocompleteModel"]["model"], "deepseek-coder:1.3b")
        self.assertEqual(template["models"][0]["model"], "qwen2.5-coder:1.5b")


if __name__ == "__main__":
    unittest.main()
