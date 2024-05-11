from _typeshed import Incomplete
from billiard import pool as _pool
from typing import NamedTuple

__all__ = ['AsynPool']

class Ack(NamedTuple):
    id: Incomplete
    fd: Incomplete
    payload: Incomplete

class Worker(_pool.Worker):
    pass

class ResultHandler(_pool.ResultHandler):
    fileno_to_outq: Incomplete
    on_process_alive: Incomplete
    def on_stop_not_started(self) -> None: ...

class AsynPool(_pool.Pool):
    sched_strategy: Incomplete
    synack: Incomplete
    outbound_buffer: Incomplete
    write_stats: Incomplete
    on_soft_timeout: Incomplete
    on_hard_timeout: Incomplete
    def __init__(self, processes: Incomplete | None = None, synack: bool = False, sched_strategy: Incomplete | None = None, proc_alive_timeout: Incomplete | None = None) -> None: ...
    handle_result_event: Incomplete
    def flush(self) -> None: ...