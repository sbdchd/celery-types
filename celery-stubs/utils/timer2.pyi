from collections.abc import Callable
from threading import Thread
from types import TracebackType
from typing import Any
from zoneinfo import ZoneInfo

from typing_extensions import Self, override

__all__ = ("Entry", "Schedule", "Timer", "to_timestamp")

def to_timestamp(
    d: Any,
    default_timezone: ZoneInfo = ...,
    time: Callable[[], float] = ...,
) -> float: ...

class Entry:
    fun: Callable[..., Any]
    args: tuple[Any, ...] | None
    kwargs: dict[str, Any] | None
    tref: Any
    canceled: bool

    def __init__(
        self,
        fun: Callable[..., Any],
        args: tuple[Any, ...] | None = None,
        kwargs: dict[str, Any] | None = None,
    ) -> None: ...
    def __call__(self) -> Any: ...
    def __lt__(self, other: Entry) -> bool: ...
    def __gt__(self, other: Entry) -> bool: ...
    def __le__(self, other: Entry) -> bool: ...
    def __ge__(self, other: Entry) -> bool: ...
    def cancel(self) -> None: ...
    @property
    def cancelled(self) -> bool: ...

_Entry = Entry

class Schedule:
    Entry: type[_Entry]
    on_error: Callable[[Exception], None] | None

    def __init__(
        self,
        max_interval: float | None = None,
        on_error: Callable[[Exception], None] | None = None,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def __iter__(
        self,
        min: Callable[..., Any] = ...,
        nowfun: Callable[[], float] = ...,
        pop: Callable[..., Any] = ...,
        push: Callable[..., Any] = ...,
    ) -> Self: ...
    def __len__(self) -> int: ...
    def apply_entry(self, entry: _Entry) -> Any: ...
    def call_after(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def call_at(
        self,
        eta: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def call_repeatedly(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def cancel(self, tref: Any) -> None: ...
    def clear(self) -> None: ...
    def enter_at(
        self,
        entry: _Entry,
        eta: float | None = None,
        priority: int = 0,
        time: Callable[[], float] = ...,
    ) -> _Entry: ...
    def enter_after(
        self,
        secs: float,
        entry: _Entry,
        priority: int = 0,
        time: Callable[[], float] = ...,
    ) -> _Entry: ...
    def handle_error(
        self, exc_info: tuple[type[BaseException], BaseException, TracebackType | None]
    ) -> None: ...
    @property
    def queue(self) -> list[_Entry]: ...
    @property
    def schedule(self) -> Any: ...
    def stop(self) -> None: ...

_Schedule = Schedule

class Timer(Thread):
    Entry: type[_Entry]
    Schedule: type[_Schedule]
    running: bool
    on_tick: Callable[[float], None] | None

    def __init__(
        self,
        schedule: Any | None = None,
        on_error: Callable[[Exception], None] | None = None,
        on_tick: Callable[[float], None] | None = None,
        on_start: Callable[[Timer], None] | None = None,
        max_interval: float | None = None,
        **kwargs: Any,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __next__(self) -> _Entry: ...
    def call_after(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def call_at(
        self,
        eta: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def call_repeatedly(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def enter(
        self,
        entry: _Entry,
        eta: float,
        priority: int | None = None,
    ) -> _Entry: ...
    def enter_after(
        self,
        secs: float,
        entry: _Entry,
        priority: int = 0,
    ) -> _Entry: ...
    def exit_after(
        self,
        secs: float,
        priority: int = 10,
    ) -> None: ...
    def cancel(self, tref: Any) -> None: ...
    def clear(self) -> None: ...
    def empty(self) -> bool: ...
    def next(self) -> _Entry | None: ...
    @override
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def ensure_started(self) -> None: ...
    @property
    def queue(self) -> list[Any]: ...
