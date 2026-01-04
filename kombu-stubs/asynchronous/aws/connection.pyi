from email.mime.message import MIMEMessage
from typing import Any

from kombu.asynchronous.http.base import Request as _Request
from vine import promise

__all__ = ("AsyncConnection", "AsyncHTTPSConnection")

def message_from_headers(hdr: list[tuple[str, str]]) -> Any: ...

class AsyncHTTPResponse:
    response: Any
    _msg: MIMEMessage | None
    version: int

    def __init__(self, response: Any) -> None: ...
    def read(self, *args: Any, **kwargs: Any) -> bytes: ...
    def getheader(self, name: str, default: str | None = ...) -> str | None: ...
    def getheaders(self) -> list[tuple[str, str]]: ...
    @property
    def msg(self) -> MIMEMessage: ...
    @property
    def status(self) -> int: ...
    @property
    def reason(self) -> str: ...

_AsyncHTTPResponse = AsyncHTTPResponse

class AsyncHTTPSConnection:
    Request: type[_Request]
    Response: type[_AsyncHTTPResponse]

    method: str
    path: str
    body: bytes | None
    default_ports: dict[str, int]
    headers: list[tuple[str, str]]
    timeout: float
    strict: Any
    http_client: Any

    def __init__(
        self, strict: Any = ..., timeout: float = ..., http_client: Any = ...
    ) -> None: ...
    def request(
        self, method: str, path: str, body: Any = ..., headers: Any = ...
    ) -> None: ...
    def getrequest(self) -> _Request: ...
    def getresponse(self, callback: Any = ...) -> Any: ...
    def set_debuglevel(self, level: int) -> None: ...
    def connect(self) -> None: ...
    def close(self) -> None: ...
    def putrequest(self, method: str, path: str) -> None: ...
    def putheader(self, header: str, value: str) -> None: ...
    def endheaders(self) -> None: ...
    def send(self, data: bytes) -> None: ...

class AsyncConnection:
    sqs_connection: Any
    _httpclient: Any

    def __init__(
        self, sqs_connection: Any, http_client: Any = ..., **kwargs: Any
    ) -> None: ...
    def get_http_connection(self) -> AsyncHTTPSConnection: ...

class AsyncAWSQueryConnection(AsyncConnection):
    STATUS_CODE_OK: int
    STATUS_CODE_REQUEST_TIMEOUT: int
    STATUS_CODE_NETWORK_CONNECT_TIMEOUT_ERROR: int
    STATUS_CODE_INTERNAL_ERROR: int
    STATUS_CODE_BAD_GATEWAY: int
    STATUS_CODE_SERVICE_UNAVAILABLE_ERROR: int
    STATUS_CODE_GATEWAY_TIMEOUT: int
    STATUS_CODES_SERVER_ERRORS: tuple[int, ...]
    STATUS_CODES_TIMEOUT: tuple[int, ...]

    def __init__(
        self,
        sqs_connection: Any,
        http_client: Any = ...,
        http_client_params: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def make_request(
        self,
        operation: str,
        params_: dict[str, Any],
        path: str,
        verb: str,
        callback: Any = ...,
        protocol_params: dict[str, Any] | None = ...,
    ) -> promise: ...
    def get_list(
        self,
        operation: str,
        params: dict[str, Any],
        markers: Any,
        path: str = ...,
        parent: Any = ...,
        verb: str = ...,
        callback: Any = ...,
        protocol_params: dict[str, Any] | None = ...,
    ) -> promise: ...
    def get_object(
        self,
        operation: str,
        params: dict[str, Any],
        path: str = ...,
        parent: Any = ...,
        verb: str = ...,
        callback: Any = ...,
        protocol_params: dict[str, Any] | None = ...,
    ) -> promise: ...
    def get_status(
        self,
        operation: str,
        params: dict[str, Any],
        path: str = ...,
        parent: Any = ...,
        verb: str = ...,
        callback: Any = ...,
        protocol_params: dict[str, Any] | None = ...,
    ) -> promise: ...
