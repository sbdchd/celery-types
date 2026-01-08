from collections.abc import Callable
from typing import Any

from vine.promises import promise

def maybe_promise(p: Any) -> promise | None: ...
def ensure_promise(p: Any) -> promise: ...
def ppartial(p: promise, *args: Any, **kwargs: Any) -> promise: ...
def preplace(p: promise, *args: Any, **kwargs: Any) -> promise: ...
def ready_promise(callback: Callable[..., Any] | None = ..., *args: Any) -> promise: ...
def starpromise(fun: Callable[..., Any], *args: Any, **kwargs: Any) -> promise: ...
def transform(
    filter_: Callable[..., Any],
    callback: Callable[..., Any],
    *filter_args: Any,
    **filter_kwargs: Any,
) -> promise: ...
def wrap(p: Any) -> promise: ...

__all__ = [
    "ensure_promise",
    "maybe_promise",
    "ppartial",
    "preplace",
    "ready_promise",
    "starpromise",
    "transform",
    "wrap",
]
