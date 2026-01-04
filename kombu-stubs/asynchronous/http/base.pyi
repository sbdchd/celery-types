from collections.abc import Callable, Mapping
from io import BytesIO
from types import TracebackType
from typing import Any

from typing_extensions import Self

__all__ = ("Headers", "Request", "Response")

class Headers(dict[str, str]):
    complete: bool
    _prev_key: str | None

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Request:
    url: str
    method: str
    headers: Headers
    body: bytes | str | None
    connect_timeout: float
    request_timeout: float
    on_ready: Any  # promise
    on_timeout: Any | None
    on_stream: Any | None
    on_prepare: Any | None
    on_header: Any | None
    auth_username: str | None
    auth_password: str | None
    auth_mode: str | None
    user_agent: str | None
    network_interface: str | None
    use_gzip: bool
    validate_cert: bool
    ca_certs: str | None
    client_key: str | None
    client_cert: str | None
    proxy_host: str | None
    proxy_port: int | None
    proxy_username: str | None
    proxy_password: str | None
    follow_redirects: bool
    max_redirects: int

    def __init__(
        self,
        url: str,
        method: str = ...,
        on_ready: Callable[[Response], None] | None = ...,
        on_timeout: Callable[[], None] | None = ...,
        on_stream: Callable[[bytes], None] | None = ...,
        on_prepare: Callable[[Request], None] | None = ...,
        on_header: Callable[[Headers], None] | None = ...,
        headers: Mapping[str, str] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def then(
        self,
        callback: Callable[[Response], None],
        errback: Callable[[Exception], None] | None = ...,
    ) -> None: ...

class Response:
    request: Request
    code: int
    headers: Headers
    buffer: BytesIO | None
    effective_url: str
    error: Exception | None
    status: str
    _body: bytes | None

    def __init__(
        self,
        request: Request,
        code: int,
        headers: Headers | None = ...,
        buffer: BytesIO | None = ...,
        effective_url: str | None = ...,
        error: Exception | None = ...,
        status: str | None = ...,
    ) -> None: ...
    def raise_for_error(self) -> None: ...
    @property
    def body(self) -> bytes | None: ...
    @property
    def status_code(self) -> int: ...
    @property
    def content(self) -> bytes | None: ...

_Headers = Headers
_Request = Request
_Response = Response

class BaseClient:
    Headers: type[_Headers]
    Request: type[_Request]
    Response: type[_Response]
    hub: Any
    _header_parser: Any

    def __init__(self, hub: Any, **kwargs: Any) -> None: ...
    def perform(self, request: _Request | str, **kwargs: Any) -> None: ...
    def add_request(self, request: _Request) -> _Request: ...
    def close(self) -> None: ...
    def on_header(self, headers: _Headers, line: bytes | str) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
