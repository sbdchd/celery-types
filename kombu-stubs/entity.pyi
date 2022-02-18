from typing import Any, Optional

from kombu.abstract import MaybeChannelBound
from kombu.transport.base import Channel

class Exchange(MaybeChannelBound):
    def __init__(
        self,
        name: str = ...,
        type: str = ...,
        channel: Optional[Channel] = ...,
        **kwargs: Any,
    ) -> None: ...

class Queue(MaybeChannelBound):
    routing_key: str
    exchange: Exchange
    def __init__(
        self,
        name: str = ...,
        exchange: Optional[Exchange] = ...,
        routing_key: str = ...,
        channel: Optional[Channel] = ...,
        bindings: Any = ...,
        on_declared: Any = ...,
        **kwargs: Any,
    ) -> None: ...
