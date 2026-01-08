from io import FileIO, TextIOWrapper
from pathlib import Path
from typing import Any, NamedTuple

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.transport.virtual.base import BrokerState
from kombu.utils.objects import cached_property
from typing_extensions import override

VERSION: tuple[int, int, int]

def lock(file: FileIO | TextIOWrapper, flags: int) -> None: ...
def unlock(file: FileIO | TextIOWrapper) -> None: ...

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
    def control_folder(self) -> Path: ...
    @cached_property
    def store_processed(self) -> bool: ...
    @property
    def transport_options(self) -> dict[str, Any]: ...
    @override
    def get_table(self, exchange: str) -> list[exchange_queue_t]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def _get(self, queue: str) -> dict[str, Any]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def _put(self, queue: str, payload: dict[str, Any], **kwargs: Any) -> None: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def _put_fanout(
        self, exchange: str, payload: dict[str, Any], routing_key: str, **kwargs: Any
    ) -> None: ...
    def _queue_bind(
        self, exchange: str, routing_key: str, pattern: str | None, queue: str
    ) -> None: ...
    @override
    def _size(self, queue: str) -> int: ...
    @override
    def _purge(self, queue: str) -> int: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    global_state: BrokerState
