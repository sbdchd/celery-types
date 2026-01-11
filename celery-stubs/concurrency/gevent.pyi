from collections.abc import Callable
from typing import Any

from celery.concurrency.base import BasePool
from typing_extensions import override

__all__ = ("TaskPool",)

class TaskPool(BasePool):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def on_start(self) -> None: ...
    @override
    def on_stop(self) -> None: ...
    @override
    def on_apply(
        self,
        target: Any,
        args: tuple[Any, ...] | None = None,
        kwargs: dict[str, Any] | None = None,
        callback: Any = None,
        accept_callback: Any = None,
        timeout: float | None = None,
        timeout_callback: Callable[..., Any] | None = None,
        apply_target: Callable[..., Any] = ...,
        **_: Any,
    ) -> Any: ...
    def grow(self, n: int = 1) -> None: ...
    def shrink(self, n: int = 1) -> None: ...
