# Decision Summary

## Live Benchmark Status

| Item | Result |
|---|---:|
| Repository unit tests | 11 passed / 11 total |
| Benchmark result files written | 1 |
| Live inference run | Completed on this machine |
| Models benchmarked | 3 configured models |
| Test cases executed | 6 Pololu robot-kit tasks |
| Total benchmark outcomes | 18 |

## Benchmark Coverage

| Model | Status | Notes |
|---|---|---|
| `Qwen2.5-Coder-1.5B` | Completed | Actual local Ollama run on this machine. |
| `DeepSeek-Coder-1.3B` | Completed | Actual local Ollama run on this machine. |
| `Granite-3.0-8B-Code-IQ2` | Aborted | The original Granite tag was not available in Ollama; the benchmark used the closest pullable Granite code model and hit the memory threshold. |

## Decision Metrics

| Model | Avg TTFT (s) | Avg Tokens/s | Avg Peak RAM (GiB) | Validation Passes | Outcome |
|---|---:|---:|---:|---:|---|
| `Qwen2.5-Coder-1.5B` | 1.710 | 20.724 | 4.926 | 0/6 | Fastest practical model in this run, but all generated snippets failed syntax validation. |
| `DeepSeek-Coder-1.3B` | 1.779 | 20.702 | 6.046 | 0/6 | Similar throughput to Qwen, but used more RAM and also failed validation. |
| `Granite-3.0-8B-Code-IQ2` | N/A | N/A | N/A | 0/6 | Aborted by the emergency memory threshold, so it is not viable on this 8GB machine. |

## Recommendation Matrix

| Priority | Recommendation | Reason |
|---:|---|---|
| 1 | Use `Qwen2.5-Coder-1.5B` as the default local coding assistant candidate | It delivered the best responsiveness with lower memory than DeepSeek in this run. |
| 2 | Avoid `DeepSeek-Coder-1.3B` as the primary choice for this machine | It was slightly slower and consumed more RAM without improving validation outcomes. |
| 3 | Do not deploy the Granite 8B option on this 8GB system | It tripped the memory threshold before completing the benchmark. |
| 4 | Keep the Pololu six-task suite as the benchmark baseline | It is a realistic student-facing workload and already exercised end-to-end. |
| 5 | Treat syntax validation as a gate before model selection | All generated outputs failed validation in this run, so speed alone is not enough to justify adoption. |

## Decision Notes

1. The live inference data in this README came from actual Ollama models served on this machine.
2. The Granite run used the closest pullable Granite code model because the exact tag from the original config was not available.
3. For this workload, the current models are not yet production-ready for student code generation because validation pass rate was 0/18.
