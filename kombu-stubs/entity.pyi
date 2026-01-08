from collections.abc import Callable, Mapping, Sequence
from typing import Any

from kombu.abstract import MaybeChannelBound, Object
from kombu.message import Message as _Message
from kombu.transport.base import StdChannel

__all__ = ("Exchange", "Queue", "binding", "maybe_delivery_mode")

def _reprstr(s: str) -> str: ...
def pretty_bindings(bindings: Sequence[binding]) -> str: ...
def maybe_delivery_mode(
    v: Any, modes: Mapping[str, int] | None = ..., default: int = ...
) -> int | None: ...

class Exchange(MaybeChannelBound):
    PERSISTENT_DELIVERY_MODE: int
    TRANSIENT_DELIVERY_MODE: int

    name: str
    type: str
    durable: bool
    auto_delete: bool
    delivery_mode: int | None
    no_declare: bool
    passive: bool
    arguments: dict[str, Any] | None

    def __init__(
        self,
        name: str = ...,
        type: str = ...,
        channel: StdChannel | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def Message(
        self,
        body: Any,
        delivery_mode: int | None = ...,
        properties: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> _Message: ...
    def declare(
        self,
        nowait: bool = ...,
        passive: bool | None = ...,
        channel: StdChannel | None = ...,
    ) -> None: ...
    def delete(self, if_unused: bool = ..., nowait: bool = ...) -> None: ...
    def bind_to(
        self,
        exchange: str | Exchange = ...,
        routing_key: str = ...,
        arguments: dict[str, Any] | None = ...,
        nowait: bool = ...,
        channel: StdChannel | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def unbind_from(
        self,
        source: str | Exchange = ...,
        routing_key: str = ...,
        nowait: bool = ...,
        arguments: dict[str, Any] | None = ...,
        channel: StdChannel | None = ...,
    ) -> None: ...
    def publish(
        self,
        message: Any,
        routing_key: str | None = ...,
        mandatory: bool = ...,
        immediate: bool = ...,
        exchange: str | None = ...,
    ) -> None: ...
    def binding(
        self,
        routing_key: str = ...,
        arguments: dict[str, Any] | None = ...,
        unbind_arguments: dict[str, Any] | None = ...,
    ) -> binding: ...  # ty: ignore[invalid-type-form]
    def _can_declare(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class Queue(MaybeChannelBound):
    ContentDisallowed: type[Exception]

    name: str
    exchange: Exchange
    routing_key: str
    durable: bool
    exclusive: bool
    auto_delete: bool
    no_ack: bool
    queue_arguments: dict[str, Any] | None
    binding_arguments: dict[str, Any] | None
    consumer_arguments: dict[str, Any] | None
    bindings: Sequence[binding]
    on_declared: Callable[..., Any] | None

    def __init__(
        self,
        name: str = ...,
        exchange: Exchange | str | None = ...,
        routing_key: str = ...,
        channel: StdChannel | None = ...,
        bindings: Sequence[binding] | None = ...,
        on_declared: Callable[..., Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def from_dict(cls, queue: str, **options: Any) -> Queue: ...
    def declare(
        self, nowait: bool = ..., channel: StdChannel | None = ...
    ) -> str | None: ...
    def queue_declare(
        self, nowait: bool = ..., passive: bool = ..., channel: StdChannel | None = ...
    ) -> str | None: ...
    def queue_bind(
        self, nowait: bool = ..., channel: StdChannel | None = ...
    ) -> None: ...
    def queue_unbind(
        self,
        arguments: dict[str, Any] | None = ...,
        nowait: bool = ...,
        channel: StdChannel | None = ...,
    ) -> None: ...
    def delete(
        self,
        if_unused: bool = ...,
        if_empty: bool = ...,
        nowait: bool = ...,
    ) -> int | None: ...
    def bind_to(
        self,
        exchange: str | Exchange = ...,
        routing_key: str = ...,
        arguments: dict[str, Any] | None = ...,
        nowait: bool = ...,
        channel: StdChannel | None = ...,
    ) -> None: ...
    def unbind_from(
        self,
        exchange: str | Exchange = ...,
        routing_key: str = ...,
        arguments: dict[str, Any] | None = ...,
        nowait: bool = ...,
        channel: StdChannel | None = ...,
    ) -> None: ...
    def get(
        self, no_ack: bool | None = ..., accept: Sequence[str] | None = ...
    ) -> _Message | None: ...
    def purge(self, nowait: bool = ...) -> int | None: ...
    def consume(
        self,
        consumer_tag: str = ...,
        callback: Callable[[Any, _Message], None] | None = ...,
        no_ack: bool | None = ...,
        nowait: bool = ...,
        on_cancel: Callable[[str], None] | None = ...,
    ) -> str: ...
    def cancel(self, consumer_tag: str) -> None: ...
    def _create_exchange(
        self, nowait: bool = ..., channel: StdChannel | None = ...
    ) -> None: ...
    def _create_queue(
        self, nowait: bool = ..., channel: StdChannel | None = ...
    ) -> str | None: ...
    def _create_bindings(
        self, nowait: bool = ..., channel: StdChannel | None = ...
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class binding(Object):
    exchange: Exchange | None
    routing_key: str
    arguments: dict[str, Any] | None
    unbind_arguments: dict[str, Any] | None

    def __init__(
        self,
        exchange: Exchange | None = ...,
        routing_key: str = ...,
        arguments: dict[str, Any] | None = ...,
        unbind_arguments: dict[str, Any] | None = ...,
    ) -> None: ...
    def declare(self, channel: StdChannel, nowait: bool = ...) -> None: ...
    def bind(
        self,
        entity: Exchange | Queue,
        nowait: bool = ...,
        channel: StdChannel | None = ...,
    ) -> None: ...
    def unbind(
        self,
        entity: Exchange | Queue,
        nowait: bool = ...,
        channel: StdChannel | None = ...,
    ) -> None: ...
