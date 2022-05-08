from datetime import datetime
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar, Union, overload

from celery.app import beat as beat
from celery.app import control as control
from celery.app import events as events
from celery.app import task as task
from celery.app.task import Task as Task
from celery.utils.threads import _LocalStack
from typing_extensions import Concatenate, Literal, ParamSpec

_T = TypeVar("_T", bound=Task[Any, Any])
_P = ParamSpec("_P")
_R = TypeVar("_R")

@overload
def shared_task(fun: Callable[_P, _R]) -> Task[_P, _R]: ...
@overload
def shared_task(
    *,
    name: str = ...,
    serializer: str = ...,
    bind: Literal[False] = ...,
    autoretry_for: Tuple[Type[Exception], ...] = ...,
    max_retries: int = ...,
    default_retry_delay: int = ...,
    acks_late: bool = ...,
    ignore_result: bool = ...,
    soft_time_limit: int = ...,
    time_limit: int = ...,
    base: None = ...,
    retry_kwargs: Dict[str, Any] = ...,
    retry_backoff: Union[bool, int] = ...,
    retry_backoff_max: int = ...,
    retry_jitter: bool = ...,
    typing: bool = ...,
    rate_limit: Optional[str] = ...,
    trail: bool = ...,
    send_events: bool = ...,
    store_errors_even_if_ignored: bool = ...,
    autoregister: bool = ...,
    track_started: bool = ...,
    acks_on_failure_or_timeout: bool = ...,
    reject_on_worker_lost: bool = ...,
    throws: Tuple[Type[Exception], ...] = ...,
    expires: Optional[Union[float, datetime]] = ...,
    priority: Optional[int] = ...,
    resultrepr_maxsize: int = ...,
    request_stack: _LocalStack = ...,
    abstract: bool = ...,
    queue: str = ...,
) -> Callable[[Callable[_P, _R]], Task[_P, _R]]: ...
@overload
def shared_task(
    *,
    name: str = ...,
    serializer: str = ...,
    bind: Literal[True],
    autoretry_for: Tuple[Type[Exception], ...] = ...,
    max_retries: int = ...,
    default_retry_delay: int = ...,
    acks_late: bool = ...,
    ignore_result: bool = ...,
    soft_time_limit: int = ...,
    time_limit: int = ...,
    base: None = ...,
    retry_kwargs: Dict[str, Any] = ...,
    retry_backoff: Union[bool, int] = ...,
    retry_backoff_max: int = ...,
    retry_jitter: bool = ...,
    typing: bool = ...,
    rate_limit: Optional[str] = ...,
    trail: bool = ...,
    send_events: bool = ...,
    store_errors_even_if_ignored: bool = ...,
    autoregister: bool = ...,
    track_started: bool = ...,
    acks_on_failure_or_timeout: bool = ...,
    reject_on_worker_lost: bool = ...,
    throws: Tuple[Type[Exception], ...] = ...,
    expires: Optional[Union[float, datetime]] = ...,
    priority: Optional[int] = ...,
    resultrepr_maxsize: int = ...,
    request_stack: _LocalStack = ...,
    abstract: bool = ...,
    queue: str = ...,
) -> Callable[[Callable[Concatenate[Task[_P, _R], _P], _R]], Task[_P, _R]]: ...
@overload
def shared_task(
    *,
    name: str = ...,
    serializer: str = ...,
    bind: bool = ...,
    autoretry_for: Tuple[Type[Exception], ...] = ...,
    max_retries: int = ...,
    default_retry_delay: int = ...,
    acks_late: bool = ...,
    ignore_result: bool = ...,
    soft_time_limit: int = ...,
    time_limit: int = ...,
    base: Type[_T],
    retry_kwargs: Dict[str, Any] = ...,
    retry_backoff: Union[bool, int] = ...,
    retry_backoff_max: int = ...,
    retry_jitter: bool = ...,
    typing: bool = ...,
    rate_limit: Optional[str] = ...,
    trail: bool = ...,
    send_events: bool = ...,
    store_errors_even_if_ignored: bool = ...,
    autoregister: bool = ...,
    track_started: bool = ...,
    acks_on_failure_or_timeout: bool = ...,
    reject_on_worker_lost: bool = ...,
    throws: Tuple[Type[Exception], ...] = ...,
    expires: Optional[Union[float, datetime]] = ...,
    priority: Optional[int] = ...,
    resultrepr_maxsize: int = ...,
    request_stack: _LocalStack = ...,
    abstract: bool = ...,
    queue: str = ...,
) -> Callable[[Callable[..., Any]], _T]: ...
