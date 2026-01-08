from collections.abc import Callable, Mapping
from typing import Any, TypeAlias

from amqp.basic_message import Message

__all__ = ("Channel",)

_MessageType: TypeAlias = Message

class Channel:
    Message: type[_MessageType]

    connection: Any
    channel_id: int | None
    auto_decode: bool
    is_open: bool

    def __init__(
        self,
        connection: Any,
        channel_id: int | None = ...,
        auto_decode: bool = ...,
        on_open: Callable[..., Any] | None = ...,
    ) -> None: ...
    def open(self) -> None: ...
    def close(
        self,
        reply_code: int = ...,
        reply_text: str = ...,
        method_sig: tuple[int, int] = ...,
        argsig: str = ...,
    ) -> None: ...
    def collect(self) -> None: ...
    def flow(self, active: bool) -> None: ...
    def exchange_declare(
        self,
        exchange: str,
        type: str,
        passive: bool = ...,
        durable: bool = ...,
        auto_delete: bool = ...,
        nowait: bool = ...,
        arguments: Mapping[str, Any] | None = ...,
        argsig: str = ...,
    ) -> None: ...
    def exchange_delete(
        self,
        exchange: str,
        if_unused: bool = ...,
        nowait: bool = ...,
        argsig: str = ...,
    ) -> None: ...
    def exchange_bind(
        self,
        destination: str,
        source: str = ...,
        routing_key: str = ...,
        nowait: bool = ...,
        arguments: Mapping[str, Any] | None = ...,
        argsig: str = ...,
    ) -> None: ...
    def exchange_unbind(
        self,
        destination: str,
        source: str = ...,
        routing_key: str = ...,
        nowait: bool = ...,
        arguments: Mapping[str, Any] | None = ...,
        argsig: str = ...,
    ) -> None: ...
    def queue_declare(
        self,
        queue: str = ...,
        passive: bool = ...,
        durable: bool = ...,
        exclusive: bool = ...,
        auto_delete: bool = ...,
        nowait: bool = ...,
        arguments: Mapping[str, Any] | None = ...,
        argsig: str = ...,
    ) -> tuple[str, int, int] | None: ...
    def queue_delete(
        self,
        queue: str = ...,
        if_unused: bool = ...,
        if_empty: bool = ...,
        nowait: bool = ...,
        argsig: str = ...,
    ) -> int | None: ...
    def queue_bind(
        self,
        queue: str,
        exchange: str = ...,
        routing_key: str = ...,
        nowait: bool = ...,
        arguments: Mapping[str, Any] | None = ...,
        argsig: str = ...,
    ) -> None: ...
    def queue_unbind(
        self,
        queue: str,
        exchange: str,
        routing_key: str = ...,
        nowait: bool = ...,
        arguments: Mapping[str, Any] | None = ...,
        argsig: str = ...,
    ) -> None: ...
    def queue_purge(
        self, queue: str = ..., nowait: bool = ..., argsig: str = ...
    ) -> int | None: ...
    def basic_qos(
        self,
        prefetch_size: int,
        prefetch_count: int,
        a_global: bool,
        argsig: str = ...,
    ) -> None: ...
    def basic_consume(
        self,
        queue: str = ...,
        consumer_tag: str = ...,
        no_local: bool = ...,
        no_ack: bool = ...,
        exclusive: bool = ...,
        nowait: bool = ...,
        callback: Callable[..., Any] | None = ...,
        arguments: Mapping[str, Any] | None = ...,
        on_cancel: Callable[..., Any] | None = ...,
        argsig: str = ...,
    ) -> str: ...
    def basic_cancel(
        self, consumer_tag: str, nowait: bool = ..., argsig: str = ...
    ) -> None: ...
    def basic_get(
        self, queue: str = ..., no_ack: bool = ..., argsig: str = ...
    ) -> _MessageType | None: ...
    def basic_ack(
        self, delivery_tag: int, multiple: bool = ..., argsig: str = ...
    ) -> None: ...
    def basic_reject(
        self, delivery_tag: int, requeue: bool, argsig: str = ...
    ) -> None: ...
    def basic_recover(self, requeue: bool = ...) -> None: ...
    def basic_recover_async(self, requeue: bool = ...) -> None: ...
    def basic_publish(
        self,
        msg: _MessageType,
        exchange: str = ...,
        routing_key: str = ...,
        mandatory: bool = ...,
        immediate: bool = ...,
        timeout: float | None = ...,
        confirm_timeout: float | None = ...,
        argsig: str = ...,
    ) -> None: ...
    def basic_publish_confirm(self, *args: Any, **kwargs: Any) -> None: ...
    def tx_select(self) -> None: ...
    def tx_commit(self) -> None: ...
    def tx_rollback(self) -> None: ...
    def confirm_select(self, nowait: bool = ...) -> None: ...
    def dispatch_method(
        self, method_sig: tuple[int, int], payload: bytes, content: Any
    ) -> None: ...
    def send_method(
        self,
        sig: tuple[int, int],
        format: str | None = ...,
        args: tuple[Any, ...] | None = ...,
        content: Any | None = ...,
        wait: Any | None = ...,
        callback: Callable[..., Any] | None = ...,
        returns_tuple: bool = ...,
    ) -> Any: ...
    def wait(
        self,
        method: Any,
        callback: Callable[..., Any] | None = ...,
        timeout: float | None = ...,
        returns_tuple: bool = ...,
    ) -> Any: ...
    def then(
        self,
        on_success: Callable[..., Any],
        on_error: Callable[..., Any] | None = ...,
    ) -> Any: ...
