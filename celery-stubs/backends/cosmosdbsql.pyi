from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("CosmosDBSQLBackend",)

class CosmosDBSQLBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        database_name: str | None = None,
        collection_name: str | None = None,
        consistency_level: str | None = None,
        max_retry_attempts: int | None = None,
        max_retry_wait_time: int | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
