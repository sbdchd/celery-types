from typing import Any, Callable, Dict, List, Optional

from kombu.transport.base import Transport

class Connection:
    def __init__(
        self,
        hostname: str = ...,
        userid: Optional[str] = ...,
        password: Optional[str] = ...,
        virtual_host: Optional[str] = ...,
        port: Optional[int] = ...,
        insist: bool = ...,
        ssl: bool = ...,
        transport: Optional[Transport] = ...,
        connect_timeout: float = ...,
        transport_options: Optional[Dict[str, Any]] = ...,
        login_method: Optional[str] = ...,
        uri_prefix: Optional[str] = ...,
        heartbeat: float = ...,
        failover_strategy: str = ...,
        alternates: Optional[List[Any]] = ...,
    ) -> None: ...
    def ensure_connection(
        self,
        errback: Optional[Callable[[Exception, float], None]] = ...,
        max_retries: int = ...,
        interval_start: int = ...,
        interval_step: int = ...,
        interval_max: int = ...,
        callback: Optional[Callable[[], None]] = ...,
        reraise_as_library_errors: bool = ...,
        timeout: Optional[int] = ...,
    ) -> Connection: ...
