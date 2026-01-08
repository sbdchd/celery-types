from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport

DEFAULT_PORT: int
KZ_CONNECTION_ERRORS: tuple[type[Exception], ...]
KZ_CHANNEL_ERRORS: tuple[type[Exception], ...]

class Channel(VirtualChannel):
    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
    @property
    def client(self) -> Any: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    channel_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
