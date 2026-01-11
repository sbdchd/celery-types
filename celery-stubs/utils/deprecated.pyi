from collections.abc import Callable as _Callable
from typing import Any, TypeVar

__all__ = ("Callable", "Property", "warn")

_F = TypeVar("_F", bound=_Callable[..., Any])

DEPRECATION_FMT: str
PENDING_DEPRECATION_FMT: str

class CDeprecationWarning(UserWarning): ...
class CPendingDeprecationWarning(PendingDeprecationWarning): ...

def warn(
    description: str | None = None,
    deprecation: str | None = None,
    removal: str | None = None,
    alternative: str | None = None,
    stacklevel: int = 2,
) -> None: ...
def Callable(
    deprecation: str | None = None,
    removal: str | None = None,
    alternative: str | None = None,
    description: str | None = None,
) -> _Callable[[_F], _F]: ...
def Property(
    deprecation: str | None = None,
    removal: str | None = None,
    alternative: str | None = None,
    description: str | None = None,
) -> _Callable[[_F], _F]: ...
