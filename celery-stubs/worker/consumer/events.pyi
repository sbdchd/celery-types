from typing import Any, ClassVar

from celery.bootsteps import Step
from typing_extensions import override

__all__ = ("Events",)

class Events(Step):
    name: ClassVar[str]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __init__(
        self,
        c: Any,
        task_events: bool = True,
        without_heartbeat: bool = False,
        without_gossip: bool = False,
        **kwargs: Any,
    ) -> None: ...
    @override
    def create(self, parent: Any) -> Any: ...
    def start(self, c: Any) -> None: ...
    def stop(self, c: Any) -> None: ...
    def shutdown(self, c: Any) -> None: ...
    @override
    def include_if(self, parent: Any) -> bool: ...
    @override
    def info(self, obj: Any) -> dict[str, Any]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
