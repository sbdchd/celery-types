from collections.abc import Callable
from typing import Any, Generic, TypeVar, overload

__all__ = ("cached_property",)

_T = TypeVar("_T")
_S = TypeVar("_S")

class cached_property(Generic[_T]):
    fget: Callable[[Any], _T] | None
    fset: Callable[[Any, _T], None] | None
    fdel: Callable[[Any], None] | None
    attrname: str | None

    @overload
    def __init__(
        self,
        fget: Callable[[Any], _T],
        fset: Callable[[Any, _T], None] | None = ...,
        fdel: Callable[[Any], None] | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: cached_property[Any],
        fget: None = ...,
        fset: Callable[[Any, Any], None] | None = ...,
        fdel: Callable[[Any], None] | None = ...,
    ) -> None: ...
    @overload
    def __get__(
        self, instance: None, owner: type[Any] | None = ...
    ) -> cached_property[_T]: ...
    @overload
    def __get__(self, instance: _S, owner: type[_S] | None = ...) -> _T: ...
    def __set__(self, instance: Any, value: _T) -> None: ...
    def __delete__(self, instance: Any) -> None: ...
    def setter(self, fset: Callable[[Any, _T], None]) -> cached_property[_T]: ...
    def deleter(self, fdel: Callable[[Any], None]) -> cached_property[_T]: ...
