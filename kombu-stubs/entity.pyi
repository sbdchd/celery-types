from typing import Any

from kombu.abstract import MaybeChannelBound
from kombu.transport.base import StdChannel

class Exchange(MaybeChannelBound):
    def __init__(
        self,
        name: str = ...,
        type: str = ...,
        channel: StdChannel | None = ...,
        **kwargs: Any,
    ) -> None: ...

class Queue(MaybeChannelBound):
    routing_key: str
    exchange: Exchange
    name: str
    def __init__(
        self,
        name: str = ...,
        exchange: Exchange | str | None = ...,
        routing_key: str = ...,
        channel: StdChannel | None = ...,
        bindings: Any = ...,
        on_declared: Any = ...,
        **kwargs: Any,
    ) -> None: ...
