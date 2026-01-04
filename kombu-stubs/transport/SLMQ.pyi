from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property
from typing_extensions import override

CHARS_REPLACE_TABLE: dict[int, int]

class Channel(VirtualChannel):
    default_visibility_timeout: int
    domain_format: str
    _slmq: Any
    _queue_cache: dict[str, str]
    _noack_queues: set[str]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def basic_consume(
        self, queue: str, no_ack: bool, *args: Any, **kwargs: Any
    ) -> str: ...
    @override
    def basic_cancel(self, consumer_tag: str) -> None: ...
    def entity_name(self, name: str, table: dict[int, int] = ...) -> str: ...
    @override
    def basic_ack(self, delivery_tag: int) -> None: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def delete_message(self, queue: str, message_id: str) -> None: ...
    @property
    def visibility_timeout(self) -> int: ...
    @cached_property
    def queue_name_prefix(self) -> str: ...
    @property
    def slmq(self) -> Any: ...
    @property
    def conninfo(self) -> Any: ...
    @property
    def transport_options(self) -> dict[str, Any]: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[Exception] | None, ...]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]
