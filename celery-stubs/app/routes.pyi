from typing import Any

__all__ = ("MapRoute", "Router", "expand_router_string", "prepare")

from celery.app.base import Celery
from celery.app.task import Task

def expand_router_string(router: str) -> Any: ...
def prepare(routes: list[Any] | tuple[Any, ...] | None) -> list[Any]: ...

class MapRoute:
    def __init__(self, map: dict[str, Any]) -> None: ...
    def __call__(
        self, name: str, *args: Any, **kwargs: Any
    ) -> dict[str, Any] | None: ...

class Router:
    def __init__(
        self,
        routes: Any = ...,
        queues: Any = ...,
        create_missing: bool = ...,
        app: Celery | None = ...,
    ) -> None: ...
    def expand_destination(self, route: dict[str, Any]) -> dict[str, Any]: ...
    def lookup_route(
        self,
        name: str,
        args: tuple[Any, ...] | None = None,
        kwargs: dict[str, Any] | None = None,
        options: dict[str, Any] | None = None,
        task_type: type[Task[Any, Any]] | None = None,
    ) -> dict[str, Any] | None: ...
    def query_router(
        self,
        router: Any,
        task: str,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
        options: dict[str, Any],
        task_type: type[Task[Any, Any]] | None,
    ) -> dict[str, Any] | None: ...
    def route(
        self,
        options: dict[str, Any],
        name: str,
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        task_type: type[Task[Any, Any]] | None = None,
    ) -> dict[str, Any]: ...
