import re
from collections.abc import Callable, Generator, Mapping
from contextlib import contextmanager
from socket import socket
from ssl import SSLError as SSLError
from typing import Any

from amqp.exceptions import UnexpectedFrame as UnexpectedFrame

AMQP_PORT: int
AMQP_PROTOCOL_HEADER: bytes
DEFAULT_SOCKET_SETTINGS: dict[str, Any]
EMPTY_BUFFER: bytes
IPV6_LITERAL: re.Pattern[str]
KNOWN_TCP_OPTS: set[str]
SIGNED_INT_MAX: int
SOL_TCP: int

class TCPTransport:
    host: str
    port: int
    connect_timeout: float | None
    read_timeout: float | None
    write_timeout: float | None
    socket_settings: Mapping[str, Any] | None
    sock: socket | None
    connection: Any
    raise_on_initial_eintr: bool

    def __init__(
        self,
        host: str,
        connect_timeout: float | None = ...,
        read_timeout: float | None = ...,
        write_timeout: float | None = ...,
        socket_settings: Mapping[str, Any] | None = ...,
        raise_on_initial_eintr: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def connect(self) -> None: ...
    def close(self) -> None: ...
    def read_frame(
        self, unpack: Callable[[str, bytes], tuple[Any, ...]] = ...
    ) -> tuple[int, int, bytes]: ...
    def write(self, s: bytes) -> None: ...
    @contextmanager
    def having_timeout(self, timeout: float | None) -> Generator[None, None, None]: ...

class SSLTransport(TCPTransport):
    sslopts: dict[str, Any] | bool | None

    def __init__(
        self,
        host: str,
        connect_timeout: float | None = ...,
        ssl: bool | dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...

def Transport(
    host: str,
    connect_timeout: float | None = ...,
    ssl: bool | dict[str, Any] = ...,
    **kwargs: Any,
) -> TCPTransport | SSLTransport: ...
def to_host_port(host: str, default: int = ...) -> tuple[str, int]: ...
def set_cloexec(fd: int, cloexec: bool) -> None: ...
