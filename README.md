# ICDK2500ASU

A local-first benchmarking workspace for comparing lightweight, free code LLMs on an Intel Core Ultra 5 225U system with an 8GB RAM ceiling.

## Target system profile

- **CPU:** Intel Core Ultra 5 225U (1.5 GHz, AVX2/AVX-VNNI)
- **System memory:** 8GB DDR5 total
- **Safe model allocation:** 2.5GB-3.5GB max, leaving headroom for the OS and editor
- **Serving constraint:** 100% free, open-source, and locally hosted through Ollama

## Repository layout

```text
.github/workflows/lint-and-test.yml
config/models.json
config/test_cases.json
src/__init__.py
src/benchmark_runner.py
src/metrics_collector.py
src/report_generator.py
templates/continue_config_template.json
results/.gitkeep
requirements.txt
README.md
```

## Included benchmark targets

The default `config/models.json` profiles these local code models:

- `qwen2.5-coder:1.5b` for higher-logic sidebar/chat evaluation
- `deepseek-coder:1.3b` for low-latency autocomplete evaluation
- `granite3.0:8b-code-instruct-q2_K` as a compressed larger-model candidate

All configured context windows are capped at **2048 or 4096 tokens** to stay within the requested memory budget.

## Setup

1. Install Python 3.11+.
2. Install Ollama and pull the configured models.
3. Install repository dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start Ollama locally:

   ```bash
   ollama serve
   ```

## Running benchmarks

Execute the benchmark runner against the local Ollama API:

```bash
python -m src.benchmark_runner \
  --models /tmp/workspace/utkarshbyahut/ICDK2500ASU/config/models.json \
  --test-cases /tmp/workspace/utkarshbyahut/ICDK2500ASU/config/test_cases.json \
  --results /tmp/workspace/utkarshbyahut/ICDK2500ASU/results/benchmark_results.json
```

The runner will:

- iterate through the standardized prompt set in `config/test_cases.json`
- stream generations from the Ollama `/api/generate` endpoint
- record **time-to-first-token**, **tokens/sec**, **peak RAM**, and **CPU load**
- abort a run with an emergency stop if system memory exceeds **90% usage / 7.2GB**
- optionally validate generated snippets with the configured compilation/syntax command for each test case

## Generating a report

After one or more benchmark runs have produced JSON in `results/`, build a markdown summary:

```bash
python -m src.report_generator \
  --results-dir /tmp/workspace/utkarshbyahut/ICDK2500ASU/results \
  --output /tmp/workspace/utkarshbyahut/ICDK2500ASU/results/benchmark_report.md
```

## Evaluation scorecard

The evaluation framework is intentionally split into two pillars:

### 1. Speed and resource efficiency

- **Peak RAM footprint** during generation
- **Time-to-first-token (TTFT)** for perceived responsiveness
- **Tokens/sec** for sustained generation throughput
- **Average CPU load** to understand thermal and background pressure on the 225U platform

### 2. Code accuracy

- **Compilation/syntax validation** of generated snippets using language-specific commands from `config/test_cases.json`
- **Pass rate** across the prompt set to quantify whether a model returns executable code instead of only fast output

The report generator combines these signals into a simple ranking table so lightweight models can be compared quickly without leaving the local machine.

## Continue.dev template

`templates/continue_config_template.json` provides a dual-model local setup:

- **`tabAutocompleteModel`** -> `deepseek-coder:1.3b` for ultra-light inline completions
- **`models`** -> `qwen2.5-coder:1.5b` for sidebar chat and higher-logic coding help

Copy the template into your Continue configuration and adjust model tags if you want to benchmark alternative quantizations.

## CI validation

GitHub Actions runs a lightweight validation workflow that:

- installs the Python dependencies
- byte-compiles the `src/` and `tests/` modules
- runs the unit tests in `tests/`
