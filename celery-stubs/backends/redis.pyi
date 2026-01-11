from collections.abc import Callable, Iterable
from types import ModuleType
from typing import Any

from celery.backends.asynchronous import BaseResultConsumer
from celery.backends.base import KeyValueStoreBackend
from kombu.utils.objects import cached_property
from typing_extensions import override

__all__ = ("RedisBackend", "SentinelBackend")

class RedisBackend(KeyValueStoreBackend):
    ResultConsumer: type[BaseResultConsumer]
    connection_class_ssl: type[Any]
    max_connections: int | None
    redis: Any  # redis module

    retry_policy: cached_property[dict[str, Any]]  # pyright: ignore[reportIncompatibleVariableOverride]

    @property
    def ConnectionPool(self) -> Any: ...
    @property
    def client(self) -> Any: ...
    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        db: int | None = None,
        password: str | None = None,
        max_connections: int | None = None,
        url: str | None = None,
        connection_pool: Any | None = None,
        **kwargs: Any,
    ) -> None: ...
    def ensure(
        self, fun: Callable[..., Any], args: tuple[Any, ...], **policy: Any
    ) -> Any: ...
    def on_connection_error(
        self, max_retries: int, exc: Exception, intervals: Iterable[float], retries: int
    ) -> None: ...
    @override
    def add_to_chord(self, group_id: str, result: Any) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    @override
    def on_chord_part_return(
        self,
        request: Any,
        state: str,
        result: Any,
        propagate: bool | None = None,
        **kwargs: Any,
    ) -> None: ...

class SentinelBackend(RedisBackend):
    sentinel: ModuleType  # redis.sentinel module
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
