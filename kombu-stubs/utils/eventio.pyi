from collections.abc import Callable
from typing import Any

__all__: tuple[str, ...]

READ: int
WRITE: int
ERR: int

def poll(*args: Any) -> Any: ...
