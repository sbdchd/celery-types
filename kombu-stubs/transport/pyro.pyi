from logging import Logger
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.transport.virtual.base import BrokerState
from kombu.utils.objects import cached_property
from typing_extensions import override

DEFAULT_PORT: int
E_NAMESERVER: str
E_LOOKUP: str
logger: Logger

class Channel(VirtualChannel):
    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
    @override
    def close(self) -> None: ...
    def queues(self) -> list[str]: ...
    @cached_property
    def shared_queues(self) -> Any: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    channel_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    global_state: BrokerState
    @cached_property
    def shared_queues(self) -> Any: ...
