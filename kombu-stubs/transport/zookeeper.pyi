from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport

DEFAULT_PORT: int
KZ_CONNECTION_ERRORS: tuple[type[Exception], ...]
KZ_CHANNEL_ERRORS: tuple[type[Exception], ...]

class Channel(VirtualChannel):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Transport(VirtualTransport):
    Channel: type[Channel]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]
