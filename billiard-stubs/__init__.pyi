from collections.abc import Callable, Iterable
from ctypes import Array as _CTypesArray
from ctypes import _CData
from logging import Logger
from multiprocessing import (
    AuthenticationError as AuthenticationError,
)
from multiprocessing import (
    BufferTooShort as BufferTooShort,
)
from multiprocessing import (
    ProcessError as ProcessError,
)
from multiprocessing import (
    TimeoutError as TimeoutError,
)
from multiprocessing.context import BaseContext
from multiprocessing.managers import SyncManager
from multiprocessing.queues import (
    JoinableQueue as _JoinableQueue,
)
from multiprocessing.queues import (
    Queue as _Queue,
)
from multiprocessing.queues import (
    SimpleQueue as _SimpleQueue,
)
from multiprocessing.sharedctypes import SynchronizedBase
from multiprocessing.synchronize import (
    Barrier as _Barrier,
)
from multiprocessing.synchronize import (
    BoundedSemaphore as _BoundedSemaphore,
)
from multiprocessing.synchronize import (
    Condition as _Condition,
)
from multiprocessing.synchronize import (
    Event as _Event,
)
from multiprocessing.synchronize import (
    Lock as _Lock,
)
from multiprocessing.synchronize import (
    RLock as _RLock,
)
from multiprocessing.synchronize import (
    Semaphore as _Semaphore,
)
from typing import Any

from billiard import einfo as einfo
from billiard import exceptions as exceptions
from billiard.connection import Connection
from billiard.context import Process as Process
from billiard.exceptions import (
    SoftTimeLimitExceeded as SoftTimeLimitExceeded,
)
from billiard.exceptions import (
    TimeLimitExceeded as TimeLimitExceeded,
)
from billiard.exceptions import (
    WorkerLostError as WorkerLostError,
)
from billiard.pool import Pool as _Pool
from billiard.process import active_children as active_children
from billiard.process import current_process as current_process

__all__ = [
    "Array",
    "AuthenticationError",
    "Barrier",
    "BoundedSemaphore",
    "BufferTooShort",
    "Condition",
    "Event",
    "JoinableQueue",
    "Lock",
    "Manager",
    "Pipe",
    "Pool",
    "Process",
    "ProcessError",
    "Queue",
    "RLock",
    "RawArray",
    "RawValue",
    "Semaphore",
    "SimpleQueue",
    "SoftTimeLimitExceeded",
    "TimeLimitExceeded",
    "TimeoutError",
    "Value",
    "WorkerLostError",
    "active_children",
    "allow_connection_pickling",
    "cpu_count",
    "current_process",
    "forking_enable",
    "forking_is_enabled",
    "freeze_support",
    "get_all_start_methods",
    "get_context",
    "get_logger",
    "get_start_method",
    "log_to_stderr",
    "set_executable",
    "set_forkserver_preload",
    "set_start_method",
]

def Array(
    typecode_or_type: str | type[_CData],
    size_or_initializer: int | Iterable[Any],
    *args: Any,
    **kwargs: Any,
) -> _CTypesArray[Any]: ...
def Barrier(
    parties: int, action: Callable[[], Any] | None = ..., timeout: float | None = ...
) -> _Barrier: ...
def BoundedSemaphore(value: int = ...) -> _BoundedSemaphore: ...
def Condition(lock: _Lock | _RLock | None = ...) -> _Condition: ...
def Event() -> _Event: ...
def JoinableQueue(maxsize: int = ...) -> _JoinableQueue[Any]: ...
def Lock() -> _Lock: ...
def Manager() -> SyncManager: ...
def Pipe(
    duplex: bool = ..., rnonblock: bool = ..., wnonblock: bool = ...
) -> tuple[Connection, Connection]: ...
def Pool(
    processes: int | None = ...,
    initializer: Callable[..., Any] | None = ...,
    initargs: tuple[Any, ...] = ...,
    maxtasksperchild: int | None = ...,
    timeout: float | None = ...,
    soft_timeout: float | None = ...,
    lost_worker_timeout: float | None = ...,
    max_restarts: int | None = ...,
    max_restart_freq: int = ...,
    on_process_up: Callable[..., Any] | None = ...,
    on_process_down: Callable[..., Any] | None = ...,
    on_timeout_set: Callable[..., Any] | None = ...,
    on_timeout_cancel: Callable[..., Any] | None = ...,
    threads: bool = ...,
    semaphore: Any | None = ...,
    putlocks: bool = ...,
    allow_restart: bool = ...,
) -> _Pool: ...
def Queue(maxsize: int = ...) -> _Queue[Any]: ...
def RLock() -> _RLock: ...
def RawArray(
    typecode_or_type: str | type[_CData], size_or_initializer: int | Iterable[Any]
) -> _CTypesArray[Any]: ...
def RawValue(typecode_or_type: str | type[_CData], *args: Any) -> Any: ...
def Semaphore(value: int = ...) -> _Semaphore: ...
def SimpleQueue() -> _SimpleQueue[Any]: ...
def Value(
    typecode_or_type: str | type[_CData], *args: Any, **kwargs: Any
) -> SynchronizedBase[Any]: ...
def allow_connection_pickling() -> None: ...
def cpu_count() -> int: ...
def forking_enable(value: bool) -> None: ...
def forking_is_enabled() -> bool: ...
def freeze_support() -> None: ...
def get_all_start_methods() -> list[str]: ...
def get_context(method: str | None = ...) -> BaseContext: ...
def get_logger() -> Logger: ...
def get_start_method(allow_none: bool = ...) -> str | None: ...
def log_to_stderr(level: int | None = ...) -> Logger: ...
def set_executable(executable: str) -> None: ...
def set_forkserver_preload(module_names: list[str]) -> None: ...
def set_start_method(method: str, force: bool = ...) -> None: ...
