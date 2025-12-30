from collections import UserDict
from collections.abc import Callable, Hashable, Mapping
from typing import Any

__all__ = (
    "LRUCache",
    "dictfilter",
    "is_list",
    "lazy",
    "maybe_evaluate",
    "maybe_list",
    "memoize",
)

KEYWORD_MARK = object()

class ChannelPromise:
    def __init__(self, contract: Any) -> None: ...
    def __call__(self) -> Any: ...

class LRUCache(UserDict[str, Any]): ...

def memoize(
    maxsize: int | None = None,
    keyfun: Callable[..., Any] | None = None,
    Cache: type[Mapping[Hashable, Any]] = ...,
) -> Callable[..., Callable[..., Any]]: ...

class lazy:
    def __init__(self, fun: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...

def maybe_evaluate(value: Any) -> Any: ...
def is_list(
    obj: Any,
    scalars: tuple[type[Any], ...] = ...,
    iters: tuple[type[Any], ...] = ...,
) -> bool: ...
def maybe_list(obj: Any, scalars: tuple[type[Any], ...] = ...) -> list[Any]: ...
def dictfilter(
    d: dict[Hashable, Any] | None = None, **kw: Any
) -> dict[Hashable, Any]: ...

promise = lazy
maybe_promise = maybe_evaluate
