from collections.abc import Callable
from typing import Any

from kombu.transport.base import Channel, Transport

class Connection:
    def __init__(
        self,
        hostname: str = ...,
        userid: str | None = ...,
        password: str | None = ...,
        virtual_host: str | None = ...,
        port: int | None = ...,
        insist: bool = ...,
        ssl: bool = ...,
        transport: Transport | None = ...,
        connect_timeout: float = ...,
        transport_options: dict[str, Any] | None = ...,
        login_method: str | None = ...,
        uri_prefix: str | None = ...,
        heartbeat: float = ...,
        failover_strategy: str = ...,
        alternates: list[Any] | None = ...,
    ) -> None: ...
    def ensure_connection(
        self,
        errback: Callable[[Exception, float], None] | None = ...,
        max_retries: int = ...,
        interval_start: int = ...,
        interval_step: int = ...,
        interval_max: int = ...,
        callback: Callable[[], None] | None = ...,
        reraise_as_library_errors: bool = ...,
        timeout: int | None = ...,
    ) -> Connection: ...
    def _ensure_connection(
        self,
        errback: Callable[[Exception, float], None] | None = ...,
        max_retries: int = ...,
        interval_start: int = ...,
        interval_step: int = ...,
        interval_max: int = ...,
        callback: Callable[[], None] | None = ...,
        reraise_as_library_errors: bool = ...,
        timeout: int | None = ...,
    ) -> Connection: ...
    def connect(self) -> Connection: ...
    def channel(self) -> Channel: ...
    def release(self) -> None: ...
    def __enter__(self) -> Connection: ...
    def __exit__(self, *args: Any) -> None: ...
    close = release
