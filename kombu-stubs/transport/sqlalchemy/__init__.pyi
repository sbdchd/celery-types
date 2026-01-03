from typing import Any

from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from kombu.transport.virtual import Channel as VirtualChannel
from kombu.transport.virtual import Transport as VirtualTransport
from kombu.utils.objects import cached_property

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

_Channel = Channel

class Transport(VirtualTransport):
    Channel: type[_Channel]

    can_parse_url: bool
    default_port: int
    driver_type: str
    driver_name: str
    connection_errors: tuple[type[OperationalError], ...]

    def driver_version(self) -> str: ...
