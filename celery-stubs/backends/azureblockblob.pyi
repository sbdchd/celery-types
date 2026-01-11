from typing import Any

from celery.backends.base import KeyValueStoreBackend

__all__ = ("AzureBlockBlobBackend",)

class AzureBlockBlobBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        container_name: str | None = None,
        connection_string: str | None = None,
        **kwargs: Any,
    ) -> None: ...
