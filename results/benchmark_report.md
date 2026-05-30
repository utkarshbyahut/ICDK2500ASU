# Benchmark Report

## Model Ranking

| Model               |   Runs |   Avg TTFT (s) |   Avg Tokens/s |   Avg Peak RAM (GiB) |   Compilation Pass % |   Efficiency Score |   Overall Score |
|---------------------|--------|----------------|----------------|----------------------|----------------------|--------------------|-----------------|
| Qwen2.5-Coder-0.5B  |      6 |          1.157 |         46.327 |                5.106 |                 0    |             100    |           50    |
| Qwen2.5-Coder-1.5B  |     12 |          1.767 |         21.454 |                5.182 |                 0    |              53.55 |           26.77 |
| DeepSeek-Coder-1.3B |     12 |          1.687 |         21.31  |                5.711 |                 0    |              45.66 |           22.83 |
| CodeGemma-2B        |      6 |          2.088 |         12.785 |                6.745 |                16.67 |               2.64 |            9.66 |
| Stable-Code-3B      |      1 |          1.742 |         10.398 |                6.766 |                 0    |              12.39 |            6.2  |

## Detailed Runs

| Model                   | Case                  | Scenario         | TTFT (s)   | Tokens/s   | Peak RAM (GiB)   | CPU Avg %   | Validation               | Source                                  |
|-------------------------|-----------------------|------------------|------------|------------|------------------|-------------|--------------------------|-----------------------------------------|
| Qwen2.5-Coder-1.5B      | pololu-drive-forward  | movement-basics  | 6.069      | 20.317     | 4.912            | 14.679      | failed                   | benchmark_results.json                  |
| Qwen2.5-Coder-1.5B      | pololu-turn-left      | movement-basics  | 0.943      | 20.373     | 4.923            | 21.277      | failed                   | benchmark_results.json                  |
| Qwen2.5-Coder-1.5B      | pololu-obstacle-stop  | sensor-response  | 0.812      | 23.058     | 4.916            | 17.867      | failed                   | benchmark_results.json                  |
| Qwen2.5-Coder-1.5B      | pololu-line-following | sensor-response  | 0.809      | 21.098     | 4.928            | 22.885      | failed                   | benchmark_results.json                  |
| Qwen2.5-Coder-1.5B      | pololu-led-status     | student-feedback | 0.703      | 20.715     | 4.933            | 25.6        | failed                   | benchmark_results.json                  |
| Qwen2.5-Coder-1.5B      | pololu-button-control | student-feedback | 0.923      | 18.781     | 4.941            | 28.223      | failed                   | benchmark_results.json                  |
| DeepSeek-Coder-1.3B     | pololu-drive-forward  | movement-basics  | 6.707      | 19.256     | 6.341            | 18.481      | failed                   | benchmark_results.json                  |
| DeepSeek-Coder-1.3B     | pololu-turn-left      | movement-basics  | 1.091      | 21.672     | 6.325            | 18.071      | failed                   | benchmark_results.json                  |
| DeepSeek-Coder-1.3B     | pololu-obstacle-stop  | sensor-response  | 0.727      | 21.8       | 6.326            | 19.192      | failed                   | benchmark_results.json                  |
| DeepSeek-Coder-1.3B     | pololu-line-following | sensor-response  | 0.774      | 19.293     | 6.235            | 25.638      | failed                   | benchmark_results.json                  |
| DeepSeek-Coder-1.3B     | pololu-led-status     | student-feedback | 0.653      | 22.008     | 5.589            | 19.583      | failed                   | benchmark_results.json                  |
| DeepSeek-Coder-1.3B     | pololu-button-control | student-feedback | 0.721      | 20.184     | 5.461            | 18.15       | failed                   | benchmark_results.json                  |
| Granite-3.0-8B-Code-IQ2 | pololu-drive-forward  | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json                  |
| Granite-3.0-8B-Code-IQ2 | pololu-turn-left      | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json                  |
| Granite-3.0-8B-Code-IQ2 | pololu-obstacle-stop  | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json                  |
| Granite-3.0-8B-Code-IQ2 | pololu-line-following | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json                  |
| Granite-3.0-8B-Code-IQ2 | pololu-led-status     | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json                  |
| Granite-3.0-8B-Code-IQ2 | pololu-button-control | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results.json                  |
| Qwen2.5-Coder-0.5B      | pololu-drive-forward  | movement-basics  | 4.72       | 35.89      | 5.993            | 16.212      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-0.5B      | pololu-turn-left      | movement-basics  | 0.445      | 49.738     | 4.935            | 11.733      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-0.5B      | pololu-obstacle-stop  | sensor-response  | 0.473      | 47.469     | 4.948            | 13.175      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-0.5B      | pololu-line-following | sensor-response  | 0.445      | 47.985     | 4.945            | 13.475      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-0.5B      | pololu-led-status     | student-feedback | 0.384      | 48.797     | 4.923            | 11.333      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-0.5B      | pololu-button-control | student-feedback | 0.477      | 48.08      | 4.889            | 12.2        | failed                   | benchmark_results_exploratory_fast.json |
| DeepSeek-Coder-1.3B     | pololu-drive-forward  | movement-basics  | 4.791      | 19.361     | 5.51             | 9.988       | failed                   | benchmark_results_exploratory_fast.json |
| DeepSeek-Coder-1.3B     | pololu-turn-left      | movement-basics  | 0.909      | 22.106     | 5.466            | 15.043      | failed                   | benchmark_results_exploratory_fast.json |
| DeepSeek-Coder-1.3B     | pololu-obstacle-stop  | sensor-response  | 0.893      | 22.559     | 5.406            | 26.771      | failed                   | benchmark_results_exploratory_fast.json |
| DeepSeek-Coder-1.3B     | pololu-line-following | sensor-response  | 1.06       | 23.513     | 5.36             | 16.286      | failed                   | benchmark_results_exploratory_fast.json |
| DeepSeek-Coder-1.3B     | pololu-led-status     | student-feedback | 0.912      | 23.14      | 5.287            | 16.767      | failed                   | benchmark_results_exploratory_fast.json |
| DeepSeek-Coder-1.3B     | pololu-button-control | student-feedback | 1.002      | 20.823     | 5.231            | 16.929      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-1.5B      | pololu-drive-forward  | movement-basics  | 6.697      | 21.96      | 5.582            | 13.211      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-1.5B      | pololu-turn-left      | movement-basics  | 0.878      | 23.28      | 5.526            | 17.586      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-1.5B      | pololu-obstacle-stop  | sensor-response  | 0.938      | 23.02      | 5.455            | 14.7        | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-1.5B      | pololu-line-following | sensor-response  | 0.823      | 21.949     | 5.405            | 15.917      | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-1.5B      | pololu-led-status     | student-feedback | 0.76       | 21.913     | 5.347            | 16.4        | failed                   | benchmark_results_exploratory_fast.json |
| Qwen2.5-Coder-1.5B      | pololu-button-control | student-feedback | 0.851      | 20.978     | 5.314            | 19.486      | failed                   | benchmark_results_exploratory_fast.json |
| CodeGemma-2B            | pololu-drive-forward  | movement-basics  | 5.916      | 9.51       | 6.781            | 12.691      | failed                   | benchmark_results_exploratory_fast.json |
| CodeGemma-2B            | pololu-turn-left      | movement-basics  | 1.531      | 12.327     | 6.797            | 15.8        | failed                   | benchmark_results_exploratory_fast.json |
| CodeGemma-2B            | pololu-obstacle-stop  | sensor-response  | 1.386      | 16.077     | 6.796            | 21.0        | passed                   | benchmark_results_exploratory_fast.json |
| CodeGemma-2B            | pololu-line-following | sensor-response  | 1.29       | 13.184     | 6.8              | 13.039      | failed                   | benchmark_results_exploratory_fast.json |
| CodeGemma-2B            | pololu-led-status     | student-feedback | 1.055      | 12.98      | 6.65             | 14.589      | failed                   | benchmark_results_exploratory_fast.json |
| CodeGemma-2B            | pololu-button-control | student-feedback | 1.349      | 12.633     | 6.646            | 16.16       | failed                   | benchmark_results_exploratory_fast.json |
| Stable-Code-3B          | pololu-drive-forward  | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_exploratory_fast.json |
| Stable-Code-3B          | pololu-turn-left      | movement-basics  | 1.742      | 10.398     | 6.766            | 21.377      | failed                   | benchmark_results_exploratory_fast.json |
| Stable-Code-3B          | pololu-obstacle-stop  | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_exploratory_fast.json |
| Stable-Code-3B          | pololu-line-following | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_exploratory_fast.json |
| Stable-Code-3B          | pololu-led-status     | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_exploratory_fast.json |
| Stable-Code-3B          | pololu-button-control | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_exploratory_fast.json |
