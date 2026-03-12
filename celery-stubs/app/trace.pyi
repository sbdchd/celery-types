from collections.abc import Callable
from logging import Logger
from typing import Any, NamedTuple

import billiard.einfo
from celery.app.base import Celery
from celery.app.task import Task

__all__ = (
    "TraceInfo",
    "build_tracer",
    "reset_worker_optimizations",
    "setup_worker_optimizations",
    "trace_task",
)

logger: Logger

LOG_RECEIVED: str
LOG_SUCCESS: str
LOG_FAILURE: str
LOG_INTERNAL_ERROR: str
LOG_IGNORED: str
LOG_REJECTED: str
LOG_RETRY: str

class log_policy_t(NamedTuple):
    format: str
    description: str
    severity: int
    traceback: int
    mail: int

class trace_ok_t(NamedTuple):
    retval: Any
    info: TraceInfo | None
    runtime: float | None
    retstr: str | None

log_policy_reject: log_policy_t
log_policy_ignore: log_policy_t
log_policy_internal: log_policy_t
log_policy_expected: log_policy_t
log_policy_unexpected: log_policy_t

send_prerun: Callable[..., list[tuple[Callable[..., Any], Any]]]
send_postrun: Callable[..., list[tuple[Callable[..., Any], Any]]]
send_success: Callable[..., list[tuple[Callable[..., Any], Any]]]

STARTED: str
SUCCESS: str
IGNORED: str
REJECTED: str
RETRY: str
FAILURE: str
EXCEPTION_STATES: frozenset[str]
IGNORE_STATES: frozenset[str]

def info(fmt: str, context: dict[str, Any]) -> None: ...
def task_has_custom(task: Task[..., Any], attr: str) -> Any: ...
def get_log_policy(
    task: Task[..., Any],
    einfo: billiard.einfo.ExceptionInfo,
    exc: BaseException,
) -> log_policy_t: ...
def get_task_name(request: Any, default: str) -> str: ...
def traceback_clear(exc: BaseException | None = None) -> None: ...

class TraceInfo:
    state: str
    retval: Any

    def __init__(self, state: str, retval: Any = None) -> None: ...
    def handle_error_state(
        self,
        task: Task[..., Any],
        req: Any,
        eager: bool = False,
        call_errbacks: bool = True,
    ) -> billiard.einfo.ExceptionInfo: ...
    def handle_failure(
        self,
        task: Task[..., Any],
        req: Any,
        store_errors: bool = True,
        call_errbacks: bool = True,
    ) -> billiard.einfo.ExceptionInfo: ...
    def handle_ignore(self, task: Task[..., Any], req: Any, **kwargs: Any) -> None: ...
    def handle_reject(self, task: Task[..., Any], req: Any, **kwargs: Any) -> None: ...
    def handle_retry(
        self,
        task: Task[..., Any],
        req: Any,
        store_errors: bool = True,
        **kwargs: Any,
    ) -> billiard.einfo.ExceptionInfo: ...

def build_tracer(
    name: str,
    task: Task[..., Any],
    loader: Any | None = None,
    hostname: str | None = None,
    store_errors: bool = True,
    Info: type[TraceInfo] = ...,
    eager: bool = False,
    propagate: bool = False,
    app: Celery | None = None,
    monotonic: Callable[[], float] = ...,
    trace_ok_t: type[trace_ok_t] = ...,
    IGNORE_STATES: frozenset[str] = ...,
) -> Callable[[str, list[Any], dict[str, Any], dict[str, Any] | None], trace_ok_t]: ...
def trace_task(
    task: Task[..., Any],
    uuid: str,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    request: dict[str, Any] | None = None,
    **opts: Any,
) -> trace_ok_t: ...
def trace_task_ret(
    name: str,
    uuid: str,
    request: dict[str, Any],
    body: Any,
    content_type: str | None,
    content_encoding: str | None,
    loads: Callable[..., Any] = ...,
    app: Celery | None = None,
    **extra_request: Any,
) -> tuple[int, Any, float]: ...
def fast_trace_task(
    task: str,
    uuid: str,
    request: dict[str, Any],
    body: Any,
    content_type: str | None,
    content_encoding: str | None,
    loads: Callable[..., Any] = ...,
    _loc: list[Any] | None = None,
    hostname: str | None = None,
    **_: Any,
) -> tuple[int, Any, float]: ...
def report_internal_error(
    task: Task[..., Any],
    exc: BaseException,
) -> billiard.einfo.ExceptionInfo: ...
def setup_worker_optimizations(app: Celery, hostname: str | None = None) -> None: ...
def reset_worker_optimizations(app: Celery = ...) -> None: ...
