from typing import Any, ClassVar

from celery.bootsteps import Step
from typing_extensions import override

__all__ = ("Connection",)

class Connection(Step):
    name: ClassVar[str]  # pyright: ignore[reportIncompatibleVariableOverride]

    def __init__(self, c: Any, **kwargs: Any) -> None: ...
    @override
    def info(self, c: Any) -> dict[str, Any]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def start(self, c: Any) -> None: ...
    def shutdown(self, c: Any) -> None: ...
