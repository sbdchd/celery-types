from collections.abc import Callable, Generator, Iterable, Mapping
from contextlib import contextmanager
from typing import Any, BinaryIO, TextIO, TypeVar
from uuid import UUID

from kombu.utils.functional import retry_over_time as retry_over_time
from kombu.utils.objects import cached_property as cached_property

# Note: runtime __all__ includes reprkwargs but it's not actually defined (kombu bug)
# We match the runtime __all__ exactly
__all__ = (
    "EqualityDict",
    "uuid",
    "maybe_list",
    "fxrange",
    "fxrangemax",
    "retry_over_time",
    "emergency_dump_state",
    "cached_property",
    "register_after_fork",
    "reprkwargs",
    "reprcall",
    "symbol_by_name",
    "nested",
    "fileno",
    "maybe_fileno",
)

# Defined in __all__ but not actually implemented at runtime (kombu bug)
# We define it in the stub to match __all__
def reprkwargs(kwargs: Mapping[str, Any], sep: str = ..., fmt: str = ...) -> str: ...

_T = TypeVar("_T")

class EqualityDict(dict[Any, Any]): ...

def uuid(_uuid: Callable[[], UUID] = ...) -> str: ...
def maybe_list(
    obj: Any, scalars: tuple[type[Any], ...] = ...
) -> list[Any] | None: ...
def fxrange(
    start: float = ...,
    stop: float | None = ...,
    step: float = ...,
    repeatlast: bool = ...,
) -> Generator[float, None, None]: ...
def fxrangemax(
    start: float = ...,
    stop: float | None = ...,
    step: float = ...,
    max: float = ...,
) -> Generator[float, None, None]: ...
def emergency_dump_state(
    state: Any,
    open_file: Callable[..., BinaryIO | TextIO] = ...,
    dump: Callable[..., None] | None = ...,
    stderr: TextIO | None = ...,
) -> None: ...
def register_after_fork(obj: Any, func: Callable[..., Any]) -> None: ...
def reprcall(
    name: str,
    args: Iterable[Any] = ...,
    kwargs: Mapping[str, Any] | None = ...,
    sep: str = ...,
) -> str: ...
def symbol_by_name(
    name: str,
    aliases: Mapping[str, str] | None = ...,
    imp: Callable[[str], Any] | None = ...,
    package: str | None = ...,
    sep: str = ...,
    default: _T | None = ...,
    **kwargs: Any,
) -> Any: ...
@contextmanager
def nested(*managers: Any) -> Generator[tuple[Any, ...], None, None]: ...
def fileno(f: Any) -> int: ...
def maybe_fileno(f: Any) -> int | None: ...
