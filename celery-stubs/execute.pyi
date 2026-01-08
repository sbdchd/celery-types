from datetime import datetime
from typing import Any

from celery.result import AsyncResult
from kombu import Connection
from kombu.messaging import Producer

def send_task(
    name: str,
    args: tuple[Any, ...] | None = ...,
    kwargs: dict[str, Any] | None = ...,
    countdown: float | None = ...,
    eta: datetime | None = ...,
    task_id: str | None = ...,
    producer: Producer | None = ...,
    connection: Connection | None = ...,
    router: Any | None = ...,
    result_cls: type[AsyncResult[Any]] | None = ...,
    expires: float | datetime | None = ...,
    publisher: Any | None = ...,
    link: Any | None = ...,
    link_error: Any | None = ...,
    add_to_parent: bool = ...,
    group_id: str | None = ...,
    group_index: int | None = ...,
    retries: int = ...,
    chord: Any | None = ...,
    reply_to: str | None = ...,
    time_limit: float | None = ...,
    soft_time_limit: float | None = ...,
    root_id: str | None = ...,
    parent_id: str | None = ...,
    route_name: str | None = ...,
    shadow: str | None = ...,
    chain: Any | None = ...,
    task_type: Any | None = ...,
    replaced_task_nesting: int = ...,
    **options: Any,
) -> AsyncResult[Any]: ...

__all__ = ["send_task"]
