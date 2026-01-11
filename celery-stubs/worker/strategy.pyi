import logging
from collections.abc import Callable
from typing import Any

__all__ = ("default",)

logger: logging.Logger

def default(
    task: Any,
    app: Any,
    consumer: Any,
    info: Callable[..., None] = ...,
    error: Callable[..., None] = ...,
    task_reserved: Callable[..., Any] = ...,
    to_system_tz: Callable[..., Any] = ...,
    bytes: type[bytes] = ...,
    proto1_to_proto2: Callable[..., Any] = ...,
) -> Callable[..., Any]: ...
