from collections.abc import Callable
from types import TracebackType
from typing import Any

from typing_extensions import Self

__all__ = ("DummyLock", "LaxBoundedSemaphore")

class DummyLock:
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

class LaxBoundedSemaphore:
    initial_value: int
    value: int

    def __init__(self, value: int) -> None: ...
    def acquire(
        self, callback: Callable[..., None], *partial_args: Any, **partial_kwargs: Any
    ) -> bool: ...
    def release(self) -> None: ...
    def grow(self, n: int = ...) -> None: ...
    def shrink(self, n: int = ...) -> None: ...
    def clear(self) -> None: ...
