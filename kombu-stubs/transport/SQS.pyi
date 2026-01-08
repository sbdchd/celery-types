import re
from logging import Logger
from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import QoS as VirtualQoS
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property
from typing_extensions import override

logger: Logger
CHARS_REPLACE_TABLE: dict[int, int]
SQS_MAX_MESSAGES: int

def maybe_int(x: Any) -> int | Any: ...

class UndefinedQueueException(Exception): ...
class InvalidQueueException(Exception): ...
class AccessDeniedQueueException(Exception): ...
class DoesNotExistQueueException(Exception): ...

class QoS(VirtualQoS):
    @override
    def reject(self, delivery_tag: str, requeue: bool = ...) -> None: ...
    def apply_backoff_policy(
        self,
        routing_key: str,
        delivery_tag: str,
        backoff_policy: dict[int, int],
        backoff_tasks: list[str],
    ) -> None: ...
    def extract_task_name_and_number_of_retries(
        self, delivery_tag: str
    ) -> tuple[str, int]: ...

_QoS = QoS

class Channel(VirtualChannel):
    default_region: str
    default_visibility_timeout: int
    default_wait_time_seconds: int
    domain_format: str
    _asynsqs: Any | None
    _predefined_queue_async_clients: dict[str, Any]
    _sqs: Any | None
    _predefined_queue_clients: dict[str, Any]
    _queue_cache: dict[str, str]
    _noack_queues: set[str]
    QoS: type[_QoS]  # pyright: ignore[reportIncompatibleVariableOverride]
    B64_REGEX: re.Pattern[bytes]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def basic_consume(
        self, queue: str, no_ack: bool, *args: Any, **kwargs: Any
    ) -> str: ...
    @override
    def basic_cancel(self, consumer_tag: str) -> Any: ...
    @override
    def drain_events(
        self, timeout: float | None = ..., callback: Any | None = ..., **kwargs: Any
    ) -> None: ...
    def entity_name(self, name: str, table: dict[int, int] = ...) -> str: ...
    def canonical_queue_name(self, queue_name: str) -> str: ...
    @override
    def basic_ack(self, delivery_tag: str, multiple: bool = ...) -> None: ...
    @override
    def close(self) -> None: ...
    def new_sqs_client(
        self,
        region: str,
        access_key_id: str,
        secret_access_key: str,
        session_token: str | None = ...,
    ) -> Any: ...
    def sqs(self, queue: str | None = ...) -> Any: ...
    def asynsqs(self, queue: str | None = ...) -> Any: ...
    def generate_sts_session_token(
        self, role_arn: str, token_expiry_seconds: int
    ) -> dict[str, Any]: ...
    def generate_sts_session_token_with_buffer(
        self, role_arn: str, token_expiry_seconds: int, token_buffer_seconds: int = ...
    ) -> dict[str, Any]: ...
    @property
    def conninfo(self) -> Any: ...
    @property
    def transport_options(self) -> dict[str, Any]: ...
    @cached_property
    def visibility_timeout(self) -> int: ...
    @cached_property
    def predefined_queues(self) -> dict[str, Any]: ...
    @cached_property
    def queue_name_prefix(self) -> str: ...
    @cached_property
    def supports_fanout(self) -> bool: ...  # pyright: ignore[reportIncompatibleVariableOverride]
    @cached_property
    def region(self) -> str: ...
    @cached_property
    def regioninfo(self) -> Any: ...
    @cached_property
    def is_secure(self) -> bool | None: ...
    @cached_property
    def port(self) -> int | None: ...
    @cached_property
    def endpoint_url(self) -> str | None: ...
    @cached_property
    def wait_time_seconds(self) -> int: ...
    @cached_property
    def sqs_base64_encoding(self) -> bool: ...
    @cached_property
    def fetch_message_attributes(self) -> Any: ...
    @property
    def get_message_attributes(self) -> dict[str, Any]: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

    polling_interval: int  # pyright: ignore[reportIncompatibleVariableOverride]
    wait_time_seconds: int
    default_port: None  # pyright: ignore[reportIncompatibleVariableOverride]
    connection_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    channel_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    implements: Any

    @property
    @override
    def default_connection_params(self) -> dict[str, Any]: ...
