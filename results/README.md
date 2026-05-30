# Decision Summary

## Latest Benchmark Status

| Item | Result |
|---|---:|
| Repository unit tests | 12 passed / 12 total |
| Live benchmark runs completed | 4 |
| Exploratory model set size | 5 models |
| Task set size | 6 Pololu robot-kit tasks |
| Exploratory outcomes | 30 |

## Rerun Log (2026-05-30)

| Item | Value |
|---|---|
| Rerun result file | results/benchmark_results_targeted_tiny_rerun_20260530.json |
| Command | `python -m src.benchmark_runner --models config/models_targeted_tiny.json --test-cases config/test_cases_targeted_tiny.json --results results/benchmark_results_targeted_tiny_rerun_20260530.json` |
| Report refresh command | `python -m src.report_generator --results-dir results --output results/benchmark_report.md` |
| Total outcomes | 12 |
| Models in rerun | StarCoder-1B, Qwen2.5-Coder-0.5B |

## Phi/Gemma Probe Log (2026-05-30)

| Item | Value |
|---|---|
| Probe result file | results/benchmark_results_phi_gemma4_20260530.json |
| Model request | "phi-1" and "gemma 4" |
| Resolved Ollama tags | phi:latest and gemma3:4b |
| Note on phi tag | `phi:1` is not available in Ollama manifest; `phi:latest` was used. |
| Total outcomes | 12 |

### Phi/Gemma Probe Metrics

| Model | Completed Runs | Validation Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Aborts |
|---|---:|---:|---:|---:|---:|---:|
| Phi (phi:latest) | 6 | 0/6 | 2.781 | 12.483 | 6.632 | 0 |
| Gemma 4B (gemma3:4b) | 0 | 0/0 | - | - | - | 6 |

## Gemma Mobile-Line Follow-up (2026-05-30)

| Item | Value |
|---|---|
| Intended model line | Gemma 3n (mobile/on-device line often referenced for phone-class hardware) |
| Ollama probe result | `gemma3n:e2b` not found in local Ollama registry (v0.24.0) |
| Proxy benchmark model | Gemma 3 1B (`gemma3:1b`) |
| Proxy result file | results/benchmark_results_gemma3_1b_mobile_proxy_20260530.json |

### Gemma 3 1B Proxy Metrics

| Model | Completed Runs | Validation Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Aborts |
|---|---:|---:|---:|---:|---:|---:|
| Gemma 3 1B (gemma3:1b) | 6 | 0/6 | 1.343 | 23.880 | 6.170 | 0 |

## Inference Optimization Log (2026-05-30)

| Item | Value |
|---|---|
| Code change | Added per-model warm-up in benchmark runner to reduce cold-start TTFT bias |
| New runner option | `--no-warmup` to disable warm-up when needed |
| Primary optimized file | results/benchmark_results_phi_gemma_optimized_20260530.json |
| Gemma-focused optimized file | results/benchmark_results_gemma3_1b_optimized_v3_20260530.json |

### Optimization Outcomes

| Model | Baseline File | Optimized File | Completed Runs | Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Aborts |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Phi (phi:latest) | benchmark_results_phi_gemma4_20260530.json | benchmark_results_phi_gemma_optimized_20260530.json | 6 | 0/6 | 2.781 -> 1.399 | 12.483 -> 12.986 | 6.632 -> 6.384 | 0 -> 0 |
| Gemma 3 1B (gemma3:1b) | benchmark_results_gemma3_1b_mobile_proxy_20260530.json | benchmark_results_gemma3_1b_optimized_v3_20260530.json | 6 | 0/6 | 1.343 -> 1.082 | 23.880 -> 27.592 | 6.170 -> 5.677 | 0 -> 0 |

### Notes

1. A stricter v2 config caused full memory-threshold aborts and was discarded.
2. Best Gemma result used isolated single-model execution plus tighter generation limits.

## Use-Case Cleanup + Fastlane Pass (2026-05-30)

| Item | Value |
|---|---|
| Goal | Remove redundant/non-essential tasks and run a fresh consolidated pass |
| Kept task set | `config/test_cases_usecase_essential3.json` |
| Removed from this pass | duplicate prompt variants and lower-value overlap tasks |
| Model set used | `config/models_all_usecase_fastlane.json` |
| Result file | results/benchmark_results_all_usecase_fastlane_20260530.json |
| Total outcomes | 15 |

### Essential3 Fastlane Metrics

| Model | Completed Runs | Validation Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Aborts |
|---|---:|---:|---:|---:|---:|---:|
| StarCoder-1B Fastlane | 3 | 3/3 | 1.005 | 29.371 | 5.814 | 0 |
| Qwen2.5-Coder-0.5B Fastlane | 3 | 1/3 | 0.603 | 60.377 | 5.131 | 0 |
| TinyLlama-1.1B Fastlane | 3 | 0/3 | 1.242 | 34.803 | 5.868 | 0 |
| Gemma3-1B Fastlane | 3 | 0/3 | 1.605 | 22.015 | 6.449 | 0 |
| Phi Fastlane | 3 | 0/3 | 2.806 | 11.713 | 6.597 | 0 |

### Rerun Metrics

| Model | Completed Runs | Validation Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Aborts |
|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-Coder-0.5B | 6 | 4/6 | 1.030 | 49.097 | 5.986 | 0 |
| StarCoder-1B | 6 | 1/6 | 1.726 | 30.114 | 5.613 | 0 |

### Rerun Interpretation

1. Qwen2.5-Coder-0.5B remained strong and repeated a high pass-rate result (4/6).
2. StarCoder-1B performance regressed relative to the prior targeted run (from 2/6 to 1/6).
3. The rerun supports selecting Qwen2.5-Coder-0.5B as the default workshop model under this strict-template regime.

## Targeted Tiny Results (Strict Template Prompts)

| Model | Completed Runs | Validation Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Notes |
|---|---:|---:|---:|---:|---:|---|
| Qwen2.5-Coder-0.5B | 6 | 4/6 | 1.006 | 50.198 | 6.008 | Best current balance for meaningful suggestions under strict function-template prompting. |
| StarCoder-1B | 6 | 2/6 | 1.200 | 29.923 | 5.655 | Solid fallback with better syntax pass-rate than earlier sweeps. |

## Tiny-Focus Results (Newest Run)

| Model | Completed Runs | Validation Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Notes |
|---|---:|---:|---:|---:|---:|---|
| StarCoder-1B | 6 | 1/6 | 0.920 | 26.363 | 5.460 | Best tiny-model balance of speed and meaningful syntax-valid output. |
| Qwen2.5-Coder-0.5B | 6 | 0/6 | 0.985 | 49.088 | 4.765 | Fastest and lowest RAM, but no syntax-valid suggestions in this run. |
| TinyLlama-1.1B | 6 | 0/6 | 1.147 | 28.947 | 6.049 | Good speed, but no syntax-valid suggestions. |
| Qwen2.5-Coder-1.5B | 2 | 0/2 | 0.863 | 19.396 | 6.716 | 4/6 memory-threshold aborts under this tiny-focus setup. |
| DeepSeek-Coder-1.3B | 0 | 0/0 | - | - | - | 6/6 memory-threshold aborts in this run. |

## Exploratory Results (Fast Sweep)

| Model | Completed Runs | Validation Passes | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Notes |
|---|---:|---:|---:|---:|---:|---|
| Qwen2.5-Coder-0.5B | 6 | 0/6 | 1.157 | 46.327 | 5.106 | Fastest model by a large margin, but no syntax-valid outputs. |
| DeepSeek-Coder-1.3B | 6 | 0/6 | 1.595 | 21.917 | 5.377 | Stable and memory-safe, but still no passing outputs. |
| Qwen2.5-Coder-1.5B | 6 | 0/6 | 1.824 | 22.183 | 5.438 | Similar profile to DeepSeek with no validation wins. |
| CodeGemma-2B | 6 | 1/6 | 2.088 | 12.785 | 6.745 | First model to produce at least one syntax-valid answer in this workload. |
| Stable-Code-3B | 1 | 0/1 | 1.742 | 10.398 | 6.766 | 5/6 cases aborted on memory threshold; poor fit for this machine. |

## What Changed in This Rerun

1. Added fenced-code extraction before validation, so markdown-wrapped code is checked more fairly.
2. Added smaller coding models to broaden exploration beyond the original three-model set.
3. Reduced generation length for faster iteration under 8GB memory constraints.

## Recommendation Matrix

| Priority | Recommendation | Why |
|---:|---|---|
| 1 | Use Qwen2.5-Coder-0.5B as the primary tiny-model candidate | In two targeted strict-template runs, it repeatedly produced the highest pass-rate result (4/6) with excellent latency. |
| 2 | Keep StarCoder-1B as the fallback tiny model | It still produces some valid outputs (1/6 in rerun) and maintains manageable memory usage. |
| 3 | Keep CodeGemma-2B as a secondary quality candidate | It also produced syntax-valid output in the earlier exploratory run, though slower and heavier than StarCoder-1B. |
| 4 | De-prioritize DeepSeek-Coder-1.3B and Qwen2.5-Coder-1.5B for this exact profile | They showed memory-threshold abort behavior in the tiny-focus run. |
| 5 | Continue prompt and output-shape tuning | Correctness (pass-rate) remains the main limiting factor for classroom usefulness. |

## Evidence Files

1. Main run results: results/benchmark_results.json
2. Exploratory run results: results/benchmark_results_exploratory_fast.json
3. Tiny-focus run results: results/benchmark_results_tiny_focus.json
4. Targeted strict-template run results: results/benchmark_results_targeted_tiny.json
5. Targeted strict-template rerun results: results/benchmark_results_targeted_tiny_rerun_20260530.json
6. Aggregated report: results/benchmark_report.md
