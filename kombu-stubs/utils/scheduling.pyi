from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any, Generic, TypeVar, overload

__all__ = ("FairCycle", "priority_cycle", "round_robin_cycle", "sorted_cycle")

_T = TypeVar("_T")

class round_robin_cycle(Generic[_T]):
    items: list[_T] | None
    @overload
    def __init__(self, it: Iterable[_T]) -> None: ...
    @overload
    def __init__(self: "round_robin_cycle[Any]", it: None = ...) -> None: ...
    def update(self, it: Iterable[_T]) -> None: ...
    def consume(self, n: int) -> Iterator[_T]: ...
    def rotate(self, last_used: _T) -> None: ...

class priority_cycle(round_robin_cycle[_T]): ...
class sorted_cycle(round_robin_cycle[_T]): ...

class FairCycle:
    fun: Callable[..., Any]
    resources: Sequence[Any]
    predicate: type[BaseException]
    pos: int

    def __init__(
        self,
        fun: Callable[..., Any],
        resources: Sequence[Any],
        predicate: type[BaseException] = ...,
    ) -> None: ...
    def get(self, callback: Callable[..., _T], **kwargs: Any) -> _T: ...
    def close(self) -> None: ...
