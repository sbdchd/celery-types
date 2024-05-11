import threading
from _typeshed import Incomplete
from queue import Queue as Queue
from threading import BoundedSemaphore as BoundedSemaphore, Event as Event, Lock as Lock, RLock as RLock, Semaphore as Semaphore

__all__ = ['Process', 'current_process', 'freeze_support', 'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Event', 'Queue', 'JoinableQueue']

class DummyProcess(threading.Thread):
    def __init__(self, group: Incomplete | None = None, target: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def start(self) -> None: ...

Process = DummyProcess
current_process = threading.current_thread

def freeze_support() -> None: ...

JoinableQueue = Queue
