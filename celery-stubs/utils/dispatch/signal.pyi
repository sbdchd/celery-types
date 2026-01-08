from collections.abc import Callable, Sequence
from typing import Any, TypeVar, overload

__all__ = ("Signal",)

_F = TypeVar("_F", bound=Callable[..., Any])

class Signal:
    receivers: list[tuple[Any, Any]] | None

    def __init__(
        self,
        providing_args: Sequence[str] | None = None,
        use_caching: bool = False,
        name: str | None = None,
    ) -> None: ...
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
    def disconnect(
        self,
        receiver: Callable[..., Any] | None = None,
        sender: Any | None = None,
        weak: bool | None = None,
        dispatch_uid: str | None = None,
    ) -> bool: ...
    def has_listeners(self, sender: Any | None = None) -> bool: ...
    def send(
        self, sender: Any | None, **named: Any
    ) -> list[tuple[Callable[..., Any], Any]]: ...
    send_robust = send
