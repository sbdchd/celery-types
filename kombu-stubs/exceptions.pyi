from types import TracebackType
from typing import Any

from amqp import ChannelError as ChannelError
from amqp import ConnectionError as ConnectionError

__all__ = (
    "reraise",
    "KombuError",
    "OperationalError",
    "NotBoundError",
    "MessageStateError",
    "TimeoutError",
    "LimitExceeded",
    "ConnectionLimitExceeded",
    "ChannelLimitExceeded",
    "ConnectionError",
    "ChannelError",
    "VersionMismatch",
    "SerializerNotInstalled",
    "ResourceError",
    "SerializationError",
    "EncodeError",
    "DecodeError",
    "HttpError",
    "InconsistencyError",
)

class KombuError(Exception): ...
class OperationalError(KombuError): ...
class SerializationError(KombuError): ...
class EncodeError(SerializationError): ...
class DecodeError(SerializationError): ...
class NotBoundError(KombuError): ...
class MessageStateError(KombuError): ...
class TimeoutError(KombuError): ...
class LimitExceeded(KombuError): ...
class ConnectionLimitExceeded(LimitExceeded): ...
class ChannelLimitExceeded(LimitExceeded): ...
class VersionMismatch(KombuError): ...
class SerializerNotInstalled(KombuError): ...
class ContentDisallowed(SerializerNotInstalled): ...

class ResourceError(KombuError):
    code: int

class InconsistencyError(ConnectionError): ...

class HttpError(Exception):
    code: int
    message: str | None
    response: Any | None

    def __init__(
        self, code: int, message: str | None = ..., response: Any | None = ...
    ) -> None: ...

def reraise(
    tp: type[BaseException] | None,
    value: BaseException | None,
    tb: TracebackType | None = ...,
) -> None: ...
