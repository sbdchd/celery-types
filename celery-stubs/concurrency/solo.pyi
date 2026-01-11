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
        **opts: Any,
    ) -> Any: ...
