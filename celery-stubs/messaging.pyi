from typing import Any

from kombu import Connection
from kombu.transport.virtual import Channel

def establish_connection(
    hostname: str | None = ...,
    userid: str | None = ...,
    password: str | None = ...,
    virtual_host: str | None = ...,
    port: int | None = ...,
    ssl: bool | dict[str, Any] | None = ...,
    connect_timeout: float | None = ...,
    transport: str | None = ...,
    transport_options: dict[str, Any] | None = ...,
    heartbeat: float | None = ...,
    login_method: str | None = ...,
    failover_strategy: str | None = ...,
    **kwargs: Any,
) -> Connection: ...
def get_consumer_set(
    channel: Channel,
    queues: Any | None = ...,
    accept: list[str] | None = ...,
    **kw: Any,
) -> Any: ...
def TaskConsumer(
    channel: Channel,
    queues: Any | None = ...,
    accept: list[str] | None = ...,
    **kw: Any,
) -> Any: ...

__all__ = ["TaskConsumer", "establish_connection", "get_consumer_set"]
