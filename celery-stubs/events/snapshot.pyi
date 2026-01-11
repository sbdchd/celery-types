from typing import Any

from celery.app.base import Celery
from celery.events.state import State
from typing_extensions import Self

__all__ = ("Polaroid", "evcam")

class Polaroid:
    app: Celery
    state: State
    freq: float
    timer: Any

    def __init__(
        self,
        state: State,
        freq: float = 1.0,
        maxrate: str | None = None,
        cleanup_freq: float = 3600.0,
        timer: Any | None = None,
        app: Celery | None = None,
    ) -> None: ...
    cleanup_signal: Any
    clear_after: bool
    shutter_signal: Any

    def install(self) -> None: ...
    def on_cleanup(self) -> None: ...
    def on_shutter(self, state: State) -> None: ...
    def shutter(self) -> None: ...
    def capture(self) -> None: ...
    def cancel(self) -> None: ...
    def cleanup(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...

def evcam(
    camera: str,
    freq: float = 1.0,
    maxrate: str | None = None,
    loglevel: int = 0,
    logfile: str | None = None,
    pidfile: str | None = None,
    timer: Any | None = None,
    app: Celery | None = None,
    **kwargs: Any,
) -> None: ...
