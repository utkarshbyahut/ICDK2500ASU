from __future__ import annotations

import argparse
import os
import json
import re
import shlex
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import requests

try:
    from src.metrics_collector import MetricsCollector, MemoryThresholdExceeded
except ModuleNotFoundError:  # pragma: no cover
    from metrics_collector import MetricsCollector, MemoryThresholdExceeded


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def estimate_token_count(text: str) -> int:
    return max(len(text.split()), 1) if text.strip() else 0


def extract_code_for_validation(output_text: str, file_extension: str) -> str:
    if file_extension != ".py":
        return output_text

    # Prefer fenced python blocks when the model wraps output in markdown.
    fenced = re.findall(r"```(?:python|py)?\s*(.*?)```", output_text, flags=re.IGNORECASE | re.DOTALL)
    if fenced:
        return "\n\n".join(block.strip() for block in fenced if block.strip()) or output_text

    # If no fences are present, strip leading prose by finding first python-like line.
    lines = output_text.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith(("import ", "from ", "def ", "class ", "if __name__", "#")):
            return "\n".join(lines[index:]).strip() or output_text

    return output_text


def validate_generated_code(output_text: str, test_case: Dict[str, Any]) -> Dict[str, Any]:
    command_template = test_case.get("validation_command")
    if not command_template:
        return {"status": "not_configured", "passed": None, "details": "No validation command configured."}

    suffix = test_case.get("file_extension", ".txt")
    candidate_text = extract_code_for_validation(output_text, suffix)
    with tempfile.NamedTemporaryFile("w", suffix=suffix, delete=False, encoding="utf-8") as handle:
        handle.write(candidate_text)
        file_path = handle.name

    command = shlex.split(command_template.format(file_path=file_path), posix=os.name != "nt")
    try:
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
    except FileNotFoundError as exc:
        return {"status": "tool_missing", "passed": None, "details": str(exc), "command": command}

    passed = completed.returncode == 0
    details = (completed.stdout or completed.stderr or "Validation completed without output.").strip()
    return {
        "status": "passed" if passed else "failed",
        "passed": passed,
        "details": details,
        "command": command,
        "returncode": completed.returncode,
    }


def run_generation(
    session: requests.Session,
    base_url: str,
    model: Dict[str, Any],
    test_case: Dict[str, Any],
) -> Dict[str, Any]:
    started = time.perf_counter()
    ttft_seconds: Optional[float] = None
    output_chunks: List[str] = []
    final_payload: Dict[str, Any] = {}

    payload = {
        "model": model["ollama_tag"],
        "prompt": test_case["prompt"],
        "stream": True,
        "options": model.get("parameters", {}),
    }

    with MetricsCollector() as collector:
        response = session.post(
            f"{base_url.rstrip('/')}/api/generate",
            json=payload,
            stream=True,
            timeout=(10, 600),
        )
        response.raise_for_status()

        try:
            for raw_line in response.iter_lines():
                if collector.threshold_exceeded:
                    response.close()
                    collector.raise_if_threshold_exceeded()
                if not raw_line:
                    continue
                message = json.loads(raw_line.decode("utf-8"))
                token = message.get("response", "")
                if token and ttft_seconds is None:
                    ttft_seconds = time.perf_counter() - started
                if token:
                    output_chunks.append(token)
                if message.get("done"):
                    final_payload = message
        finally:
            response.close()

        collector.raise_if_threshold_exceeded()
        resource_summary = collector.summarize()
        samples = collector.serialize_samples()

    generated_text = "".join(output_chunks)
    eval_count = final_payload.get("eval_count") or estimate_token_count(generated_text)
    eval_duration_ns = final_payload.get("eval_duration") or 0
    tokens_per_second = round(eval_count / (eval_duration_ns / 1_000_000_000), 3) if eval_duration_ns else 0.0
    validation = validate_generated_code(generated_text, test_case)

    return {
        "model": model["name"],
        "ollama_tag": model["ollama_tag"],
        "test_case": test_case["id"],
        "scenario": test_case.get("scenario"),
        "skill_focus": test_case.get("skill_focus"),
        "language": test_case.get("language"),
        "prompt": test_case["prompt"],
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "ttft_seconds": round(ttft_seconds or 0.0, 3),
        "tokens_per_second": tokens_per_second,
        "generated_tokens": eval_count,
        "resource_summary": resource_summary,
        "validation": validation,
        "response_metadata": {
            "total_duration_ns": final_payload.get("total_duration"),
            "load_duration_ns": final_payload.get("load_duration"),
            "prompt_eval_count": final_payload.get("prompt_eval_count"),
            "prompt_eval_duration_ns": final_payload.get("prompt_eval_duration"),
        },
        "samples": samples,
        "output": generated_text,
    }


def benchmark(models: Iterable[Dict[str, Any]], test_cases: Iterable[Dict[str, Any]], base_url: str) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    session = requests.Session()
    for model in models:
        for test_case in test_cases:
            try:
                results.append(run_generation(session, base_url, model, test_case))
            except MemoryThresholdExceeded as exc:
                results.append(
                    {
                        "model": model["name"],
                        "ollama_tag": model["ollama_tag"],
                        "test_case": test_case["id"],
                        "scenario": test_case.get("scenario"),
                        "skill_focus": test_case.get("skill_focus"),
                        "language": test_case.get("language"),
                        "prompt": test_case["prompt"],
                        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                        "status": "aborted_memory_threshold",
                        "error": str(exc),
                    }
                )
            except requests.RequestException as exc:
                results.append(
                    {
                        "model": model["name"],
                        "ollama_tag": model["ollama_tag"],
                        "test_case": test_case["id"],
                        "scenario": test_case.get("scenario"),
                        "skill_focus": test_case.get("skill_focus"),
                        "language": test_case.get("language"),
                        "prompt": test_case["prompt"],
                        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                        "status": "request_failed",
                        "error": str(exc),
                    }
                )
    return results


def write_results(results: List[Dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results": results,
    }
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Benchmark locally served Ollama code models.")
    parser.add_argument("--models", type=Path, default=repo_root / "config" / "models.json")
    parser.add_argument("--test-cases", type=Path, default=repo_root / "config" / "test_cases.json")
    parser.add_argument("--results", type=Path, default=repo_root / "results" / "benchmark_results.json")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    models = load_json(args.models)
    test_cases = load_json(args.test_cases)
    results = benchmark(models, test_cases, args.ollama_url)
    write_results(results, args.results)
    print(f"Saved benchmark results to {args.results}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
