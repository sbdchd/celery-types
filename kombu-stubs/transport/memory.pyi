from collections import defaultdict
from queue import Queue
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.transport.virtual.base import BrokerState
from typing_extensions import override

class Channel(VirtualChannel):
    events: defaultdict[str, set[Any]]
    queues: dict[str, Queue[Any]]
    do_restore: bool
    supports_fanout: bool

    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
    @override
    def close(self) -> None: ...
    def _queue_for(self, queue: str) -> Queue[Any]: ...
    def _put_fanout(
        self,
        exchange: str,
        message: dict[str, Any],
        routing_key: str | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def _queue_bind(self, *args: Any) -> None: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    default_port: int | None
    driver_type: str
    driver_name: str
    global_state: BrokerState
