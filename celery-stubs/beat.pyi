import shelve
from _typeshed import Incomplete
from billiard.context import Process
from threading import Thread
from typing import NamedTuple

__all__ = ['SchedulingError', 'ScheduleEntry', 'Scheduler', 'PersistentScheduler', 'Service']

class event_t(NamedTuple):
    time: Incomplete
    priority: Incomplete
    entry: Incomplete

class SchedulingError(Exception): ...

class BeatLazyFunc: ...

class ScheduleEntry:
    name: Incomplete
    schedule: Incomplete
    args: Incomplete
    kwargs: Incomplete
    options: Incomplete
    last_run_at: Incomplete
    total_run_count: int
    app: Incomplete
    task: Incomplete
    __next__: Incomplete
    next: Incomplete

class Scheduler:
    Entry = ScheduleEntry
    schedule: Incomplete
    sync_every: Incomplete
    sync_every_tasks: Incomplete
    app: Incomplete
    data: Incomplete
    Producer: Incomplete
    old_schedulers: Incomplete
    def setup_schedule(self) -> None: ...
    def sync(self) -> None: ...
    def close(self) -> None: ...

class PersistentScheduler(Scheduler):
    persistence = shelve
    known_suffixes: Incomplete
    schedule_filename: Incomplete
    def setup_schedule(self) -> None: ...
    schedule: Incomplete
    def sync(self) -> None: ...
    def close(self) -> None: ...

class Service:
    scheduler_cls = PersistentScheduler
    app: Incomplete
    max_interval: Incomplete
    schedule_filename: Incomplete
    def start(self, embedded_process: bool = False) -> None: ...
    def sync(self) -> None: ...
    def stop(self, wait: bool = False) -> None: ...

class _Threaded(Thread):
    app: Incomplete
    service: Incomplete
    daemon: bool
    name: str
    def run(self) -> None: ...
    def stop(self) -> None: ...

class _Process(Process):
    app: Incomplete
    service: Incomplete
    name: str
    def run(self) -> None: ...
    def stop(self) -> None: ...