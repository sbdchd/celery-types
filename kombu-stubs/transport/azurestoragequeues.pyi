from typing import Any

from azure.storage.queue import QueueServiceClient
from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property
from typing_extensions import override

CHARS_REPLACE_TABLE: dict[int, int]

class Channel(VirtualChannel):
    domain_format: str
    _queue_service: QueueServiceClient | None
    _queue_name_cache: dict[Any, Any]
    no_ack: bool
    _noack_queues: set[Any]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def basic_consume(
        self, queue: str, no_ack: bool, *args: Any, **kwargs: Any
    ) -> str: ...
    def entity_name(self, name: str, table: dict[int, int] = ...) -> str: ...
    @property
    def queue_service(self) -> QueueServiceClient: ...
    @property
    def conninfo(self) -> Any: ...
    @property
    def transport_options(self) -> dict[str, Any]: ...
    @cached_property
    def queue_name_prefix(self) -> str: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

    polling_interval: int  # pyright: ignore[reportIncompatibleVariableOverride]
    default_port: int | None
    can_parse_url: bool

    @staticmethod
    def parse_uri(uri: str) -> tuple[Any, str]: ...
    @classmethod
    @override
    def as_uri(cls, uri: str, include_password: bool = ..., mask: str = ...) -> str: ...  # pyright: ignore[reportIncompatibleMethodOverride]
