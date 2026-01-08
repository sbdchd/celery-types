from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("S3Backend",)

class S3Backend(KeyValueStoreBackend):
    def __init__(self, **kwargs: Any) -> None: ...
