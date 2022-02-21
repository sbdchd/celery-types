from enum import Enum
from typing import Any, Callable, Optional, Sequence, Union

from kombu.connection import Connection
from kombu.entity import Exchange, Queue
from kombu.message import Message
from kombu.transport.base import Channel

class Producer:
    def __init__(
        self,
        channel: Union[Connection, Channel],
        exchange: Optional[Union[Exchange, str]] = ...,
        routing_key: Optional[str] = ...,
        serializer: Optional[str] = ...,
        auto_declare: Optional[bool] = ...,
        compression: Optional[str] = ...,
        on_return: Optional[
            Callable[[Exception, Union[Exchange, str], str, Message], None]
        ] = ...,
    ) -> None: ...
    def publish(
        self,
        body: Any,
        routing_key: Optional[str] = ...,
        delivery_mode: Optional[Enum] = ...,
        mandatory: bool = ...,
        immediate: bool = ...,
        priority: int = ...,
        content_type: Optional[str] = ...,
        content_encoding: Optional[str] = ...,
        serializer: Optional[str] = ...,
        headers: Optional[dict[Any, Any]] = ...,
        compression: Optional[str] = ...,
        exchange: Optional[Union[Exchange, str]] = ...,
        retry: bool = ...,
        retry_policy: Optional[dict[Any, Any]] = ...,
        declare: Sequence[Union[Exchange, Queue]] = ...,
        expiration: Optional[float] = ...,
        timeout: Optional[float] = ...,
        **properties: Any
    ) -> None: ...

class Consumer:
    def __init__(
        self,
        channel: Union[Connection, Channel],
        queues: Optional[Sequence[Queue]] = ...,
        no_ack: Optional[bool] = ...,
        auto_declare: Optional[bool] = ...,
        callbacks: Optional[Sequence[Callable[[Any, Message], None]]] = ...,
        on_decode_error: Optional[Callable[[Message, Exception], None]] = ...,
        on_message: Optional[Callable[[Message], None]] = ...,
        accept: Optional[Sequence[str]] = ...,
        prefetch_count: Optional[int] = ...,
        tag_prefix: Optional[str] = ...,
    ) -> None: ...
