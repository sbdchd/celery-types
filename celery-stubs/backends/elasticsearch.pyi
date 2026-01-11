from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("ElasticsearchBackend",)

class ElasticsearchBackend(KeyValueStoreBackend):
    doc_type: str | None
    es_max_retries: int
    es_retry_on_timeout: bool
    es_timeout: int
    host: str
    port: int
    index: str
    scheme: str
    username: str | None
    password: str | None

    @property
    def server(self) -> str: ...
    def __init__(self, url: str | None = None, *args: Any, **kwargs: Any) -> None: ...
