from collections.abc import Callable, Generator
from typing import Any
from uuid import UUID

from kombu import pools as pools
from kombu.connection import Connection as Connection
from kombu.entity import Exchange as Exchange
from kombu.entity import Queue as Queue
from kombu.entity import binding as binding
from kombu.message import Message as Message
from kombu.messaging import Consumer as Consumer
from kombu.messaging import Producer as Producer
from kombu.pools import Connections as _Connections
from kombu.pools import Producers as _Producers

__all__ = (
    "BrokerConnection",
    "Connection",
    "Consumer",
    "Exchange",
    "Message",
    "Producer",
    "Queue",
    "binding",
    "connections",
    "disable_insecure_serializers",
    "enable_insecure_serializers",
    "eventloop",
    "parse_url",
    "producers",
    "uuid",
)

BrokerConnection = Connection

connections: _Connections
producers: _Producers

def parse_url(url: str) -> dict[str, Any]: ...
def eventloop(
    conn: Connection,
    limit: int | None = ...,
    timeout: float | None = ...,
    ignore_timeouts: bool = ...,
) -> Generator[Any, None, None]: ...
def uuid(_uuid: Callable[[], UUID] = ...) -> str: ...
def enable_insecure_serializers(choices: Any = ...) -> None: ...
def disable_insecure_serializers(allowed: Any = ...) -> None: ...
