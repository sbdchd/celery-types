from collections.abc import Callable
from logging import Logger
from typing import Any

__all__ = (
    "TraceInfo",
    "build_tracer",
    "reset_worker_optimizations",
    "setup_worker_optimizations",
    "trace_task",
)

from celery.app.base import Celery
from celery.app.task import Task

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
    ) -> None: ...
    def handle_failure(
        self,
        task: Task[..., Any],
        req: Any,
        store_errors: bool = True,
        call_errbacks: bool = True,
    ) -> None: ...
    def handle_ignore(self, task: Task[..., Any], req: Any) -> None: ...
    def handle_reject(self, task: Task[..., Any], req: Any, **kwargs: Any) -> None: ...
    def handle_retry(
        self,
        task: Task[..., Any],
        req: Any,
        store_errors: bool = True,
        **kwargs: Any,
    ) -> None: ...

def build_tracer(
    name: str,
    task: Task[..., Any],
    loader: Any | None = None,
    hostname: str | None = None,
    store_errors: bool = True,
    Info: type = ...,
    eager: bool = False,
    propagate: bool = False,
    app: Celery | None = None,
    monotonic: Callable[[], float] = ...,
    trace_ok_t: type = ...,
    IGNORE_STATES: frozenset[str] = ...,
) -> Callable[..., Any]: ...
def trace_task(
    task: Task[..., Any],
    uuid: str,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    request: Any | None = None,
    **opts: Any,
) -> TraceInfo: ...
def trace_task_ret(
    name: str,
    uuid: str,
    request: Any,
    body: Any,
    content_type: str,
    content_encoding: str,
    loads: Callable[..., Any] = ...,
    app: Any = None,
    **extra_request: Any,
) -> TraceInfo: ...
def fast_trace_task(
    task: Task[..., Any],
    uuid: str,
    request: Any,
    body: Any,
    content_type: str,
    content_encoding: str,
    loads: Callable[..., Any] = ...,
    _loc: Any = None,
    hostname: str | None = None,
    **extra_request: Any,
) -> TraceInfo: ...
def setup_worker_optimizations(app: Celery, hostname: str | None = None) -> None: ...
def reset_worker_optimizations(app: Any = ...) -> None: ...

logger: Logger
