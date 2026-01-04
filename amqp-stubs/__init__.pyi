from collections.abc import Callable, Mapping, Sequence
from typing import Any

from amqp.basic_message import Message as Message
from amqp.channel import Channel as Channel
from amqp.connection import Connection as Connection
from amqp.exceptions import (
    AccessRefused as AccessRefused,
)
from amqp.exceptions import (
    AMQPError as AMQPError,
)
from amqp.exceptions import (
    AMQPNotImplementedError as AMQPNotImplementedError,
)
from amqp.exceptions import (
    ChannelError as ChannelError,
)
from amqp.exceptions import (
    ChannelNotOpen as ChannelNotOpen,
)
from amqp.exceptions import (
    ConnectionError as ConnectionError,
)
from amqp.exceptions import (
    ConnectionForced as ConnectionForced,
)
from amqp.exceptions import (
    ConsumerCancelled as ConsumerCancelled,
)
from amqp.exceptions import (
    ContentTooLarge as ContentTooLarge,
)
from amqp.exceptions import (
    FrameError as FrameError,
)
from amqp.exceptions import (
    FrameSyntaxError as FrameSyntaxError,
)
from amqp.exceptions import (
    InternalError as InternalError,
)
from amqp.exceptions import (
    InvalidCommand as InvalidCommand,
)
from amqp.exceptions import (
    InvalidPath as InvalidPath,
)
from amqp.exceptions import (
    IrrecoverableChannelError as IrrecoverableChannelError,
)
from amqp.exceptions import (
    IrrecoverableConnectionError as IrrecoverableConnectionError,
)
from amqp.exceptions import (
    NoConsumers as NoConsumers,
)
from amqp.exceptions import (
    NotAllowed as NotAllowed,
)
from amqp.exceptions import (
    NotFound as NotFound,
)
from amqp.exceptions import (
    PreconditionFailed as PreconditionFailed,
)
from amqp.exceptions import (
    RecoverableChannelError as RecoverableChannelError,
)
from amqp.exceptions import (
    RecoverableConnectionError as RecoverableConnectionError,
)
from amqp.exceptions import (
    ResourceError as ResourceError,
)
from amqp.exceptions import (
    ResourceLocked as ResourceLocked,
)
from amqp.exceptions import (
    UnexpectedFrame as UnexpectedFrame,
)
from amqp.exceptions import (
    error_for_code as error_for_code,
)

__all__ = (
    "AMQPError",
    "AMQPNotImplementedError",
    "AccessRefused",
    "Channel",
    "ChannelError",
    "ChannelNotOpen",
    "Connection",
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
    "Message",
    "NoConsumers",
    "NotAllowed",
    "NotFound",
    "PreconditionFailed",
    "RecoverableChannelError",
    "RecoverableConnectionError",
    "ResourceError",
    "ResourceLocked",
    "UnexpectedFrame",
    "error_for_code",
    "promise",
)

class promise:
    fun: Callable[..., Any] | None
    args: Sequence[Any]
    kwargs: Mapping[str, Any]
    on_error: Callable[..., Any] | None
    cancelled: bool
    failed: bool
    ready: bool
    reason: BaseException | None
    weak: bool
    ignore_result: bool
    value: Any

    def __init__(
        self,
        fun: Callable[..., Any] | None = ...,
        args: Sequence[Any] | None = ...,
        kwargs: Mapping[str, Any] | None = ...,
        callback: Callable[..., Any] | None = ...,
        on_error: Callable[..., Any] | None = ...,
        weak: bool = ...,
        ignore_result: bool = ...,
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def then(
        self, callback: Callable[..., Any], on_error: Callable[..., Any] | None = ...
    ) -> promise: ...
    def throw(
        self,
        exc: BaseException | None = ...,
        tb: Any | None = ...,
        propagate: bool = ...,
    ) -> None: ...
    def throw1(self, exc: BaseException | None = ...) -> None: ...
    def cancel(self) -> None: ...
    @property
    def listeners(self) -> list[promise]: ...
