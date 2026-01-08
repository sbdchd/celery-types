from collections.abc import Callable
from typing import Any

__all__ = ("Event", "event_exchange", "get_exchange", "group_from")

event_exchange: Any

def Event(
    type: str,
    _fields: dict[str, Any] | None = None,
    __dict__: type[dict[str, Any]] = ...,
    __now__: Callable[[], float] = ...,
    **fields: Any,
) -> dict[str, Any]: ...
def group_from(type: str) -> str: ...
def get_exchange(conn: Any, name: str = ...) -> Any: ...
