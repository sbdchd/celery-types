from typing import Any

__all__ = ("Heart",)

class Heart:
    def __init__(
        self,
        timer: Any,
        eventer: Any,
        interval: float | None = None,
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
