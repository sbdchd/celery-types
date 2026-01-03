"""librabbitmq transport stubs.

Note: librabbitmq is abandoned (last release 2018, Python 3.6 max).
These stubs are based on the kombu transport source code.
"""

from typing import Any

from kombu.transport import base

DEFAULT_PORT: int
DEFAULT_SSL_PORT: int
NO_SSL_ERROR: str
W_VERSION: str

class Message(base.Message):
    def __init__(
        self, channel: Channel, props: dict[str, Any],
        info: dict[str, Any], body: bytes
    ) -> None: ...

class Channel(base.StdChannel):
    Message: type[Message]

    def prepare_message(
        self, body: bytes, priority: int | None = ...,
        content_type: str | None = ..., content_encoding: str | None = ...,
        headers: dict[str, Any] | None = ..., properties: dict[str, Any] | None = ...
    ) -> tuple[bytes, dict[str, Any]]: ...
    def prepare_queue_arguments(  # type: ignore[override]
        self, arguments: dict[str, Any] | None, **kwargs: Any
    ) -> dict[bytes, Any]: ...

_Channel = Channel

class Connection:
    Channel: type[_Channel]
    Message: type[Message]
    channels: dict[int, _Channel]
    callbacks: dict[str, Any]
    client: Any

    def channel(self) -> _Channel: ...
    def drain_events(self, **kwargs: Any) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    @property
    def connected(self) -> bool: ...
    @property
    def server_properties(self) -> dict[str, Any]: ...

_Connection = Connection

class Transport(base.Transport):
    Connection: type[_Connection]

    default_port: int
    default_ssl_port: int
    connection_errors: tuple[type[BaseException], ...]
    channel_errors: tuple[type[BaseException], ...]
    driver_type: str
    driver_name: str
    implements: Any

    def __init__(self, client: Any, **kwargs: Any) -> None: ...
    def driver_version(self) -> str: ...
    def create_channel(self, connection: _Connection) -> _Channel: ...
    def drain_events(self, connection: _Connection, **kwargs: Any) -> None: ...
    def establish_connection(self) -> _Connection: ...
    def close_connection(self, connection: _Connection) -> None: ...
    def verify_connection(self, connection: _Connection) -> bool: ...
    def register_with_event_loop(self, connection: _Connection, loop: Any) -> None: ...
    def get_manager(self, *args: Any, **kwargs: Any) -> Any: ...
    def qos_semantics_matches_spec(self, connection: _Connection) -> bool: ...
    @property
    def default_connection_params(self) -> dict[str, Any]: ...
