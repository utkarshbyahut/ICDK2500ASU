import tempfile
import unittest
from pathlib import Path

from src.report_generator import load_result_entries, render_markdown, summarize_models


class ReportGeneratorTests(unittest.TestCase):
    def test_summarize_models_includes_accuracy_weighting(self) -> None:
        entries = [
            {
                "model": "Model A",
                "test_case": "case-template-1",
                "ttft_seconds": 0.8,
                "tokens_per_second": 40.0,
                "resource_summary": {"max_ram_gib": 2.0},
                "validation": {"passed": True},
            },
            {
                "model": "Model B",
                "test_case": "case-2",
                "ttft_seconds": 1.2,
                "tokens_per_second": 20.0,
                "resource_summary": {"max_ram_gib": 3.0},
                "validation": {"passed": False},
            },
        ]
        summaries = summarize_models(entries)
        self.assertEqual(summaries[0]["Model"], "Model A")
        self.assertGreater(summaries[0]["Overall Score"], summaries[1]["Overall Score"])
        self.assertEqual(summaries[0]["Passes"], "1/1")
        self.assertEqual(summaries[1]["Passes"], "0/1")
        self.assertIn("Overfit Pass %", summaries[0])

    def test_load_and_render_report_from_results_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            results_path = Path(tmpdir) / "sample.json"
            results_path.write_text(
                '{"results": [{"model": "Model A", "test_case": "case-1", "ttft_seconds": 0.9, "tokens_per_second": 30.0, "resource_summary": {"max_ram_gib": 2.2, "avg_cpu_percent": 28.0}, "validation": {"status": "passed", "passed": true}}]}',
                encoding="utf-8",
            )
            entries = load_result_entries(Path(tmpdir))
            report = render_markdown(entries)
        self.assertIn("# Benchmark Report", report)
        self.assertIn("Core Assumptions and PM Cues", report)
        self.assertIn("Model Ranking", report)
        self.assertIn("Model A", report)
        self.assertIn("Passes", report)
        self.assertIn("Overfit Pass %", report)


if __name__ == "__main__":
    unittest.main()
