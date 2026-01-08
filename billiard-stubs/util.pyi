from logging import Logger, _Level
from multiprocessing.util import Finalize as Finalize
from multiprocessing.util import ForkAwareLocal as ForkAwareLocal
from multiprocessing.util import ForkAwareThreadLock as ForkAwareThreadLock
from multiprocessing.util import get_temp_dir as get_temp_dir
from multiprocessing.util import is_exiting as is_exiting
from multiprocessing.util import register_after_fork as register_after_fork

__all__ = [
    "SUBDEBUG",
    "SUBWARNING",
    "Finalize",
    "ForkAwareLocal",
    "ForkAwareThreadLock",
    "debug",
    "get_logger",
    "get_temp_dir",
    "info",
    "is_exiting",
    "log_to_stderr",
    "register_after_fork",
    "sub_debug",
    "sub_warning",
]

SUBDEBUG: int
SUBWARNING: int

def sub_debug(msg: str, *args: object, **kwargs: object) -> None: ...
def debug(msg: str, *args: object, **kwargs: object) -> None: ...
def info(msg: str, *args: object, **kwargs: object) -> None: ...
def sub_warning(msg: str, *args: object, **kwargs: object) -> None: ...
def warning(msg: str, *args: object, **kwargs: object) -> None: ...
def get_logger() -> Logger: ...
def log_to_stderr(level: _Level | None = ...) -> Logger: ...
