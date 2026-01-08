from typing import Any

from celery.backends.base import Backend
from typing_extensions import override

__all__ = ("MongoBackend",)

class MongoBackend(Backend):
    host: str
    port: int
    database_name: str
    taskmeta_collection: str
    groupmeta_collection: str
    options: dict[str, Any] | None
    mongo_host: str | None
    max_pool_size: int
    user: str | None
    password: str | None

    @property
    def collection(self) -> Any: ...
    @property
    def database(self) -> Any: ...
    @property
    def group_collection(self) -> Any: ...
    @property
    def expires_delta(self) -> float: ...
    def __init__(self, app: Any = None, **kwargs: Any) -> None: ...
    @override
    def decode(self, data: Any) -> Any: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
