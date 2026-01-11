from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("ConsulBackend",)

class ConsulBackend(KeyValueStoreBackend):
    consistency: str
    path: str | None
    consul: Any

    @property
    def client(self) -> Any: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
