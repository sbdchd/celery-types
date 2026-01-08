from collections.abc import Callable, Generator
from contextlib import contextmanager
from logging import Logger
from typing import Any, NamedTuple

import redis as redis_module
from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import QoS as VirtualQoS
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property
from redis.client import Pipeline as _RedisPipeline
from redis.client import PubSub as _RedisPubSub
from typing_extensions import override

logger: Logger
crit: Callable[..., None]
warning: Callable[..., None]

DEFAULT_PORT: int
DEFAULT_DB: int
DEFAULT_HEALTH_CHECK_INTERVAL: int
PRIORITY_STEPS: list[int]

class error_classes_t(NamedTuple):
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]

def get_redis_error_classes() -> error_classes_t: ...
def get_redis_ConnectionError() -> type[Exception]: ...
def _after_fork_cleanup_channel(channel: Channel) -> None: ...

class MutexHeld(Exception): ...

@contextmanager
def Mutex(client: Any, name: str, expire: int) -> Generator[None, None, None]: ...

class GlobalKeyPrefixMixin:
    PREFIXED_SIMPLE_COMMANDS: list[str]
    PREFIXED_COMPLEX_COMMANDS: dict[str, dict[str, int | None]]
    global_keyprefix: str

    def _prefix_args(self, args: tuple[Any, ...] | list[Any]) -> list[Any]: ...
    def parse_response(
        self, connection: Any, command_name: str, **options: Any
    ) -> Any: ...
    def execute_command(self, *args: Any, **kwargs: Any) -> Any: ...
    def pipeline(
        self, transaction: bool = ..., shard_hint: Any | None = ...
    ) -> PrefixedRedisPipeline: ...

class PrefixedStrictRedis(GlobalKeyPrefixMixin, redis_module.Redis):
    global_keyprefix: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def pubsub(self, **kwargs: Any) -> PrefixedRedisPubSub: ...

class PrefixedRedisPipeline(GlobalKeyPrefixMixin, _RedisPipeline):
    global_keyprefix: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class PrefixedRedisPubSub(_RedisPubSub):
    PUBSUB_COMMANDS: tuple[str, ...]
    global_keyprefix: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _prefix_args(self, args: tuple[Any, ...] | list[Any]) -> list[Any]: ...
    @override
    def parse_response(self, *args: Any, **kwargs: Any) -> Any: ...
    @override
    def execute_command(self, *args: Any, **kwargs: Any) -> Any: ...

class QoS(VirtualQoS):
    restore_at_shutdown: bool

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def append(self, message: Any, delivery_tag: str) -> None: ...
    @override
    def restore_unacked(self, client: Any | None = ...) -> None: ...
    @override
    def ack(self, delivery_tag: str) -> None: ...
    @override
    def reject(self, delivery_tag: str, requeue: bool = ...) -> None: ...
    @contextmanager
    def pipe_or_acquire(
        self, pipe: Any | None = ..., client: Any | None = ...
    ) -> Generator[Any, None, None]: ...
    @override
    def restore_visible(
        self, start: int = ..., num: int = ..., interval: int = ...
    ) -> None: ...
    def restore_by_tag(
        self, tag: str, client: Any | None = ..., leftmost: bool = ...
    ) -> None: ...
    @cached_property
    def unacked_key(self) -> str: ...
    @cached_property
    def unacked_index_key(self) -> str: ...
    @cached_property
    def unacked_mutex_key(self) -> str: ...
    @cached_property
    def unacked_mutex_expire(self) -> int: ...
    @cached_property
    def visibility_timeout(self) -> int: ...

class MultiChannelPoller:
    eventflags: int
    after_read: set[Any] | None
    poller: Any

    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def add(self, channel: Channel) -> None: ...
    def discard(self, channel: Channel) -> None: ...
    def on_poll_start(self) -> None: ...
    def on_poll_init(self, poller: Any) -> Any: ...
    def maybe_restore_messages(self) -> Any: ...
    def maybe_check_subclient_health(self) -> None: ...
    def on_readable(self, fileno: int) -> None: ...
    def handle_event(
        self, fileno: int, event: int
    ) -> tuple[Any, MultiChannelPoller] | None: ...
    def get(
        self, callback: Callable[..., Any], timeout: float | None = ...
    ) -> None: ...
    @property
    def fds(self) -> dict[int, tuple[Channel, str]]: ...

_QoS = QoS

class Channel(VirtualChannel):
    QoS: type[_QoS]  # pyright: ignore[reportIncompatibleVariableOverride]

    supports_fanout: bool
    keyprefix_queue: str
    keyprefix_fanout: str
    sep: str
    ack_emulation: bool
    unacked_key: str
    unacked_index_key: str
    unacked_mutex_key: str
    unacked_mutex_expire: int
    unacked_restore_limit: int | None
    visibility_timeout: int
    priority_steps: list[int]
    socket_timeout: float | None
    socket_connect_timeout: float | None
    socket_keepalive: bool | None
    socket_keepalive_options: dict[str, Any] | None
    retry_on_timeout: bool | None
    max_connections: int
    health_check_interval: int
    client_name: str | None
    fanout_prefix: bool | str
    fanout_patterns: bool
    global_keyprefix: str
    queue_order_strategy: str

    connection_class: type[Any] | None
    connection_class_ssl: type[Any] | None

    from_transport_options: tuple[str, ...]

    handlers: dict[str, Callable[..., Any]]
    brpop_timeout: int
    active_fanout_queues: set[str]
    auto_delete_queues: set[str]
    Client: type[Any]
    ResponseError: type[Exception]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def basic_consume(self, queue: str, *args: Any, **kwargs: Any) -> Any: ...
    @override
    def basic_cancel(self, consumer_tag: str) -> Any: ...
    @override
    def close(self) -> None: ...
    @override
    def get_table(self, exchange: str) -> list[tuple[str, str, str]]: ...
    def priority(self, n: int) -> int: ...
    @contextmanager
    def conn_or_acquire(
        self, client: Any | None = ...
    ) -> Generator[Any, None, None]: ...
    @property
    def pool(self) -> Any: ...
    @property
    def async_pool(self) -> Any: ...
    @cached_property
    def client(self) -> Any: ...
    @cached_property
    def subclient(self) -> Any: ...
    @property
    def active_queues(self) -> set[str]: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

    polling_interval: None  # pyright: ignore[reportIncompatibleVariableOverride]
    brpop_timeout: int
    default_port: int  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    implements: Any
    connection_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    channel_errors: tuple[type[Exception], ...]  # pyright: ignore[reportIncompatibleVariableOverride]
    cycle: MultiChannelPoller | None  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def driver_version(self) -> str: ...
    @override
    def register_with_event_loop(self, connection: Any, loop: Any) -> None: ...
    @override
    def on_readable(self, fileno: int) -> None: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

class SentinelManagedSSLConnection:
    def __init__(self, **kwargs: Any) -> None: ...

class SentinelChannel(Channel):
    from_transport_options: tuple[str, ...]
    connection_class: type[Any] | None
    connection_class_ssl: type[Any] | None

class SentinelTransport(Transport):
    default_port: int
    Channel: type[SentinelChannel]  # pyright: ignore[reportIncompatibleVariableOverride]
