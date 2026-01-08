from collections.abc import Callable
from types import TracebackType
from typing import Any

from typing_extensions import override
from vine.abstract import Thenable

class promise(Thenable):
    args: tuple[Any, ...] | None
    kwargs: dict[str, Any] | None
    fun: Callable[..., Any] | None
    on_error: Callable[..., Any] | None
    weak: bool

    @property
    def listeners(self) -> list[Callable[..., Any]]: ...
    ignore_result: bool
    cancelled: bool
    ready: bool
    failed: bool
    value: Any
    reason: BaseException | None

    def __init__(
        self,
        fun: Callable[..., Any] | None = ...,
        args: tuple[Any, ...] | None = ...,
        kwargs: dict[str, Any] | None = ...,
        callback: Callable[..., Any] | None = ...,
        on_error: Callable[..., Any] | None = ...,
        weak: bool = ...,
        ignore_result: bool = ...,
    ) -> None: ...
    @override
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    @override
    def then(  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
        self,
        callback: Callable[..., Any],
        on_error: Callable[..., Any] | None = ...,
    ) -> promise: ...
    @override
    def throw(
        self,
        exc: BaseException | None = ...,
        tb: TracebackType | None = ...,
        propagate: bool = ...,
    ) -> None: ...
    def throw1(self, exc: BaseException | None = ...) -> None: ...
    @override
    def cancel(self) -> None: ...

__all__ = ["promise"]
