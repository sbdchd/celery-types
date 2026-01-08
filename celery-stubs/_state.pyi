from collections.abc import Callable
from typing import Any

from celery.app.base import Celery
from celery.app.task import Task
from celery.local import Proxy

__all__ = (
    "connect_on_app_finalize",
    "current_app",
    "current_task",
    "get_current_app",
    "get_current_task",
    "get_current_worker_task",
    "set_default_app",
)

current_app: Proxy[Celery]
current_task: Proxy[Task[Any, Any]]

def get_current_task() -> Task[Any, Any]: ...
def get_current_app() -> Celery: ...
def get_current_worker_task() -> Task[Any, Any] | None: ...
def set_default_app(app: Celery) -> None: ...
def connect_on_app_finalize(
    callback: Callable[[Celery], Any],
) -> Callable[[Celery], Any]: ...
