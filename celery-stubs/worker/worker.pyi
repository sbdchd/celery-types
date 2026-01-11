from collections.abc import Callable, Sequence
from typing import Any

from celery import bootsteps
from celery.worker.components import Hub, Pool, Timer

__all__ = ("WorkController",)

class WorkController:
    class Blueprint(bootsteps.Blueprint): ...
    app: Any
    blueprint: bootsteps.Blueprint | None
    exitcode: int | None
    hub: Hub | None
    pidlock: Any
    pool: Pool | None
    semaphore: Any
    timer: Timer | None

    def rusage(self) -> Any: ...
    @property
    def state(self) -> str: ...
    def __init__(
        self, app: Any = None, hostname: str | None = None, **kwargs: Any
    ) -> None: ...
    def info(self) -> dict[str, Any]: ...
    def on_after_init(self, **kwargs: Any) -> None: ...
    def on_before_init(self, **kwargs: Any) -> None: ...
    def on_close(self) -> None: ...
    def on_consumer_ready(self, consumer: Any) -> None: ...
    def on_init_blueprint(self) -> None: ...
    def on_start(self) -> None: ...
    def on_stopped(self) -> None: ...
    def prepare_args(self, **kwargs: Any) -> dict[str, Any]: ...
    def register_with_event_loop(self, hub: Any) -> None: ...
    def reload(
        self,
        modules: Sequence[str] | None = None,
        reload: bool = False,
        reloader: Any | None = None,
    ) -> None: ...
    def setup_defaults(
        self,
        concurrency: int | None = None,
        loglevel: str | int = "WARN",
        logfile: str | None = None,
        task_events: bool | None = None,
        pool: Any | None = None,
        consumer_cls: Any | None = None,
        timer_cls: Any | None = None,
        timer_precision: float | None = None,
        autoscaler_cls: Any | None = None,
        pool_putlocks: bool | None = None,
        pool_restarts: bool | None = None,
        optimization: str | None = None,
        O: str | None = None,
        statedb: str | None = None,
        time_limit: float | None = None,
        soft_time_limit: float | None = None,
        scheduler: str | None = None,
        pool_cls: Any | None = None,
        state_db: str | None = None,
        task_time_limit: float | None = None,
        task_soft_time_limit: float | None = None,
        scheduler_cls: Any | None = None,
        schedule_filename: str | None = None,
        max_tasks_per_child: int | None = None,
        prefetch_multiplier: int | None = None,
        disable_rate_limits: bool | None = None,
        worker_lost_wait: float | None = None,
        max_memory_per_child: int | None = None,
        **_kw: Any,
    ) -> dict[str, Any]: ...
    def setup_includes(self, includes: Sequence[str]) -> None: ...
    def setup_instance(
        self,
        queues: Sequence[str] | None = None,
        ready_callback: Callable[[], None] | None = None,
        pidfile: str | None = None,
        include: Sequence[str] | None = None,
        use_eventloop: bool | None = None,
        exclude_queues: Sequence[str] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def setup_queues(
        self, include: Sequence[str], exclude: Sequence[str] | None = None
    ) -> None: ...
    def should_use_eventloop(self) -> bool: ...
    def signal_consumer_close(self) -> None: ...
    def start(self) -> None: ...
    def stats(self) -> dict[str, Any]: ...
    def stop(
        self, in_sighandler: bool = False, exitcode: int | None = None
    ) -> None: ...
    def terminate(self, in_sighandler: bool = False) -> None: ...
    def wait_for_soft_shutdown(self) -> bool: ...
