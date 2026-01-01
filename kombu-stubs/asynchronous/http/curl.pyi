from typing import Any

from kombu.asynchronous.http.base import BaseClient

class CurlClient(BaseClient):
    def __init__(self, hub: Any = ..., **kwargs: Any) -> None: ...
