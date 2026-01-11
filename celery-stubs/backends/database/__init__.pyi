from typing import Any

from celery.backends.base import Backend
from celery.backends.database.models import Task, TaskSet

__all__ = ("DatabaseBackend",)

class DatabaseBackend(Backend):
    task_cls: type[Task]
    taskset_cls: type[TaskSet]

    @property
    def extended_result(self) -> bool: ...
    def ResultSession(self, session_manager: Any | None = None) -> Any: ...
    def __init__(
        self,
        dburi: str | None = None,
        engine_options: dict[str, Any] | None = None,
        url: str | None = None,
        **kwargs: Any,
    ) -> None: ...
