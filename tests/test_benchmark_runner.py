import tempfile
import unittest
from pathlib import Path

from src.benchmark_runner import extract_code_for_validation, estimate_token_count, validate_generated_code, write_results


class BenchmarkRunnerTests(unittest.TestCase):
    def test_estimate_token_count_handles_blank_text(self) -> None:
        self.assertEqual(estimate_token_count(""), 0)
        self.assertEqual(estimate_token_count("move forward now"), 3)

    def test_validate_generated_code_passes_for_valid_python(self) -> None:
        output_text = "def drive_forward(speed, seconds):\n    return f'forward:{speed}:{seconds}'\n"
        test_case = {"file_extension": ".py", "validation_command": "python -m py_compile {file_path}"}

        result = validate_generated_code(output_text, test_case)

        self.assertEqual(result["status"], "passed")
        self.assertTrue(result["passed"])

    def test_extract_code_for_validation_prefers_python_fence(self) -> None:
        output_text = "Here is the function:\n```python\ndef drive_forward(speed, seconds):\n    return speed * seconds\n```"

        extracted = extract_code_for_validation(output_text, ".py")

        self.assertIn("def drive_forward", extracted)
        self.assertNotIn("Here is the function", extracted)

    def test_extract_code_for_validation_strips_leading_prose(self) -> None:
        output_text = "This should help your robot.\nUse the function below.\ndef turn_left(angle):\n    return angle\n"

        extracted = extract_code_for_validation(output_text, ".py")

        self.assertTrue(extracted.startswith("def turn_left"))
        self.assertNotIn("This should help", extracted)

    def test_validate_generated_code_fails_for_invalid_python(self) -> None:
        output_text = "def drive_forward(:\n    pass\n"
        test_case = {"file_extension": ".py", "validation_command": "python -m py_compile {file_path}"}

        result = validate_generated_code(output_text, test_case)

        self.assertEqual(result["status"], "failed")
        self.assertFalse(result["passed"])

    def test_write_results_persists_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "nested" / "results.json"
            write_results([{"model": "Model A", "test_case": "pololu-drive-forward"}], output_path)

            content = output_path.read_text(encoding="utf-8")

        self.assertIn("generated_at", content)
        self.assertIn("pololu-drive-forward", content)


if __name__ == "__main__":
    unittest.main()