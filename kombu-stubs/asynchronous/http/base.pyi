from collections.abc import Callable, Mapping
from typing import Any

class Headers(dict[str, str]):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Request:
    url: str
    method: str
    headers: Headers
    body: bytes | None
    connect_timeout: float | None
    request_timeout: float | None
    on_ready: Callable[[Response], None] | None

    def __init__(
        self,
        url: str,
        method: str = ...,
        on_ready: Callable[[Response], None] | None = ...,
        on_timeout: Callable[[], None] | None = ...,
        on_stream: Callable[[bytes], None] | None = ...,
        headers: Mapping[str, str] | None = ...,
        body: bytes | str | None = ...,
        connect_timeout: float | None = ...,
        request_timeout: float | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def then(self, callback: Callable[[Response], None]) -> Request: ...

class Response:
    request: Request
    code: int
    headers: Headers
    body: bytes | None
    effective_url: str
    error: Exception | None

    def __init__(
        self,
        request: Request,
        code: int,
        headers: Headers | None = ...,
        body: bytes | None = ...,
        effective_url: str | None = ...,
        error: Exception | None = ...,
    ) -> None: ...
    def raise_for_error(self) -> None: ...

class BaseClient:
    hub: Any

    def __init__(self, hub: Any = ..., **kwargs: Any) -> None: ...
    def add_request(self, request: Request) -> Request: ...
    def close(self) -> None: ...
