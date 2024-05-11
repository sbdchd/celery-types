from . import process as process
from .exceptions import AuthenticationError as AuthenticationError, BufferTooShort as BufferTooShort, ProcessError as ProcessError, SoftTimeLimitExceeded as SoftTimeLimitExceeded, TimeLimitExceeded as TimeLimitExceeded, TimeoutError as TimeoutError, WorkerLostError as WorkerLostError
from _typeshed import Incomplete

W_NO_EXECV: str

class BaseContext:
    current_process: Incomplete
    active_children: Incomplete
    def freeze_support(self) -> None: ...
    def allow_connection_pickling(self) -> None: ...
    def set_start_method(self, method: Incomplete | None = None) -> None: ...

class Process(process.BaseProcess): ...

class DefaultContext(BaseContext): ...
class ForkProcess(process.BaseProcess): ...
class SpawnProcess(process.BaseProcess): ...
class ForkServerProcess(process.BaseProcess): ...

class ForkContext(BaseContext):
    Process = ForkProcess

class SpawnContext(BaseContext):
    Process = SpawnProcess

class ForkServerContext(BaseContext):
    Process = ForkServerProcess
