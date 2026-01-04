from collections.abc import Callable
from logging import Logger
from typing import Any

from amqp.exceptions import AMQPNotImplementedError as AMQPNotImplementedError
from amqp.exceptions import RecoverableConnectionError as RecoverableConnectionError
from typing_extensions import Self
from vine import promise

__all__ = ("AbstractChannel",)

AMQP_LOGGER: Logger
IGNORED_METHOD_DURING_CHANNEL_CLOSE: str

class AbstractChannel:
    auto_decode: bool
    channel_id: int | None
    connection: Any
    is_closing: bool
    method_queue: list[Any]

    def __init__(self, connection: Any, channel_id: int | None) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
    def close(self) -> None: ...
    def dispatch_method(
        self, method_sig: tuple[int, int], payload: bytes, content: Any
    ) -> None: ...
    def send_method(
        self,
        sig: tuple[int, int],
        format: str | None = ...,
        args: tuple[Any, ...] | None = ...,
        content: Any | None = ...,
        wait: Any | None = ...,
        callback: Callable[..., Any] | None = ...,
        returns_tuple: bool = ...,
    ) -> Any: ...
    def wait(
        self,
        method: Any,
        callback: Callable[..., Any] | None = ...,
        timeout: float | None = ...,
        returns_tuple: bool = ...,
    ) -> Any: ...

def dumps(format: str, values: tuple[Any, ...]) -> bytes: ...
def loads(format: str, buf: bytes, offset: int) -> tuple[Any, ...]: ...
def ensure_promise(p: promise | Callable[..., Any] | None) -> promise: ...
