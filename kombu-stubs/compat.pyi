from collections.abc import Generator, Iterable, Iterator
from types import TracebackType
from typing import Any

from kombu.connection import Connection
from kombu.entity import Exchange, Queue
from kombu.message import Message
from kombu.messaging import Consumer as _Consumer
from kombu.messaging import Producer
from kombu.transport.base import StdChannel
from typing_extensions import Self, override

__all__ = ("Consumer", "Publisher")

def entry_to_queue(queue: str, **options: Any) -> Queue: ...

class Publisher(Producer):
    exchange: Exchange | str  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]
    exchange_type: str
    routing_key: str
    durable: bool
    auto_delete: bool
    _closed: bool

    def __init__(
        self,
        connection: Connection | StdChannel,
        exchange: str | Exchange | None = ...,
        routing_key: str | None = ...,
        exchange_type: str | None = ...,
        durable: bool | None = ...,
        auto_delete: bool | None = ...,
        channel: StdChannel | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def send(self, *args: Any, **kwargs: Any) -> Any: ...
    @override
    def close(self) -> None: ...
    @override
    def __enter__(self) -> Self: ...
    @override
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    @property
    def backend(self) -> StdChannel: ...

class Consumer(_Consumer):
    queue: str
    exchange: str
    routing_key: str
    exchange_type: str
    durable: bool
    exclusive: bool
    auto_delete: bool
    backend: StdChannel
    _closed: bool

    def __init__(
        self,
        connection: Connection,
        queue: str | None = ...,
        exchange: str | None = ...,
        routing_key: str | None = ...,
        exchange_type: str | None = ...,
        durable: bool | None = ...,
        exclusive: bool | None = ...,
        auto_delete: bool | None = ...,
        **kwargs: Any,
    ) -> None: ...
    @override
    def revive(self, channel: StdChannel) -> None: ...
    @override
    def close(self) -> None: ...
    @override
    def __enter__(self) -> Self: ...
    @override
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def __iter__(self) -> Iterator[Message | None]: ...
    def fetch(
        self, no_ack: bool | None = ..., enable_callbacks: bool = ...
    ) -> Message | None: ...
    def process_next(self) -> None: ...
    def discard_all(self, filterfunc: Any = ...) -> int: ...
    def iterconsume(
        self, limit: int | None = ..., no_ack: bool | None = ...
    ) -> Generator[Any, None, None]: ...
    def wait(self, limit: int | None = ...) -> list[Any]: ...
    def iterqueue(
        self, limit: int | None = ..., infinite: bool = ...
    ) -> Generator[Message | None, None, None]: ...

class ConsumerSet(_Consumer):
    backend: StdChannel
    _provided_channel: bool

    def __init__(
        self,
        connection: Connection,
        from_dict: dict[str, dict[str, Any]] | None = ...,
        consumers: Iterable[_Consumer] | None = ...,
        channel: StdChannel | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def iterconsume(
        self, limit: int | None = ..., no_ack: bool = ...
    ) -> Generator[Any, None, None]: ...
    def discard_all(self) -> int: ...
    def add_consumer_from_dict(self, queue: str, **options: Any) -> Queue: ...
    def add_consumer(self, consumer: _Consumer) -> None: ...
    @override
    def revive(self, channel: StdChannel) -> None: ...
    @override
    def close(self) -> None: ...
