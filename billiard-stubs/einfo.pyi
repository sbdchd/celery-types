from types import TracebackType
from typing import Any, TypeAlias

__all__ = ["ExceptionInfo", "Traceback"]

class _Code:
    co_filename: str
    co_name: str
    co_argcount: int
    co_cellvars: tuple[()]
    co_firstlineno: int
    co_flags: int
    co_freevars: tuple[()]
    co_code: bytes
    co_lnotab: bytes
    co_names: tuple[str, ...]
    co_nlocals: int
    co_stacksize: int
    co_varnames: tuple[()]

    def __init__(self, code: Any) -> None: ...

class _Frame:
    Code = _Code
    f_builtins: dict[str, Any]
    f_globals: dict[str, Any]
    f_locals: dict[str, Any]
    f_back: None
    f_trace: None
    f_exc_traceback: None
    f_exc_type: None
    f_exc_value: None
    f_code: _Code
    f_lineno: int
    f_lasti: int
    f_restricted: bool

    def __init__(self, frame: Any) -> None: ...

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
