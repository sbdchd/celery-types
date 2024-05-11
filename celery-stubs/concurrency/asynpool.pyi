from typing import NamedTuple

from billiard import pool as _pool

__all__ = ["AsynPool"]

class Ack(NamedTuple): ...
class Worker(_pool.Worker): ...

class ResultHandler(_pool.ResultHandler):
    def on_stop_not_started(self) -> None: ...

class AsynPool(_pool.Pool):
    def flush(self) -> None: ...
