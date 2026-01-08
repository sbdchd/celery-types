from collections.abc import Callable, Generator, Iterable, Iterator
from contextlib import contextmanager
from types import TracebackType
from typing import Any, TypeVar

from kombu.messaging import Consumer as _Consumer
from kombu.messaging import Producer as _Producer
from kombu.simple import SimpleBuffer as _SimpleBuffer
from kombu.simple import SimpleQueue as _SimpleQueue
from kombu.transport.base import Management, StdChannel, Transport
from kombu.utils.objects import cached_property
from typing_extensions import Self, override

__all__ = ("ChannelPool", "Connection", "ConnectionPool")

def is_connection(obj: Any) -> bool: ...
def maybe_channel(channel: StdChannel | Connection | None) -> StdChannel | None: ...

_T = TypeVar("_T")

class Resource:
    LimitExceeded: type[Exception]
    close_after_fork: bool
    limit: int | None
    preload: int | None

    def __init__(
        self,
        limit: int | None = ...,
        preload: int | None = ...,
        close_after_fork: bool | None = ...,
    ) -> None: ...
    def setup(self) -> None: ...
    def acquire(self, block: bool = ..., timeout: float | None = ...) -> Any: ...
    def prepare(self, resource: Any) -> Any: ...
    def close_resource(self, resource: Any) -> None: ...
    def release_resource(self, resource: Any) -> None: ...
    def release(self, resource: Any) -> None: ...
    def collect_resource(self, resource: Any) -> None: ...
    def replace(self, resource: Any) -> None: ...
    def force_close_all(self, close_pool: bool = ...) -> None: ...
    def resize(
        self,
        limit: int,
        force: bool = ...,
        ignore_errors: bool = ...,
        reset: bool = ...,
    ) -> None: ...

class Connection:
    port: int | None
    virtual_host: str
    connect_timeout: float
    uri_prefix: str | None
    declared_entities: set[Any] | None
    cycle: Iterator[str] | None
    transport_options: dict[str, Any] | None
    failover_strategy: str | Callable[[Iterable[str]], Iterator[str]]
    heartbeat: float | None
    resolve_aliases: dict[str, str]
    failover_strategies: dict[str, Callable[[Iterable[str]], Iterator[str]]]
    hostname: str | None
    userid: str | None
    password: str | None
    ssl: bool | dict[str, Any] | None
    login_method: str | None
    alt: list[str]
    insist: bool
    transport_cls: str
    credential_provider: Any | None

    def __init__(
        self,
        hostname: str = ...,
        userid: str | None = ...,
        password: str | None = ...,
        virtual_host: str | None = ...,
        port: int | None = ...,
        insist: bool = ...,
        ssl: bool | dict[str, Any] = ...,
        transport: str | type[Transport] | None = ...,
        connect_timeout: float = ...,
        transport_options: dict[str, Any] | None = ...,
        login_method: str | None = ...,
        uri_prefix: str | None = ...,
        heartbeat: float = ...,
        failover_strategy: str | Callable[[Iterable[str]], Iterator[str]] = ...,
        alternates: list[str] | None = ...,
        credential_provider: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def switch(self, conn_str: str) -> None: ...
    def maybe_switch_next(self) -> None: ...
    def register_with_event_loop(self, loop: Any) -> None: ...
    def connect(self) -> Self: ...
    def channel(self) -> StdChannel: ...
    def drain_events(self, **kwargs: Any) -> None: ...
    def maybe_close_channel(self, channel: StdChannel | None) -> None: ...
    def collect(self, socket_timeout: float | None = ...) -> None: ...
    def release(self) -> None: ...
    close = release
    def ensure_connection(
        self,
        errback: Callable[[Exception, float], None] | None = ...,
        max_retries: int = ...,
        interval_start: int = ...,
        interval_step: int = ...,
        interval_max: int = ...,
        callback: Callable[[], None] | None = ...,
        reraise_as_library_errors: bool = ...,
        timeout: int | None = ...,
    ) -> Self: ...
    def _ensure_connection(
        self,
        errback: Callable[[Exception, float], None] | None = ...,
        max_retries: int | None = ...,
        interval_start: int = ...,
        interval_step: int = ...,
        interval_max: int = ...,
        callback: Callable[[], None] | None = ...,
        reraise_as_library_errors: bool = ...,
        timeout: int | None = ...,
    ) -> Self: ...
    def autoretry(
        self,
        fun: Callable[..., _T],
        channel: StdChannel | None = ...,
        **ensure_options: Any,
    ) -> _T: ...
    def ensure(
        self,
        obj: Any,
        fun: Callable[..., _T],
        errback: Callable[[Exception, float], None] | None = ...,
        max_retries: int | None = ...,
        interval_start: int = ...,
        interval_step: int = ...,
        interval_max: int = ...,
        on_revive: Callable[[StdChannel], None] | None = ...,
        retry_errors: tuple[type[BaseException], ...] | None = ...,
    ) -> Callable[..., _T]: ...
    def revive(self, new_channel: StdChannel) -> None: ...
    def completes_cycle(self, retries: int) -> bool: ...
    def create_transport(self) -> Transport: ...
    def get_transport_cls(self) -> type[Transport]: ...
    def clone(self, **kwargs: Any) -> Connection: ...
    def get_heartbeat_interval(self) -> int: ...
    def heartbeat_check(self, rate: int = ...) -> None: ...
    def get_manager(self, *args: Any, **kwargs: Any) -> Management: ...
    def info(self) -> dict[str, Any]: ...
    def as_uri(
        self,
        include_password: bool = ...,
        mask: str = ...,
        getfields: Callable[..., Any] | None = ...,
    ) -> str: ...
    def Pool(self, limit: int | None = ..., **kwargs: Any) -> ConnectionPool: ...
    def ChannelPool(self, limit: int | None = ..., **kwargs: Any) -> ChannelPool: ...  # ty: ignore[invalid-type-form]
    def Producer(
        self, channel: StdChannel | None = ..., *args: Any, **kwargs: Any
    ) -> _Producer: ...
    def Consumer(
        self,
        queues: Any | None = ...,
        channel: StdChannel | None = ...,
        *args: Any,
        **kwargs: Any,
    ) -> _Consumer: ...
    def SimpleQueue(
        self,
        name: str,
        no_ack: bool | None = ...,
        queue_opts: dict[str, Any] | None = ...,
        queue_args: dict[str, Any] | None = ...,
        exchange_opts: dict[str, Any] | None = ...,
        channel: StdChannel | None = ...,
        **kwargs: Any,
    ) -> _SimpleQueue: ...
    def SimpleBuffer(
        self,
        name: str,
        no_ack: bool | None = ...,
        queue_opts: dict[str, Any] | None = ...,
        queue_args: dict[str, Any] | None = ...,
        exchange_opts: dict[str, Any] | None = ...,
        channel: StdChannel | None = ...,
        **kwargs: Any,
    ) -> _SimpleBuffer: ...
    def supports_exchange_type(self, exchange_type: str) -> bool: ...
    def _init_params(
        self,
        hostname: str,
        userid: str | None,
        password: str | None,
        virtual_host: str | None,
        port: int | None,
        insist: bool,
        ssl: bool | dict[str, Any],
        transport: str | type[Transport] | None,
        connect_timeout: float,
        login_method: str | None,
        heartbeat: float,
        credential_provider: Any | None,
    ) -> None: ...
    def _extract_failover_opts(self) -> dict[str, Any]: ...
    def _reraise_as_library_errors(
        self,
        ConnectionError: type[Exception] = ...,
        ChannelError: type[Exception] = ...,
    ) -> Generator[None, None, None]: ...
    def _debug(self, msg: str, *args: Any, **kwargs: Any) -> None: ...
    def _establish_connection(self) -> Any: ...
    def _connection_factory(self) -> Any: ...
    @contextmanager
    def _dummy_context(self) -> Generator[Self, None, None]: ...
    def _info(self, resolve: bool = ...) -> dict[str, Any]: ...
    def _do_close_self(self) -> None: ...
    def _do_close_transport(self) -> None: ...
    def _close(self) -> None: ...
    def __reduce__(self) -> tuple[Any, ...]: ...
    def __copy__(self) -> Connection: ...
    def __eqhash__(self) -> tuple[str, ...]: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    @property
    def connected(self) -> bool: ...
    @property
    def connection(self) -> Any: ...
    @cached_property
    def connection_errors(self) -> tuple[type[BaseException], ...]: ...
    @cached_property
    def channel_errors(self) -> tuple[type[BaseException], ...]: ...
    @cached_property
    def recoverable_connection_errors(self) -> tuple[type[BaseException], ...]: ...
    @cached_property
    def recoverable_channel_errors(self) -> tuple[type[BaseException], ...]: ...
    @property
    def transport(self) -> Transport: ...
    @property
    def default_channel(self) -> StdChannel: ...
    @property
    def host(self) -> str: ...
    @cached_property
    def manager(self) -> Management: ...
    @property
    def supports_heartbeats(self) -> bool: ...
    @property
    def is_evented(self) -> bool: ...
    @property
    def qos_semantics_matches_spec(self) -> bool: ...

class ConnectionPool(Resource):
    LimitExceeded: type[Exception]
    connection: Connection

    def __init__(
        self, connection: Connection, limit: int | None = ..., **kwargs: Any
    ) -> None: ...
    def new(self) -> Connection: ...
    @override
    def prepare(self, resource: Connection) -> Connection: ...
    @override
    def release_resource(self, resource: Connection) -> None: ...
    @override
    def close_resource(self, resource: Connection) -> None: ...
    @override
    def collect_resource(
        self, resource: Connection, socket_timeout: float | None = ...
    ) -> None: ...
    def acquire_channel(
        self, block: bool = ...
    ) -> Generator[StdChannel, None, None]: ...

class PooledConnection:
    pool: ConnectionPool

    def __init__(self, pool: ConnectionPool) -> None: ...
    def __enter__(self) -> Connection: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

class ChannelPool(Resource):
    LimitExceeded: type[Exception]
    connection: Connection

    def __init__(
        self, connection: Connection, limit: int | None = ..., **kwargs: Any
    ) -> None: ...
    def new(self) -> StdChannel: ...
    @override
    def setup(self) -> None: ...
    @override
    def prepare(self, channel: StdChannel) -> StdChannel: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    @override
    def release_resource(self, resource: StdChannel) -> None: ...
    @override
    def close_resource(self, resource: StdChannel) -> None: ...
