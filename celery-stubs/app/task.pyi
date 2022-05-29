from datetime import datetime
from typing import (
    Any,
    Dict,
    Generic,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import billiard
import celery
import kombu
from celery import canvas
from celery.app.base import Celery
from celery.backends.base import Backend
from celery.canvas import Signature, xmap, xstarmap
from celery.exceptions import Retry
from celery.result import EagerResult
from celery.utils.threads import _LocalStack
from celery.worker.request import Request
from typing_extensions import Literal, ParamSpec

_P = ParamSpec("_P")
_R = TypeVar("_R")

class Task(Generic[_P, _R]):
    name: str
    typing: bool
    max_retries: int
    default_retry_delay: int
    rate_limit: Optional[str]
    ignore_result: bool
    trail: bool
    send_events: bool
    store_errors_even_if_ignored: bool
    serializer: str
    time_limit: Optional[int]
    soft_time_limit: Optional[int]
    autoregister: bool
    track_started: bool
    acks_late: bool
    acks_on_failure_or_timeout: bool
    reject_on_worker_lost: bool
    throws: Tuple[Type[Exception], ...]
    expires: Optional[Union[float, datetime]]
    priority: Optional[int]
    resultrepr_maxsize: int
    request_stack: _LocalStack
    abstract: bool
    @classmethod
    def bind(cls, app: Celery) -> Celery: ...
    @classmethod
    def on_bound(cls, app: Celery) -> None: ...
    @property
    def app(self) -> Celery: ...
    @classmethod
    def annotate(cls) -> None: ...
    @classmethod
    def add_around(cls, attr: str, around: Any) -> None: ...
    # TODO(sbdchd): might be able to use overloads to handle the case where
    # `bind=True` passes in the first argument.
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...
    def run(self, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...
    def start_strategy(self, app: Celery, consumer: Any, **kwargs: Any) -> Any: ...
    def delay(
        self, *args: _P.args, **kwargs: _P.kwargs
    ) -> celery.result.AsyncResult[_R]: ...
    def apply_async(
        self,
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature[Any]] = ...,
        link_error: Optional[Signature[Any]] = ...,
        shadow: Optional[str] = ...,
        # options
        countdown: float = ...,
        eta: datetime = ...,
        expires: Union[float, datetime] = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: Union[str, kombu.Queue] = ...,
        exchange: Union[str, kombu.Exchange] = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: Dict[str, str] = ...,
    ) -> celery.result.AsyncResult[_R]: ...
    def shadow_name(
        self, args: Tuple[Any, ...], kwargs: Dict[str, Any], options: Dict[str, Any]
    ) -> None: ...
    def signature_from_request(
        self,
        request: Optional[Request] = ...,
        args: Tuple[Any, ...] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        queue: Optional[str] = ...,
        **extra_options: Any
    ) -> Signature[_R]: ...
    subtask_from_request = signature_from_request  # XXX compat
    def retry(
        self,
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        exc: Optional[Exception] = ...,
        throw: bool = ...,
        eta: Optional[datetime] = ...,
        countdown: Optional[float] = ...,
        max_retries: Optional[int] = ...,
        # options
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature[Any]] = ...,
        link_error: Optional[Signature[Any]] = ...,
        shadow: Optional[str] = ...,
        expires: Union[float, datetime] = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: Union[str, kombu.Queue] = ...,
        exchange: Union[str, kombu.Exchange] = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: Dict[str, str] = ...,
    ) -> Retry: ...
    def apply(
        self,
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        link: Optional[Signature[Any]] = ...,
        link_error: Optional[Signature[Any]] = ...,
        task_id: Optional[str] = ...,
        retries: Optional[int] = ...,
        throw: Optional[bool] = ...,
        logfile: Optional[str] = ...,
        loglevel: Optional[str] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> EagerResult[_R]: ...
    def AsyncResult(
        self, task_id: str, **kwargs: Any
    ) -> celery.result.AsyncResult[_R]: ...
    def signature(
        self, args: Optional[Tuple[Any, ...]] = ..., *starargs: Any, **starkwargs: Any
    ) -> Signature[_R]: ...
    def subtask(
        self, args: Optional[Tuple[Any, ...]] = ..., *starargs: Any, **starkwargs: Any
    ) -> Signature[_R]: ...
    def s(self, *args: Any, **kwargs: Any) -> Signature[_R]: ...
    def si(self, *args: Any, **kwargs: Any) -> Signature[_R]: ...
    def chunks(self, it: Iterable[Any], n: int) -> canvas.chunks: ...
    def map(self, it: Iterable[Any]) -> xmap: ...
    def starmap(self, it: Iterable[Any]) -> xstarmap: ...
    def send_event(
        self,
        type_: str,
        retry: bool = ...,
        retry_policy: Optional[Mapping[str, int]] = ...,
        **fields: Mapping[str, Any]
    ) -> List[Tuple[object, object]]: ...
    def replace(self, sig: Signature[Any]) -> None: ...
    @overload
    def add_to_chord(
        self, sig: Signature[Any], lazy: Literal[True]
    ) -> celery.result.AsyncResult[Any]: ...
    @overload
    def add_to_chord(
        self, sig: Signature[Any], lazy: Literal[False] = ...
    ) -> EagerResult[Any]: ...
    def update_state(
        self,
        task_id: Optional[str] = ...,
        state: Optional[str] = ...,
        meta: Optional[Dict[str, Any]] = ...,
        **kwargs: Any
    ) -> None: ...
    def on_success(
        self, retval: Any, task_id: str, args: Tuple[Any, ...], kwargs: Dict[str, Any]
    ) -> None: ...
    def on_retry(
        self,
        exc: Exception,
        task_id: str,
        args: Tuple[Any, ...],
        kwargs: Dict[str, Any],
        einfo: billiard.einfo.ExceptionInfo,
    ) -> None: ...
    def on_failure(
        self,
        exc: Exception,
        task_id: str,
        args: Tuple[Any, ...],
        kwargs: Dict[str, Any],
        einfo: billiard.einfo.ExceptionInfo,
    ) -> None: ...
    def after_return(
        self,
        status: str,
        retval: Any,
        task_id: str,
        args: Tuple[Any, ...],
        kwargs: Dict[str, Any],
        einfo: billiard.einfo.ExceptionInfo,
    ) -> None: ...
    def add_trail(self, result: Any) -> Any: ...
    def push_request(self, *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    def pop_request(self) -> None: ...
    @property
    def request(self) -> Request: ...
    @property
    def backend(self) -> Backend: ...
    @backend.setter
    def backend(self, value: Backend) -> None: ...
    @property
    def __name__(self) -> str: ...
