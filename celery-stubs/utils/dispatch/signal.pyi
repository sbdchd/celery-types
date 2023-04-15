from collections.abc import Callable
from typing import Any, TypeVar, overload

_F = TypeVar("_F", bound=Callable[..., Any])

class Signal:
    @overload
    def connect(
        self,
        receiver: _F,
        sender: Any | None = ...,
        weak: bool = ...,
        dispatch_uid: str = ...,
        retry: bool = ...,
    ) -> _F: ...
    @overload
    def connect(
        self,
        *,
        sender: Any | None = ...,
        weak: bool = ...,
        dispatch_uid: str = ...,
        retry: bool = ...,
    ) -> Callable[[_F], _F]: ...
