from abc import ABC, abstractmethod
from collections.abc import Callable
from types import TracebackType
from typing import Any

class Thenable(ABC):
    @abstractmethod
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    def cancel(self) -> None: ...
    @classmethod
    def register(cls, other: type[Any]) -> type[Any]: ...
    @abstractmethod
    def then(
        self,
        on_success: Callable[..., Any],
        on_error: Callable[..., Any] | None = ...,
    ) -> Thenable: ...
    @abstractmethod
    def throw(
        self,
        exc: BaseException | None = ...,
        tb: TracebackType | None = ...,
        propagate: bool = ...,
    ) -> None: ...

__all__ = ["Thenable"]
