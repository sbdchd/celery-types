from collections.abc import Callable, Hashable, Sequence
from threading import Lock
from typing import Any, TypeAlias, TypeVar, overload
from weakref import ReferenceType

__all__ = ("Signal",)

_F = TypeVar("_F", bound=Callable[..., Any])

# Receiver return types vary, and weak references are invariant in their target.
_Receiver: TypeAlias = Callable[..., Any]
# ((receiver/dispatch key, sender key), strong callable or weak reference).
_ReceiverEntry: TypeAlias = tuple[
    tuple[Hashable, Hashable], _Receiver | ReferenceType[_Receiver]
]

class Signal:
    receivers: list[_ReceiverEntry]  # None at class level, always set on instances
    lock: Lock

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
        dispatch_uid: Hashable | None = ...,
        retry: bool = ...,
    ) -> _F: ...
    @overload
    def connect(
        self,
        *,
        sender: Any | None = ...,
        weak: bool = ...,
        dispatch_uid: Hashable | None = ...,
        retry: bool = ...,
    ) -> Callable[[_F], _F]: ...
    def disconnect(
        self,
        receiver: Callable[..., Any] | None = None,
        sender: Any | None = None,
        weak: bool | None = None,
        dispatch_uid: Hashable | None = None,
    ) -> bool: ...
    def has_listeners(self, sender: Any | None = None) -> bool: ...
    def send(
        self, sender: Any | None, **named: Any
    ) -> list[tuple[Callable[..., Any], Any]]: ...
    send_robust = send
