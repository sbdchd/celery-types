from typing import Any, Callable, Optional, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

class Signal:
    def connect(
        self,
        receiver: Callable[..., Any] = ...,
        sender: Optional[Any] = ...,
        weak: bool = ...,
        dispatch_uid: str = ...,
        retry: bool = ...,
    ) -> Callable[[_F], _F]: ...
