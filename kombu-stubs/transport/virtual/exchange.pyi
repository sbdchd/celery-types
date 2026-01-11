from collections.abc import Iterable
from typing import Any

STANDARD_EXCHANGE_TYPES: dict[str, type[ExchangeType]]

class ExchangeType:
    type: str | None

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
    def equivalent(
        self,
        prev: dict[str, Any],
        exchange: str,
        type: str,
        durable: bool,
        auto_delete: bool,
        arguments: dict[str, Any] | None,
    ) -> bool: ...

class DirectExchange(ExchangeType):
    type: str  # pyright: ignore[reportIncompatibleVariableOverride]

    def deliver(
        self,
        message: Any,
        exchange: str,
        routing_key: str,
        **kwargs: Any,
    ) -> None: ...

class TopicExchange(ExchangeType):
    type: str  # pyright: ignore[reportIncompatibleVariableOverride]
    wildcards: dict[str, str]

    def key_to_pattern(self, rkey: str) -> Any: ...
    def deliver(
        self,
        message: Any,
        exchange: str,
        routing_key: str,
        **kwargs: Any,
    ) -> None: ...

class FanoutExchange(ExchangeType):
    type: str  # pyright: ignore[reportIncompatibleVariableOverride]

    def deliver(
        self,
        message: Any,
        exchange: str,
        routing_key: str,
        **kwargs: Any,
    ) -> None: ...
