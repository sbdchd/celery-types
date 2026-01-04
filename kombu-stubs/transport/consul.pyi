from logging import Logger
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property

logger: Logger
DEFAULT_PORT: int
DEFAULT_HOST: str

class LockError(Exception): ...

class Channel(VirtualChannel):
    prefix: str
    index: int | None
    timeout: str
    session_ttl: int

    @cached_property
    def lock_name(self) -> str: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Transport(VirtualTransport):
    Channel: type[Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
