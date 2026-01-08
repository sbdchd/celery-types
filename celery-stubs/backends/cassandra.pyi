from typing import Any

from celery.backends.base import Backend

__all__ = ("CassandraBackend",)

class CassandraBackend(Backend):
    servers: list[str] | None
    bundle_path: str | None

    def __init__(
        self,
        servers: list[str] | None = None,
        keyspace: str | None = None,
        table: str | None = None,
        entry_ttl: int | None = None,
        port: int | None = None,
        bundle_path: str | None = None,
        **kwargs: Any,
    ) -> None: ...
