from collections.abc import Callable
from typing import Any

def add_autoretry_behaviour(task: Any, **options: Any) -> Callable[..., Any]: ...
