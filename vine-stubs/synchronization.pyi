from collections.abc import Callable
from types import TracebackType
from typing import Any

from typing_extensions import override
from vine.abstract import Thenable
from vine.promises import promise

class barrier(Thenable):
    p: promise
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    ready: bool
    cancelled: bool
    finalized: bool

    def __init__(
        self,
        promises: list[promise] | None = ...,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        callback: Callable[..., Any] | None = ...,
        size: int | None = ...,
    ) -> None: ...
    @override
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def add(self, p: promise) -> promise: ...
    def add_noincr(self, p: promise) -> promise: ...
    @override
    def cancel(self) -> None: ...
    def finalize(self) -> None: ...
    @override
    def then(  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
        self,
        callback: Callable[..., Any],
        errback: Callable[..., Any] | None = ...,
    ) -> promise: ...
    @override
    def throw(
        self,
        exc: BaseException | None = ...,
        tb: TracebackType | None = ...,
        propagate: bool = ...,
    ) -> None: ...
    def throw1(self, exc: BaseException | None = ...) -> None: ...

__all__ = ["barrier"]
