import numbers
from datetime import datetime
from typing import Any

from billiard.exceptions import (
    SoftTimeLimitExceeded,
    Terminated,
    TimeLimitExceeded,
    WorkerLostError,
)
from celery.canvas import Signature
from click.exceptions import ClickException
from kombu.exceptions import OperationalError

__all__ = (
    "AlreadyRegistered",
    "AlwaysEagerIgnored",
    "BackendError",
    "BackendGetMetaError",
    "BackendStoreError",
    "CDeprecationWarning",
    "CPendingDeprecationWarning",
    "CeleryCommandException",
    "CeleryError",
    "CeleryWarning",
    "ChordError",
    "DuplicateNodenameWarning",
    "FixupWarning",
    "Ignore",
    "ImproperlyConfigured",
    "IncompleteStream",
    "InvalidTaskError",
    "MaxRetriesExceededError",
    "NotConfigured",
    "NotRegistered",
    "OperationalError",
    "QueueNotFound",
    "Reject",
    "Retry",
    "SecurityError",
    "SecurityWarning",
    "SoftTimeLimitExceeded",
    "TaskError",
    "TaskPredicate",
    "TaskRevokedError",
    "Terminated",
    "TimeLimitExceeded",
    "TimeoutError",
    "WorkerLostError",
    "WorkerShutdown",
    "WorkerTerminate",
    "reraise",
)

class CeleryWarning(UserWarning): ...
class AlwaysEagerIgnored(CeleryWarning): ...
class DuplicateNodenameWarning(CeleryWarning): ...
class FixupWarning(CeleryWarning): ...
class NotConfigured(CeleryWarning): ...
class CeleryError(Exception): ...
class TaskPredicate(CeleryError): ...

class Retry(TaskPredicate):
    message: str | None
    exc: Exception | None
    when: numbers.Real | datetime | None
    def __init__(
        self,
        message: str | None = ...,
        exc: Exception | None = ...,
        when: numbers.Real | datetime | None = ...,
        is_eager: bool = ...,
        sig: Signature[Any] | None = ...,
        **kwargs: object,
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
    task_args: list[Any]
    task_kwargs: dict[str, Any]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class TaskRevokedError(TaskError): ...
class InvalidTaskError(TaskError): ...
class ChordError(TaskError): ...
class CPendingDeprecationWarning(PendingDeprecationWarning): ...
class CDeprecationWarning(DeprecationWarning): ...
class WorkerTerminate(SystemExit): ...

SystemTerminate = WorkerTerminate

class WorkerShutdown(SystemExit): ...
class BackendError(Exception): ...
class BackendGetMetaError(BackendError): ...
class BackendStoreError(BackendError): ...
class SecurityWarning(CeleryWarning): ...

def reraise(tp: type[BaseException], value: BaseException, tb: Any = None) -> None: ...

class CeleryCommandException(ClickException):
    def __init__(self, message: str, exit_code: int) -> None: ...
