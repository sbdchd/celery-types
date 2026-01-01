from typing import Any, TypeAlias

from kombu.connection import Connection, ConnectionPool
from kombu.messaging import Producer

__all__ = (
    "ProducerPool",
    "PoolGroup",
    "register_group",
    "connections",
    "producers",
    "get_limit",
    "set_limit",
    "reset",
)

_ProducerType: TypeAlias = Producer

class PoolGroup(dict[Any, Any]):
    def __init__(
        self, limit: int | None = ..., close_after_fork: bool = ...
    ) -> None: ...
    def __missing__(self, resource: Any) -> Any: ...
    def create(self, resource: Any, limit: int | None) -> Any: ...

class Connections(PoolGroup):
    def create(self, connection: Connection, limit: int | None) -> ConnectionPool: ...

class Producers(PoolGroup):
    def create(self, connection: Connection, limit: int | None) -> ProducerPool: ...

class ProducerPool:
    Producer: type[_ProducerType]
    connections: ConnectionPool
    limit: int | None
    close_after_fork: bool

    def __init__(
        self,
        connections: ConnectionPool,
        Producer: type[_ProducerType] = ...,
        limit: int | None = ...,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def setup(self) -> None: ...
    def create_producer(self) -> _ProducerType: ...
    def new(self) -> _ProducerType: ...
    def acquire(self, block: bool = ..., timeout: float | None = ...) -> _ProducerType: ...
    def prepare(self, p: _ProducerType) -> _ProducerType: ...
    def release(self, resource: _ProducerType) -> None: ...
    def close_resource(self, resource: _ProducerType) -> None: ...

connections: Connections
producers: Producers

def register_group(group: PoolGroup) -> PoolGroup: ...
def get_limit() -> int | None: ...
def set_limit(
    limit: int,
    force: bool = ...,
    reset_after: bool = ...,
    ignore_errors: bool = ...,
) -> int | None: ...
def reset(*args: Any, **kwargs: Any) -> None: ...
