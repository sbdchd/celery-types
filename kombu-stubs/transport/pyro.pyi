from logging import Logger
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.transport.virtual.base import BrokerState
from kombu.utils.objects import cached_property

DEFAULT_PORT: int
E_NAMESERVER: str
E_LOOKUP: str
logger: Logger

class Channel(VirtualChannel):
    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    def queues(self) -> list[str]: ...
    @cached_property
    def shared_queues(self) -> Any: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]
    global_state: BrokerState
    @cached_property
    def shared_queues(self) -> Any: ...
