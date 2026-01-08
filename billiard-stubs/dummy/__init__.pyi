import threading
from collections.abc import Callable, Iterable, Mapping
from queue import Queue as Queue
from threading import BoundedSemaphore as BoundedSemaphore

# Note: Condition is a custom class in billiard.dummy, not threading.Condition
from threading import Event as Event
from threading import Lock as Lock
from threading import Semaphore as Semaphore
from typing import Any

from billiard.connection import Pipe as Pipe
from typing_extensions import override

__all__ = [
    "BoundedSemaphore",
    "Condition",
    "Event",
    "JoinableQueue",
    "Lock",
    "Manager",
    "Pipe",
    "Pool",
    "Process",
    "Queue",
    "RLock",
    "Semaphore",
    "active_children",
    "current_process",
    "freeze_support",
]

class DummyProcess(threading.Thread):
    def __init__(
        self,
        group: None = ...,
        target: Callable[..., object] | None = ...,
        name: str | None = ...,
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] = ...,
    ) -> None: ...
    @override
    def start(self) -> None: ...
    @property
    def exitcode(self) -> int | None: ...

Process = DummyProcess
current_process = threading.current_thread

def freeze_support() -> None: ...
def active_children() -> list[DummyProcess]: ...
def Manager() -> Any: ...
def Pool(
    processes: int | None = ...,
    initializer: Callable[..., object] | None = ...,
    initargs: Iterable[Any] = ...,
) -> Any: ...
def RLock(*args: Any, **kwargs: Any) -> threading.RLock: ...

class Condition:
    def __init__(self, lock: Any = ...) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args: object) -> None: ...
    def wait(self, timeout: float | None = ...) -> bool: ...
    def wait_for(
        self, predicate: Callable[[], bool], timeout: float | None = ...
    ) -> bool: ...
    def notify(self, n: int = ...) -> None: ...
    def notify_all(self) -> None: ...

JoinableQueue = Queue
