from typing import Any

from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session, sessionmaker
from typing_extensions import override

VERSION: tuple[int, int, int]

class Channel(VirtualChannel):
    _session: Any | None
    _engines: dict[str, Any]
    queue_tablename: str
    message_tablename: str

    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
    @property
    def session(self) -> Session: ...
    @cached_property
    def queue_cls(self) -> type[Any]: ...
    @cached_property
    def message_cls(self) -> type[Any]: ...
    def _configure_entity_tablenames(self, opts: dict[str, Any]) -> None: ...
    def _engine_from_config(self) -> Engine: ...
    def _open(self) -> tuple[Engine, sessionmaker[Session]]: ...
    @override
    def _get(self, queue: str) -> Any: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def _put(self, queue: str, payload: Any, **kwargs: Any) -> None: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def _size(self, queue: str) -> int: ...

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

    can_parse_url: bool
    default_port: int  # pyright: ignore[reportIncompatibleVariableOverride]
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[OperationalError], ...]  # pyright: ignore[reportIncompatibleVariableOverride]

    @override
    def driver_version(self) -> str: ...
