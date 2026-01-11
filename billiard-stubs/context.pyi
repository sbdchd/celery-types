from collections.abc import Callable, Iterable
from ctypes import Array as _CTypesArray
from ctypes import _CData
from logging import Logger
from multiprocessing import (
    AuthenticationError,
    BufferTooShort,
    ProcessError,
    TimeoutError,
)
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

from billiard import process
from billiard.connection import Connection
from billiard.exceptions import (
    SoftTimeLimitExceeded,
    TimeLimitExceeded,
    WorkerLostError,
)
from billiard.pool import Pool as _Pool
from billiard.process import BaseProcess
from typing_extensions import override

__all__: list[str] = []

W_NO_EXECV: str

class BaseContext:
    Process: type[BaseProcess]
    AuthenticationError: type[AuthenticationError]
    BufferTooShort: type[BufferTooShort]
    ProcessError: type[ProcessError]
    TimeoutError: type[TimeoutError]
    SoftTimeLimitExceeded: type[SoftTimeLimitExceeded]
    TimeLimitExceeded: type[TimeLimitExceeded]
    WorkerLostError: type[WorkerLostError]

    def Array(
        self,
        typecode_or_type: str | type[_CData],
        size_or_initializer: int | Iterable[Any],
        *args: Any,
        **kwargs: Any,
    ) -> _CTypesArray[Any]: ...
    def Barrier(
        self,
        parties: int,
        action: Callable[[], Any] | None = ...,
        timeout: float | None = ...,
    ) -> _Barrier: ...
    def BoundedSemaphore(self, value: int = ...) -> _BoundedSemaphore: ...
    def Condition(self, lock: _Lock | _RLock | None = ...) -> _Condition: ...
    def Event(self) -> _Event: ...
    def JoinableQueue(self, maxsize: int = ...) -> _JoinableQueue[Any]: ...
    def Lock(self) -> _Lock: ...
    def Manager(self) -> SyncManager: ...
    def Pipe(
        self, duplex: bool = ..., rnonblock: bool = ..., wnonblock: bool = ...
    ) -> tuple[Connection, Connection]: ...
    def Pool(
        self,
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
    def Queue(self, maxsize: int = ...) -> _Queue[Any]: ...
    def RLock(self) -> _RLock: ...
    def RawArray(
        self,
        typecode_or_type: str | type[_CData],
        size_or_initializer: int | Iterable[Any],
    ) -> _CTypesArray[Any]: ...
    def RawValue(self, typecode_or_type: str | type[_CData], *args: Any) -> Any: ...
    def Semaphore(self, value: int = ...) -> _Semaphore: ...
    def SimpleQueue(self) -> _SimpleQueue[Any]: ...
    def Value(
        self, typecode_or_type: str | type[_CData], *args: Any, **kwargs: Any
    ) -> SynchronizedBase[Any]: ...
    @staticmethod
    def active_children(_cleanup: Callable[[], None] = ...) -> list[BaseProcess]: ...
    def allow_connection_pickling(self) -> None: ...
    def cpu_count(self) -> int: ...
    @staticmethod
    def current_process() -> BaseProcess: ...
    def forking_enable(self, value: bool) -> None: ...
    def forking_is_enabled(self) -> bool: ...
    def freeze_support(self) -> None: ...
    def get_context(self, method: str | None = ...) -> BaseContext: ...
    def get_logger(self) -> Logger: ...
    def get_start_method(self, allow_none: bool = ...) -> str | None: ...
    def log_to_stderr(self, level: int | None = ...) -> Logger: ...
    def set_executable(self, executable: str) -> None: ...
    def set_forkserver_preload(self, module_names: list[str]) -> None: ...
    def set_start_method(self, method: str | None = ...) -> None: ...

class Process(process.BaseProcess): ...

class DefaultContext(BaseContext):
    __all__: list[str]
    def __init__(self, context: BaseContext) -> None: ...
    def get_all_start_methods(self) -> list[str]: ...
    @override
    def set_start_method(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, method: str, force: bool = ...
    ) -> None: ...

class ForkProcess(process.BaseProcess): ...
class SpawnProcess(process.BaseProcess): ...
class ForkServerProcess(process.BaseProcess): ...

class ForkContext(BaseContext):
    Process: type[ForkProcess]  # pyright: ignore[reportIncompatibleVariableOverride]

class SpawnContext(BaseContext):
    Process: type[SpawnProcess]  # pyright: ignore[reportIncompatibleVariableOverride]

class ForkServerContext(BaseContext):
    Process: type[ForkServerProcess]  # pyright: ignore[reportIncompatibleVariableOverride]
