from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("GCSBackend",)

class GCSBackend(KeyValueStoreBackend):
    @property
    def firestore_client(self) -> Any: ...
    def __init__(self, **kwargs: Any) -> None: ...
