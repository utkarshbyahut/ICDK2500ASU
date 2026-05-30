from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List

from tabulate import tabulate


def load_result_entries(results_dir: Path) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    for path in sorted(results_dir.glob("*.json")):
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        file_entries = payload.get("results", []) if isinstance(payload, dict) else []
        for entry in file_entries:
            entry = dict(entry)
            entry["source_file"] = path.name
            entries.append(entry)
    return entries


def _normalized(values: Dict[str, float], higher_is_better: bool) -> Dict[str, float]:
    if not values:
        return {}
    minimum = min(values.values())
    maximum = max(values.values())
    if minimum == maximum:
        return {key: 100.0 for key in values}
    if higher_is_better:
        return {key: ((value - minimum) / (maximum - minimum)) * 100 for key, value in values.items()}
    return {key: ((maximum - value) / (maximum - minimum)) * 100 for key, value in values.items()}


def summarize_models(entries: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, Dict[str, Any]] = {}
    for entry in entries:
        if entry.get("status"):
            continue
        model_name = entry["model"]
        group = grouped.setdefault(
            model_name,
            {
                "model": model_name,
                "runs": 0,
                "ttft_seconds_total": 0.0,
                "tokens_per_second_total": 0.0,
                "peak_ram_gib_total": 0.0,
                "validation_passes": 0,
                "overfit_runs": 0,
                "overfit_passes": 0,
            },
        )
        group["runs"] += 1
        group["ttft_seconds_total"] += float(entry.get("ttft_seconds", 0.0))
        group["tokens_per_second_total"] += float(entry.get("tokens_per_second", 0.0))
        group["peak_ram_gib_total"] += float(entry.get("resource_summary", {}).get("max_ram_gib", 0.0))
        if entry.get("validation", {}).get("passed") is True:
            group["validation_passes"] += 1
        is_overfit_case = bool(entry.get("overfit_case")) or "template" in str(entry.get("test_case", ""))
        if is_overfit_case:
            group["overfit_runs"] += 1
            if entry.get("validation", {}).get("passed") is True:
                group["overfit_passes"] += 1

    if not grouped:
        return []

    avg_tps = {model: data["tokens_per_second_total"] / data["runs"] for model, data in grouped.items()}
    avg_ttft = {model: data["ttft_seconds_total"] / data["runs"] for model, data in grouped.items()}
    avg_ram = {model: data["peak_ram_gib_total"] / data["runs"] for model, data in grouped.items()}
    accuracy = {model: (data["validation_passes"] / data["runs"]) * 100 for model, data in grouped.items()}

    tps_score = _normalized(avg_tps, higher_is_better=True)
    ttft_score = _normalized(avg_ttft, higher_is_better=False)
    ram_score = _normalized(avg_ram, higher_is_better=False)

    summaries: List[Dict[str, Any]] = []
    for model, data in grouped.items():
        efficiency_score = round((tps_score[model] + ttft_score[model] + ram_score[model]) / 3, 2)
        accuracy_score = round(accuracy[model], 2)
        overfit_pass_percent = (
            round((data["overfit_passes"] / data["overfit_runs"]) * 100, 2) if data["overfit_runs"] else 0.0
        )
        overall_score = round((efficiency_score * 0.5) + (accuracy_score * 0.5), 2)
        summaries.append(
            {
                "Model": model,
                "Runs": data["runs"],
                "Passes": f"{data['validation_passes']}/{data['runs']}",
                "Avg TTFT (s)": round(avg_ttft[model], 3),
                "Avg Tokens/s": round(avg_tps[model], 3),
                "Avg Peak RAM (GiB)": round(avg_ram[model], 3),
                "Compilation Pass %": accuracy_score,
                "Overfit Pass %": overfit_pass_percent,
                "Efficiency Score": efficiency_score,
                "Overall Score": overall_score,
            }
        )
    return sorted(summaries, key=lambda row: row["Overall Score"], reverse=True)


def render_markdown(entries: List[Dict[str, Any]]) -> str:
    if not entries:
        return "# Benchmark Report\n\nNo benchmark result files were found."

    detail_rows = []
    for entry in entries:
        detail_rows.append(
            {
                "Model": entry.get("model"),
                "Case": entry.get("test_case"),
                "Scenario": entry.get("scenario", "-"),
                "TTFT (s)": entry.get("ttft_seconds", "-"),
                "Tokens/s": entry.get("tokens_per_second", "-"),
                "Peak RAM (GiB)": entry.get("resource_summary", {}).get("max_ram_gib", "-"),
                "CPU Avg %": entry.get("resource_summary", {}).get("avg_cpu_percent", "-"),
                "Validation": entry.get("validation", {}).get("status", entry.get("status", "-")),
                "Source": entry.get("source_file", "-"),
            }
        )

    summaries = summarize_models(entries)
    ranking_table = tabulate(summaries, headers="keys", tablefmt="github") if summaries else "No successful runs yet."
    detail_table = tabulate(detail_rows, headers="keys", tablefmt="github")
    return (
        "# Benchmark Report\n\n"
        "## Core Assumptions and PM Cues\n\n"
        "1. This report blends speed and code validity. Overall Score is weighted 50% efficiency and 50% compilation pass-rate.\n"
        "2. Compilation Pass % indicates syntax-valid Python output only; it does not guarantee classroom-ready behavior quality.\n"
        "3. Overfit Pass % is computed from template-like or explicitly overfit-tagged cases and reflects performance on narrow, constrained prompts.\n"
        "4. Runs with memory-threshold aborts are excluded from ranking averages and appear in Detailed Runs with aborted status.\n"
        "5. Compare models first by pass metrics for reliability, then by TTFT/Tokens/s/RAM for deployment fit on this hardware.\n\n"
        "## Abbreviations and Settings Glossary\n\n"
        "- TTFT: Time To First Token. Lower is better for perceived responsiveness.\n"
        "- Tokens/s (TPS): Tokens generated per second after generation starts. Higher is better for throughput.\n"
        "- Peak RAM (GiB): Highest observed RAM usage during the run. Lower is better for 8GB-class systems.\n"
        "- Compilation Pass %: Percentage of runs where generated Python passed syntax compilation.\n"
        "- Passes: Raw pass count shown as passed/total runs in the ranking table.\n"
        "- Overfit Pass %: Pass percentage on template-like or explicitly overfit-tagged cases only.\n"
        "- Efficiency Score: Normalized blend of TTFT, TPS, and Peak RAM.\n"
        "- Overall Score: 50% Efficiency Score + 50% Compilation Pass %.\n"
        "- Temperature: Sampling randomness. Lower values are more deterministic.\n"
        "- num_predict: Maximum output tokens allowed for a generation.\n"
        "- num_ctx: Model context window used for prompt + generation.\n"
        "- top_k/top_p: Token sampling filters; they constrain token choice breadth.\n"
        "- repeat_penalty: Reduces repetition by penalizing previously used tokens.\n"
        "- Warm-up: Optional pre-run model touch used to reduce cold-start latency skew.\n\n"
        "## Model Ranking\n\n"
        f"{ranking_table}\n\n"
        "## Detailed Runs\n\n"
        f"{detail_table}\n"
    )


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Generate a markdown benchmark report from JSON results.")
    parser.add_argument("--results-dir", type=Path, default=repo_root / "results")
    parser.add_argument("--output", type=Path, default=repo_root / "results" / "benchmark_report.md")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entries = load_result_entries(args.results_dir)
    report = render_markdown(entries)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"Saved markdown report to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
