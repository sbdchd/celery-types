from collections.abc import Callable
from typing import Any

from celery.backends.base import KeyValueStoreBackend

E_NO_PATH_SET: str
E_PATH_INVALID: str
E_PATH_NON_CONFORMING_SCHEME: str
default_encoding: str

class FilesystemBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        open: Callable[..., Any] = ...,
        unlink: Callable[[str], None] = ...,
        sep: str = "/",
        encoding: str = "UTF-8",
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
