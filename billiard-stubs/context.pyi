from billiard import process as process
from billiard.exceptions import AuthenticationError as AuthenticationError
from billiard.exceptions import BufferTooShort as BufferTooShort
from billiard.exceptions import ProcessError as ProcessError
from billiard.exceptions import SoftTimeLimitExceeded as SoftTimeLimitExceeded
from billiard.exceptions import TimeLimitExceeded as TimeLimitExceeded
from billiard.exceptions import TimeoutError as TimeoutError
from billiard.exceptions import WorkerLostError as WorkerLostError

W_NO_EXECV: str

class BaseContext:
    def freeze_support(self) -> None: ...
    def allow_connection_pickling(self) -> None: ...

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
