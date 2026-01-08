import logging
import types
from collections import OrderedDict
from collections.abc import Callable, Generator, Iterable
from typing import Any, NamedTuple, TypeAlias

from amqp.protocol import queue_declare_ok_t
from kombu.connection import Connection
from kombu.message import Message as BaseMessage
from kombu.transport.base import Management as BaseManagement
from kombu.transport.base import StdChannel
from kombu.transport.base import Transport as BaseTransport
from kombu.transport.virtual.exchange import ExchangeType
from kombu.utils.scheduling import FairCycle
from typing_extensions import Self, override

ARRAY_TYPE_H: str
NOT_EQUIVALENT_FMT: str
RESTORE_PANIC_FMT: str
RESTORING_FMT: str
UNDELIVERABLE_FMT: str
W_NO_CONSUMERS: str

logger: logging.Logger

# Forward references for type annotations to avoid name collisions with class attributes
_QoSType: TypeAlias = QoS
_MessageType: TypeAlias = Message
_ChannelType: TypeAlias = Channel

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
    exchanges: dict[str, dict[str, Any]] | None
    bindings: dict[binding_key_t, queue_binding_t] | None
    queue_index: dict[str, set[binding_key_t]] | None

    def __init__(self, exchanges: dict[str, dict[str, Any]] | None = ...) -> None: ...
    def clear(self) -> None: ...
    def has_binding(self, queue: str, exchange: str, routing_key: str) -> bool: ...
    def binding_declare(
        self,
        queue: str,
        exchange: str,
        routing_key: str,
        arguments: dict[str, Any] | None,
    ) -> None: ...
    def binding_delete(self, queue: str, exchange: str, routing_key: str) -> None: ...
    def queue_bindings_delete(self, queue: str) -> None: ...
    def queue_bindings(self, queue: str) -> Generator[queue_binding_t, None, None]: ...

class QoS:
    channel: Channel
    prefetch_count: int
    restore_at_shutdown: bool

    _delivered: OrderedDict[str, Any] | None
    _dirty: set[str] | None

    def __init__(self, channel: Channel, prefetch_count: int = ...) -> None: ...
    def can_consume(self) -> bool: ...
    def can_consume_max_estimate(self) -> int: ...
    def append(self, message: Any, delivery_tag: str) -> None: ...
    def get(self, delivery_tag: str) -> Any: ...
    def ack(self, delivery_tag: str) -> None: ...
    def reject(self, delivery_tag: str, requeue: bool = ...) -> None: ...
    def restore_unacked(self) -> None: ...
    def restore_unacked_once(self, stderr: Any | None = ...) -> None: ...
    def restore_visible(self, *args: Any, **kwargs: Any) -> None: ...

class Message(BaseMessage):
    def __init__(
        self,
        payload: dict[str, Any],
        channel: Channel | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def serializable(self) -> dict[str, Any]: ...

# AbstractChannel is a base class with only internal methods
class AbstractChannel:
    def _get(self, queue: str, timeout: float | None = ...) -> Any: ...
    def _put(self, queue: str, message: Any) -> None: ...
    def _purge(self, queue: str) -> int: ...
    def _size(self, queue: str) -> int: ...
    def _delete(self, queue: str, *args: Any, **kwargs: Any) -> None: ...
    def _new_queue(self, queue: str, **kwargs: Any) -> None: ...
    def _has_queue(self, queue: str, **kwargs: Any) -> bool: ...
    def _poll(
        self,
        cycle: FairCycle,
        callback: Callable[..., Any],
        timeout: float | None = ...,
    ) -> None: ...

# Channel inherits from AbstractChannel and StdChannel (multiple inheritance)
class Channel(AbstractChannel, StdChannel):
    Message: type[Message]
    QoS: type[QoS]

    do_restore: bool
    exchange_types: dict[str, type[ExchangeType]]
    supports_fanout: bool

    codecs: dict[str, Base64]
    body_encoding: str

    default_priority: int
    min_priority: int
    max_priority: int
    deadletter_queue: str | None

    connection: Transport

    closed: bool
    _active_queues: list[str]
    _delivery_tags: Iterable[int]
    _consumers: set[str]
    _cycle: FairCycle | None
    _qos: _QoSType | None
    _tag_to_queue: dict[str, str]

    from_transport_options: tuple[str, ...]

    # NOTE: Despite the name, 'connection' is actually a Transport (from establish_connection())
    def __init__(self, connection: Transport, **kwargs: Any) -> None: ...
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
    def exchange_bind(
        self,
        destination: str,
        source: str = ...,
        routing_key: str = ...,
        nowait: bool = ...,
        arguments: dict[str, Any] | None = ...,
    ) -> None: ...
    def exchange_unbind(
        self,
        destination: str,
        source: str = ...,
        routing_key: str = ...,
        nowait: bool = ...,
        arguments: dict[str, Any] | None = ...,
    ) -> None: ...
    def queue_declare(
        self,
        queue: str | None = ...,
        passive: bool = ...,
        **kwargs: Any,
    ) -> queue_declare_ok_t: ...
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
        exchange: str,
        routing_key: str,
        **kwargs: Any,
    ) -> None: ...
    def basic_consume(
        self,
        queue: str,
        no_ack: bool,
        callback: Callable[..., Any] | None,
        consumer_tag: str | None,
        **kwargs: Any,
    ) -> str: ...
    def basic_cancel(self, consumer_tag: str) -> Any: ...
    def basic_get(
        self,
        queue: str,
        no_ack: bool = ...,
        **kwargs: Any,
    ) -> _MessageType | None: ...
    def basic_ack(self, delivery_tag: str, multiple: bool = ...) -> None: ...
    def basic_qos(
        self,
        prefetch_size: int = ...,
        prefetch_count: int = ...,
        apply_global: bool = ...,
    ) -> None: ...
    def basic_recover(self, requeue: bool = ...) -> None: ...
    def basic_reject(self, delivery_tag: str, requeue: bool = ...) -> None: ...
    def close(self) -> None: ...
    def encode_body(
        self, body: bytes, encoding: str | None = ...
    ) -> tuple[Any, str]: ...
    def decode_body(self, body: Any, encoding: str | None = ...) -> bytes: ...
    def drain_events(
        self, timeout: float | None = ..., callback: Callable[..., Any] | None = ...
    ) -> None: ...
    def get_exchanges(self) -> list[str]: ...
    def get_table(self, exchange: str) -> list[tuple[str, str, str]]: ...
    def typeof(self, exchange: str, default: str = ...) -> ExchangeType: ...
    def list_bindings(self) -> Generator[tuple[str, str, str], None, None]: ...
    def message_to_python(self, raw_message: Any) -> _MessageType: ...
    def prepare_message(
        self,
        body: Any,
        priority: int | None = ...,
        content_type: str | None = ...,
        content_encoding: str | None = ...,
        headers: dict[str, Any] | None = ...,
        properties: dict[str, Any] | None = ...,
    ) -> dict[str, Any]: ...
    def flow(self, active: bool = ...) -> None: ...
    def _next_delivery_tag(self) -> str: ...
    def _get_message_priority(self, message: Any, reverse: bool = ...) -> int: ...
    def _restore(self, message: Any) -> None: ...
    def _restore_at_beginning(self, message: Any) -> None: ...
    def _get_and_deliver(self, queue: str, callback: Callable[..., Any]) -> None: ...
    def _get_free_channel_id(self) -> int: ...
    def _inplace_augment_message(
        self, message: Any, exchange: str | None, routing_key: str
    ) -> None: ...
    def _lookup(
        self, exchange: str, routing_key: str, default: str | None = ...
    ) -> list[str] | set[str]: ...
    def _reset_cycle(self) -> None: ...
    @override
    def after_reply_message_received(self, queue: str) -> None: ...
    @override
    def __enter__(self) -> Self: ...
    @override
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None: ...
    @property
    def state(self) -> BrokerState: ...
    @property
    def qos(self) -> _QoSType: ...
    @property
    def cycle(self) -> FairCycle: ...

class Management(BaseManagement):
    transport: Transport  # pyright: ignore[reportIncompatibleVariableOverride]
    channel: _ChannelType | None

    def __init__(self, transport: Transport) -> None: ...
    @override
    def get_bindings(self) -> list[dict[str, Any]]: ...
    def close(self) -> None: ...

class Transport(BaseTransport):
    Channel: type[_ChannelType]
    Cycle: type[FairCycle]
    Management: type[Management]  # pyright: ignore[reportIncompatibleVariableOverride]

    polling_interval: float | None
    channel_max: int
    channels: list[_ChannelType] | None
    cycle: FairCycle | None

    _callbacks: dict[str, Callable[..., Any]] | None

    def __init__(self, client: Connection, **kwargs: Any) -> None: ...
    @override
    def create_channel(self, connection: Connection) -> _ChannelType: ...
    @override
    def close_channel(self, channel: StdChannel) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    @override
    def establish_connection(self) -> Self: ...
    @override
    def close_connection(self, connection: Connection) -> None: ...
    @override
    def drain_events(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, connection: Connection, timeout: float | None = ...
    ) -> None: ...
    def on_message_ready(
        self, channel: _ChannelType, message: _MessageType, queue: str
    ) -> None: ...
    def _deliver(self, message: Any, queue: str | None) -> None: ...
    def _drain_channel(
        self,
        channel: _ChannelType,
        callback: Callable[..., Any],
        timeout: float | None = ...,
    ) -> None: ...
    def _make_reader(
        self,
        connection: Any,
        timeout: type[BaseException] = ...,
        error: type[BaseException] = ...,
        _unavail: tuple[int, ...] = ...,
    ) -> Callable[..., Any]: ...
    def _reject_inbound_message(self, raw_message: Any) -> None: ...
    @property
    @override
    def default_connection_params(self) -> dict[str, Any]: ...
