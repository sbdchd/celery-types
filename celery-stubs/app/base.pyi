import datetime
from collections import defaultdict
from collections.abc import Callable, Sequence
from types import TracebackType
from typing import (
    Any,
    Concatenate,
    Generic,
    Literal,
    NoReturn,
    overload,
)

__all__ = ("Celery",)

import celery.app
import celery.result
import kombu
from celery.app.amqp import AMQP
from celery.app.control import Control
from celery.app.events import Events
from celery.app.log import Logging
from celery.app.registry import TaskRegistry
from celery.app.routes import Router
from celery.app.task import Context
from celery.app.task import Task as CeleryTask
from celery.app.utils import Settings
from celery.apps.beat import Beat as CeleryBeat
from celery.apps.worker import Worker as CeleryWorker
from celery.backends.base import Backend
from celery.canvas import Signature, chord
from celery.loaders.base import BaseLoader
from celery.schedules import BaseSchedule
from celery.utils.dispatch import Signal
from celery.utils.objects import FallbackContext
from celery.utils.threads import _LocalStack
from celery.worker import WorkController as CeleryWorkController
from typing_extensions import ParamSpec, Self, TypeVar

_T = TypeVar("_T", bound=CeleryTask[Any, Any])
_T_1 = TypeVar("_T_1")
_T_Global = TypeVar(
    "_T_Global",
    bound=CeleryTask[Any, Any],
    default=CeleryTask[Any, Any],
)
_P = ParamSpec("_P")
_R = TypeVar("_R")

class Celery(Generic[_T_Global]):
    # Class-level constants
    IS_WINDOWS: bool
    IS_macOS: bool
    SYSTEM: str
    Pickler: type[Any]

    # Configuration class names
    amqp_cls: str | None
    backend_cls: str | None
    control_cls: str | None
    events_cls: str | None
    loader_cls: str | None
    log_cls: str | None
    registry_cls: str | None
    task_cls: str | None

    # Instance attributes (None at class level)
    main: str | None
    steps: defaultdict[str, set[Any]] | None
    user_options: dict[str, Any] | None
    builtin_fixups: set[str]

    # Signals (always set on instances in __init__)
    on_configure: Signal
    on_after_configure: Signal
    on_after_finalize: Signal
    on_after_fork: Signal

    # Reduce methods for pickling
    def __reduce_args__(self) -> tuple[Any, ...]: ...
    def __reduce_keys__(self) -> dict[str, Any]: ...
    def __reduce_v1__(self) -> tuple[Any, ...]: ...
    def __init__(
        self,
        main: str | None = None,
        loader: Any | None = None,
        backend: str | type[Backend] | None = None,
        amqp: str | type[AMQP] | None = None,
        events: str | type[celery.app.events.Events] | None = None,
        log: str | type[Logging] | None = None,
        control: str | type[celery.app.control.Control] | None = None,
        set_as_current: bool = True,
        tasks: str | type[TaskRegistry] | None = None,
        broker: str | None = None,
        include: list[str] | tuple[str, ...] | None = None,
        changes: dict[str, Any] | None = None,
        config_source: str | object | None = None,
        fixups: list[str] | None = None,
        task_cls: str | type[_T_Global] | None = None,
        autofinalize: bool = True,
        namespace: str | None = None,
        strict_typing: bool = True,
        **kwargs: Any,
    ) -> None: ...
    def _task_from_fun(
        self,
        fun: Callable[_P, _R],
        name: str | None = None,
        base: type[_T_Global] | None = None,
        bind: bool = False,
        pydantic: bool = False,
        pydantic_strict: bool = False,
        pydantic_context: dict[str, Any] | None = None,
        pydantic_dump_kwargs: dict[str, Any] | None = None,
        **options: Any,
    ) -> _T_Global: ...
    def on_init(self) -> None: ...
    def set_current(self) -> None: ...
    def set_default(self) -> None: ...
    def close(self) -> None: ...
    def start(self, argv: list[str] | None = None) -> NoReturn: ...
    def worker_main(self, argv: list[str] | None = None) -> NoReturn: ...
    @overload
    def task(self, fun: Callable[_P, _R]) -> _T_Global: ...
    @overload
    def task(
        self,
        *,
        name: str = ...,
        serializer: str = ...,
        bind: bool = ...,
        autoretry_for: Sequence[type[BaseException]] = ...,
        dont_autoretry_for: Sequence[type[BaseException]] = ...,
        max_retries: int | None = ...,
        default_retry_delay: int = ...,
        acks_late: bool = ...,
        ignore_result: bool = ...,
        soft_time_limit: int = ...,
        time_limit: int = ...,
        base: type[_T],
        retry_kwargs: dict[str, Any] = ...,
        retry_backoff: bool | int = ...,
        retry_backoff_max: int = ...,
        retry_jitter: bool = ...,
        typing: bool = ...,
        rate_limit: str | None = ...,
        trail: bool = ...,
        send_events: bool = ...,
        store_errors_even_if_ignored: bool = ...,
        autoregister: bool = ...,
        track_started: bool = ...,
        acks_on_failure_or_timeout: bool = ...,
        reject_on_worker_lost: bool = ...,
        throws: tuple[type[Exception], ...] = ...,
        expires: float | datetime.datetime | None = ...,
        priority: int | None = ...,
        resultrepr_maxsize: int = ...,
        request_stack: _LocalStack[Context] = ...,
        abstract: bool = ...,
        queue: str = ...,
        after_return: Callable[..., Any] = ...,
        on_retry: Callable[..., Any] = ...,
        **options: Any,
    ) -> Callable[[Callable[..., Any]], _T]: ...
    @overload
    def task(
        self,
        *,
        name: str = ...,
        serializer: str = ...,
        bind: Literal[False] = ...,
        autoretry_for: Sequence[type[BaseException]] = ...,
        dont_autoretry_for: Sequence[type[BaseException]] = ...,
        max_retries: int | None = ...,
        default_retry_delay: int = ...,
        acks_late: bool = ...,
        ignore_result: bool = ...,
        soft_time_limit: int = ...,
        time_limit: int = ...,
        base: None = ...,
        retry_kwargs: dict[str, Any] = ...,
        retry_backoff: bool | int = ...,
        retry_backoff_max: int = ...,
        retry_jitter: bool = ...,
        typing: bool = ...,
        rate_limit: str | None = ...,
        trail: bool = ...,
        send_events: bool = ...,
        store_errors_even_if_ignored: bool = ...,
        autoregister: bool = ...,
        track_started: bool = ...,
        acks_on_failure_or_timeout: bool = ...,
        reject_on_worker_lost: bool = ...,
        throws: tuple[type[Exception], ...] = ...,
        expires: float | datetime.datetime | None = ...,
        priority: int | None = ...,
        resultrepr_maxsize: int = ...,
        request_stack: _LocalStack[Context] = ...,
        abstract: bool = ...,
        queue: str = ...,
        after_return: Callable[..., Any] = ...,
        on_retry: Callable[..., Any] = ...,
        **options: Any,
    ) -> Callable[[Callable[_P, _R]], _T_Global]: ...
    @overload
    def task(
        self,
        *,
        name: str = ...,
        serializer: str = ...,
        bind: Literal[True],
        autoretry_for: Sequence[type[BaseException]] = ...,
        dont_autoretry_for: Sequence[type[BaseException]] = ...,
        max_retries: int | None = ...,
        default_retry_delay: int = ...,
        acks_late: bool = ...,
        ignore_result: bool = ...,
        soft_time_limit: int = ...,
        time_limit: int = ...,
        base: None = ...,
        retry_kwargs: dict[str, Any] = ...,
        retry_backoff: bool | int = ...,
        retry_backoff_max: int = ...,
        retry_jitter: bool = ...,
        typing: bool = ...,
        rate_limit: str | None = ...,
        trail: bool = ...,
        send_events: bool = ...,
        store_errors_even_if_ignored: bool = ...,
        autoregister: bool = ...,
        track_started: bool = ...,
        acks_on_failure_or_timeout: bool = ...,
        reject_on_worker_lost: bool = ...,
        throws: tuple[type[Exception], ...] = ...,
        expires: float | datetime.datetime | None = ...,
        priority: int | None = ...,
        resultrepr_maxsize: int = ...,
        request_stack: _LocalStack[Context] = ...,
        abstract: bool = ...,
        queue: str = ...,
        after_return: Callable[..., Any] = ...,
        on_retry: Callable[..., Any] = ...,
        **options: Any,
    ) -> Callable[[Callable[Concatenate[_T_Global, _P], _R]], _T_Global]: ...
    def type_checker(
        self, fun: Callable[_P, _T_1], bound: bool = False
    ) -> Callable[_P, _T_1]: ...
    def register_task(
        self,
        task: _T | type[_T],
        *,
        autoretry_for: Sequence[type[BaseException]] = ...,
        dont_autoretry_for: Sequence[type[BaseException]] = ...,
        retry_kwargs: dict[str, Any] = ...,
        retry_backoff: bool | int = ...,
        retry_backoff_max: int = ...,
        retry_jitter: bool = ...,
    ) -> _T: ...
    def gen_task_name(self, name: str, module: str) -> str: ...
    def finalize(self, auto: bool = False) -> None: ...
    def add_defaults(self, fun: Callable[[], dict[str, Any]]) -> None: ...
    def config_from_object(
        self,
        obj: Any,
        silent: bool = False,
        force: bool = False,
        namespace: str | None = None,
    ) -> Settings: ...
    def config_from_envvar(
        self, variable_name: str, silent: bool = False, force: bool = False
    ) -> None: ...
    def config_from_cmdline(
        self, argv: list[str], namespace: str = "celery"
    ) -> None: ...
    def setup_security(
        self,
        allowed_serializers: set[str] | None = None,
        key: str | None = None,
        key_password: str | None = None,
        cert: str | None = None,
        store: str | None = None,
        digest: str = "sha256",
        serializer: str = "json",
    ) -> None: ...
    def autodiscover_tasks(
        self,
        packages: list[str] | Callable[[], list[str]] | None = None,
        related_name: str = "tasks",
        force: bool = False,
    ) -> None: ...
    def send_task(
        self,
        name: str,
        args: Sequence[Any] | None = None,
        kwargs: dict[str, Any] | None = None,
        countdown: float | None = None,
        eta: datetime.datetime | None = None,
        task_id: str | None = None,
        producer: kombu.Producer | None = None,
        connection: kombu.Connection | None = None,
        router: Router | None = None,
        result_cls: type[celery.result.AsyncResult[Any]] | None = None,
        expires: float | datetime.datetime | None = None,
        publisher: kombu.Producer | None = None,
        link: Signature[Any] | None = None,
        link_error: Signature[Any] | None = None,
        add_to_parent: bool = True,
        group_id: str | None = None,
        group_index: int | None = None,
        retries: int = 0,
        chord: chord | None = None,
        reply_to: str | None = None,
        time_limit: int | None = None,
        soft_time_limit: int | None = None,
        root_id: str | None = None,
        parent_id: str | None = None,
        route_name: str | None = None,
        shadow: str | None = None,
        chain: Any | None = None,
        task_type: Any | None = None,
        replaced_task_nesting: int = 0,
        **options: Any,
    ) -> celery.result.AsyncResult[Any]: ...
    def connection_for_read(
        self, url: str | None = None, **kwargs: Any
    ) -> kombu.Connection: ...
    def connection_for_write(
        self, url: str | None = None, **kwargs: Any
    ) -> kombu.Connection: ...
    def connection(
        self,
        hostname: str | None = None,
        userid: str | None = None,
        password: str | None = None,
        virtual_host: str | None = None,
        port: int | None = None,
        ssl: bool | dict[str, Any] | None = None,
        connect_timeout: int | None = None,
        transport: str | None = None,
        transport_options: dict[str, Any] | None = None,
        heartbeat: int | None = None,
        login_method: int | None = None,
        failover_strategy: str | Callable[[], Any] | None = None,
        **kwargs: Any,
    ) -> kombu.Connection: ...

    broker_connection = connection

    def connection_or_acquire(
        self,
        connection: kombu.Connection | None = None,
        pool: bool = True,
        *_: Any,
        **__: Any,
    ) -> FallbackContext[Any, Any]: ...

    default_connection = connection_or_acquire

    def producer_or_acquire(
        self, producer: kombu.Producer | None = None
    ) -> FallbackContext[Any, Any]: ...

    default_producer = producer_or_acquire

    def prepare_config(self, c: Settings) -> Settings: ...
    def now(self) -> datetime.datetime: ...
    def select_queues(self, queues: Sequence[str] | None = None) -> None: ...
    def either(self, default_key: str, *defaults: Any) -> Any: ...
    def bugreport(self) -> str: ...
    def signature(self, *args: Any, **kwargs: Any) -> Signature[Any]: ...
    def add_periodic_task(
        self,
        schedule: BaseSchedule | float,
        sig: Signature[Any],
        args: tuple[Any, ...] = (),
        kwargs: tuple[()] = (),  # runtime uses empty tuple
        name: str | None = None,
        **opts: Any,
    ) -> str: ...
    def create_task_cls(self) -> type[Any]: ...
    def subclass_with_self(
        self,
        Class: type[Any],
        name: str | None = None,
        attribute: str = "app",
        reverse: str | None = None,
        keep_reduce: bool = False,
        **kw: Any,
    ) -> type[Any]: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        typ: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    @property
    def Worker(self) -> type[CeleryWorker]: ...
    @property
    def WorkController(self) -> type[CeleryWorkController]: ...
    @property
    def Beat(self) -> type[CeleryBeat]: ...
    @property
    def Task(self) -> type[_T_Global]: ...
    @property
    def annotations(self) -> list[dict[str, Any]]: ...
    @property
    def AsyncResult(self) -> type[celery.result.AsyncResult[Any]]: ...
    @property
    def ResultSet(self) -> type[celery.result.ResultSet]: ...
    @property
    def GroupResult(self) -> type[celery.result.GroupResult]: ...
    @property
    def pool(self) -> kombu.pools.ProducerPool: ...
    @property
    def current_task(self) -> _T_Global | None: ...
    @property
    def current_worker_task(self) -> _T_Global | None: ...
    @property
    def oid(self) -> str: ...
    @property
    def thread_oid(self) -> str: ...
    @property
    def amqp(self) -> AMQP: ...
    @property
    def backend(self) -> Backend: ...
    @property
    def conf(self) -> Settings: ...
    @conf.setter
    def conf(self, d: Any) -> None: ...
    @property
    def control(self) -> Control: ...
    @property
    def events(self) -> Events: ...
    @property
    def loader(self) -> BaseLoader: ...
    @property
    def log(self) -> Logging: ...
    @property
    def tasks(self) -> TaskRegistry: ...
    @property
    def producer_pool(self) -> kombu.pools.ProducerPool: ...
    def uses_utc_timezone(self) -> bool: ...
    @property
    def timezone(self) -> datetime.timezone: ...
