from collections.abc import Callable
from typing import Any, BinaryIO, TextIO

def default_encode(obj: Any) -> bytes: ...
def emergency_dump_state(
    state: Any,
    open_file: Callable[..., BinaryIO | TextIO] = ...,
    dump: Callable[..., None] | None = ...,
    stderr: TextIO | None = ...,
) -> None: ...
