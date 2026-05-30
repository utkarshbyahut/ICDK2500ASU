# Benchmark Report

## Model Ranking

| Model               |   Runs |   Avg TTFT (s) |   Avg Tokens/s |   Avg Peak RAM (GiB) |   Compilation Pass % |   Efficiency Score |   Overall Score |
|---------------------|--------|----------------|----------------|----------------------|----------------------|--------------------|-----------------|
| Qwen2.5-Coder-0.5B  |     12 |          1.071 |         47.707 |                4.935 |                 0    |              95.69 |           47.84 |
| StarCoder-1B        |      6 |          0.92  |         26.363 |                5.46  |                16.67 |              71.38 |           44.02 |
| TinyLlama-1.1B      |      6 |          1.147 |         28.947 |                6.049 |                 0    |              56.46 |           28.23 |
| Qwen2.5-Coder-1.5B  |     14 |          1.638 |         21.16  |                5.401 |                 0    |              47.31 |           23.66 |
| DeepSeek-Coder-1.3B |     12 |          1.687 |         21.31  |                5.711 |                 0    |              40.4  |           20.2  |
| CodeGemma-2B        |      6 |          2.088 |         12.785 |                6.745 |                16.67 |               2.52 |            9.6  |
| Stable-Code-3B      |      1 |          1.742 |         10.398 |                6.766 |                 0    |               9.87 |            4.93 |

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
| Qwen2.5-Coder-0.5B      | pololu-drive-forward  | movement-basics  | 3.567      | 49.964     | 4.756            | 14.138      | failed                   | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-0.5B      | pololu-turn-left      | movement-basics  | 0.397      | 56.729     | 4.768            | 17.025      | failed                   | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-0.5B      | pololu-obstacle-stop  | sensor-response  | 0.575      | 44.358     | 4.771            | 23.96       | failed                   | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-0.5B      | pololu-line-following | sensor-response  | 0.481      | 42.311     | 4.771            | 23.233      | failed                   | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-0.5B      | pololu-led-status     | student-feedback | 0.424      | 47.395     | 4.76             | 18.911      | failed                   | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-0.5B      | pololu-button-control | student-feedback | 0.466      | 53.77      | 4.764            | 16.733      | failed                   | benchmark_results_tiny_focus.json       |
| StarCoder-1B            | pololu-drive-forward  | movement-basics  | 2.3        | 23.726     | 5.491            | 16.191      | failed                   | benchmark_results_tiny_focus.json       |
| StarCoder-1B            | pololu-turn-left      | movement-basics  | 0.557      | 28.315     | 5.491            | 17.182      | failed                   | benchmark_results_tiny_focus.json       |
| StarCoder-1B            | pololu-obstacle-stop  | sensor-response  | 0.795      | 26.366     | 5.487            | 16.507      | failed                   | benchmark_results_tiny_focus.json       |
| StarCoder-1B            | pololu-line-following | sensor-response  | 0.669      | 27.071     | 5.431            | 16.586      | failed                   | benchmark_results_tiny_focus.json       |
| StarCoder-1B            | pololu-led-status     | student-feedback | 0.494      | 27.228     | 5.431            | 17.115      | failed                   | benchmark_results_tiny_focus.json       |
| StarCoder-1B            | pololu-button-control | student-feedback | 0.705      | 25.47      | 5.429            | 18.329      | passed                   | benchmark_results_tiny_focus.json       |
| TinyLlama-1.1B          | pololu-drive-forward  | movement-basics  | 3.437      | 26.165     | 6.093            | 23.607      | failed                   | benchmark_results_tiny_focus.json       |
| TinyLlama-1.1B          | pololu-turn-left      | movement-basics  | 0.602      | 27.157     | 6.043            | 24.6        | failed                   | benchmark_results_tiny_focus.json       |
| TinyLlama-1.1B          | pololu-obstacle-stop  | sensor-response  | 0.786      | 29.339     | 6.042            | 20.264      | failed                   | benchmark_results_tiny_focus.json       |
| TinyLlama-1.1B          | pololu-line-following | sensor-response  | 0.659      | 30.43      | 6.039            | 17.792      | failed                   | benchmark_results_tiny_focus.json       |
| TinyLlama-1.1B          | pololu-led-status     | student-feedback | 0.654      | 30.533     | 6.039            | 17.846      | failed                   | benchmark_results_tiny_focus.json       |
| TinyLlama-1.1B          | pololu-button-control | student-feedback | 0.747      | 30.058     | 6.039            | 18.536      | failed                   | benchmark_results_tiny_focus.json       |
| DeepSeek-Coder-1.3B     | pololu-drive-forward  | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| DeepSeek-Coder-1.3B     | pololu-turn-left      | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| DeepSeek-Coder-1.3B     | pololu-obstacle-stop  | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| DeepSeek-Coder-1.3B     | pololu-line-following | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| DeepSeek-Coder-1.3B     | pololu-led-status     | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| DeepSeek-Coder-1.3B     | pololu-button-control | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-1.5B      | pololu-drive-forward  | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-1.5B      | pololu-turn-left      | movement-basics  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-1.5B      | pololu-obstacle-stop  | sensor-response  | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-1.5B      | pololu-line-following | sensor-response  | 0.862      | 18.902     | 6.758            | 23.853      | failed                   | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-1.5B      | pololu-led-status     | student-feedback | 0.864      | 19.891     | 6.674            | 21.256      | failed                   | benchmark_results_tiny_focus.json       |
| Qwen2.5-Coder-1.5B      | pololu-button-control | student-feedback | -          | -          | -                | -           | aborted_memory_threshold | benchmark_results_tiny_focus.json       |
