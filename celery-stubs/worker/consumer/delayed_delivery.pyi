from typing import Any, ClassVar

from celery.bootsteps import Step
from typing_extensions import override

__all__ = ("DelayedDelivery",)

class DelayedDelivery(Step):
    name: ClassVar[str]  # pyright: ignore[reportIncompatibleVariableOverride]

    @override
    def include_if(self, c: Any) -> bool: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    def start(self, c: Any) -> None: ...
