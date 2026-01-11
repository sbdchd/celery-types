from collections.abc import Callable, Iterable, Iterator
from contextlib import contextmanager
from operator import itemgetter
from typing import Any

import kombu
from celery.app.base import Celery
from kombu.utils.objects import cached_property

__all__ = ("EventReceiver",)

class EventReceiver:
    Consumer: Callable[..., Any]
    app: Celery | None
    handlers: dict[str, Callable[..., Any]]
    channel_errors: cached_property[tuple[type[Exception], ...]]
    connection_errors: cached_property[tuple[type[Exception], ...]]
    connect_max_retries: int | None
    restart_limit: Any
    should_stop: bool

    def __init__(
        self,
        channel: Any,
        handlers: dict[str, Callable[..., Any]] | None = None,
        routing_key: str = "#",
        node_id: str | None = None,
        app: Celery | None = None,
        queue_prefix: str | None = None,
        accept: Iterable[str] | None = None,
        queue_ttl: float | None = None,
        queue_expires: float | None = None,
        queue_exclusive: bool | None = None,
        queue_durable: bool | None = None,
    ) -> None: ...
    @property
    def connection(self) -> kombu.Connection: ...
    def process(
        self,
        type: str,
        event: dict[str, Any],
    ) -> None: ...
    def capture(
        self,
        limit: int | None = None,
        timeout: float | None = None,
        wakeup: bool = True,
    ) -> None: ...
    def itercapture(
        self,
        limit: int | None = None,
        timeout: float | None = None,
        wakeup: bool = True,
    ) -> Iterator[tuple[str, dict[str, Any]]]: ...
    def consume(
        self,
        limit: int | None = None,
        timeout: float | None = None,
        safety_interval: float = 1,
        **kwargs: Any,
    ) -> None: ...
    def run(
        self,
        _tokens: int = 1,
        **kwargs: Any,
    ) -> None: ...
    @contextmanager
    def consumer_context(self, wakeup: bool = True) -> Iterator[kombu.Consumer]: ...
    def on_consume_ready(
        self,
        connection: Any,
        channel: Any,
        consumers: list[Any],
        wakeup: bool = True,
        **kwargs: Any,
    ) -> None: ...
    def on_consume_end(self, connection: Any, channel: Any) -> None: ...
    def on_connection_revived(self) -> None: ...
    def on_connection_error(self, exc: Exception, interval: float) -> None: ...
    def on_decode_error(self, message: Any, exc: Exception) -> None: ...
    def on_iteration(self) -> None: ...
    def maybe_conn_error(self, fun: Callable[..., Any]) -> Any: ...
    def create_connection(self) -> kombu.Connection: ...
    def establish_connection(self) -> kombu.Connection: ...
    @contextmanager
    def extra_context(
        self, connection: kombu.Connection, channel: Any
    ) -> Iterator[None]: ...
    def event_from_message(
        self,
        body: Any,
        localize: bool = True,
        now: Callable[[], float] = ...,
        tzfields: itemgetter[Any] = ...,
        adjust_timestamp: Callable[..., float] = ...,
        CLIENT_CLOCK_SKEW: int = -1,
    ) -> tuple[str, dict[str, Any]]: ...
    def get_consumers(self, Consumer: type[Any], channel: Any) -> list[Any]: ...
    def wakeup_workers(self, channel: Any = None) -> None: ...
