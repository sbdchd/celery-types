from builtins import type as _type
from collections.abc import Callable
from typing import Any

__all__ = ("NAMESPACES", "Option", "find", "flatten")

class Option:
    default: Any
    type: str | None
    deprecate_by: str | None
    remove_by: str | None
    alt: tuple[str, ...] | None
    old: set[str]
    typemap: dict[str, _type]

    def __init__(
        self,
        default: Any = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def to_python(self, value: Any) -> Any: ...

DEFAULTS: dict[str, dict[str, Any]]
NAMESPACES: dict[str, dict[str, Option]]
SETTING_KEYS: set[str]

def find(name: str, namespace: str = "celery") -> tuple[str, Option] | None: ...
def flatten(
    d: dict[str, dict[str, Any]], root: str = "", keyfilter: Callable[..., Any] = ...
) -> dict[str, Any]: ...
def strtobool(
    term: str | bool | int | None, table: dict[str, bool] | None = None
) -> bool: ...
