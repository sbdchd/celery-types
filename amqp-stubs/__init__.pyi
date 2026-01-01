from collections.abc import Callable, Mapping, Sequence
from typing import Any

from amqp.channel import Channel as Channel
from amqp.connection import Connection as Connection
from amqp.exceptions import (
    AMQPError as AMQPError,
    AMQPNotImplementedError as AMQPNotImplementedError,
    AccessRefused as AccessRefused,
    ChannelError as ChannelError,
    ChannelNotOpen as ChannelNotOpen,
    ConnectionError as ConnectionError,
    ConnectionForced as ConnectionForced,
    ConsumerCancelled as ConsumerCancelled,
    ContentTooLarge as ContentTooLarge,
    FrameError as FrameError,
    FrameSyntaxError as FrameSyntaxError,
    InternalError as InternalError,
    InvalidCommand as InvalidCommand,
    InvalidPath as InvalidPath,
    IrrecoverableChannelError as IrrecoverableChannelError,
    IrrecoverableConnectionError as IrrecoverableConnectionError,
    NoConsumers as NoConsumers,
    NotAllowed as NotAllowed,
    NotFound as NotFound,
    PreconditionFailed as PreconditionFailed,
    RecoverableChannelError as RecoverableChannelError,
    RecoverableConnectionError as RecoverableConnectionError,
    ResourceError as ResourceError,
    ResourceLocked as ResourceLocked,
    UnexpectedFrame as UnexpectedFrame,
    error_for_code as error_for_code,
)
from amqp.basic_message import Message as Message

__all__ = (
    "Connection",
    "Channel",
    "Message",
    "promise",
    "AMQPError",
    "ConnectionError",
    "RecoverableConnectionError",
    "IrrecoverableConnectionError",
    "ChannelError",
    "RecoverableChannelError",
    "IrrecoverableChannelError",
    "ConsumerCancelled",
    "ContentTooLarge",
    "NoConsumers",
    "ConnectionForced",
    "InvalidPath",
    "AccessRefused",
    "NotFound",
    "ResourceLocked",
    "PreconditionFailed",
    "FrameError",
    "FrameSyntaxError",
    "InvalidCommand",
    "ChannelNotOpen",
    "UnexpectedFrame",
    "ResourceError",
    "NotAllowed",
    "AMQPNotImplementedError",
    "InternalError",
    "error_for_code",
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
    def then(self, callback: Callable[..., Any], on_error: Callable[..., Any] | None = ...) -> promise: ...
    def throw(self, exc: BaseException | None = ..., tb: Any | None = ..., propagate: bool = ...) -> None: ...
    def throw1(self, exc: BaseException | None = ...) -> None: ...
    def cancel(self) -> None: ...
    @property
    def listeners(self) -> list[promise]: ...
