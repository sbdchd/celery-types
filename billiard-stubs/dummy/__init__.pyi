import threading
from queue import Queue as Queue
from threading import BoundedSemaphore as BoundedSemaphore
from threading import Event as Event
from threading import Lock as Lock
from threading import RLock as RLock
from threading import Semaphore as Semaphore

__all__ = [
    "Process",
    "current_process",
    "freeze_support",
    "Lock",
    "RLock",
    "Semaphore",
    "BoundedSemaphore",
    "Event",
    "Queue",
    "JoinableQueue",
]

class DummyProcess(threading.Thread):
    def __init__(
        self,
    ) -> None: ...
    def start(self) -> None: ...

Process = DummyProcess
current_process = threading.current_thread

def freeze_support() -> None: ...

JoinableQueue = Queue
