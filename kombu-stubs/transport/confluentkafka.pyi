from logging import Logger
from typing import Any

from confluent_kafka import KafkaException  # type: ignore[import-untyped]
from confluent_kafka.admin import AdminClient  # type: ignore[import-untyped]
from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Message as VirtualMessage
from kombu.transport.virtual import QoS as VirtualQoS
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property

logger: Logger
DEFAULT_PORT: int
KAFKA_CONNECTION_ERRORS: tuple[type[Exception], ...]
KAFKA_CHANNEL_ERRORS: tuple[type[Exception], ...]

class NoBrokersAvailable(KafkaException):
    retriable: bool

class Message(VirtualMessage):
    topic: str | None

    def __init__(
        self, payload: dict[str, Any], channel: Any | None = ..., **kwargs: Any
    ) -> None: ...

_Message = Message

class QoS(VirtualQoS):
    _not_yet_acked: dict[int, Any]

    def can_consume(self) -> bool: ...
    def can_consume_max_estimate(self) -> int: ...
    def append(self, message: Any, delivery_tag: int) -> None: ...
    def get(self, delivery_tag: int) -> Any: ...
    def ack(self, delivery_tag: int) -> None: ...
    def reject(self, delivery_tag: int, requeue: bool = ...) -> None: ...
    def restore_unacked_once(self, stderr: Any | None = ...) -> None: ...

_QoS = QoS

class Channel(VirtualChannel):
    QoS: type[_QoS]  # pyright: ignore[reportIncompatibleVariableOverride]
    Message: type[_Message]  # pyright: ignore[reportIncompatibleVariableOverride]

    default_wait_time_seconds: int
    default_connection_wait_time_seconds: int

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def sanitize_queue_name(self, queue: str) -> str: ...
    def close(self) -> None: ...
    @property
    def client(self) -> AdminClient: ...
    @property
    def options(self) -> dict[str, Any]: ...
    @property
    def conninfo(self) -> Any: ...
    @cached_property
    def wait_time_seconds(self) -> int: ...
    @cached_property
    def connection_wait_time_seconds(self) -> int: ...
    @cached_property
    def common_config(self) -> dict[str, Any]: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

    default_port: int  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    recoverable_connection_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __init__(self, client: Any, **kwargs: Any) -> None: ...
    def as_uri(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, uri: str, include_password: bool = ..., mask: str = ...
    ) -> None: ...
    def driver_version(self) -> str: ...
    def establish_connection(self) -> Any: ...
    def close_connection(self, connection: Any) -> None: ...
