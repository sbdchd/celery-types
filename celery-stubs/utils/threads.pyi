from typing import Generic, TypeVar

_T = TypeVar("_T")

class _LocalStack(Generic[_T]):
    top: _T | None
