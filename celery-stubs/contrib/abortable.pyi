from typing import Any, Generic, ParamSpec, TypeVar

from celery import Task
from celery.result import AsyncResult
from typing_extensions import override

__all__ = ("AbortableAsyncResult", "AbortableTask")

ABORTED: str = "ABORTED"

_R_co = TypeVar("_R_co", covariant=True)
_P = ParamSpec("_P")

class AbortableAsyncResult(AsyncResult[_R_co], Generic[_R_co]):
    def is_aborted(self) -> bool: ...
    def abort(self) -> Any: ...

class AbortableTask(Task[_P, _R_co], Generic[_P, _R_co]):
    abstract: bool = True

    @override
    def AsyncResult(self, task_id: str) -> AbortableAsyncResult[_R_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def is_aborted(self, *, task_id: str, **kwargs: Any) -> bool: ...
