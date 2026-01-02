from io import FileIO
from typing import Any, NamedTuple

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport

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
    control_folder: Any
    processed_folder: Any
    store_processed: bool
    transport_options: dict[str, Any]

    def __init__(self, connection: Any, **kwargs: Any) -> None: ...

class Transport(VirtualTransport):
    Channel: type[Channel]
    driver_type: str
    driver_name: str
