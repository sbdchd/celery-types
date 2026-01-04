from collections import defaultdict
from queue import Queue
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.transport.virtual.base import BrokerState

class Channel(VirtualChannel):
    events: defaultdict[str, set[Any]]
    queues: dict[str, Queue[Any]]
    do_restore: bool
    supports_fanout: bool

    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
    def close(self) -> None: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    default_port: int | None
    driver_type: str
    driver_name: str
    global_state: BrokerState
