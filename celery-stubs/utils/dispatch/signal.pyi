from typing import Any, Callable, Optional, TypeVar, overload

_F = TypeVar("_F", bound=Callable[..., Any])

class Signal:
    @overload
    def connect(
        self,
        receiver: _F,
        sender: Optional[Any] = ...,
        weak: bool = ...,
        dispatch_uid: str = ...,
        retry: bool = ...,
    ) -> _F: ...
    @overload
    def connect(
        self,
        *,
        sender: Optional[Any] = ...,
        weak: bool = ...,
        dispatch_uid: str = ...,
        retry: bool = ...,
    ) -> Callable[[_F], _F]: ...
