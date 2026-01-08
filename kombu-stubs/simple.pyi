from queue import Empty as Empty
from types import TracebackType
from typing import Any

from kombu.entity import Exchange, Queue
from kombu.message import Message
from kombu.messaging import Consumer, Producer
from kombu.transport.base import StdChannel
from typing_extensions import Self

__all__ = ("SimpleBuffer", "SimpleQueue")

class SimpleBase:
    Empty: type[Empty]

    channel: StdChannel
    producer: Producer
    consumer: Consumer
    queue: Queue
    exchange: Exchange
    no_ack: bool

    def __init__(
        self,
        channel: StdChannel,
        producer: Producer,
        consumer: Consumer,
        no_ack: bool = ...,
    ) -> None: ...
    def get(self, block: bool = ..., timeout: float | None = ...) -> Message: ...
    def get_nowait(self) -> Message: ...
    def put(
        self,
        message: Any,
        serializer: str | None = ...,
        headers: dict[str, Any] | None = ...,
        compression: str | None = ...,
        routing_key: str | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def clear(self) -> int: ...
    def qsize(self) -> int: ...
    def close(self) -> None: ...
    def _consume(self) -> None: ...
    def _receive(self, message_data: Any, message: Message) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    @property
    def __name__(self) -> str: ...

class SimpleQueue(SimpleBase):
    queue_opts: dict[str, Any]
    queue_args: dict[str, Any]
    exchange_opts: dict[str, Any]

    def __init__(
        self,
        channel: StdChannel,
        name: str,
        no_ack: bool | None = ...,
        queue_opts: dict[str, Any] | None = ...,
        queue_args: dict[str, Any] | None = ...,
        exchange_opts: dict[str, Any] | None = ...,
        serializer: str | None = ...,
        compression: str | None = ...,
        accept: list[str] | None = ...,
    ) -> None: ...

class SimpleBuffer(SimpleQueue):
    queue_opts: dict[str, Any]
    exchange_opts: dict[str, Any]
