from collections.abc import Callable
from typing import Any

READ: int
WRITE: int
ERR: int

def poll() -> Any: ...
