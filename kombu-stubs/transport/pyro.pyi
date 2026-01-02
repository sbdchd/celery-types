from logging import Logger
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport

DEFAULT_PORT: int
E_NAMESERVER: str
E_LOOKUP: str
logger: Logger

class Channel(VirtualChannel):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    def queues(self) -> list[str]: ...

class Transport(VirtualTransport):
    Channel: type[Channel]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]
