import types
from collections import OrderedDict
from collections.abc import Callable, Generator, Iterable
from typing import Any, NamedTuple, Self

from kombu.connection import Connection
from kombu.message import Message as BaseMessage
from kombu.transport.base import Management as BaseManagement
from kombu.transport.base import StdChannel
from kombu.transport.base import Transport as BaseTransport
from kombu.transport.virtual.exchange import ExchangeType
from kombu.utils.scheduling import FairCycle

class binding_key_t(NamedTuple):
    queue: str
    exchange: str
    routing_key: str

class queue_binding_t(NamedTuple):
    exchange: str
    routing_key: str
    arguments: dict[str, Any] | None

class Base64:
    def encode(self, s: str | bytes) -> str: ...
    def decode(self, s: str) -> bytes: ...

class NotEquivalentError(Exception): ...

class UndeliverableWarning(UserWarning): ...

class BrokerState:
    exchanges: dict[str, dict[str, Any]]
    bindings: dict[binding_key_t, queue_binding_t]
    queue_index: dict[str, set[binding_key_t]]

    def __init__(
        self, exchanges: dict[str, dict[str, Any]] | None = ...
    ) -> None: ...
    def clear(self) -> None: ...
    def has_binding(
        self, queue: str, exchange: str, routing_key: str
    ) -> bool: ...
    def binding_declare(
        self,
        queue: str,
        exchange: str,
        routing_key: str,
        arguments: dict[str, Any] | None,
    ) -> None: ...
    def binding_delete(
        self, queue: str, exchange: str, routing_key: str
    ) -> None: ...
    def queue_bindings_delete(self, queue: str) -> None: ...
    def queue_bindings(self, queue: str) -> Generator[queue_binding_t, None, None]: ...

class QoS:
    channel: AbstractChannel
    prefetch_count: int
    restore_at_shutdown: bool

    _delivered: OrderedDict[int, Any]
    _dirty: set[int]

    def __init__(
        self, channel: AbstractChannel, prefetch_count: int = ...
    ) -> None: ...
    def can_consume(self) -> bool: ...
    def can_consume_max_estimate(self) -> int: ...
    def append(self, message: Any, delivery_tag: int) -> None: ...
    def get(self, delivery_tag: int) -> Any: ...
    def ack(self, delivery_tag: int) -> None: ...
    def reject(self, delivery_tag: int, requeue: bool = ...) -> None: ...
    def restore_unacked(self) -> None: ...
    def restore_unacked_once(self, stderr: Any | None = ...) -> None: ...
    def restore_visible(
        self, *args: Any, **kwargs: Any
    ) -> None: ...

class Message(BaseMessage):
    def __init__(
        self,
        payload: dict[str, Any],
        channel: AbstractChannel | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def serializable(self) -> dict[str, Any]: ...

class AbstractChannel(StdChannel):
    do_restore: bool
    exchange_types: dict[str, type[ExchangeType]]
    supports_fanout: bool

    codecs: dict[str, Base64]
    body_encoding: str

    default_priority: int
    min_priority: int
    max_priority: int
    deadletter_queue: str | None

    _delivery_tags: Iterable[int]
    _consumers: dict[str, Any]
    _cycle: FairCycle | None
    _qos: QoS | None
    _tag_to_queue: dict[str, str]

    def __init__(self, connection: Connection, **kwargs: Any) -> None: ...
    def exchange_declare(
        self,
        exchange: str | None = ...,
        type: str = ...,
        durable: bool = ...,
        auto_delete: bool = ...,
        arguments: dict[str, Any] | None = ...,
        nowait: bool = ...,
        passive: bool = ...,
    ) -> None: ...
    def exchange_delete(
        self,
        exchange: str,
        if_unused: bool = ...,
        nowait: bool = ...,
    ) -> None: ...
    def queue_declare(
        self,
        queue: str | None = ...,
        passive: bool = ...,
        **kwargs: Any,
    ) -> Any: ...
    def queue_delete(
        self,
        queue: str,
        if_unused: bool = ...,
        if_empty: bool = ...,
        **kwargs: Any,
    ) -> int | None: ...
    def queue_bind(
        self,
        queue: str,
        exchange: str | None = ...,
        routing_key: str = ...,
        arguments: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def queue_unbind(
        self,
        queue: str,
        exchange: str | None = ...,
        routing_key: str = ...,
        arguments: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def queue_purge(self, queue: str, **kwargs: Any) -> int | None: ...
    def basic_publish(
        self,
        message: Any,
        exchange: str = ...,
        routing_key: str = ...,
        **kwargs: Any,
    ) -> None: ...
    def basic_consume(
        self,
        queue: str,
        no_ack: bool = ...,
        callback: Callable[..., Any] | None = ...,
        consumer_tag: str | None = ...,
        **kwargs: Any,
    ) -> str: ...
    def basic_cancel(self, consumer_tag: str) -> None: ...
    def basic_get(
        self,
        queue: str,
        no_ack: bool = ...,
        **kwargs: Any,
    ) -> Message | None: ...
    def basic_ack(self, delivery_tag: int, multiple: bool = ...) -> None: ...
    def basic_qos(
        self,
        prefetch_size: int = ...,
        prefetch_count: int = ...,
        apply_global: bool = ...,
    ) -> None: ...
    def basic_recover(self, requeue: bool = ...) -> None: ...
    def basic_reject(self, delivery_tag: int, requeue: bool = ...) -> None: ...
    def close(self) -> None: ...
    def encode_body(
        self, body: bytes, encoding: str | None = ...
    ) -> tuple[Any, str]: ...
    def decode_body(
        self, body: Any, encoding: str | None = ...
    ) -> bytes: ...
    def drain_events(
        self, timeout: float | None = ..., callback: Callable[..., Any] | None = ...
    ) -> None: ...
    def get_exchanges(self) -> list[str]: ...
    def get_table(self, exchange: str) -> list[tuple[str, str, str]]: ...
    def typeof(
        self, exchange: str, default: str = ...
    ) -> ExchangeType: ...
    def list_bindings(self) -> Generator[tuple[str, str, str], None, None]: ...
    def message_to_python(self, raw_message: Any) -> Message: ...
    def prepare_message(
        self,
        body: Any,
        priority: int | None = ...,
        content_type: str | None = ...,
        content_encoding: str | None = ...,
        headers: dict[str, Any] | None = ...,
        properties: dict[str, Any] | None = ...,
    ) -> dict[str, Any]: ...
    def flow(self, active: bool) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None: ...
    @property
    def state(self) -> BrokerState: ...
    @property
    def qos(self) -> QoS: ...
    @property
    def cycle(self) -> FairCycle: ...

Channel = AbstractChannel

class Management(BaseManagement):
    transport: Transport
    channel: AbstractChannel | None

    def __init__(self, transport: Transport) -> None: ...
    def get_bindings(self) -> list[dict[str, Any]]: ...
    def close(self) -> None: ...

class Transport(BaseTransport):
    polling_interval: float
    channel_max: int
    channels: list[AbstractChannel]
    cycle: FairCycle | None

    _callbacks: dict[str, Callable[..., Any]]

    def __init__(self, client: Connection, **kwargs: Any) -> None: ...
    def create_channel(self, connection: Connection) -> AbstractChannel: ...
    def close_channel(self, channel: StdChannel) -> None: ...
    def establish_connection(self) -> Connection: ...
    def close_connection(self, connection: Connection) -> None: ...
    def drain_events(
        self, connection: Connection, timeout: float | None = ..., **kwargs: Any
    ) -> None: ...
    def on_message_ready(
        self, channel: AbstractChannel, message: Message, queue: str
    ) -> None: ...
    @property
    def default_connection_params(self) -> dict[str, Any]: ...
