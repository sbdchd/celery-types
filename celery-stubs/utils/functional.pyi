from collections.abc import Callable, Container, Generator, Iterable
from typing import Any, TypeAlias, TypeGuard, TypeVar

from kombu.utils.functional import (
    LRUCache,
    dictfilter,
    is_list,
    lazy,
    maybe_evaluate,
    maybe_list,
    memoize,
)
from typing_extensions import Self

__all__ = (
    "LRUCache",
    "chunks",
    "dictfilter",
    "first",
    "firstmethod",
    "fun_accepts_kwargs",
    "head_from_fun",
    "is_list",
    "lazy",
    "mattrgetter",
    "maybe",
    "maybe_evaluate",
    "maybe_list",
    "memoize",
    "mlazy",
    "noop",
    "padlist",
    "regen",
    "uniq",
)

class DummyContext:
    def __enter__(self) -> Self: ...
    def __exit__(self, *exc_info: object) -> None: ...

class mlazy:
    evaluated: bool
    _value: Any

    def evaluate(self) -> Any: ...

def noop(*args: object, **kwargs: object) -> None: ...

_T = TypeVar("_T")

def pass1(arg: _T, *args: object, **kwargs: object) -> _T: ...
def evaluate_promises(it: Iterable[Any]) -> Generator[Any, None, None]: ...
def first(predicate: Callable[[_T], bool] | None, it: Iterable[_T]) -> _T | None: ...
def firstmethod(
    method: Callable[..., Any], on_call: Callable[..., Any] | None = None
) -> Callable[..., Any]: ...
def chunks(it: Iterable[_T], n: int) -> Generator[list[_T], None, None]: ...
def padlist(
    container: Container[_T], size: int, default: _T | None = None
) -> list[_T]: ...
def mattrgetter(*attrs: str) -> Callable[[object], dict[str, Any]]: ...
def uniq(it: Iterable[_T]) -> Generator[_T, None, None]: ...
def lookahead(it: Iterable[_T]) -> Iterable[tuple[_T, _T | None]]: ...
def regen(it: Iterable[_T]) -> list[_T] | tuple[_T]: ...

_FuncType: TypeAlias = Callable[..., Any]

def head_from_fun(fun: _FuncType, bound: bool = False) -> _FuncType: ...
def arity_greater(fun: _FuncType, n: int) -> bool: ...
def fun_takes_argument(
    name: str, fun: _FuncType, position: int | None = None
) -> bool: ...
def fun_accepts_kwargs(fun: _FuncType) -> bool: ...
def maybe(typ: Callable[..., _T], val: object | None) -> _T | None: ...
def seq_concat_item(seq: list[_T] | tuple[_T], item: _T) -> list[_T] | tuple[_T]: ...
def seq_concat_seq(
    a: list[Any] | tuple[Any], b: list[Any] | tuple[Any]
) -> list[Any] | tuple[Any]: ...
def is_numeric_value(value: Any) -> TypeGuard[bool]: ...
