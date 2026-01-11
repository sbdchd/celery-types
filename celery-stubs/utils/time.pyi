from collections.abc import Callable
from datetime import datetime, timedelta, tzinfo
from time import struct_time
from types import ModuleType
from typing import Any

from typing_extensions import override

__all__ = (
    "LocalTimezone",
    "adjust_timestamp",
    "delta_resolution",
    "ffwd",
    "get_exponential_backoff_interval",
    "humanize_seconds",
    "is_naive",
    "localize",
    "make_aware",
    "maybe_iso8601",
    "maybe_make_aware",
    "maybe_timedelta",
    "rate",
    "remaining",
    "timezone",
    "to_utc",
    "utcoffset",
    "weekday",
)

class LocalTimezone(tzinfo):
    @override
    def utcoffset(self, dt: datetime | None) -> timedelta: ...
    @override
    def dst(self, dt: datetime | None) -> timedelta: ...
    @override
    def tzname(self, dt: datetime | None) -> str: ...
    @override
    def fromutc(self, dt: datetime) -> datetime: ...

class _Zone:
    @property
    def local(self) -> tzinfo: ...
    @property
    def utc(self) -> tzinfo: ...
    def get_timezone(self, zone: str | tzinfo) -> tzinfo: ...
    def to_local(
        self,
        dt: datetime,
        local: tzinfo | None = None,
        orig: tzinfo | None = None,
    ) -> datetime: ...
    def to_local_fallback(self, dt: datetime) -> datetime: ...
    def to_system(self, dt: datetime) -> datetime: ...
    def tz_or_local(self, tzinfo: tzinfo | None = None) -> tzinfo: ...

timezone: _Zone

class ffwd:
    def __init__(
        self,
        year: int | None = None,
        month: int | None = None,
        weeks: int = 0,
        weekday: int | None = None,
        day: int | None = None,
        hour: int | None = None,
        minute: int | None = None,
        second: int | None = None,
        microsecond: int | None = None,
        **kwargs: Any,
    ) -> None: ...
    def __radd__(self, other: Any) -> timedelta: ...

def adjust_timestamp(
    ts: float,
    offset: int,
    here: Callable[..., float] = ...,
) -> float: ...
def delta_resolution(dt: datetime, delta: timedelta) -> datetime: ...
def get_exponential_backoff_interval(
    factor: int,
    retries: int,
    maximum: int,
    full_jitter: bool = False,
) -> int: ...
def humanize_seconds(
    secs: int,
    prefix: str = "",
    sep: str = "",
    now: str = "now",
    microseconds: bool = False,
) -> str: ...
def is_naive(dt: datetime) -> bool: ...
def localize(dt: datetime, tz: tzinfo) -> datetime: ...
def make_aware(dt: datetime, tz: tzinfo) -> datetime: ...
def maybe_iso8601(dt: datetime | str | None) -> datetime | None: ...
def maybe_make_aware(
    dt: datetime,
    tz: tzinfo | None = None,
    naive_as_utc: bool = True,
) -> datetime: ...
def maybe_timedelta(delta: int) -> timedelta: ...
def rate(r: str) -> float: ...
def remaining(
    start: datetime,
    ends_in: timedelta,
    now: datetime | None = None,
    relative: bool = False,
) -> timedelta: ...
def to_utc(dt: datetime) -> datetime: ...
def utcoffset(
    time: ModuleType = ...,
    localtime: Callable[..., struct_time] = ...,
) -> float: ...
def weekday(name: str) -> int: ...
