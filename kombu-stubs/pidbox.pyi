from collections.abc import Callable, Sequence
from contextlib import contextmanager
from typing import Any, Generator, Type, TypeAlias

from kombu.connection import Connection
from kombu.entity import Exchange, Queue
from kombu.message import Message
from kombu.messaging import Consumer, Producer
from kombu.transport.base import StdChannel
from kombu.utils.objects import cached_property

__all__ = ("Node", "Mailbox")

_ConsumerType: TypeAlias = Consumer
_NodeType: TypeAlias = "Node"

class Node:
    hostname: str | None
    state: Any | None
    channel: StdChannel | None
    handlers: dict[str, Callable[..., Any]] | None
    mailbox: Mailbox | None

    def __init__(
        self,
        hostname: str | None,
        state: Any | None = ...,
        channel: StdChannel | None = ...,
        handlers: dict[str, Callable[..., Any]] | None = ...,
        mailbox: Mailbox | None = ...,
    ) -> None: ...
    def Consumer(
        self,
        channel: StdChannel | None = ...,
        no_ack: bool = ...,
        accept: Sequence[str] | None = ...,
        **options: Any,
    ) -> _ConsumerType: ...
    def handler(self, fun: Callable[..., Any]) -> Callable[..., Any]: ...
    def listen(
        self,
        channel: StdChannel | None = ...,
        callback: Callable[..., Any] | None = ...,
    ) -> _ConsumerType: ...
    def dispatch(
        self,
        method: str,
        arguments: dict[str, Any] | None = ...,
        reply_to: dict[str, Any] | None = ...,
        ticket: str | None = ...,
        **kwargs: Any,
    ) -> Any: ...
    def dispatch_from_message(
        self, body: Any, message: Message | None = ...
    ) -> None: ...
    def handle_message(self, body: Any, message: Message | None = ...) -> None: ...
    def handle(self, method: str, arguments: dict[str, Any] | None = ...) -> Any: ...
    def handle_call(self, method: str, arguments: dict[str, Any] | None) -> Any: ...
    def handle_cast(self, method: str, arguments: dict[str, Any] | None) -> Any: ...
    def reply(
        self,
        data: Any,
        exchange: Exchange | str,
        routing_key: str,
        ticket: str | None,
        **kwargs: Any,
    ) -> None: ...
    def on_decode_error(self, message: Message, exc: Exception) -> None: ...

class Mailbox:
    namespace: str | None
    connection: Connection | None
    type: str
    exchange: Exchange | None
    exchange_fmt: str
    reply_exchange: Exchange | None
    reply_exchange_fmt: str
    accept: list[str]
    serializer: str | None
    producer_pool: Any | None
    queue_ttl: float | None
    queue_expires: float | None
    queue_durable: bool
    queue_exclusive: bool
    reply_queue_ttl: float | None
    reply_queue_expires: float | None
    node_cls: Type[_NodeType]

    def __init__(
        self,
        namespace: str,
        type: str = ...,
        connection: Connection | None = ...,
        clock: Any | None = ...,
        accept: Sequence[str] | None = ...,
        serializer: str | None = ...,
        producer_pool: Any | None = ...,
        queue_ttl: float | None = ...,
        queue_expires: float | None = ...,
        queue_durable: bool = ...,
        queue_exclusive: bool = ...,
        reply_queue_ttl: float | None = ...,
        reply_queue_expires: float | None = ...,
    ) -> None: ...
    def __call__(self, connection: Connection) -> _NodeType: ...
    def Node(
        self,
        hostname: str | None = ...,
        state: Any | None = ...,
        channel: StdChannel | None = ...,
        handlers: dict[str, Callable[..., Any]] | None = ...,
    ) -> _NodeType: ...
    def get_queue(self, hostname: str) -> Queue: ...
    def get_reply_queue(self) -> Queue: ...
    @contextmanager
    def producer_or_acquire(
        self, producer: Producer | None = ..., channel: StdChannel | None = ...
    ) -> Generator[Producer, None, None]: ...
    def call(
        self,
        destination: Sequence[str],
        command: str,
        kwargs: dict[str, Any] | None = ...,
        timeout: float | None = ...,
        callback: Callable[..., Any] | None = ...,
        channel: StdChannel | None = ...,
    ) -> list[Any] | None: ...
    def cast(
        self,
        destination: Sequence[str],
        command: str,
        kwargs: dict[str, Any] | None = ...,
    ) -> None: ...
    def abcast(self, command: str, kwargs: dict[str, Any] | None = ...) -> None: ...
    def multi_call(
        self,
        command: str,
        kwargs: dict[str, Any] | None = ...,
        timeout: float = ...,
        limit: int | None = ...,
        callback: Callable[..., Any] | None = ...,
        channel: StdChannel | None = ...,
    ) -> list[Any] | None: ...
    @property
    def oid(self) -> str: ...
    @cached_property
    def reply_queue(self) -> Queue: ...
