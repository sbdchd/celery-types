from datetime import datetime
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

import celery
import kombu
from celery.app.base import Celery
from celery.app.task import Task
from celery.result import EagerResult
from celery.utils import abstract

_F = TypeVar("_F", bound=Callable[..., Any])

class Signature(Dict[str, Any]):
    def __init__(
        self,
        task: Task | str | None = ...,
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        options: Optional[Dict[str, Any]] = ...,
        type: Optional[Any] = ...,
        subtask_type: Optional[Any] = ...,
        immutable: bool = ...,
        app: Optional[Celery] = ...,
        # **ex expanded
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
        # apply_async options
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
    ) -> None: ...
    def __call__(self, *partial_args: Any, **partial_kwargs: Any) -> Any: ...
    def delay(
        self, *partial_args: Any, **partial_kwargs: Any
    ) -> celery.result.AsyncResult: ...
    def apply(
        self,
        args: Optional[Tuple[Any]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        **options: Dict[str, Any],
    ) -> EagerResult: ...
    def apply_async(
        self,
        args: Optional[Tuple[Any]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        route_name: Optional[str] = ...,
        # options
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
        # apply_async options
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
    ) -> celery.result.AsyncResult: ...
    def clone(
        self,
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        # **ex expanded
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
        # apply_async options
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
    ) -> Signature: ...
    partial = clone
    def freeze(
        self,
        _id: Optional[str] = ...,
        group_id: Optional[str] = ...,
        chord: Optional[chord] = ...,
        root_id: Optional[str] = ...,
        parent_id: Optional[str] = ...,
    ) -> celery.result.AsyncResult: ...
    def replace(
        self,
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        options: Optional[Dict[str, Any]] = ...,
    ) -> Signature: ...
    def set(
        self,
        immutable: Optional[bool] = ...,
        # **options expanded
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
        # apply_async options
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
    ) -> Signature: ...
    def set_immutable(self, immutable: bool) -> None: ...
    def append_to_list_option(self, key: str, value: Any) -> Any: ...
    def extend_list_option(self, key: str, value: Any) -> None: ...
    def link(self, callback: _F) -> _F: ...
    def link_error(self, errback: Callable[..., Any]) -> Signature: ...
    def on_error(self, errback: _F) -> _F: ...
    def flatten_links(self) -> List[Signature]: ...
    # TODO(sbdchd): use overloads to properly type this
    def __or__(self, other: Signature) -> Signature: ...
    def election(self) -> celery.result.AsyncResult: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> Any: ...
    @property
    def app(self) -> Celery: ...
    def AsyncResult(self) -> celery.result.AsyncResult: ...
    id: Optional[str]
    parent_id: Optional[str]
    root_id: Optional[str]
    task: Optional[str]
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    options: Dict[str, Any]
    subtask_type: Any
    chord_size: Optional[int]
    immutable: bool

class _chain(Signature):
    def __init__(
        self,
        *tasks: Signature,
        # Signature extras
        options: Optional[Dict[str, Any]] = ...,
        type: Optional[Any] = ...,
        subtask_type: Optional[Any] = ...,
        immutable: bool = ...,
        app: Optional[Celery] = ...,
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
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
    ) -> None: ...

class chain(_chain): ...

class _basemap(Signature):
    def __init__(
        self,
        task: Optional[Task],
        it: Iterable[Any],
        # Signature extras
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        options: Optional[Dict[str, Any]] = ...,
        type: Optional[Any] = ...,
        subtask_type: Optional[Any] = ...,
        immutable: bool = ...,
        app: Optional[Celery] = ...,
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
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
    ) -> None: ...

class xmap(_basemap): ...
class xstarmap(_basemap): ...

class chunks(Signature):
    def __init__(
        self,
        task: Optional[Task],
        it: Iterable[Any],
        n: int,
        # Signature extras
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        options: Optional[Dict[str, Any]] = ...,
        type: Optional[Any] = ...,
        subtask_type: Optional[Any] = ...,
        immutable: bool = ...,
        app: Optional[Celery] = ...,
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
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
    ) -> None: ...
    def group(self) -> _group: ...

class group(Signature):
    def __init__(
        self,
        *tasks: Signature,
        # Signature extras
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        options: Optional[Dict[str, Any]] = ...,
        type: Optional[Any] = ...,
        subtask_type: Optional[Any] = ...,
        immutable: bool = ...,
        app: Optional[Celery] = ...,
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
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
    ) -> None: ...
    def skew(
        self, start: float = ..., stop: float | None = ..., step: float = ...
    ) -> group: ...
    def __or__(self, other: Signature) -> chord: ...

_group = group

class chord(Signature):
    def __init__(
        self,
        header: Any,
        body: Optional[Any] = ...,
        task: str = ...,
        args: Optional[Tuple[Any, ...]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        app: Optional[Celery] = ...,
        # from Signature
        options: Optional[Dict[str, Any]] = ...,
        type: Optional[Any] = ...,
        subtask_type: Optional[Any] = ...,
        immutable: bool = ...,
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        shadow: Optional[str] = ...,
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
    ) -> None: ...
    def __or__(self, other: Signature) -> chord: ...

def signature(
    varies: Signature | str | Dict[str, Any], *args: Any, **kwargs: Any
) -> Signature: ...

subtask = signature

def maybe_signature(
    d: Optional[Union[abstract.CallableSignature, Mapping[str, Any]]],
    app: Optional[Celery] = ...,
    clone: bool = ...,
) -> Optional[abstract.CallableSignature]: ...

maybe_subtask = maybe_signature
