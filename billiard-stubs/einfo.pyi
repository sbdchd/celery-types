from types import TracebackType
from typing import Any, TypeAlias

__all__ = ["ExceptionInfo", "Traceback"]

class _Code:
    def __init__(self, code: Any) -> None: ...
    @property
    def co_positions(self) -> Any: ...

class _Frame:
    Code = _Code

    def __init__(self, frame: Any) -> None: ...
    @property
    def co_positions(self) -> Any: ...

class Traceback:
    Frame = _Frame
    Code = _Code

    def __init__(
        self, tb: TracebackType | None, max_frames: int = ..., depth: int = ...
    ) -> None: ...

_ExcInfo: TypeAlias = tuple[type[BaseException], BaseException, TracebackType | None]

class ExceptionInfo:
    exception: BaseException | None
    internal: bool
    tb: TracebackType | None
    traceback: str | None

    def __init__(
        self,
        exc_info: _ExcInfo | None = ...,
        internal: bool = ...,
    ) -> None: ...
    @property
    def type(self) -> type[BaseException] | None: ...  # ty: ignore[invalid-type-form]
    @property
    def exc_info(self) -> _ExcInfo | None: ...
