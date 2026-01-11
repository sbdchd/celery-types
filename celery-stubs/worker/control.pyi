from abc import ABCMeta
from collections.abc import Callable
from typing import Any, NamedTuple

__all__ = ("Panel",)

class controller_info_t(NamedTuple):
    alias: str | None
    type: str
    visible: bool
    default_timeout: float
    help: str
    signature: str | None
    args: list[tuple[str, type]] | None  # type: ignore[valid-type]
    variadic: str | None

class Panel(metaclass=ABCMeta):
    data: dict[str, Callable[..., Any]]
    meta: dict[str, controller_info_t]

    @classmethod
    def register(
        cls,
        method: Callable[..., Any],
        name: str | None = None,
    ) -> Callable[..., Any]: ...

def control_command(
    **kwargs: Any,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
def inspect_command(
    **kwargs: Any,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
