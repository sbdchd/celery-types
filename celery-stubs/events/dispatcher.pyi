from collections.abc import Callable
from typing import Any

import kombu
from celery.app.base import Celery
from kombu.transport.virtual import Channel
from typing_extensions import Self

__all__ = ("EventDispatcher",)

class EventDispatcher:
    DISABLED_TRANSPORTS: set[str]
    app: Celery | None
    connection: kombu.Connection | None
    hostname: str
    groups: set[str] | None
    enabled: bool
    on_enabled: Callable[[], None] | None
    on_disabled: Callable[[], None] | None

    def __init__(
        self,
        connection: kombu.Connection | None = None,
        hostname: str | None = None,
        enabled: bool = True,
        channel: Channel | None = None,
        buffer_while_offline: bool = True,
        app: Celery | None = None,
        serializer: str | None = None,
        groups: list[str] | None = None,
        delivery_mode: int | str = ...,
        buffer_group: list[str] | None = None,
        buffer_limit: int = 24,
        on_send_buffered: Callable[..., Any] | None = None,
    ) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def publish(
        self,
        type: str,
        fields: dict[str, Any],
        producer: kombu.Producer,
        blind: bool = False,
        Event: Callable[..., dict[str, Any]] = ...,
        **kwargs: Any,
    ) -> None: ...
    def send(
        self,
        type: str,
        blind: bool = False,
        utcoffset: Callable[[], int] = ...,
        retry: bool = False,
        retry_policy: dict[str, Any] | None = None,
        Event: Callable[..., dict[str, Any]] = ...,
        **fields: Any,
    ) -> None: ...
    def extend_buffer(
        self,
        other: EventDispatcher,
    ) -> None: ...
    def flush(
        self,
        errors: bool = True,
        groups: bool = True,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def publisher(self) -> kombu.Producer | None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object) -> None: ...
