from typing import Any

from kombu.asynchronous.http.base import BaseClient
from kombu.asynchronous.hub import Hub
from typing_extensions import override

__all__ = ("CurlClient",)

class CurlClient(BaseClient):
    Curl: type[Any] | None
    max_clients: int
    _multi: Any
    _curls: list[Any]
    _free_list: list[Any]
    _pending: Any
    _fds: dict[int, int]
    _socket_action: Any
    _timeout_check_tref: Any

    def __init__(self, hub: Hub | None = ..., max_clients: int = ...) -> None: ...
    @override
    def close(self) -> None: ...
    @override
    def add_request(self, request: Any) -> Any: ...
    def on_readable(self, fd: int, _pycurl: Any = ...) -> Any: ...
    def on_writable(self, fd: int, _pycurl: Any = ...) -> Any: ...
