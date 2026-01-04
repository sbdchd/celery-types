from collections.abc import Callable, Mapping
from socket import socket
from typing import Any, TypeAlias

from amqp.channel import Channel as _ChannelType
from typing_extensions import Self

__all__ = ("Connection",)

_ChannelTypeAlias: TypeAlias = _ChannelType

class Connection:
    Channel: type[_ChannelTypeAlias]

    host: str
    userid: str
    password: str
    login_method: str | None
    virtual_host: str
    locale: str
    client_properties: dict[str, Any]
    ssl: bool | dict[str, Any]
    connect_timeout: float | None
    channel_max: int | None
    frame_max: int
    heartbeat: int | None
    confirm_publish: bool
    read_timeout: float | None
    write_timeout: float | None

    bytes_sent: int
    bytes_recv: int
    last_heartbeat_sent: int
    last_heartbeat_received: int
    channel_errors: tuple[type[Exception], ...]
    connection_errors: tuple[type[Exception], ...]
    recoverable_channel_errors: tuple[type[Exception], ...]
    recoverable_connection_errors: tuple[type[Exception], ...]

    client_heartbeat: int | None
    server_heartbeat: int | None
    prev_recv: float | None
    prev_sent: float | None
    library_properties: dict[str, Any]
    negotiate_capabilities: dict[str, bool]

    auto_decode: bool
    channel_id: int | None
    connection: Any
    is_closing: bool
    method_queue: list[Any]

    def __init__(
        self,
        host: str = ...,
        userid: str = ...,
        password: str = ...,
        login_method: str | None = ...,
        login_response: Any | None = ...,
        authentication: tuple[Any, ...] = ...,
        virtual_host: str = ...,
        locale: str = ...,
        client_properties: dict[str, Any] | None = ...,
        ssl: bool | dict[str, Any] = ...,
        connect_timeout: float | None = ...,
        channel_max: int | None = ...,
        frame_max: int | None = ...,
        heartbeat: int = ...,
        on_open: Callable[..., Any] | None = ...,
        on_blocked: Callable[..., Any] | None = ...,
        on_unblocked: Callable[..., Any] | None = ...,
        confirm_publish: bool = ...,
        on_tune_ok: Callable[..., Any] | None = ...,
        read_timeout: float | None = ...,
        write_timeout: float | None = ...,
        socket_settings: Mapping[str, Any] | None = ...,
        frame_handler: Callable[..., Any] = ...,
        frame_writer: Callable[..., Any] = ...,
        **kwargs: Any,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *eargs: object) -> None: ...
    def Transport(
        self,
        host: str,
        connect_timeout: float | None,
        ssl: bool | dict[str, Any] = ...,
        read_timeout: float | None = ...,
        write_timeout: float | None = ...,
        socket_settings: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> Any: ...
    def connect(self, callback: Callable[..., Any] | None = ...) -> None: ...
    def close(
        self,
        reply_code: int = ...,
        reply_text: str = ...,
        method_sig: tuple[int, int] = ...,
        argsig: str = ...,
    ) -> None: ...
    def channel(
        self, channel_id: int | None = ..., callback: Callable[..., Any] | None = ...
    ) -> _ChannelTypeAlias: ...
    def drain_events(self, timeout: float | None = ...) -> None: ...
    def blocking_read(self, timeout: float | None = ...) -> None: ...
    def collect(self) -> None: ...
    def heartbeat_tick(self, rate: int = ...) -> None: ...
    def send_heartbeat(self) -> None: ...
    def is_alive(self) -> bool: ...
    def dispatch_method(
        self, method_sig: tuple[int, int], payload: bytes, content: Any
    ) -> None: ...
    def on_inbound_method(
        self,
        channel_id: int,
        method_sig: tuple[int, int],
        payload: bytes,
        content: Any,
    ) -> None: ...
    def send_method(
        self,
        sig: tuple[int, int],
        format: str | None = ...,
        args: tuple[Any, ...] | None = ...,
        content: Any | None = ...,
        wait: Any | None = ...,
        callback: Callable[..., Any] | None = ...,
        returns_tuple: bool = ...,
    ) -> Any: ...
    def wait(
        self,
        method: Any,
        callback: Callable[..., Any] | None = ...,
        timeout: float | None = ...,
        returns_tuple: bool = ...,
    ) -> Any: ...
    def then(
        self,
        on_success: Callable[..., Any],
        on_error: Callable[..., Any] | None = ...,
    ) -> Any: ...
    @property
    def connected(self) -> bool: ...
    @property
    def sock(self) -> socket | None: ...
    @property
    def server_capabilities(self) -> dict[str, Any]: ...
    @property
    def transport(self) -> Any: ...
    @property
    def frame_writer(self) -> Callable[..., Any]: ...
    @property
    def on_inbound_frame(self) -> Callable[..., Any]: ...
