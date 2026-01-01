from collections.abc import Iterable
from typing import Any

class ExchangeType:
    type: str

    def __init__(self, channel: Any) -> None: ...
    def lookup(
        self,
        table: list[tuple[str, str, str]],
        exchange: str,
        routing_key: str,
        default: str | None,
    ) -> Iterable[str]: ...
    def prepare_bind(
        self,
        queue: str,
        exchange: str,
        routing_key: str,
        arguments: dict[str, Any] | None,
    ) -> tuple[str, str, str, dict[str, Any] | None]: ...
    def deliver(
        self,
        message: Any,
        exchange: str,
        routing_key: str,
        **kwargs: Any,
    ) -> None: ...

class DirectExchange(ExchangeType):
    type: str

class TopicExchange(ExchangeType):
    type: str

    def key_to_pattern(self, routing_key: str) -> Any: ...

class FanoutExchange(ExchangeType):
    type: str
