import threading
from .common import TERM_SIGNAL as TERM_SIGNAL, human_status as human_status, pickle_loads as pickle_loads, reset_signals as reset_signals, restart_state as restart_state
from .compat import get_errno as get_errno, mem_rss as mem_rss, send_offset as send_offset
from .dummy import Process as DummyProcess
from .einfo import ExceptionInfo as ExceptionInfo
from .exceptions import CoroStop as CoroStop, RestartFreqExceeded as RestartFreqExceeded, SoftTimeLimitExceeded as SoftTimeLimitExceeded, Terminated as Terminated, TimeLimitExceeded as TimeLimitExceeded, TimeoutError as TimeoutError, WorkerLostError as WorkerLostError
from .util import Finalize as Finalize, debug as debug, warning as warning
from _typeshed import Incomplete
from collections.abc import Generator

MAXMEM_USED_FMT: str
PY3: Incomplete
SIGKILL = TERM_SIGNAL
TIMEOUT_MAX: Incomplete
RUN: int
CLOSE: int
TERMINATE: int
ACK: int
READY: int
TASK: int
NACK: int
DEATH: int
EX_OK: int
EX_FAILURE: int
EX_RECYCLE: int
SIG_SOFT_TIMEOUT: Incomplete
LOST_WORKER_TIMEOUT: float
GUARANTEE_MESSAGE_CONSUMPTION_RETRY_LIMIT: int
GUARANTEE_MESSAGE_CONSUMPTION_RETRY_INTERVAL: float
job_counter: Incomplete
Lock = threading.Lock

class LaxBoundedSemaphore(threading.Semaphore):
    def shrink(self) -> None: ...
    def __init__(self, value: int = 1, verbose: Incomplete | None = None) -> None: ...
    def grow(self) -> None: ...
    def release(self) -> None: ...
    def clear(self) -> None: ...

class MaybeEncodingError(Exception):
    exc: Incomplete
    value: Incomplete
    def __init__(self, exc: object, value: object) -> None: ...

class WorkersJoined(Exception): ...

class Worker:
    initializer: Incomplete
    initargs: Incomplete
    maxtasks: Incomplete
    max_memory_per_child: Incomplete
    on_exit: Incomplete
    sigprotection: Incomplete
    wrap_exception: Incomplete
    on_ready_counter: Incomplete
    def after_fork(self) -> None: ...

class PoolThread(DummyProcess):
    daemon: bool
    def on_stop_not_started(self) -> None: ...
    def stop(self, timeout: Incomplete | None = None) -> None: ...
    def terminate(self) -> None: ...
    def close(self) -> None: ...

class Supervisor(PoolThread):
    pool: Incomplete
    def body(self) -> None: ...

class TaskHandler(PoolThread):
    taskqueue: Incomplete
    put: Incomplete
    outqueue: Incomplete
    pool: Incomplete
    cache: Incomplete
    def body(self) -> None: ...
    def tell_others(self) -> None: ...
    def on_stop_not_started(self) -> None: ...

class TimeoutHandler(PoolThread):
    processes: Incomplete
    cache: Incomplete
    t_soft: Incomplete
    t_hard: Incomplete
    def handle_timeouts(self) -> Generator[None, None, Incomplete]: ...
    def body(self) -> None: ...

class ResultHandler(PoolThread):
    outqueue: Incomplete
    get: Incomplete
    cache: Incomplete
    poll: Incomplete
    join_exited_workers: Incomplete
    putlock: Incomplete
    restart_state: Incomplete
    check_timeouts: Incomplete
    on_job_ready: Incomplete
    on_ready_counters: Incomplete
    def on_stop_not_started(self) -> None: ...
    def handle_event(self, fileno: Incomplete | None = None, events: Incomplete | None = None) -> None: ...
    def body(self) -> None: ...
    def finish_at_shutdown(self, handle_timeouts: bool = False) -> None: ...

class Pool:
    synack: Incomplete
    timeout: Incomplete
    soft_timeout: Incomplete
    lost_worker_timeout: Incomplete
    on_process_up: Incomplete
    on_process_down: Incomplete
    on_timeout_set: Incomplete
    on_timeout_cancel: Incomplete
    threads: Incomplete
    readers: Incomplete
    allow_restart: Incomplete
    enable_timeouts: Incomplete
    max_restarts: Incomplete
    restart_state: Incomplete
    putlocks: Incomplete
    check_timeouts: Incomplete
    def shrink(self, n: int = 1) -> None: ...
    def grow(self, n: int = 1) -> None: ...
    def maintain_pool(self) -> None: ...
    def __reduce__(self) -> None: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
    def restart(self) -> None: ...

class ApplyResult:
    correlation_id: Incomplete
    def discard(self) -> None: ...
    def wait(self, timeout: Incomplete | None = None) -> None: ...
    def handle_timeout(self, soft: bool = False) -> None: ...

class MapResult(ApplyResult): ...

class IMapIterator: ...

class IMapUnorderedIterator(IMapIterator): ...

class ThreadPool(Pool):
    Process = DummyProcess
    def __init__(self) -> None: ...
