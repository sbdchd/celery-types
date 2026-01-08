from collections.abc import Callable, Iterable, Mapping
from datetime import datetime
from typing import (
    Any,
    Generic,
    overload,
)

__all__ = (
    "Signature",
    "chain",
    "chord",
    "chunks",
    "group",
    "maybe_signature",
    "signature",
    "xmap",
    "xstarmap",
)

import celery.result
import kombu
from celery.app.base import Celery
from celery.app.task import Task
from celery.result import EagerResult
from celery.utils import abstract
from typing_extensions import TypeVar, override

_F = TypeVar("_F", bound=Callable[..., Any])
_R_co = TypeVar("_R_co", covariant=True, default=Any)

class Signature(dict[str, Any], Generic[_R_co]):
    TYPES: dict[str, type[Signature[Any]]]  # ty: ignore[invalid-type-form]

    @classmethod
    def register_type(
        cls, name: str | None = None
    ) -> Callable[[type[Signature[Any]]], type[Signature[Any]]]: ...  # ty: ignore[invalid-type-form]
    @classmethod
    def from_dict(
        cls, d: dict[str, Any], app: Celery | None = ...
    ) -> Signature[Any]: ...
    def __init__(
        self,
        task: Task[Any, _R_co] | str | None = ...,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        options: dict[str, Any] | None = ...,
        type: Any | None = ...,
        subtask_type: Any | None = ...,
        immutable: bool = ...,
        app: Celery | None = ...,
        *,
        # **ex expanded
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        # apply_async options
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> None: ...
    def __call__(self, *partial_args: Any, **partial_kwargs: Any) -> _R_co: ...
    def delay(
        self, *partial_args: Any, **partial_kwargs: Any
    ) -> celery.result.AsyncResult[_R_co]: ...
    def apply(
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        **options: Any,
    ) -> EagerResult[_R_co]: ...
    def apply_async(
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        route_name: str | None = ...,
        **options: Any,
    ) -> celery.result.AsyncResult[_R_co]: ...
    def clone(
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        *,
        # **ex expanded
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        # apply_async options
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> Signature[_R_co]: ...
    partial = clone
    def freeze(
        self,
        _id: str | None = ...,
        group_id: str | None = ...,
        chord: chord | None = ...,
        root_id: str | None = ...,
        parent_id: str | None = ...,
        group_index: int | None = ...,
    ) -> celery.result.AsyncResult[_R_co]: ...
    def replace(
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        options: dict[str, Any] | None = ...,
    ) -> Signature[_R_co]: ...
    def set(
        self,
        immutable: bool | None = ...,
        *,
        # **options expanded
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        # apply_async options
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> Signature[_R_co]: ...
    def set_immutable(self, immutable: bool) -> None: ...
    def append_to_list_option(self, key: str, value: Any) -> Any: ...
    def extend_list_option(self, key: str, value: Any) -> None: ...
    def link(self, callback: _F) -> _F: ...
    def link_error(self, errback: Callable[..., Any]) -> Signature[_R_co]: ...
    def on_error(self, errback: _F) -> _F: ...
    def flatten_links(self) -> list[Signature[Any]]: ...
    def stamp(
        self,
        visitor: Any = ...,
        append_stamps: bool = ...,
        **headers: Any,
    ) -> Any: ...
    def stamp_links(
        self,
        visitor: Any,
        append_stamps: bool = ...,
        **headers: Any,
    ) -> Any: ...
    def __deepcopy__(self, memo: dict[int, Any]) -> Signature[_R_co]: ...
    def __invert__(self) -> Any: ...
    def __json__(self) -> dict[str, Any]: ...
    def reprcall(self, *args: Any, **kwargs: Any) -> str: ...
    # TODO(sbdchd): use overloads to properly type this
    @override
    def __or__(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, other: Signature[Any]
    ) -> Signature[Any]: ...
    def election(self) -> celery.result.AsyncResult[_R_co]: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> Any: ...
    @property
    def app(self) -> Celery: ...
    @property
    def AsyncResult(self) -> celery.result.AsyncResult[_R_co]: ...
    @property
    def id(self) -> str | None: ...
    @property
    def parent_id(self) -> str | None: ...
    @property
    def root_id(self) -> str | None: ...
    @property
    def task(self) -> str | None: ...
    @property
    def args(self) -> tuple[Any, ...]: ...
    @property
    def kwargs(self) -> dict[str, Any]: ...
    @property
    def options(self) -> dict[str, Any]: ...
    @property
    def subtask_type(self) -> Any: ...
    @property
    def immutable(self) -> bool: ...

class _chain(Signature[Any]):
    @property
    def tasks(self) -> tuple[Signature[Any], ...]: ...
    def __init__(
        self,
        *tasks: Signature[Any],
        # Signature extras
        options: dict[str, Any] | None = ...,
        type: Any | None = ...,
        subtask_type: Any | None = ...,
        immutable: bool = ...,
        app: Celery | None = ...,
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> None: ...
    @override
    def apply_async(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        **options: Any,
    ) -> celery.result.AsyncResult[Any]: ...
    def prepare_steps(
        self,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
        tasks: list[Signature[Any]],
        root_id: str | None = None,
        parent_id: str | None = None,
        link_error: Signature[Any] | None = None,
        app: Celery | None = None,
        last_task_id: str | None = None,
        group_id: str | None = None,
        chord_body: Signature[Any] | None = None,
        clone: bool = True,
        from_dict: Callable[[dict[str, Any], Celery | None], Signature[Any]] = ...,
        group_index: int | None = None,
    ) -> tuple[Any, ...]: ...
    def run(
        self,
        args: tuple[Any, ...] | None = None,
        kwargs: dict[str, Any] | None = None,
        group_id: str | None = None,
        chord: chord | None = None,
        task_id: str | None = None,
        link: Signature[Any] | None = None,
        link_error: Signature[Any] | None = None,
        publisher: kombu.Producer | None = None,
        producer: kombu.Producer | None = None,
        root_id: str | None = None,
        parent_id: str | None = None,
        app: Celery | None = None,
        group_index: int | None = None,
        **options: Any,
    ) -> celery.result.AsyncResult[Any]: ...
    def unchain_tasks(self) -> list[Signature[Any]]: ...

class chain(_chain): ...

class _basemap(Signature[Any]):
    def __init__(
        self,
        task: Task[Any, Any] | None,
        it: Iterable[Any],
        *,
        # Signature extras
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        options: dict[str, Any] | None = ...,
        type: Any | None = ...,
        subtask_type: Any | None = ...,
        immutable: bool = ...,
        app: Celery | None = ...,
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> None: ...
    @override
    def apply_async(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        **opts: Any,
    ) -> celery.result.AsyncResult[Any]: ...

class xmap(_basemap): ...
class xstarmap(_basemap): ...

class chunks(Signature[Any]):
    def __init__(
        self,
        task: Task[Any, Any] | None,
        it: Iterable[Any],
        n: int,
        *,
        # Signature extras
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        options: dict[str, Any] | None = ...,
        type: Any | None = ...,
        subtask_type: Any | None = ...,
        immutable: bool = ...,
        app: Celery | None = ...,
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> None: ...
    @classmethod
    def apply_chunks(
        cls,
        task: Task[Any, Any],
        it: Iterable[Any],
        n: int,
        app: Celery | None = ...,
    ) -> list[Any]: ...
    @override
    def __call__(self, **options: Any) -> Any: ...
    @override
    def apply_async(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        **opts: Any,
    ) -> celery.result.AsyncResult[Any]: ...
    def group(self) -> _group: ...

class group(Signature[Any]):
    @property
    def tasks(self) -> list[Signature[Any]]: ...
    @overload
    def __init__(
        self,
        *tasks: group | abstract.CallableSignature | Iterable[Signature[Any]],
        **options: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *tasks: Signature[Any],
        # Signature extras
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        options: dict[str, Any] | None = ...,
        type: Any | None = ...,
        subtask_type: Any | None = ...,
        immutable: bool = ...,
        app: Celery | None = ...,
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> None: ...
    def skew(
        self, start: float = ..., stop: float | None = ..., step: float = ...
    ) -> group: ...
    @override
    def apply_async(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        add_to_parent: bool = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | list[Signature[Any]] | None = ...,
        link_error: Signature[Any] | list[Signature[Any]] | None = ...,
        **options: Any,
    ) -> celery.result.AsyncResult[Any]: ...
    @override
    def link(self, sig: Signature[Any]) -> Signature[Any]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def link_error(self, sig: Signature[Any]) -> Signature[Any]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def stamp(
        self,
        visitor: Any = ...,
        append_stamps: bool = ...,
        **headers: Any,
    ) -> Any: ...
    @override
    def __or__(self, other: Signature[Any]) -> chord: ...  # type: ignore[override]

_group = group

class chord(Signature[Any]):
    @property
    def tasks(self) -> Any: ...
    @property
    def body(self) -> Any: ...
    def __init__(
        self,
        header: Any,
        body: Any | None = ...,
        task: str = ...,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        app: Celery | None = ...,
        *,
        # from Signature
        options: dict[str, Any] | None = ...,
        type: Any | None = ...,
        subtask_type: Any | None = ...,
        immutable: bool = ...,
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        link: Signature[Any] | None = ...,
        link_error: Signature[Any] | None = ...,
        shadow: str | None = ...,
        countdown: float = ...,
        eta: datetime | None = ...,
        expires: float | datetime = ...,
        retry: bool = ...,
        retry_policy: Mapping[str, Any] = ...,
        queue: str | kombu.Queue = ...,
        exchange: str | kombu.Exchange = ...,
        routing_key: str = ...,
        priority: int = ...,
        serializer: str = ...,
        compression: str = ...,
        add_to_parent: bool = ...,
        publisher: kombu.Producer = ...,
        headers: dict[str, str] = ...,
    ) -> None: ...
    def run(
        self,
        header: Any,
        body: Any,
        partial_args: tuple[Any, ...],
        app: Celery | None = ...,
        interval: float | None = ...,
        countdown: int = ...,
        max_retries: int | None = ...,
        eager: bool = ...,
        task_id: str | None = ...,
        kwargs: dict[str, Any] | None = ...,
        **options: Any,
    ) -> Any: ...
    def __length_hint__(self) -> int: ...
    @override
    def apply(
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        propagate: bool = ...,
        body: Signature[Any] | None = ...,
        **options: Any,
    ) -> EagerResult[Any]: ...
    @override
    def apply_async(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        task_id: str | None = ...,
        producer: kombu.Producer | None = ...,
        publisher: kombu.Producer | None = ...,
        connection: kombu.Connection | None = ...,
        router: Any | None = ...,
        result_cls: type[celery.result.AsyncResult[Any]] | None = ...,
        **options: Any,
    ) -> celery.result.AsyncResult[Any]: ...
    @override
    def stamp(
        self,
        visitor: Any = ...,
        append_stamps: bool = ...,
        **headers: Any,
    ) -> Any: ...
    @override
    def __or__(self, other: Signature[Any]) -> chord: ...  # type: ignore[override]
    @override
    def __call__(
        self,
        body: Signature[Any] | None = ...,
        **options: Any,
    ) -> celery.result.AsyncResult[Any]: ...

def signature(
    varies: Signature[Any] | str | dict[str, Any], *args: Any, **kwargs: Any
) -> Signature[Any]: ...

subtask = signature

def maybe_signature(
    d: abstract.CallableSignature | Mapping[str, Any] | None,
    app: Celery | None = ...,
    clone: bool = ...,
) -> abstract.CallableSignature | None: ...

maybe_subtask = maybe_signature
