from collections.abc import Callable
from datetime import datetime
from typing import Any, NamedTuple
from zoneinfo import ZoneInfo

__all__ = ("Entry", "Timer", "to_timestamp")

class scheduled(NamedTuple):
    eta: float
    priority: int
    entry: Entry

class Entry:
    fun: Callable[..., Any]
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    tref: Any
    cancelled: bool

    def __init__(
        self,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
    ) -> None: ...
    def __call__(self) -> Any: ...
    def cancel(self) -> None: ...

class Timer:
    queue: list[scheduled]
    on_error: Callable[[Exception], None] | None

    def __init__(self, on_error: Callable[[Exception], None] | None = ...) -> None: ...
    def __len__(self) -> int: ...
    def call_at(
        self,
        eta: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
        priority: int = ...,
    ) -> Entry: ...
    def call_after(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
        priority: int = ...,
    ) -> Entry: ...
    def call_repeatedly(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = ...,
        kwargs: dict[str, Any] | None = ...,
        priority: int = ...,
    ) -> Entry: ...
    def apply_at(self, eta: float, fun: Callable[..., Any], *args: Any, **kwargs: Any) -> Entry: ...
    def apply_after(self, secs: float, fun: Callable[..., Any], *args: Any, **kwargs: Any) -> Entry: ...
    def apply_interval(self, secs: float, fun: Callable[..., Any], *args: Any, **kwargs: Any) -> Entry: ...
    def enter_at(self, entry: Entry, eta: float, priority: int = ...) -> Entry: ...
    def enter_after(self, entry: Entry, secs: float, priority: int = ...) -> Entry: ...
    def cancel(self, tref: Entry) -> None: ...
    def clear(self) -> None: ...
    def empty(self) -> bool: ...

def to_timestamp(
    d: datetime | float,
    default_timezone: ZoneInfo = ...,
    time: Callable[[], float] = ...,
) -> float: ...
