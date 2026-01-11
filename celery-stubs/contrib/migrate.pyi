from collections.abc import Callable, Container, Mapping, Sequence
from functools import partial
from typing import Any, TypeVar

import kombu
from celery import Celery
from celery.utils.nodenames import worker_direct
from kombu import Consumer, Message, Producer, Queue

__all__ = (
    "State",
    "StopFiltering",
    "migrate_task",
    "migrate_tasks",
    "move",
    "move_by_idmap",
    "move_by_taskmap",
    "move_direct",
    "move_direct_by_id",
    "move_task_by_id",
    "republish",
    "start_filter",
    "task_id_eq",
    "task_id_in",
)

class StopFiltering(Exception): ...

class State:
    count: int = 0
    filtered: int = 0
    total_apx: int = 0

    @property
    def strtotal(self) -> str: ...

def republish(
    producer: Producer,
    message: Message,
    exchange: float | None = None,
    routing_key: str | None = None,
    remove_props: list[str] | None = None,
) -> None: ...
def migrate_task(
    producer: Producer,
    body_: Mapping[str, Any],
    message: Message,
    queues: Mapping[str, Any] | None = None,
) -> None: ...

_T = TypeVar("_T")

def filter_callback(
    callback: Callable[[Mapping[str, Any], Message], _T],
    tasks: Container[str],
) -> Callable[[Mapping[str, Any], Message], _T | None]: ...
def migrate_tasks(
    source: Sequence[str],
    dest: str | Queue,
    migrate: Callable[..., Any] = ...,
    app: Celery[Any] | None = None,
    queues: str | list[str] | dict[str, str] | None = None,
    **kwargs: Any,
) -> State: ...
def move(
    predicate: Callable[[Any, Any], Any],
    connection: kombu.Connection | None = None,
    exchange: str | kombu.Exchange | None = None,
    routing_key: str | None = None,
    source: Sequence[str] | None = None,
    app: Celery[Any] | None = None,
    callback: Callable[[Any, Any, Any], Any] | None = None,
    limit: int | None = None,
    transform: Callable[[Any], Any] | None = None,
    **kwargs: Any,
) -> State: ...
def expand_dest(
    ret: tuple[str | kombu.Exchange, str],
    exchange: str | kombu.Exchange,
    routing_key: str,
) -> tuple[str | kombu.Exchange, str]: ...
def task_id_eq(task_id: str, body: Mapping[str, Any], message: Message) -> bool: ...
def task_id_in(
    ids: Container[str], body: Mapping[str, Any], message: Message
) -> bool: ...
def prepare_queues(
    queues: str | list[str] | dict[str, str] | None,
) -> dict[str, str]: ...

class Filterer:
    def __init__(
        self,
        app: Celery[Any],
        conn: kombu.Connection,
        filter: Callable[[Any, Any], Any],
        limit: int | None = None,
        timeout: float = 1.0,
        ack_messages: bool = False,
        tasks: str | None = None,
        queues: str | list[str] | dict[str, str] | None = None,
        callback: Callable[..., Any] | None = None,
        forever: bool = False,
        on_declare_queue: Callable[[Queue], None] | None = None,
        consume_from: Container[str] | None = None,
        state: State | None = None,
        accept: Sequence[str] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def start(self) -> State: ...
    def update_state(self, body: Mapping[str, Any], message: Message) -> None: ...
    def ack_message(self, body: Mapping[str, Any], message: Message) -> None: ...
    def create_consumer(self) -> Consumer: ...
    def prepare_consumer(self, consumer: Consumer) -> Consumer: ...
    def declare_queues(self, consumer: Consumer) -> None: ...

def start_filter(
    app: Celery[Any],
    conn: kombu.Connection | None,
    filter: Callable[[Any, Any], Any],
    limit: int | None = None,
    timeout: float = 1.0,
    ack_messages: bool = False,
    tasks: str | None = None,
    queues: str | list[str] | dict[str, str] | None = None,
    callback: Callable[..., Any] | None = None,
    forever: bool = False,
    on_declare_queue: Callable[[Queue], None] | None = None,
    consume_from: Container[str] | None = None,
    state: State | None = None,
    accept: Sequence[str] | None = None,
    **kwargs: Any,
) -> State: ...
def move_task_by_id(task_id: str, dest: str | Queue, **kwargs: Any) -> State: ...
def move_by_idmap(map: Mapping[str, Any], **kwargs: Any) -> State: ...
def move_by_taskmap(map: Mapping[str, Any], **kwargs: Any) -> State: ...
def filter_status(
    state: State, body: Mapping[str, Any], message: Message, **kwargs: Any
) -> None: ...

move_direct = partial(move, transform=worker_direct)
move_direct_by_id = partial(move_task_by_id, transform=worker_direct)
move_direct_by_idmap = partial(move_by_idmap, transform=worker_direct)
move_direct_by_taskmap = partial(move_by_taskmap, transform=worker_direct)
