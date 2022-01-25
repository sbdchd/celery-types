from typing import Any, Callable, Iterable, Mapping, Sequence, Tuple, Union

from celery.app.base import Celery
from kombu import Connection
from kombu.pidbox import Mailbox as KombuMailbox

_Reply = Any

_Destination = Union[Sequence[str], Tuple[str, ...]]

def flatten_reply(reply: Iterable[Mapping[str, _Reply]]) -> dict[str, _Reply]: ...

class Inspect:
    app: Celery | None
    def __init__(
        self,
        destination: _Destination | None = ...,
        timeout: float = ...,
        callback: Callable[..., Any] | None = ...,
        connection: Connection | None = ...,
        app: Celery | None = ...,
        limit: int | None = ...,
        pattern: str | None = ...,
        matcher: Callable[..., Any] | None = ...,
    ) -> None: ...
    def _prepare(self, reply: bool) -> None | dict[str, _Reply]: ...
    def _request(self, command: str, **kwargs: Any) -> list[dict[str, _Reply]]: ...
    def report(self) -> list[dict[str, Any]]: ...
    def clock(self) -> list[dict[str, Any]]: ...
    def active(self, safe: Any | None = ...) -> list[dict[str, _Reply]]: ...
    def scheduled(self, safe: Any | None = ...) -> list[dict[str, Any]]: ...
    def reserved(self, safe: Any | None = ...) -> list[dict[str, Any]]: ...
    def stats(self) -> dict[str, _Reply]: ...
    def revoked(self) -> list[dict[str, _Reply]]: ...
    def registered(self, *taskinfoitems: Any) -> list[dict[str, _Reply]]: ...
    registered_tasks = registered
    def ping(
        self, destination: _Destination | None = ...
    ) -> list[dict[str, _Reply]]: ...
    def active_queues(self) -> list[dict[str, _Reply]]: ...
    def query_task(self, *ids: str) -> list[dict[str, _Reply]]: ...
    def conf(self, with_defaults: bool = ...) -> list[dict[str, _Reply]]: ...
    def hello(
        self, from_node: Any, revoked: Any | None = ...
    ) -> list[dict[str, _Reply]]: ...
    def memsample(self) -> list[dict[str, _Reply]]: ...
    def memdump(self, samples: int = ...) -> list[dict[str, _Reply]]: ...
    def objgraph(
        self, type: str = ..., n: int = ..., max_depth: int = ...
    ) -> list[dict[str, _Reply]]: ...

class Control:
    Mailbox: KombuMailbox
    app: Celery | None
    def __init__(self, app: Celery | None = ...) -> None: ...
    def inspect(self) -> Any: ...
    def purge(self, connection: Connection | None = ...) -> int: ...
    discard_all = purge
    def election(
        self,
        id: str,
        topic: str,
        action: str | None = ...,
        connection: Connection | None = ...,
    ) -> None: ...
    def revoke(
        self,
        task_id: str | Sequence[str],
        destination: _Destination | None = ...,
        terminate: bool = ...,
        signal: str = ...,
        **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def terminate(
        self,
        task_id: str,
        destination: _Destination | None = ...,
        signal: str = ...,
        **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def ping(
        self,
        destination: _Destination | None = ...,
        timeout: float = ...,
        **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def rate_limit(
        self,
        task_name: str,
        rate_limit: int | str,
        destination: _Destination | None = ...,
        **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def add_consumer(
        self,
        queue: str,
        exchange: str | None = ...,
        exchange_type: str = ...,
        routing_key: str | None = ...,
        options: Mapping[str, Any] | None = ...,
        destination: _Destination | None = ...,
        **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def cancel_consumer(
        self, queue: str, destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def time_limit(
        self,
        task_name: str,
        soft: float | None = ...,
        hard: float | None = ...,
        destination: _Destination | None = ...,
        **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def enable_events(
        self, destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def disable_events(
        self, destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def pool_grow(
        self, n: int = ..., destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def pool_shrink(
        self, n: int = ..., destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def autoscale(
        self, max: int, min: int, destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def shutdown(
        self, destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def pool_restart(
        self,
        modules: Sequence[str] | None = ...,
        reload: bool = ...,
        reloader: Callable[..., Any] | None = ...,
        destination: _Destination | None = ...,
        **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def heartbeat(
        self, destination: _Destination | None = ..., **kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
    def broadcast(
        self,
        command: str,
        arguments: Mapping[str, Any] | None = ...,
        destination: _Destination | None = ...,
        connection: Connection | None = ...,
        reply: bool = ...,
        timeout: float = ...,
        limit: int | None = ...,
        callback: Callable[..., Any] | None = ...,
        channel: Any | None = ...,
        pattern: str | None = ...,
        matcher: Callable[..., Any] = ...,
        **extra_kwargs: Any
    ) -> list[dict[str, _Reply]] | None: ...
