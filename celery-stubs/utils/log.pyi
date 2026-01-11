from collections.abc import Iterable
from logging import Formatter, Logger, LogRecord, _SysExcInfoType
from typing import ClassVar

from celery.utils.term import colored
from typing_extensions import override

__all__ = (
    "LOG_LEVELS",
    "ColorFormatter",
    "LoggingProxy",
    "base_logger",
    "get_logger",
    "get_multiprocessing_logger",
    "get_task_logger",
    "in_sighandler",
    "mlevel",
    "reset_multiprocessing_logger",
    "set_in_sighandler",
)

LOG_LEVELS: dict[str, int]
base_logger: Logger
task_logger: Logger
worker_logger: Logger

def get_logger(name: str) -> Logger: ...
def get_multiprocessing_logger() -> Logger | None: ...
def get_task_logger(name: str) -> Logger: ...
def in_sighandler() -> bool: ...
def mlevel(level: int | str) -> int: ...
def reset_multiprocessing_logger() -> None: ...
def set_in_sighandler(value: bool) -> None: ...

class LoggingProxy:
    loglevel: int
    mode: str
    name: str | None
    closed: bool

    def __init__(self, logger: Logger, loglevel: int | None = None) -> None: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def write(self, data: str) -> None: ...
    def writelines(self, sequence: Iterable[str]) -> None: ...

class ColorFormatter(Formatter):
    use_color: bool

    COLORS: ClassVar[dict[str, colored]]
    colors: ClassVar[dict[str, colored]]
    def __init__(self, fmt: str | None = ..., use_color: bool = ...) -> None: ...
    @override
    def formatException(self, ei: _SysExcInfoType) -> str: ...
    @override
    def format(self, record: LogRecord) -> str: ...
