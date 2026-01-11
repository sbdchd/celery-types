from collections.abc import Callable, Mapping
from types import TracebackType
from typing import Any, TypeVar

_ExcT = TypeVar("_ExcT", bound=BaseException)

def symbol_by_name(
    name: str,
    aliases: Mapping[str, str] | None = ...,
    imp: Callable[[str], Any] | None = ...,
    package: str | None = ...,
    sep: str = ...,
    default: Any = ...,
    **kwargs: Any,
) -> Any: ...
def reraise(tp: type[_ExcT], value: _ExcT, tb: TracebackType | None = ...) -> _ExcT: ...
