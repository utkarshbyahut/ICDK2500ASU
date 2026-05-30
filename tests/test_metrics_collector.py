import unittest
from types import SimpleNamespace
from unittest import mock

from src.metrics_collector import MetricsCollector, MemoryThresholdExceeded


class MetricsCollectorTests(unittest.TestCase):
    def test_snapshot_raises_when_ram_limit_is_exceeded(self) -> None:
        collector = MetricsCollector()
        with mock.patch(
            "src.metrics_collector.psutil.virtual_memory",
            return_value=SimpleNamespace(used=int(7.3 * (1024 ** 3)), percent=91.0),
        ), mock.patch("src.metrics_collector.psutil.cpu_percent", return_value=12.5):
            with self.assertRaises(MemoryThresholdExceeded):
                collector.snapshot()

    def test_summary_reports_peak_resource_usage(self) -> None:
        collector = MetricsCollector()
        samples = [
            SimpleNamespace(used=int(2.1 * (1024 ** 3)), percent=41.0),
            SimpleNamespace(used=int(2.4 * (1024 ** 3)), percent=46.0),
        ]
        cpu_values = [15.0, 35.0]
        with mock.patch("src.metrics_collector.psutil.virtual_memory", side_effect=samples), mock.patch(
            "src.metrics_collector.psutil.cpu_percent", side_effect=cpu_values
        ):
            collector._capture_sample()
            collector._capture_sample()
        summary = collector.summarize()
        self.assertEqual(summary["sample_count"], 2)
        self.assertAlmostEqual(summary["max_ram_gib"], 2.4, places=1)
        self.assertEqual(summary["peak_cpu_percent"], 35.0)


if __name__ == "__main__":
    unittest.main()
