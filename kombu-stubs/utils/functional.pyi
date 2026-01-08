from collections import UserDict
from collections.abc import Callable, Hashable, Iterable, Iterator
from typing import Any, TypeVar

from typing_extensions import override

__all__ = (
    "LRUCache",
    "dictfilter",
    "is_list",
    "lazy",
    "maybe_evaluate",
    "maybe_list",
    "memoize",
    "retry_over_time",
)

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

KEYWORD_MARK: object

class ChannelPromise:
    def __init__(self, contract: Any) -> None: ...
    def __call__(self) -> Any: ...

class LRUCache(UserDict[_KT, _VT]):
    limit: int | None

    def __init__(self, limit: int | None = ...) -> None: ...
    def incr(self, key: _KT, delta: int = ...) -> int: ...
    def iteritems(self) -> Iterator[tuple[_KT, _VT]]: ...
    def iterkeys(self) -> Iterator[_KT]: ...
    def itervalues(self) -> Iterator[_VT]: ...
    @override
    def popitem(self, last: bool = ...) -> tuple[_KT, _VT]: ...
    def _iterate_keys(self) -> Iterator[_KT]: ...
    def _iterate_items(self) -> Iterator[tuple[_KT, _VT]]: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def __setstate__(self, state: dict[str, Any]) -> None: ...

def memoize(
    maxsize: int | None = ...,
    keyfun: Callable[..., Any] | None = ...,
    Cache: type[LRUCache[Any, Any] | dict[Any, Any]] = ...,
) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...

class lazy:
    def __init__(self, fun: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    def __call__(self) -> Any: ...
    def __deepcopy__(self, memo: dict[int, Any]) -> lazy: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> tuple[Any, ...]: ...
    def evaluate(self) -> Any: ...

def maybe_evaluate(value: Any) -> Any: ...
def is_list(
    obj: Any,
    scalars: tuple[type[Any], ...] = ...,
    iters: tuple[type[Any], ...] = ...,
) -> bool: ...
def maybe_list(obj: Any, scalars: tuple[type[Any], ...] = ...) -> list[Any]: ...
def dictfilter(
    d: dict[Hashable, Any] | None = ..., **kw: Any
) -> dict[Hashable, Any]: ...
def retry_over_time(
    fun: Callable[..., _T],
    catch: type[BaseException] | tuple[type[BaseException], ...],
    args: Iterable[Any] | None = ...,
    kwargs: dict[str, Any] | None = ...,
    errback: Callable[[BaseException, float], None] | None = ...,
    max_retries: int | None = ...,
    interval_start: float = ...,
    interval_step: float = ...,
    interval_max: float = ...,
    callback: Callable[[], None] | None = ...,
    timeout: float | None = ...,
) -> _T: ...
def reprkwargs(kwargs: dict[str, Any], sep: str = ..., fmt: str = ...) -> str: ...
def reprcall(
    name: str,
    args: tuple[Any, ...] = ...,
    kwargs: dict[str, Any] | None = ...,
    sep: str = ...,
) -> str: ...
def accepts_argument(func: Callable[..., Any], argument_name: str) -> bool: ...
def fxrange(
    start: float = ...,
    stop: float | None = ...,
    step: float = ...,
    repeatlast: bool = ...,
) -> Iterator[float]: ...
def fxrangemax(
    start: float = ...,
    stop: float | None = ...,
    step: float = ...,
    max: float | None = ...,
) -> Iterator[float]: ...
def shufflecycle(it: Iterable[_T]) -> Iterator[_T]: ...

promise = lazy
maybe_promise = maybe_evaluate
