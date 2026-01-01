from typing import Any

from kombu.asynchronous.http.base import Headers as Headers
from kombu.asynchronous.http.base import Request as Request
from kombu.asynchronous.http.base import Response as Response

def get_client(hub: Any = ..., **kwargs: Any) -> Any: ...
