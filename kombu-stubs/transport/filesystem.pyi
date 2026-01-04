from io import FileIO
from typing import Any, NamedTuple

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.transport.virtual.base import BrokerState
from kombu.utils.objects import cached_property

VERSION: tuple[int, int, int]

def lock(file: FileIO, flags: int) -> None: ...
def unlock(file: FileIO) -> None: ...

class exchange_queue_t(NamedTuple):
    routing_key: str
    pattern: str
    queue: str

class Channel(VirtualChannel):
    supports_fanout: bool
    data_folder_in: Any
    data_folder_out: Any
    processed_folder: Any

    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
    @property
    def control_folder(self) -> Any: ...
    @cached_property
    def store_processed(self) -> bool: ...
    @property
    def transport_options(self) -> dict[str, Any]: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    global_state: BrokerState
