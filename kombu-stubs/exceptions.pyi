from types import TracebackType
from typing import Any

from amqp import ChannelError as ChannelError
from amqp import ConnectionError as ConnectionError

__all__ = (
    "ChannelError",
    "ChannelLimitExceeded",
    "ConnectionError",
    "ConnectionLimitExceeded",
    "DecodeError",
    "EncodeError",
    "HttpError",
    "InconsistencyError",
    "KombuError",
    "LimitExceeded",
    "MessageStateError",
    "NotBoundError",
    "OperationalError",
    "ResourceError",
    "SerializationError",
    "SerializerNotInstalled",
    "TimeoutError",
    "VersionMismatch",
    "reraise",
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
