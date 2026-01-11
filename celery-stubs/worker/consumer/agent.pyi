from typing import Any, ClassVar

from celery.bootsteps import Step
from typing_extensions import override

__all__ = ("Agent",)

class Agent(Step):
    name: ClassVar[str]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __init__(self, c: Any, **kwargs: Any) -> None: ...
    @override
    def create(self, c: Any) -> Any: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
