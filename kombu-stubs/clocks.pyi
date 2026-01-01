from threading import Lock
from typing import Any, NamedTuple

__all__ = ("LamportClock", "timetuple")

class timetuple(NamedTuple):
    clock: int
    timestamp: float
    id: str
    obj: Any

class LamportClock:
    counter: int
    mutex: Lock

    def __init__(self, initial_value: int = ..., Lock: type[Lock] = ...) -> None: ...
    def adjust(self, other: int) -> int: ...
    def forward(self) -> int: ...
    def sort_heap(self, h: list[timetuple]) -> list[timetuple]: ...
    def __repr__(self) -> str: ...
