# Benchmark Report

## Model Ranking

| Model               |   Runs |   Avg TTFT (s) |   Avg Tokens/s |   Avg Peak RAM (GiB) |   Compilation Pass % |   Efficiency Score |   Overall Score |
|---------------------|--------|----------------|----------------|----------------------|----------------------|--------------------|-----------------|
| Qwen2.5-Coder-1.5B  |      6 |          1.71  |         20.724 |                4.926 |                    0 |                100 |              50 |
| DeepSeek-Coder-1.3B |      6 |          1.779 |         20.702 |                6.046 |                    0 |                  0 |               0 |

## Detailed Runs

| Model                   | Case                  | Scenario         | TTFT (s)   | Tokens/s   | Peak RAM (GiB)   | CPU Avg %   | Validation               | Source                 |
|-------------------------|-----------------------|------------------|------------|------------|------------------|-------------|--------------------------|------------------------|
| Qwen2.5-Coder-1.5B      | pololu-drive-forward  | movement-basics  | 6.069      | 20.317     | 4.912            | 14.679      | failed                   | benchmark_results.json |
| Qwen2.5-Coder-1.5B      | pololu-turn-left      | movement-basics  | 0.943      | 20.373     | 4.923            | 21.277      | failed                   | benchmark_results.json |
| Qwen2.5-Coder-1.5B      | pololu-obstacle-stop  | sensor-response  | 0.812      | 23.058     | 4.916            | 17.867      | failed                   | benchmark_results.json |
| Qwen2.5-Coder-1.5B      | pololu-line-following | sensor-response  | 0.809      | 21.098     | 4.928            | 22.885      | failed                   | benchmark_results.json |
| Qwen2.5-Coder-1.5B      | pololu-led-status     | student-feedback | 0.703      | 20.715     | 4.933            | 25.6        | failed                   | benchmark_results.json |
| Qwen2.5-Coder-1.5B      | pololu-button-control | student-feedback | 0.923      | 18.781     | 4.941            | 28.223      | failed                   | benchmark_results.json |
| DeepSeek-Coder-1.3B     | pololu-drive-forward  | movement-basics  | 6.707      | 19.256     | 6.341            | 18.481      | failed                   | benchmark_results.json |
| DeepSeek-Coder-1.3B     | pololu-turn-left      | movement-basics  | 1.091      | 21.672     | 6.325            | 18.071      | failed                   | benchmark_results.json |
| DeepSeek-Coder-1.3B     | pololu-obstacle-stop  | sensor-response  | 0.727      | 21.8       | 6.326            | 19.192      | failed                   | benchmark_results.json |
| DeepSeek-Coder-1.3B     | pololu-line-following | sensor-response  | 0.774      | 19.293     | 6.235            | 25.638      | failed                   | benchmark_results.json |
| DeepSeek-Coder-1.3B     | pololu-led-status     | student-feedback | 0.653      | 22.008     | 5.589            | 19.583      | failed                   | benchmark_results.json |
| DeepSeek-Coder-1.3B     | pololu-button-control | student-feedback | 0.721      | 20.184     | 5.461            | 18.15       | failed                   | benchmark_results.json |
| Granite-3.0-8B-Code-IQ2 | pololu-drive-forward  | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json |
| Granite-3.0-8B-Code-IQ2 | pololu-turn-left      | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json |
| Granite-3.0-8B-Code-IQ2 | pololu-obstacle-stop  | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json |
| Granite-3.0-8B-Code-IQ2 | pololu-line-following | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json |
| Granite-3.0-8B-Code-IQ2 | pololu-led-status     | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json |
| Granite-3.0-8B-Code-IQ2 | pololu-button-control | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json |
