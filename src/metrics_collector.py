from __future__ import annotations

import threading
import time
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional

import psutil

GIB = 1024 ** 3
DEFAULT_MEMORY_PERCENT_THRESHOLD = 90.0
DEFAULT_MEMORY_BYTES_THRESHOLD = int(7.2 * GIB)


class MemoryThresholdExceeded(RuntimeError):
    """Raised when system RAM usage breaches the safe operating ceiling."""


@dataclass
class ResourceSample:
    timestamp: float
    used_memory_bytes: int
    memory_percent: float
    cpu_percent: float


class MetricsCollector:
    def __init__(
        self,
        sample_interval: float = 0.2,
        memory_percent_threshold: float = DEFAULT_MEMORY_PERCENT_THRESHOLD,
        memory_bytes_threshold: int = DEFAULT_MEMORY_BYTES_THRESHOLD,
    ) -> None:
        self.sample_interval = sample_interval
        self.memory_percent_threshold = memory_percent_threshold
        self.memory_bytes_threshold = memory_bytes_threshold
        self.samples: List[ResourceSample] = []
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._threshold_sample: Optional[ResourceSample] = None

    def _capture_sample(self) -> ResourceSample:
        memory = psutil.virtual_memory()
        sample = ResourceSample(
            timestamp=time.time(),
            used_memory_bytes=int(memory.used),
            memory_percent=float(memory.percent),
            cpu_percent=float(psutil.cpu_percent(interval=None)),
        )
        with self._lock:
            self.samples.append(sample)
            if self._threshold_sample is None and (
                sample.memory_percent >= self.memory_percent_threshold
                or sample.used_memory_bytes >= self.memory_bytes_threshold
            ):
                self._threshold_sample = sample
                self._stop_event.set()
        return sample

    def snapshot(self) -> ResourceSample:
        sample = self._capture_sample()
        self.raise_if_threshold_exceeded()
        return sample

    def _poll(self) -> None:
        while not self._stop_event.is_set():
            self._capture_sample()
            self._stop_event.wait(self.sample_interval)

    def start(self) -> "MetricsCollector":
        self.samples = []
        self._threshold_sample = None
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._poll, daemon=True)
        self._thread.start()
        return self

    def stop(self) -> None:
        self._stop_event.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=max(self.sample_interval * 2, 0.5))

    @property
    def threshold_exceeded(self) -> bool:
        return self._threshold_sample is not None

    def raise_if_threshold_exceeded(self) -> None:
        if not self._threshold_sample:
            return
        used_gib = self._threshold_sample.used_memory_bytes / GIB
        raise MemoryThresholdExceeded(
            "Emergency stop triggered because RAM usage exceeded the safe limit: "
            f"{used_gib:.2f} GiB used at {self._threshold_sample.memory_percent:.1f}% total usage."
        )

    def summarize(self) -> Dict[str, float]:
        with self._lock:
            samples = list(self.samples)
        if not samples:
            return {
                "sample_count": 0,
                "max_ram_bytes": 0,
                "max_ram_gib": 0.0,
                "avg_cpu_percent": 0.0,
                "peak_cpu_percent": 0.0,
                "threshold_exceeded": False,
            }
        max_ram_bytes = max(sample.used_memory_bytes for sample in samples)
        cpu_values = [sample.cpu_percent for sample in samples]
        return {
            "sample_count": len(samples),
            "max_ram_bytes": max_ram_bytes,
            "max_ram_gib": round(max_ram_bytes / GIB, 3),
            "avg_cpu_percent": round(sum(cpu_values) / len(cpu_values), 3),
            "peak_cpu_percent": round(max(cpu_values), 3),
            "threshold_exceeded": self.threshold_exceeded,
        }

    def serialize_samples(self) -> List[Dict[str, float]]:
        with self._lock:
            return [asdict(sample) for sample in self.samples]

    def __enter__(self) -> "MetricsCollector":
        return self.start()

    def __exit__(self, exc_type, exc, tb) -> None:
        self.stop()
