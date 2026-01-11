from typing import Any, ClassVar

from celery.bootsteps import Step
from typing_extensions import override

__all__ = ("Control",)

class Control(Step):
    name: ClassVar[str]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __init__(self, c: Any, **kwargs: Any) -> None: ...
    @override
    def create(self, parent: Any) -> Any: ...
    def start(self, parent: Any) -> None: ...
    def stop(self, parent: Any) -> None: ...
    @override
    def include_if(self, c: Any) -> bool: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    @override
    def info(self, obj: Any) -> dict[str, Any]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
