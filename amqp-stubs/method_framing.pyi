from collections.abc import Callable
from typing import Any

from amqp.basic_message import Message as Message
from amqp.exceptions import UnexpectedFrame as UnexpectedFrame

__all__ = ("frame_handler", "frame_writer")

FRAME_OVERHEAD: int

def frame_handler(
    connection: Any,
    callback: Callable[..., Any],
    unpack_from: Callable[..., tuple[Any, ...]] = ...,
    content_methods: frozenset[tuple[int, int]] = ...,
) -> Callable[..., Any]: ...
def frame_writer(
    connection: Any,
    transport: Any,
    pack: Callable[..., bytes] = ...,
    pack_into: Callable[..., None] = ...,
    range: type[range] = ...,
    len: Callable[[Any], int] = ...,
    bytes: type[bytes] = ...,
    str_to_bytes: Callable[[str], bytes] = ...,
    text_t: type[str] = ...,
) -> Callable[..., Any]: ...
def str_to_bytes(s: str) -> bytes: ...
