__all__ = (
    "AMQPDeprecationWarning",
    "AMQPError",
    "AMQPNotImplementedError",
    "AccessRefused",
    "ChannelError",
    "ChannelNotOpen",
    "ConnectionError",
    "ConnectionForced",
    "ConsumerCancelled",
    "ContentTooLarge",
    "FrameError",
    "FrameSyntaxError",
    "InternalError",
    "InvalidCommand",
    "InvalidPath",
    "IrrecoverableChannelError",
    "IrrecoverableConnectionError",
    "MessageNacked",
    "NoConsumers",
    "NotAllowed",
    "NotFound",
    "PreconditionFailed",
    "RecoverableChannelError",
    "RecoverableConnectionError",
    "ResourceError",
    "ResourceLocked",
    "UnexpectedFrame",
)

class AMQPError(Exception):
    code: int
    recoverable: bool
    reply_text: str | None
    method_sig: tuple[int, int] | None
    method_name: str | None
    reply_code: int | None

    def __init__(
        self,
        reply_text: str | None = ...,
        method_sig: tuple[int, int] | None = ...,
        method_name: str | None = ...,
        reply_code: int | None = ...,
    ) -> None: ...
    @property
    def method(self) -> tuple[int, int] | None: ...

class ConnectionError(AMQPError): ...
class ChannelError(AMQPError): ...
class RecoverableConnectionError(ConnectionError): ...
class IrrecoverableConnectionError(ConnectionError): ...
class RecoverableChannelError(ChannelError): ...
class IrrecoverableChannelError(ChannelError): ...

class ConsumerCancelled(RecoverableConnectionError):
    code: int

class ContentTooLarge(RecoverableChannelError):
    code: int

class NoConsumers(RecoverableChannelError):
    code: int

class ConnectionForced(RecoverableConnectionError):
    code: int

class InvalidPath(IrrecoverableConnectionError):
    code: int

class AccessRefused(IrrecoverableChannelError):
    code: int

class NotFound(IrrecoverableChannelError):
    code: int

class ResourceLocked(RecoverableChannelError):
    code: int

class PreconditionFailed(IrrecoverableChannelError):
    code: int

class FrameError(IrrecoverableConnectionError):
    code: int

class FrameSyntaxError(IrrecoverableConnectionError):
    code: int

class InvalidCommand(IrrecoverableConnectionError):
    code: int

class ChannelNotOpen(IrrecoverableConnectionError):
    code: int

class UnexpectedFrame(IrrecoverableConnectionError):
    code: int

class ResourceError(RecoverableConnectionError):
    code: int

class NotAllowed(IrrecoverableConnectionError):
    code: int

class AMQPNotImplementedError(IrrecoverableConnectionError):
    code: int

class InternalError(IrrecoverableConnectionError):
    code: int

class MessageNacked(Exception): ...
class AMQPDeprecationWarning(UserWarning): ...

def error_for_code(
    code: int,
    text: str,
    method: tuple[int, int],
    default: type[AMQPError],
) -> AMQPError: ...
