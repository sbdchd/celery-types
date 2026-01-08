from typing import Any, TypeAlias

from kombu.connection import Connection, ConnectionPool
from kombu.messaging import Producer
from typing_extensions import override

__all__ = (
    "PoolGroup",
    "ProducerPool",
    "connections",
    "get_limit",
    "producers",
    "register_group",
    "reset",
    "set_limit",
)

_ProducerType: TypeAlias = Producer

class PoolGroup(dict[Any, Any]):
    def __init__(
        self, limit: int | None = ..., close_after_fork: bool = ...
    ) -> None: ...
    def __missing__(self, resource: Any) -> Any: ...
    def create(self, resource: Any, limit: int | None) -> Any: ...

class Connections(PoolGroup):
    @override
    def create(self, connection: Connection, limit: int | None) -> ConnectionPool: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]

class Producers(PoolGroup):
    @override
    def create(self, connection: Connection, limit: int | None) -> ProducerPool: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]

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
    def acquire(
        self, block: bool = ..., timeout: float | None = ...
    ) -> _ProducerType: ...
    def prepare(self, p: _ProducerType) -> _ProducerType: ...
    def release(self, resource: _ProducerType) -> None: ...
    def close_resource(self, resource: _ProducerType) -> None: ...
    def _acquire_connection(self) -> Connection: ...

def _all_pools() -> list[PoolGroup]: ...

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
