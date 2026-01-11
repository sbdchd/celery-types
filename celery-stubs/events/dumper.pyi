from typing import Any, TextIO

__all__ = ("Dumper", "evdump")

class Dumper:
    out: TextIO

    def __init__(self, out: TextIO = ...) -> None: ...
    def say(self, msg: str) -> None: ...
    def format_task_event(
        self,
        hostname: str,
        timestamp: float,
        type: str,
        task: str,
        event: dict[str, Any],
    ) -> str: ...
    def on_event(self, ev: dict[str, Any]) -> None: ...

def evdump(app: Any | None = None, out: TextIO = ...) -> None: ...
