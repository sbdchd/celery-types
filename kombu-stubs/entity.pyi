from kombu.abstract import MaybeChannelBound
from kombu.transport.base import Channel
from typing import Any, Optional

class Exchange(MaybeChannelBound):
    def __init__(
        self,
        name: str = "",
        type: str = "",
        channel: Optional[Channel] = None,
        **kwargs: Any,
    ) -> None: ...

class Queue(MaybeChannelBound):
    def __init__(
        self,
        name: str = "",
        exchange: Optional[Exchange] = None,
        routing_key: str = "",
        channel: Optional[Channel] = None,
        bindings: Any = None,
        on_declared: Any = None,
        **kwargs: Any,
    ) -> None: ...
