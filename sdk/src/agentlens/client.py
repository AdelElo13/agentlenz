"""HTTP client that batches and sends span events to the AgentLens backend."""

from __future__ import annotations

import atexit
import logging
import threading
from collections import deque

import httpx

from agentlens.config import get_config
from agentlens.spans import Span

logger = logging.getLogger("agentlens")

_client: EventClient | None = None
_lock = threading.Lock()


class EventClient:
    def __init__(self) -> None:
        self._queue: deque[dict] = deque(maxlen=10_000)
        self._flush_lock = threading.Lock()
        self._http: httpx.Client | None = None
        self._timer: threading.Timer | None = None
        self._start_flush_timer()
        atexit.register(self.flush)

    def record(self, span: Span) -> None:
        """Queue a span for sending to the backend."""
        cfg = get_config()
        if not cfg.enabled:
            return
        self._queue.append(span.to_otel_dict())
        if len(self._queue) >= cfg.batch_size:
            self.flush()

    def flush(self) -> None:
        """Send all queued events to the backend."""
        if not self._queue:
            return
        with self._flush_lock:
            if not self._queue:
                return
            cfg = get_config()
            batch = []
            while self._queue:
                batch.append(self._queue.popleft())
        try:
            http = self._get_http()
            http.post(
                f"{cfg.endpoint}/v1/events",
                json={"events": batch},
                headers={"Authorization": f"Bearer {cfg.api_key}"},
                timeout=10.0,
            )
        except Exception:
            logger.warning("AgentLens: failed to send %d events", len(batch), exc_info=True)

    def _get_http(self) -> httpx.Client:
        if self._http is None:
            self._http = httpx.Client()
        return self._http

    def _start_flush_timer(self) -> None:
        cfg = get_config()
        self._timer = threading.Timer(cfg.flush_interval, self._periodic_flush)
        self._timer.daemon = True
        self._timer.start()

    def _periodic_flush(self) -> None:
        self.flush()
        self._start_flush_timer()


def get_client() -> EventClient:
    """Get or create the singleton event client."""
    global _client
    if _client is None:
        with _lock:
            if _client is None:
                _client = EventClient()
    return _client
