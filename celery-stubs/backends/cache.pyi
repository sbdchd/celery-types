from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("CacheBackend",)

class CacheBackend(KeyValueStoreBackend):
    servers: list[str] | None
    supports_native_join: bool

    @property
    def client(self) -> Any: ...
    def __init__(
        self,
        app: Any,
        expires: float | None = None,
        backend: str | None = None,
        options: dict[str, Any] | None = None,
        url: str | None = None,
        **kwargs: Any,
    ) -> None: ...
