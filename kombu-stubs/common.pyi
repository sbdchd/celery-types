from collections.abc import Callable, Generator, Iterable
from contextlib import contextmanager
from typing import Any
from uuid import UUID

from kombu.connection import Connection
from kombu.entity import Exchange, Queue
from kombu.messaging import Consumer, Producer
from kombu.transport.base import StdChannel

__all__ = (
    "Broadcast",
    "collect_replies",
    "drain_consumer",
    "eventloop",
    "insured",
    "itermessages",
    "maybe_declare",
    "send_reply",
    "uuid",
)

class Broadcast(Queue):
    def __init__(
        self,
        name: str | None = ...,
        queue: str | None = ...,
        unique: bool = ...,
        auto_delete: bool = ...,
        exchange: Exchange | None = ...,
        alias: str | None = ...,
        **kwargs: Any,
    ) -> None: ...

class QoS:
    callback: Callable[..., None]
    prev: int | None
    value: int
    max_prefetch: int | None
    _mutex: Any

    def __init__(
        self,
        callback: Callable[..., None],
        initial_value: int,
        max_prefetch: int | None = ...,
    ) -> None: ...
    def update(self) -> int: ...
    def decrement_eventually(self, n: int = ...) -> int: ...
    def increment_eventually(self, n: int = ...) -> int: ...
    def set(self, pcount: int) -> int: ...

@contextmanager
def _ignore_errors(conn: Connection) -> Generator[None, None, None]: ...
def _ensure_channel_is_bound(entity: Any, channel: StdChannel | None) -> StdChannel: ...
def _maybe_declare(entity: Any, channel: StdChannel) -> bool: ...
def _imaybe_declare(
    entity: Any, channel: StdChannel, **retry_policy: Any
) -> Generator[Any, None, bool]: ...
def _ensure_errback(exc: BaseException, interval: float) -> None: ...
def maybe_declare(
    entity: Any,
    channel: StdChannel | None = ...,
    retry: bool = ...,
    **retry_policy: Any,
) -> bool: ...
def uuid(_uuid: Callable[[], UUID] = ...) -> str: ...
def itermessages(
    conn: Connection,
    channel: StdChannel,
    queue: Queue,
    limit: int = ...,
    timeout: float | None = ...,
    callbacks: Iterable[Callable[..., Any]] | None = ...,
    **kwargs: Any,
) -> Generator[tuple[Any, Any], None, None]: ...
def send_reply(
    exchange: Exchange,
    req: Any,
    msg: Any,
    producer: Producer | None = ...,
    retry: bool = ...,
    retry_policy: dict[str, Any] | None = ...,
    **props: Any,
) -> None: ...
def collect_replies(
    conn: Connection,
    channel: StdChannel,
    queue: Queue,
    *args: Any,
    **kwargs: Any,
) -> Generator[Any, None, None]: ...
def insured(
    pool: Any,
    fun: Callable[..., Any],
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    errback: Callable[..., Any] | None = ...,
    on_revive: Callable[..., Any] | None = ...,
    **opts: Any,
) -> Any: ...
def drain_consumer(
    consumer: Consumer,
    limit: int = ...,
    timeout: float | None = ...,
    callbacks: Iterable[Callable[..., Any]] | None = ...,
) -> Generator[tuple[Any, Any], None, None]: ...
def eventloop(
    conn: Connection,
    limit: int | None = ...,
    timeout: float | None = ...,
    ignore_timeouts: bool = ...,
) -> Generator[Any, None, None]: ...
def ignore_errors(
    conn: Connection, fun: Callable[..., Any] | None = ..., *args: Any, **kwargs: Any
) -> Any: ...
def revive_connection(
    connection: Connection,
    channel: StdChannel,
    on_revive: Callable[..., Any] | None = ...,
) -> StdChannel: ...
def declaration_cached(entity: Any, channel: StdChannel) -> bool: ...
def oid_from(instance: Any, threads: bool = ...) -> str: ...
def get_node_id() -> str: ...
def generate_oid(
    node_id: str, process_id: int, thread_id: int, instance: Any
) -> str: ...
