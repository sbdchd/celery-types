from typing import Any

from kombu.transport.base import Transport as BaseTransport

class Transport(BaseTransport):
    default_port: int
    default_ssl_port: int
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]

class Channel:
    connection: Any
    def __init__(self, connection: Any, channel_id: int | None = ...) -> None: ...

class Connection:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
