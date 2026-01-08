import dataclasses
from concurrent.futures import ThreadPoolExecutor
from logging import Logger
from typing import Any

from google.cloud.monitoring_v3 import MetricServiceClient
from google.cloud.pubsub_v1 import (  # type: ignore[import-untyped]  # pyright: ignore[reportMissingTypeStubs]
    PublisherClient,
    SubscriberClient,
)
from kombu.transport import virtual
from kombu.utils.objects import cached_property
from typing_extensions import override

logger: Logger

PUNCTUATIONS_TO_REPLACE: set[str]
CHARS_REPLACE_TABLE: dict[int, int]

class UnackedIds:
    def __init__(self) -> None: ...
    def append(self, val: Any) -> None: ...
    def extend(self, vals: list[Any]) -> None: ...
    def pop(self, index: int = ...) -> Any: ...
    def remove(self, val: Any) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, item: int) -> Any: ...

class AtomicCounter:
    def __init__(self, initial: int = ...) -> None: ...
    def inc(self, n: int = ...) -> int: ...
    def dec(self, n: int = ...) -> int: ...
    def get(self) -> int: ...

@dataclasses.dataclass
class QueueDescriptor:
    name: str
    topic_path: str
    subscription_id: str
    subscription_path: str
    unacked_ids: UnackedIds = ...

class Channel(virtual.Channel):
    supports_fanout: bool
    do_restore: bool
    default_wait_time_seconds: int
    default_ack_deadline_seconds: int
    default_expiration_seconds: int
    default_retry_timeout_seconds: int
    default_bulk_max_messages: int

    pool: ThreadPoolExecutor
    project_id: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def entity_name(self, name: str, table: dict[int, int] = ...) -> str: ...
    @override
    def basic_ack(self, delivery_tag: str, multiple: bool = ...) -> None: ...
    @override
    def after_reply_message_received(self, queue: str) -> None: ...
    @override
    def close(self) -> None: ...
    @cached_property
    def subscriber(self) -> SubscriberClient: ...
    @cached_property
    def publisher(self) -> PublisherClient: ...
    @cached_property
    def monitor(self) -> MetricServiceClient: ...
    @property
    def conninfo(self) -> Any: ...
    @property
    def transport_options(self) -> dict[str, Any]: ...
    @cached_property
    def wait_time_seconds(self) -> int: ...
    @cached_property
    def retry_timeout_seconds(self) -> int: ...
    @cached_property
    def ack_deadline_seconds(self) -> int: ...
    @cached_property
    def queue_name_prefix(self) -> str: ...
    @cached_property
    def expiration_seconds(self) -> int: ...
    @cached_property
    def bulk_max_messages(self) -> int: ...

_Channel = Channel

class Transport(virtual.Transport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]
    can_parse_url: bool
    polling_interval: float  # pyright: ignore[reportIncompatibleVariableOverride]
    connection_errors: tuple[type[BaseException], ...]
    channel_errors: tuple[type[BaseException], ...]
    driver_type: str
    driver_name: str
    implements: Any

    def __init__(self, client: Any, **kwargs: Any) -> None: ...
    @override
    def driver_version(self) -> str: ...
    @staticmethod
    def parse_uri(uri: str) -> str: ...
    @classmethod
    @override
    def as_uri(cls, uri: str, include_password: bool = ..., mask: str = ...) -> str: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def drain_events(self, connection: Any, timeout: float | None = ...) -> None: ...  # type: ignore[override]
