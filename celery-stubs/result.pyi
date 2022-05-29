from contextlib import contextmanager
from datetime import datetime
from types import TracebackType
from typing import (
    Any,
    Callable,
    FrozenSet,
    Generic,
    Iterator,
    List,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
)

import kombu
from celery.app.base import Celery
from celery.backends.base import Backend
from celery.utils.graph import DependencyGraph, GraphFormatter
from typing_extensions import Literal
from vine import promise

@contextmanager
def denied_join_result() -> Iterator[None]: ...
@contextmanager
def allow_join_result() -> Iterator[None]: ...

class ResultBase:
    parent: Optional[ResultBase]

_State = Literal["PENDING", "STARTED", "RETRY", "FAILURE", "SUCCESS"]

_R = TypeVar("_R")

class AsyncResult(ResultBase, Generic[_R]):
    app: Celery
    id: str
    backend: Backend
    parent: Optional[ResultBase]
    on_ready: promise
    def __init__(
        self,
        id: str,
        backend: Optional[Backend] = ...,
        task_name: Optional[str] = ...,
        app: Optional[Celery] = ...,
        parent: Optional[ResultBase] = ...,
    ) -> None: ...
    @property
    def ignored(self) -> bool: ...
    @ignored.setter
    def ignored(self, value: bool) -> None: ...
    def then(
        self,
        callback: Callable[..., Any],
        on_error: Optional[Callable[..., Any]] = ...,
        weak: bool = ...,
    ) -> promise: ...
    def as_tuple(
        self,
    ) -> Tuple[int, Optional[Tuple[int, Optional[Any], None]], None]: ...
    def forget(self) -> None: ...
    def revoke(
        self,
        connection: Optional[kombu.Connection] = ...,
        terminate: bool = ...,
        signal: Optional[str] = ...,
        wait: bool = ...,
        timeout: Optional[float] = ...,
    ) -> None: ...
    def get(
        self,
        timeout: Optional[float] = ...,
        propagate: bool = ...,
        interval: float = ...,
        no_ack: bool = ...,
        follow_parents: bool = ...,
        callback: Optional[Callable[..., Any]] = ...,
        on_message: Optional[Callable[..., Any]] = ...,
        on_interval: Optional[Callable[..., Any]] = ...,
        disable_sync_subtasks: bool = ...,
        EXCEPTION_STATES: FrozenSet[str] = ...,
        PROPAGATE_STATES: FrozenSet[str] = ...,
    ) -> _R: ...
    def collect(
        self, intermediate: bool = ..., **kwargs: Any
    ) -> Iterator[Tuple[AsyncResult[Any], object]]: ...
    def get_leaf(self) -> object: ...
    def iterdeps(
        self, intermediate: bool = ...
    ) -> Iterator[Tuple[Optional[AsyncResult[Any]], AsyncResult[Any]]]: ...
    def ready(self) -> bool: ...
    def successful(self) -> bool: ...
    def failed(self) -> bool: ...
    def throw(self, *args: Any, **kwargs: Any) -> None: ...
    def maybe_throw(
        self, propagate: bool = ..., callback: Optional[Callable[..., Any]] = ...
    ) -> object: ...
    def build_graph(
        self, intermediate: bool = ..., formatter: Optional[GraphFormatter] = ...
    ) -> DependencyGraph: ...
    @property
    def graph(self) -> DependencyGraph: ...
    @property
    def supports_native_join(self) -> bool: ...
    @property
    def children(
        self,
    ) -> Optional[
        List[Tuple[int, Optional[Tuple[int, Optional[Any], None]], None]]
    ]: ...
    @property
    def result(self) -> _R | BaseException: ...
    @property
    def info(self) -> Any: ...
    @property
    def traceback(self) -> Optional[TracebackType]: ...
    @property
    def state(self) -> _State: ...
    @property
    def status(
        self,
    ) -> _State: ...
    @property
    def task_id(self) -> str: ...
    @task_id.setter
    def task_id(self, id: str) -> None: ...
    @property
    def name(self) -> Optional[str]: ...
    @property
    def args(self) -> Optional[Tuple[Any, ...]]: ...
    @property
    def kwargs(self) -> Optional[Mapping[str, Any]]: ...
    @property
    def worker(self) -> Optional[str]: ...
    @property
    def date_done(self) -> Optional[datetime]: ...
    @property
    def retries(self) -> Optional[int]: ...
    @property
    def queue(self) -> Optional[str]: ...

class EagerResult(AsyncResult[_R]): ...
class ResultSet(ResultBase): ...
class GroupResult(ResultSet): ...
