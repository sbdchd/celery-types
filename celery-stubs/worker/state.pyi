from collections.abc import Callable, MutableSet
from types import ModuleType
from typing import Any

from celery.utils.collections import LimitedSet

__all__ = (
    "SOFTWARE_INFO",
    "Persistent",
    "active_requests",
    "maybe_shutdown",
    "reserved_requests",
    "revoked",
    "task_accepted",
    "task_ready",
    "task_reserved",
    "total_count",
)

class Persistent:
    db: Any
    merge: Callable[..., Any]
    open: Callable[..., Any]
    protocol: int
    storage: ModuleType
    # These are zlib.compress and zlib.decompress functions assigned as class attributes
    compress: Callable[..., bytes]
    decompress: Callable[..., bytes]

    def __init__(self, state: Any, filename: str, clock: Any | None = None) -> None: ...
    def save(self) -> None: ...
    def close(self) -> None: ...
    def sync(self) -> None: ...

C_BENCH: None
C_BENCH_EVERY: int
REVOKES_MAX: int
REVOKE_EXPIRES: float
SUCCESSFUL_EXPIRES: float
SUCCESSFUL_MAX: int
SOFTWARE_INFO: dict[str, str]

revoked: LimitedSet
revoked_stamps: dict[str, set[str]]
active_requests: MutableSet[Any]
reserved_requests: MutableSet[Any]
successful_requests: LimitedSet
requests: dict[str, Any]
total_count: dict[str, int]
all_total_count: list[int]

should_stop: None
should_terminate: None

def maybe_shutdown() -> None: ...
def reset_state() -> None: ...
def task_accepted(
    request: Any,
    _all_total_count: list[int] | None = None,
    add_request: Callable[..., Any] = ...,
    add_active_request: Callable[..., Any] = ...,
    add_to_total_count: Callable[..., Any] = ...,
) -> None: ...
def task_reserved(
    request: Any,
    add_request: Callable[..., Any] = ...,
    add_reserved_request: Callable[..., Any] = ...,
) -> None: ...
def task_ready(
    request: Any,
    successful: bool = False,
    remove_request: Callable[..., Any] = ...,
    discard_active_request: Callable[..., Any] = ...,
    discard_reserved_request: Callable[..., Any] = ...,
) -> None: ...
