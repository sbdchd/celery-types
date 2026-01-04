from logging import Logger
from typing import Any

from kombu.transport.base import Transport as BaseTransport
from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Message
from kombu.transport.virtual import QoS as VirtualQoS
from typing_extensions import override

logger: Logger
buffer: type[bytes]
OBJECT_ALREADY_EXISTS_STRING: str
VERSION: tuple[int, int, int]

def dependency_is_none(dependency: Any) -> bool: ...

class AuthenticationFailure(Exception): ...

class QoS(VirtualQoS):
    def __init__(self, session: Any, prefetch_count: int = ...) -> None: ...

class Connection:
    Channel: type[Channel]

    def __init__(self, **conn_info: Any) -> None: ...
    def close(self) -> None: ...
    def close_channel(self, channel: Any) -> None: ...
    def get_qpid_connection(self) -> Any: ...

_Message = Message
_QoS = QoS

class Channel(VirtualChannel):
    Message: type[_Message]
    QoS: type[_QoS]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __init__(self, connection: Any, transport: Any) -> None: ...
    @override
    def close(self) -> None: ...
    @override
    def queue_declare(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        queue: str,
        passive: bool = ...,
        durable: bool = ...,
        exclusive: bool = ...,
        auto_delete: bool = ...,
        nowait: bool = ...,
        arguments: dict[str, Any] | None = ...,
    ) -> Any: ...
    @override
    def exchange_declare(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        exchange: str = ...,
        type: str = ...,
        durable: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    @override
    def exchange_delete(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, exchange_name: str, **kwargs: Any
    ) -> None: ...
    @override
    def queue_bind(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, queue: str, exchange: str, routing_key: str, **kwargs: Any
    ) -> None: ...
    @override
    def queue_unbind(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, queue: str, exchange: str, routing_key: str, **kwargs: Any
    ) -> None: ...
    @override
    def basic_qos(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, prefetch_count: int, *args: Any
    ) -> None: ...

_Connection = Connection

class Transport(BaseTransport):
    Channel: type[Channel]
    Connection: type[_Connection]
    driver_type: str
    driver_name: str
    polling_interval: None
    connection_errors: tuple[type[Exception] | None, ...]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]
    channel_errors: tuple[type[Exception] | None, ...]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]
    recoverable_connection_errors: tuple[type[BaseException] | None, ...]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]
    recoverable_channel_errors: tuple[type[BaseException] | None, ...]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __del__(self) -> None: ...
    @override
    def drain_events(
        self, connection: Any, timeout: int = ..., **kwargs: Any
    ) -> None: ...
    def verify_runtime_environment(self) -> None: ...
