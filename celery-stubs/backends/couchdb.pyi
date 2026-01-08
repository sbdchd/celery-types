from typing import Any

from celery.backends.base import Backend

__all__ = ("CouchBackend",)

class CouchBackend(Backend):
    host: str
    port: int
    container: str
    username: str | None
    password: str | None
    scheme: str

    @property
    def connection(self) -> Any: ...
    def __init__(self, url: str | None = None, *args: Any, **kwargs: Any) -> None: ...
    def get(self, key: str) -> Any: ...
    def set(self, key: str, value: Any) -> None: ...
    def mget(self, keys: list[str]) -> list[Any]: ...
    def delete(self, key: str) -> None: ...
