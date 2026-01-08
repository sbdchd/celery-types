from typing import Any

__all__ = ("poll",)

READ: int
WRITE: int
ERR: int

def poll(*args: Any) -> Any: ...
