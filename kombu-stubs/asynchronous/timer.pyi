from collections.abc import Callable, Iterator
from datetime import datetime
from types import TracebackType
from typing import Any, NamedTuple
from zoneinfo import ZoneInfo

from typing_extensions import Self

__all__ = ("Entry", "Timer", "to_timestamp")

class scheduled(NamedTuple):
    eta: float
    priority: int
    entry: Entry

class Entry:
    fun: Callable[..., Any]
    args: list[Any]
    kwargs: dict[str, Any]
    tref: Any
    canceled: bool
    _last_run: float | None

    def __init__(
        self,
        fun: Callable[..., Any],
        args: list[Any] | None = ...,
        kwargs: dict[str, Any] | None = ...,
    ) -> None: ...
    def __call__(self) -> Any: ...
    def cancel(self) -> None: ...
    def __lt__(self, other: Entry) -> bool: ...
    def __le__(self, other: Entry) -> bool: ...
    def __gt__(self, other: Entry) -> bool: ...
    def __ge__(self, other: Entry) -> bool: ...
    @property
    def cancelled(self) -> bool: ...
    @cancelled.setter
    def cancelled(self, value: bool) -> None: ...

_Entry = Entry

class Timer:
    Entry: type[_Entry]
    max_interval: float
    on_error: Callable[[Exception], None] | None
    _queue: list[scheduled]

    def __init__(
        self,
        max_interval: float | None = ...,
        on_error: Callable[[Exception], None] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __nonzero__(self) -> bool: ...
    def __iter__(
        self,
        min: Callable[..., Any] = ...,
        nowfun: Callable[[], float] = ...,
        pop: Callable[..., Any] = ...,
        push: Callable[..., Any] = ...,
    ) -> Iterator[tuple[float | None, _Entry | None]]: ...
    def call_at(
        self,
        eta: float | datetime,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
        priority: int = ...,
    ) -> _Entry: ...
    def call_after(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
        priority: int = ...,
    ) -> _Entry: ...
    def call_repeatedly(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
        priority: int = ...,
    ) -> _Entry: ...
    def enter_at(
        self,
        entry: _Entry,
        eta: float | datetime | None = ...,
        priority: int = ...,
        time: Callable[[], float] = ...,
    ) -> _Entry | None: ...
    def enter_after(
        self,
        secs: float,
        entry: _Entry,
        priority: int = ...,
        time: Callable[[], float] = ...,
    ) -> _Entry: ...
    def apply_entry(self, entry: _Entry) -> None: ...
    def handle_error(self, exc_info: Exception) -> bool | None: ...
    def stop(self) -> None: ...
    def cancel(self, tref: _Entry) -> None: ...
    def clear(self) -> None: ...
    def _enter(
        self,
        eta: float,
        priority: int,
        entry: _Entry,
        push: Callable[..., Any] = ...,
    ) -> _Entry: ...
    @property
    def queue(self) -> list[scheduled]: ...
    @property
    def schedule(self) -> Timer: ...

def to_timestamp(
    d: datetime | float,
    default_timezone: ZoneInfo = ...,
    time: Callable[[], float] = ...,
) -> float: ...
