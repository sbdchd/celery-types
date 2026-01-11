from datetime import datetime
from typing import Any, NamedTuple, TypeAlias

import kombu
import kombu.pools
from celery.app.base import Celery
from celery.app.routes import Router as RouterClass
from kombu.transport.base import StdChannel

__all__ = ("AMQP", "Queues", "task_message")

class task_message(NamedTuple):
    headers: dict[str, Any]
    properties: dict[str, Any]
    body: tuple[Any, ...]
    sent_event: dict[str, Any] | None

class Queues(dict[str, kombu.Queue]):
    def __init__(
        self,
        queues: list[kombu.Queue] | dict[str, kombu.Queue] | None = None,
        default_exchange: kombu.Exchange | None = None,
        create_missing: bool = True,
        create_missing_queue_type: str | None = None,
        create_missing_queue_exchange_type: str | None = None,
        autoexchange: kombu.Exchange | None = None,
        max_priority: int | None = None,
        default_routing_key: str | None = None,
    ) -> None: ...
    def __missing__(self, name: str) -> kombu.Queue: ...
    def add(self, queue: kombu.Queue, **kwargs: Any) -> None: ...
    def add_compat(self, name: str, **options: Any) -> kombu.Queue: ...
    @property
    def consume_from(self) -> dict[str, kombu.Queue]: ...
    def deselect(self, exclude: list[str]) -> None: ...
    def format(self, indent: int = 0, indent_first: bool = True) -> str: ...
    def new_missing(self, name: str) -> kombu.Queue: ...
    def select(self, include: list[str]) -> None: ...
    def select_add(self, queue: kombu.Queue, **kwargs: Any) -> None: ...

# Type alias to avoid conflict with AMQP.Queues method
_Queues: TypeAlias = Queues

class AMQP:
    # Class attributes
    BrokerConnection: type[kombu.Connection]
    Connection: type[kombu.Connection]
    Consumer: type[kombu.Consumer]
    Producer: type[kombu.Producer]
    queues_cls: type[_Queues]
    argsrepr_maxsize: int
    kwargsrepr_maxsize: int
    autoexchange: kombu.Exchange | None

    app: Celery

    def __init__(self, app: Celery) -> None: ...
    def TaskConsumer(
        self,
        channel: StdChannel,
        queues: list[kombu.Queue] | None = None,
        accept: list[str] | None = None,
        **kw: Any,
    ) -> kombu.Consumer: ...
    def Queues(
        self,
        queues: list[kombu.Queue] | dict[str, kombu.Queue],
        create_missing: bool | None = None,
        create_missing_queue_type: str | None = None,
        create_missing_queue_exchange_type: str | None = None,
        autoexchange: kombu.Exchange | None = None,
        max_priority: int | None = None,
    ) -> _Queues: ...
    def Router(
        self,
        queues: _Queues | None = None,
        create_missing: bool | None = None,
    ) -> RouterClass: ...
    def flush_routes(self) -> None: ...
    def as_task_v1(
        self,
        task_id: str,
        name: str,
        args: tuple[Any, ...] | None = None,
        kwargs: dict[str, Any] | None = None,
        countdown: float | None = None,
        eta: datetime | None = None,
        group_id: str | None = None,
        group_index: int | None = None,
        expires: float | datetime | None = None,
        retries: int = 0,
        chord: Any | None = None,
        callbacks: list[Any] | None = None,
        errbacks: list[Any] | None = None,
        reply_to: str | None = None,
        time_limit: int | None = None,
        soft_time_limit: int | None = None,
        create_sent_event: bool = False,
        root_id: str | None = None,
        parent_id: str | None = None,
        shadow: str | None = None,
        now: datetime | None = None,
        timezone: Any | None = None,
        **compat_kwargs: Any,
    ) -> task_message: ...
    def as_task_v2(
        self,
        task_id: str,
        name: str,
        args: tuple[Any, ...] | None = None,
        kwargs: dict[str, Any] | None = None,
        countdown: float | None = None,
        eta: datetime | None = None,
        group_id: str | None = None,
        group_index: int | None = None,
        expires: float | datetime | None = None,
        retries: int = 0,
        chord: Any | None = None,
        callbacks: list[Any] | None = None,
        errbacks: list[Any] | None = None,
        reply_to: str | None = None,
        time_limit: int | None = None,
        soft_time_limit: int | None = None,
        create_sent_event: bool = False,
        root_id: str | None = None,
        parent_id: str | None = None,
        shadow: str | None = None,
        chain: Any | None = None,
        now: datetime | None = None,
        timezone: Any | None = None,
        origin: str | None = None,
        ignore_result: bool = False,
        argsrepr: str | None = None,
        kwargsrepr: str | None = None,
        stamped_headers: list[str] | None = None,
        replaced_task_nesting: int = 0,
        **options: Any,
    ) -> task_message: ...
    @property
    def create_task_message(self) -> Any: ...
    @property
    def default_exchange(self) -> kombu.Exchange: ...
    @property
    def default_queue(self) -> kombu.Queue: ...
    @property
    def producer_pool(self) -> kombu.pools.ProducerPool: ...
    @property
    def publisher_pool(self) -> kombu.pools.ProducerPool: ...
    @property
    def queues(self) -> _Queues: ...
    @property
    def router(self) -> RouterClass: ...
    @property
    def routes(self) -> list[dict[str, Any]]: ...
    @property
    def send_task_message(self) -> Any: ...
    @property
    def utc(self) -> bool: ...
