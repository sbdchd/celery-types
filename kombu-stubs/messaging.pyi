from collections.abc import Callable, Sequence
from enum import Enum
from types import TracebackType
from typing import Any

from kombu.connection import Connection
from kombu.entity import Exchange, Queue
from kombu.message import Message
from kombu.transport.base import StdChannel
from typing_extensions import Self

__all__ = ("Consumer", "Exchange", "Producer", "Queue")

class Producer:
    channel: Connection | StdChannel | None
    exchange: Exchange | None
    routing_key: str
    serializer: str | None
    compression: str | None
    auto_declare: bool
    on_return: Callable[[Exception, Exchange | str, str, Message], None] | None

    def __init__(
        self,
        channel: Connection | StdChannel,
        exchange: Exchange | str | None = ...,
        routing_key: str | None = ...,
        serializer: str | None = ...,
        auto_declare: bool | None = ...,
        compression: str | None = ...,
        on_return: (
            Callable[[Exception, Exchange | str, str, Message], None] | None
        ) = ...,
    ) -> None: ...
    def declare(self) -> None: ...
    def maybe_declare(
        self, entity: Exchange | Queue, retry: bool = ..., **retry_policy: Any
    ) -> bool: ...
    def publish(
        self,
        body: Any,
        routing_key: str | None = ...,
        delivery_mode: Enum | int | None = ...,
        mandatory: bool = ...,
        immediate: bool = ...,
        priority: int = ...,
        content_type: str | None = ...,
        content_encoding: str | None = ...,
        serializer: str | None = ...,
        headers: dict[Any, Any] | None = ...,
        compression: str | None = ...,
        exchange: Exchange | str | None = ...,
        retry: bool = ...,
        retry_policy: dict[Any, Any] | None = ...,
        declare: Sequence[Exchange | Queue] | None = ...,
        expiration: float | None = ...,
        timeout: float | None = ...,
        confirm_timeout: float | None = ...,
        **properties: Any,
    ) -> None: ...
    def revive(self, channel: StdChannel) -> None: ...
    def close(self) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def __reduce_args__(self) -> tuple[Any, ...]: ...
    def __reduce__(self) -> tuple[Any, ...]: ...
    def _get_channel(self) -> StdChannel: ...
    def _set_channel(self, channel: Connection | StdChannel) -> None: ...
    def _delivery_details(
        self,
        exchange: Exchange | str,
        delivery_mode: int | None = ...,
        maybe_delivery_mode: Callable[..., int | None] = ...,
        Exchange: type[Exchange] = ...,
    ) -> tuple[str, int | None]: ...
    def _prepare(
        self,
        body: Any,
        serializer: str | None = ...,
        content_type: str | None = ...,
        content_encoding: str | None = ...,
        compression: str | None = ...,
        headers: dict[str, Any] | None = ...,
    ) -> tuple[bytes, str, str]: ...
    def _publish(
        self,
        body: bytes,
        priority: int | None,
        content_type: str | None,
        content_encoding: str | None,
        headers: dict[str, Any] | None,
        properties: dict[str, Any],
        routing_key: str,
        mandatory: bool,
        immediate: bool,
        exchange: str,
        declare: list[Any],
        timeout: float | None = ...,
        confirm_timeout: float | None = ...,
        retry: bool = ...,
        retry_policy: dict[str, Any] | None = ...,
    ) -> None: ...
    @property
    def __connection__(self) -> Connection | None: ...
    @property
    def connection(self) -> Connection | None: ...

class Consumer:
    ContentDisallowed: type[Exception]

    channel: Connection | StdChannel | None
    queues: list[Queue]
    accept: set[str] | None
    no_ack: bool | None
    auto_declare: bool
    callbacks: list[Callable[[Any, Message], None]] | None
    on_decode_error: Callable[[Message, Exception], None] | None
    on_message: Callable[[Message], None] | None
    prefetch_count: int | None
    tag_prefix: str

    def __init__(
        self,
        channel: Connection | StdChannel,
        queues: Sequence[Queue] | Queue | None = ...,
        no_ack: bool | None = ...,
        auto_declare: bool | None = ...,
        callbacks: Sequence[Callable[[Any, Message], None]] | None = ...,
        on_decode_error: Callable[[Message, Exception], None] | None = ...,
        on_message: Callable[[Message], None] | None = ...,
        accept: Sequence[str] | None = ...,
        prefetch_count: int | None = ...,
        tag_prefix: str | None = ...,
    ) -> None: ...
    def declare(self) -> None: ...
    def register_callback(self, callback: Callable[[Any, Message], None]) -> None: ...
    def add_queue(self, queue: Queue) -> Self: ...
    def consume(self, no_ack: bool | None = ...) -> None: ...
    def cancel(self) -> None: ...
    close = cancel
    def cancel_by_queue(self, queue: str | Queue) -> None: ...
    def consuming_from(self, queue: str | Queue) -> bool: ...
    def purge(self) -> int: ...
    def flow(self, active: bool) -> None: ...
    def qos(
        self,
        prefetch_size: int = ...,
        prefetch_count: int = ...,
        apply_global: bool = ...,
    ) -> None: ...
    def recover(self, requeue: bool = ...) -> None: ...
    def receive(self, body: Any, message: Message) -> None: ...
    def revive(self, channel: StdChannel) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def _add_tag(self, queue: Queue, consumer_tag: str | None = ...) -> str: ...
    def _basic_consume(
        self,
        queue: Queue,
        consumer_tag: str | None = ...,
        no_ack: bool | None = ...,
        nowait: bool = ...,
    ) -> str: ...
    def _receive_callback(self, message: Message) -> None: ...
    @property
    def connection(self) -> Connection | None: ...
