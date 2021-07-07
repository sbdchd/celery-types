import numbers
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from billiard.exceptions import (
    SoftTimeLimitExceeded,
    Terminated,
    TimeLimitExceeded,
    WorkerLostError,
)
from celery.canvas import Signature
from kombu.exceptions import OperationalError

__all__ = [
    "CeleryWarning",
    "AlwaysEagerIgnored",
    "DuplicateNodenameWarning",
    "FixupWarning",
    "NotConfigured",
    "CeleryError",
    "ImproperlyConfigured",
    "SecurityError",
    "OperationalError",
    "TaskPredicate",
    "Ignore",
    "Reject",
    "Retry",
    "TaskError",
    "QueueNotFound",
    "IncompleteStream",
    "NotRegistered",
    "AlreadyRegistered",
    "TimeoutError",
    "MaxRetriesExceededError",
    "TaskRevokedError",
    "InvalidTaskError",
    "ChordError",
    "SoftTimeLimitExceeded",
    "TimeLimitExceeded",
    "WorkerLostError",
    "Terminated",
    "CPendingDeprecationWarning",
    "CDeprecationWarning",
    "WorkerShutdown",
    "WorkerTerminate",
]

class CeleryWarning(UserWarning): ...
class AlwaysEagerIgnored(CeleryWarning): ...
class DuplicateNodenameWarning(CeleryWarning): ...
class FixupWarning(CeleryWarning): ...
class NotConfigured(CeleryWarning): ...
class CeleryError(Exception): ...
class TaskPredicate(CeleryError): ...

class Retry(TaskPredicate):
    message: Optional[str]
    exc: Optional[Exception]
    when: Optional[Union[numbers.Real, datetime]]
    def __init__(
        self,
        message: Optional[str] = ...,
        exc: Optional[Exception] = ...,
        when: Optional[Union[numbers.Real, datetime]] = ...,
        is_eager: bool = ...,
        sig: Signature | None = ...,
        **kwargs: object
    ) -> None: ...
    def humanize(self) -> str: ...

RetryTaskError = Retry

class Ignore(TaskPredicate): ...

class Reject(TaskPredicate):
    def __init__(
        self, reason: Exception | str | None = ..., requeue: bool | None = ...
    ) -> None: ...

class ImproperlyConfigured(CeleryError): ...
class SecurityError(CeleryError): ...
class TaskError(CeleryError): ...
class QueueNotFound(KeyError, TaskError): ...
class IncompleteStream(TaskError): ...
class NotRegistered(KeyError, TaskError): ...
class AlreadyRegistered(TaskError): ...
class TimeoutError(TaskError): ...

class MaxRetriesExceededError(TaskError):

    task_args: List[Any]
    task_kwargs: Dict[str, Any]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class TaskRevokedError(TaskError): ...
class InvalidTaskError(TaskError): ...
class ChordError(TaskError): ...
class CPendingDeprecationWarning(PendingDeprecationWarning): ...
class CDeprecationWarning(DeprecationWarning): ...
class WorkerTerminate(SystemExit): ...

SystemTerminate = WorkerTerminate

class WorkerShutdown(SystemExit): ...
