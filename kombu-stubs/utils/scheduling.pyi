from collections.abc import Callable, Sequence
from typing import Any, TypeVar

_T = TypeVar("_T")

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
    def get(
        self, callback: Callable[..., _T], **kwargs: Any
    ) -> _T: ...
    def close(self) -> None: ...
