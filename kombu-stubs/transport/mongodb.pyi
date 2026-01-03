from collections.abc import Iterator
from datetime import datetime
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database

E_SERVER_VERSION: str
E_NO_TTL_INDEXES: str

class BroadcastCursor:
    def __init__(self, cursor: Cursor[Any]) -> None: ...
    def get_size(self) -> int: ...
    def close(self) -> None: ...
    def purge(self, rewind: bool = ...) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __next__(self) -> Any: ...
    def next(self) -> Any: ...

class Channel(VirtualChannel):
    supports_fanout: bool

    ssl: bool
    ttl: bool
    connect_timeout: int | None
    capped_queue_size: int
    calc_queue_size: bool

    default_hostname: str
    default_port: int
    default_database: str

    messages_collection: str
    routing_collection: str
    broadcast_collection: str
    queues_collection: str

    from_transport_options: tuple[str, ...]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_table(self, exchange: str) -> frozenset[tuple[str, str, str]]: ...  # type: ignore[override]
    def queue_delete(  # type: ignore[override]
        self, queue: str, **kwargs: Any
    ) -> int | None: ...
    def prepare_queue_arguments(
        self, arguments: dict[str, Any] | None, **kwargs: Any
    ) -> dict[str, Any]: ...
    def get_now(self) -> datetime: ...
    @cached_property
    def client(self) -> Database[Any]: ...
    @cached_property
    def messages(self) -> Collection[Any]: ...
    @cached_property
    def routing(self) -> Collection[Any]: ...
    @cached_property
    def broadcast(self) -> Collection[Any]: ...
    @cached_property
    def queues(self) -> Collection[Any]: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]

    can_parse_url: bool
    polling_interval: int
    default_port: int
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]
    driver_type: str
    driver_name: str
    implements: Any

    def driver_version(self) -> str: ...
    def as_uri(
        self, uri: str, include_password: bool = ..., mask: str = ...
    ) -> str: ...
