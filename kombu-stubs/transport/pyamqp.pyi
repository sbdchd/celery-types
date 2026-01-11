from typing import Any

import amqp
from kombu.transport.base import Message as BaseMessage
from kombu.transport.base import StdChannel
from kombu.transport.base import Transport as BaseTransport
from typing_extensions import override

DEFAULT_PORT: int
DEFAULT_SSL_PORT: int

class Message(BaseMessage):
    def __init__(self, msg: Any, channel: Any = ..., **kwargs: Any) -> None: ...

_Message = Message

class Channel(amqp.Channel, StdChannel):
    Message: type[_Message]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]

    def prepare_message(
        self,
        body: bytes | str,
        priority: int | None = ...,
        content_type: str | None = ...,
        content_encoding: str | None = ...,
        headers: dict[str, Any] | None = ...,
        properties: dict[str, Any] | None = ...,
        _Message: type[amqp.Message] = ...,
    ) -> amqp.Message: ...
    @override
    def prepare_queue_arguments(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, arguments: dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]: ...
    def message_to_python(self, raw_message: Any) -> _Message: ...

_Connection = amqp.Connection

class Connection(amqp.Connection):
    Channel: type[Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

class Transport(BaseTransport):
    Connection: type[_Connection]
    default_port: int  # pyright: ignore[reportIncompatibleVariableOverride]
    default_ssl_port: int
    connection_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    channel_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    recoverable_connection_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    recoverable_channel_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_name: str
    driver_type: str

    def __init__(
        self,
        client: Any,
        default_port: int | None = ...,
        default_ssl_port: int | None = ...,
        **kwargs: Any,
    ) -> None: ...
    @override
    def driver_version(self) -> str: ...
    @override
    def create_channel(self, connection: _Connection) -> Channel: ...
    @override
    def drain_events(self, connection: _Connection, **kwargs: Any) -> Any: ...
    @override
    def establish_connection(self) -> _Connection: ...
    @override
    def verify_connection(self, connection: _Connection) -> bool: ...
    @override
    def close_connection(self, connection: _Connection) -> None: ...
    @override
    def get_heartbeat_interval(self, connection: _Connection) -> int: ...
    @override
    def register_with_event_loop(self, connection: _Connection, loop: Any) -> None: ...
    @override
    def heartbeat_check(self, connection: _Connection, rate: int = ...) -> Any: ...
    @override
    def qos_semantics_matches_spec(self, connection: _Connection) -> bool: ...
    @property
    @override
    def default_connection_params(self) -> dict[str, Any]: ...
    @override
    def get_manager(self, *args: Any, **kwargs: Any) -> Any: ...

class SSLTransport(Transport):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
