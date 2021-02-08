import numbers
from datetime import datetime, timedelta
from typing import Callable, NamedTuple, Optional, Set, Tuple, Union

from celery.app.base import Celery
from celery.utils.time import ffwd
from typing_extensions import Literal

import ephem

class schedstate(NamedTuple):
    is_due: bool
    next: float

def cronfield(s: Optional[str]) -> str: ...

class ParseException(Exception): ...

class BaseSchedule:
    nowfunc: Callable[[], datetime]
    def __init__(
        self,
        nowfun: Optional[Callable[[], datetime]] = ...,
        app: Optional[Celery] = ...,
    ) -> None: ...
    def now(self) -> datetime: ...
    def remaining_estimate(self, last_run_at: datetime) -> timedelta: ...
    def is_due(self, last_run_at: datetime) -> schedstate: ...
    def maybe_make_aware(self, dt: datetime) -> datetime: ...
    @property
    def app(self) -> Celery: ...
    @app.setter
    def app(self, app: Celery) -> None: ...
    @property
    def tz(self) -> str: ...
    @property
    def utc_enabled(self) -> bool: ...
    def to_local(self, dt: datetime) -> datetime: ...
    def __eq__(self, other: object) -> bool: ...

class schedule(BaseSchedule):
    def __init__(
        self,
        run_every: Optional[Union[float, timedelta]] = ...,
        relative: bool = ...,
        nowfun: Optional[Callable[[], datetime]] = ...,
        app: Optional[Celery] = ...,
    ) -> None: ...
    @property
    def seconds(self) -> int: ...
    @property
    def human_seconds(self) -> str: ...

_ModuleLevelParseException = ParseException

class crontab_parser:
    ParseException: _ModuleLevelParseException
    def __init__(self, max_: int = ..., min_: int = ...) -> None: ...
    def parse(self, spec: str) -> Set[int]: ...

class crontab(BaseSchedule):
    def __init__(
        self,
        minute: Union[str, int] = ...,
        hour: Union[str, int] = ...,
        day_of_week: Union[str, int] = ...,
        day_of_month: Union[str, int] = ...,
        month_of_year: Union[str, int] = ...,
        nowfun: Optional[Callable[[], datetime]] = ...,
        app: Optional[Celery] = ...,
    ) -> None: ...
    def remaining_delta(
        self, last_run_at: datetime, tz: Optional[str] = ..., ffwd: ffwd = ...
    ) -> Tuple[datetime, timedelta, datetime]: ...

def maybe_schedule(s: Union[numbers.Number, timedelta, BaseSchedule]) -> schedule: ...

_SolarEvent = Literal[
    "dawn_astronomical",
    "dawn_nautical",
    "dawn_civil",
    "sunrise",
    "solar_noon",
    "sunset",
    "dusk_civil",
    "dusk_nautical",
    "dusk_astronomical",
]

class solar(BaseSchedule):
    cal: ephem.Observer
    event: _SolarEvent
    lat: float
    lon: float
    def __init__(
        self,
        event: _SolarEvent,
        lat: float,
        lon: float,
        nowfun: Optional[Callable[[], datetime]] = ...,
        app: Optional[Celery] = ...,
    ) -> None: ...
