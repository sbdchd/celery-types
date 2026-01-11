from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("CouchbaseBackend",)

class CouchbaseBackend(KeyValueStoreBackend):
    bucket: str
    host: str
    port: int
    username: str | None
    password: str | None
    quiet: bool
    timeout: float
    key_t: type[str]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]

    @property
    def connection(self) -> Any: ...
    def __init__(self, url: str | None = None, *args: Any, **kwargs: Any) -> None: ...
