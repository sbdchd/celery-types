from collections.abc import Callable
from functools import partial as partial
from types import TracebackType
from typing import Any, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

WRAPPER_ASSIGNMENTS: tuple[str, ...]
WRAPPER_UPDATES: tuple[str, ...]

def update_wrapper(
    wrapper: _F,
    wrapped: Callable[..., Any],
    assigned: tuple[str, ...] = ...,
    updated: tuple[str, ...] = ...,
) -> _F: ...
def wraps(
    wrapped: Callable[..., Any],
    assigned: tuple[str, ...] = ...,
    updated: tuple[str, ...] = ...,
) -> Callable[[_F], _F]: ...
def reraise(
    tp: type[BaseException], value: BaseException, tb: TracebackType | None = ...
) -> None: ...

__all__ = ["update_wrapper", "wraps"]
