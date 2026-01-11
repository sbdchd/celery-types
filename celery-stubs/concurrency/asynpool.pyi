from typing import Any, NamedTuple

from billiard import pool as _pool
from typing_extensions import override

__all__ = ("AsynPool",)

class Ack(NamedTuple):
    id: int
    fd: int
    payload: Any

class Worker(_pool.Worker): ...

class ResultHandler(_pool.ResultHandler):
    @override
    def on_stop_not_started(self) -> None: ...
    def register_with_event_loop(self, hub: Any) -> None: ...

class AsynPool(_pool.Pool):
    @property
    def timers(self) -> dict[Any, Any]: ...
    def __init__(
        self,
        processes: int | None = None,
        synack: bool = False,
        sched_strategy: int | None = None,
        proc_alive_timeout: float | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def flush(self) -> None: ...
    def create_process_queues(self) -> tuple[Any, Any, Any]: ...
    @override
    def create_result_handler(self) -> ResultHandler: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def destroy_queues(self, queues: tuple[Any, Any, Any], proc: Any) -> None: ...
    def human_write_stats(self) -> str: ...
    @override
    def on_partial_read(self, job: Any, proc: Any) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    def on_process_alive(self, pid: int) -> None: ...
    @override
    def process_flush_queues(self, proc: Any) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    def register_with_event_loop(self, hub: Any) -> None: ...
