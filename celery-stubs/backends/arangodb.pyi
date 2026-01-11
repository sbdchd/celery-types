from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("ArangoDbBackend",)

class ArangoDbBackend(KeyValueStoreBackend):
    host: str
    port: str
    database: str
    collection: str
    http_protocol: str
    username: str | None
    password: str | None
    verify: bool
    key_t: type[str]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]

    @property
    def connection(self) -> Any: ...
    @property
    def db(self) -> Any: ...
    @property
    def expires_delta(self) -> float: ...
    def __init__(self, url: str | None = None, *args: Any, **kwargs: Any) -> None: ...
