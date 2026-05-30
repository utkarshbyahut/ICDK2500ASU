# Decision Summary

## Latest Benchmark Status

| Item | Result |
|---|---:|
| Repository unit tests | 12 passed / 12 total |
| Live benchmark runs completed | 2 |
| Exploratory model set size | 5 models |
| Task set size | 6 Pololu robot-kit tasks |
| Exploratory outcomes | 30 |

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
| 1 | Keep CodeGemma-2B in the candidate pool despite slower speed | It is the only model in this rerun with any syntax pass (1/6). |
| 2 | Keep Qwen2.5-Coder-0.5B as the latency baseline | It is dramatically faster and useful as a responsiveness floor for comparisons. |
| 3 | Use DeepSeek-Coder-1.3B and Qwen2.5-Coder-1.5B as balanced baselines | They are stable under memory limits and provide mid-tier latency. |
| 4 | Exclude Stable-Code-3B for this device class | It exceeded memory limits in most cases and did not complete the suite. |
| 5 | Next optimization target: prompt/format constraints for syntax correctness | Throughput is acceptable, but pass-rate is the current bottleneck for classroom usability. |

## Evidence Files

1. Main run results: results/benchmark_results.json
2. Exploratory run results: results/benchmark_results_exploratory_fast.json
3. Aggregated report: results/benchmark_report.md
