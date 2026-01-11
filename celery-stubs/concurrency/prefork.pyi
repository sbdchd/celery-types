from collections.abc import Callable
from typing import Any

from billiard.pool import Pool as BilliardPool
from celery.concurrency.asynpool import AsynPool
from celery.concurrency.base import BasePool
from typing_extensions import override

__all__ = ("TaskPool", "process_destructor", "process_initializer")

def process_initializer(app: Any, hostname: str) -> None: ...
def process_destructor(pid: int, exitcode: int) -> None: ...

class TaskPool(BasePool):
    Pool: type[AsynPool]
    BlockingPool: Callable[..., BilliardPool]
    uses_semaphore: bool
    write_stats: Callable[[], str | None] | None

    @override
    def on_start(self) -> None: ...
    @override
    def restart(self) -> None: ...
    @override
    def on_stop(self) -> None: ...
    @override
    def on_terminate(self) -> None: ...
    @override
    def on_close(self) -> None: ...
