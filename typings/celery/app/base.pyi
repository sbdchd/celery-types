import datetime
from typing import (
    Any,
    Callable,
    Dict,
    List,
    NoReturn,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import celery
import kombu
from celery.app.amqp import AMQP
from celery.app.beat import Beat as CeleryBeat
from celery.app.control import Control
from celery.app.events import Events
from celery.app.log import Logging
from celery.app.registry import TaskRegistry
from celery.app.routes import Router
from celery.app.task import Task as CeleryTask
from celery.app.utils import Settings
from celery.apps.worker import Worker as CeleryWorker
from celery.backends.base import Backend
from celery.canvas import Signature, chord
from celery.loaders.base import BaseLoader
from celery.schedules import BaseSchedule
from celery.utils.dispatch import Signal
from celery.utils.objects import FallbackContext
from celery.utils.threads import _LocalStack
from celery.worker import WorkController as CeleryWorkController

_T = TypeVar("_T", bound=CeleryTask)

class Celery:
    on_configure: Signal
    on_after_configure: Signal
    on_after_finalize: Signal
    on_after_fork: Signal
    def __init__(
        self,
        main: Optional[str] = ...,
        loader: Optional[Any] = ...,
        backend: Optional[Union[str, Type[Backend]]] = ...,
        amqp: Optional[Union[str, Type[AMQP]]] = ...,
        events: Optional[Union[str, Type[celery.app.events.Events]]] = ...,
        log: Optional[Union[str, Type[Logging]]] = ...,
        control: Optional[Union[str, Type[celery.app.control.Control]]] = ...,
        set_as_current: bool = ...,
        tasks: Optional[Union[str, Type[TaskRegistry]]] = ...,
        broker: Optional[str] = ...,
        include: Optional[List[str]] = ...,
        changes: Optional[Dict[str, Any]] = ...,
        config_source: Optional[Union[str, object]] = ...,
        fixups: Optional[List[str]] = ...,
        task_cls: Optional[Union[str, Type[CeleryTask]]] = ...,
        autofinalize: bool = ...,
        namespace: Optional[str] = ...,
        strict_typing: bool = ...,
    ) -> None: ...
    def _task_from_fun(
        self,
        fun: Callable[..., Any],
        name: Optional[str] = ...,
        base: Optional[CeleryTask] = ...,
        bind: bool = ...,
        # options
        autoretry_for: Tuple[Type[Exception], ...] = ...,
        retry_kwargs: Dict[str, Any] = ...,
        retry_backoff: bool = ...,
        retry_backoff_max: int = ...,
        retry_jitter: bool = ...,
        # from task
        typing: bool = ...,
        max_retries: int = ...,
        default_retry_delay: int = ...,
        rate_limit: Optional[str] = ...,
        ignore_result: bool = ...,
        trail: bool = ...,
        send_events: bool = ...,
        store_errors_even_if_ignored: bool = ...,
        serializer: str = ...,
        time_limit: Optional[int] = ...,
        soft_time_limit: Optional[int] = ...,
        autoregister: bool = ...,
        track_started: bool = ...,
        acks_late: bool = ...,
        acks_on_failure_or_timeout: bool = ...,
        reject_on_worker_lost: bool = ...,
        throws: Tuple[Type[Exception], ...] = ...,
        expires: Optional[Union[float, datetime.datetime]] = ...,
        priority: Optional[int] = ...,
        resultrepr_maxsize: int = ...,
        request_stack: _LocalStack = ...,
        abstract: bool = ...,
    ) -> CeleryTask: ...
    def on_init(self) -> None: ...
    def set_current(self) -> None: ...
    def set_default(self) -> None: ...
    def close(self) -> None: ...
    def start(self, argv: Optional[List[str]] = ...) -> NoReturn: ...
    def worker_main(self, argv: Optional[List[str]] = ...) -> NoReturn: ...
    @overload
    def task(
        self,
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
        retry_backoff: bool = ...,
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
        expires: Optional[Union[float, datetime.datetime]] = ...,
        priority: Optional[int] = ...,
        resultrepr_maxsize: int = ...,
        request_stack: _LocalStack = ...,
        abstract: bool = ...,
    ) -> Callable[[Callable[..., Any]], _T]: ...
    @overload
    def task(
        self,
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
        base: None = ...,
        retry_kwargs: Dict[str, Any] = ...,
        retry_backoff: bool = ...,
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
        expires: Optional[Union[float, datetime.datetime]] = ...,
        priority: Optional[int] = ...,
        resultrepr_maxsize: int = ...,
        request_stack: _LocalStack = ...,
        abstract: bool = ...,
    ) -> Callable[[Callable[..., Any]], CeleryTask]: ...
    def register_task(self, task: CeleryTask) -> CeleryTask: ...
    def gen_task_name(self, name: str, module: object) -> str: ...
    def finalize(self, auto: bool = ...) -> None: ...
    def add_defaults(self, fun: Callable[[], Dict[str, Any]]) -> None: ...
    def config_from_object(
        self,
        obj: Any,
        silent: bool = ...,
        force: bool = ...,
        namespace: Optional[str] = ...,
    ) -> Settings: ...
    def config_from_envvar(
        self, variable_name: str, silent: bool = ..., force: bool = ...
    ) -> None: ...
    def config_from_cmdline(self, argv: List[str], namespace: str = ...) -> None: ...
    def setup_security(
        self,
        allowed_serializers: Optional[Set[str]] = ...,
        key: Optional[str] = ...,
        cert: Optional[str] = ...,
        store: Optional[str] = ...,
        digest: str = ...,
        serializer: str = ...,
    ) -> None: ...
    def autodiscover_tasks(
        self,
        packages: Optional[List[str]] = ...,
        related_name: str = ...,
        force: bool = ...,
    ) -> None: ...
    def send_task(
        self,
        name: str,
        args: Optional[Sequence[Any]] = ...,
        kwargs: Optional[Dict[str, Any]] = ...,
        countdown: Optional[float] = ...,
        eta: Optional[datetime.datetime] = ...,
        task_id: Optional[str] = ...,
        producer: Optional[kombu.Producer] = ...,
        connection: Optional[kombu.Connection] = ...,
        router: Optional[Router] = ...,
        result_cls: Optional[Type[celery.result.AsyncResult]] = ...,
        expires: Optional[Union[float, datetime.datetime]] = ...,
        publisher: Optional[kombu.Producer] = ...,
        link: Optional[Signature] = ...,
        link_error: Optional[Signature] = ...,
        add_to_parent: bool = ...,
        group_id: Optional[str] = ...,
        retries: int = ...,
        chord: Optional[chord] = ...,
        reply_to: Optional[str] = ...,
        time_limit: Optional[int] = ...,
        soft_time_limit: Optional[int] = ...,
        root_id: Optional[str] = ...,
        parent_id: Optional[str] = ...,
        route_name: Optional[str] = ...,
        shadow: Optional[str] = ...,
        chain: Optional[Any] = ...,
        task_type: Optional[Any] = ...,
        # options
        ignore_result: bool = ...,
        **options: Any,
    ) -> celery.result.AsyncResult: ...
    def connection_for_read(
        self, url: Optional[str] = ..., **kwargs: Any
    ) -> kombu.Connection: ...
    def connection_for_write(
        self, url: Optional[str] = ..., **kwargs: Any
    ) -> kombu.Connection: ...
    def connection(
        self,
        hostname: Optional[str] = ...,
        userid: Optional[str] = ...,
        password: Optional[str] = ...,
        virtual_host: Optional[str] = ...,
        port: Optional[int] = ...,
        ssl: Optional[Union[bool, Dict[str, Any]]] = ...,
        connect_timeout: Optional[int] = ...,
        transport: Optional[str] = ...,
        transport_options: Optional[Dict[str, Any]] = ...,
        heartbeat: Optional[int] = ...,
        login_method: Optional[int] = ...,
        failover_strategy: Optional[Union[str, Callable[[], Any]]] = ...,
        **kwargs: Any,
    ) -> kombu.Connection: ...
    broker_connection = connection
    def connection_or_acquire(
        self, connection: Optional[kombu.Connection] = ..., pool: bool = ...
    ) -> FallbackContext: ...
    default_connection = connection_or_acquire
    def producer_or_acquire(
        self, producer: Optional[kombu.Producer] = ...
    ) -> FallbackContext: ...
    default_producer = producer_or_acquire  # XXX compat
    def prepare_config(self, c: Settings) -> Settings: ...
    def now(self) -> datetime.datetime: ...
    def select_queues(self, queues: Optional[Sequence[str]] = ...) -> None: ...
    def either(self, default_key: str, *defaults: Any) -> Any: ...
    def bugreport(self) -> str: ...
    def signature(self, *args: Any, **kwargs: Any) -> Signature: ...
    def add_periodic_task(
        self,
        schedule: BaseSchedule | float,
        sig: Signature,
        args: Tuple[Any, ...] = ...,
        kwargs: Dict[str, Any] = ...,
        name: Optional[str] = ...,
        **opts: Any,
    ) -> str: ...
    def __enter__(self) -> Celery: ...
    def __exit__(self, *exc_info: Any) -> None: ...
    @property
    def Worker(self) -> CeleryWorker: ...
    @property
    def WorkController(self) -> CeleryWorkController: ...
    @property
    def Beat(self) -> CeleryBeat: ...
    @property
    def Task(self) -> CeleryTask: ...
    @property
    def annotations(self) -> List[Dict[str, Any]]: ...
    @property
    def AsyncResult(self) -> celery.result.AsyncResult: ...
    @property
    def ResultSet(self) -> celery.result.ResultSet: ...
    @property
    def GroupResult(self) -> celery.result.GroupResult: ...
    @property
    def pool(self) -> kombu.pools.ProducerPool: ...
    @property
    def current_task(self) -> Optional[CeleryTask]: ...
    @property
    def current_worker_task(self) -> Optional[CeleryTask]: ...
    @property
    def oid(self) -> str: ...
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
