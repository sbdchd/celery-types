from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("DynamoDBBackend",)

class DynamoDBBackend(KeyValueStoreBackend):
    aws_region: str | None
    table_name: str
    endpoint_url: str | None
    read_capacity_units: int
    write_capacity_units: int
    time_to_live_seconds: int | None

    @property
    def client(self) -> Any: ...
    def __init__(
        self,
        url: str | None = None,
        table_name: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
