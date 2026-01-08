from typing import Any

from azure.servicebus import ServiceBusClient, ServiceBusReceiver, ServiceBusSender
from azure.servicebus.management import ServiceBusAdministrationClient
from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property
from typing_extensions import override

PUNCTUATIONS_TO_REPLACE: set[str]
CHARS_REPLACE_TABLE: dict[int, int]

class SendReceive:
    receiver: ServiceBusReceiver | None
    sender: ServiceBusSender | None

    def __init__(
        self,
        receiver: ServiceBusReceiver | None = ...,
        sender: ServiceBusSender | None = ...,
    ) -> None: ...
    def close(self) -> None: ...

class Channel(VirtualChannel):
    default_wait_time_seconds: int
    default_peek_lock_seconds: int
    default_uamqp_keep_alive_interval: int
    default_retry_total: int
    default_retry_backoff_factor: float
    default_retry_backoff_max: int
    domain_format: str
    _queue_cache: dict[str, SendReceive]
    _noack_queues: set[str]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def basic_consume(
        self, queue: str, no_ack: bool, *args: Any, **kwargs: Any
    ) -> str: ...
    @override
    def basic_cancel(self, consumer_tag: str) -> None: ...
    def entity_name(self, name: str, table: dict[int, int] | None = ...) -> str: ...
    @override
    def basic_ack(self, delivery_tag: str, multiple: bool = ...) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def close(self) -> None: ...
    @cached_property
    def queue_service(self) -> ServiceBusClient: ...
    @cached_property
    def queue_mgmt_service(self) -> ServiceBusAdministrationClient: ...
    @property
    def conninfo(self) -> Any: ...
    @property
    def transport_options(self) -> dict[str, Any]: ...
    @cached_property
    def queue_name_prefix(self) -> str: ...
    @cached_property
    def wait_time_seconds(self) -> int: ...
    @cached_property
    def peek_lock_seconds(self) -> int: ...
    @cached_property
    def uamqp_keep_alive_interval(self) -> int: ...
    @cached_property
    def retry_total(self) -> int: ...
    @cached_property
    def retry_backoff_factor(self) -> float: ...
    @cached_property
    def retry_backoff_max(self) -> int: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

    polling_interval: int  # pyright: ignore[reportIncompatibleVariableOverride]
    default_port: None  # pyright: ignore[reportIncompatibleVariableOverride]
    can_parse_url: bool

    @staticmethod
    def parse_uri(uri: str) -> tuple[str, Any]: ...
    @classmethod
    @override
    def as_uri(cls, uri: str, include_password: bool = ..., mask: str = ...) -> str: ...  # pyright: ignore[reportIncompatibleMethodOverride]
