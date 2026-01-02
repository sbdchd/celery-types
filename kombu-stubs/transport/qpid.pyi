from logging import Logger
from typing import Any

from kombu.transport.base import Transport as BaseTransport
from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Message
from kombu.transport.virtual import QoS as VirtualQoS

logger: Logger
buffer: type[bytes]
OBJECT_ALREADY_EXISTS_STRING: str
VERSION: tuple[int, int, int]

def dependency_is_none(dependency: Any) -> bool: ...

class AuthenticationFailure(Exception): ...

class QoS(VirtualQoS):
    def __init__(self, session: Any, prefetch_count: int = ...) -> None: ...

class Connection:
    def __init__(self, **conn_info: Any) -> None: ...
    def close(self) -> None: ...
    def get_qpid_connection(self) -> Any: ...

_Message = Message
_QoS = QoS

class Channel(VirtualChannel):
    Message: type[_Message]
    QoS: type[_QoS]

    def __init__(self, connection: Any, transport: Any) -> None: ...
    def close(self) -> None: ...
    def queue_declare(  # type: ignore[override]
        self,
        queue: str,
        passive: bool = ...,
        durable: bool = ...,
        exclusive: bool = ...,
        auto_delete: bool = ...,
        nowait: bool = ...,
        arguments: dict[str, Any] | None = ...,
    ) -> Any: ...
    def exchange_declare(  # type: ignore[override]
        self,
        exchange: str = ...,
        type: str = ...,
        durable: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def exchange_delete(  # type: ignore[override]
        self, exchange_name: str, **kwargs: Any
    ) -> None: ...
    def queue_bind(  # type: ignore[override]
        self, queue: str, exchange: str, routing_key: str, **kwargs: Any
    ) -> None: ...
    def queue_unbind(  # type: ignore[override]
        self, queue: str, exchange: str, routing_key: str, **kwargs: Any
    ) -> None: ...
    def basic_qos(  # type: ignore[override]
        self, prefetch_count: int, *args: Any
    ) -> None: ...

_Connection = Connection

class Transport(BaseTransport):
    Channel: type[Channel]
    Connection: type[_Connection]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]
