from datetime import datetime
from typing import Any, ClassVar

__all__ = ("Task", "TaskExtended", "TaskSet")

# Note: These are SQLAlchemy declarative models with DeclarativeMeta metaclass
# stubtest cannot reconcile the InstrumentedAttribute class-level types with
# the instance-level types users actually see. Using plain classes here since
# users access these as regular attributes on instances.

class Task:
    __tablename__: ClassVar[str]
    __table_args__: ClassVar[dict[str, Any]]
    __table__: ClassVar[Any]
    __mapper__: ClassVar[Any]

    id: int | None
    task_id: str
    status: str
    result: bytes | None
    date_done: datetime | None
    traceback: str | None

    def __init__(self, task_id: str) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def configure(cls, schema: str | None = None, name: str | None = None) -> None: ...

class TaskExtended(Task):
    name: str | None
    args: bytes | None
    kwargs: bytes | None
    worker: str | None
    retries: int | None
    queue: str | None
    children: bytes | None

    def __init__(self, task_id: str) -> None: ...

class TaskSet:
    __tablename__: ClassVar[str]
    __table_args__: ClassVar[dict[str, Any]]
    __table__: ClassVar[Any]
    __mapper__: ClassVar[Any]

    id: int | None
    taskset_id: str
    result: bytes | None
    date_done: datetime | None

    def __init__(self, taskset_id: str, result: bytes | None) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def configure(cls, schema: str | None = None, name: str | None = None) -> None: ...
