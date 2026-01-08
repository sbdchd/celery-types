from abc import ABC, ABCMeta, abstractmethod
from typing import Any

__all__ = ("CallableSignature", "CallableTask")

class CallableTask(metaclass=ABCMeta):
    __required_attributes__: frozenset[str]

    @abstractmethod
    def apply(self, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    def apply_async(self, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    def delay(self, *args: Any, **kwargs: Any) -> Any: ...
    @classmethod
    def register(cls, other: type) -> type: ...

class CallableSignature(CallableTask, ABC):
    __required_attributes__: frozenset[str]

    @property
    @abstractmethod
    def app(self) -> Any: ...
    @property
    @abstractmethod
    def args(self) -> tuple[Any, ...]: ...
    @property
    @abstractmethod
    def chord_size(self) -> int | None: ...
    @property
    @abstractmethod
    def id(self) -> str | None: ...
    @property
    @abstractmethod
    def immutable(self) -> bool: ...
    @property
    @abstractmethod
    def kwargs(self) -> dict[str, Any]: ...
    @property
    @abstractmethod
    def name(self) -> str | None: ...
    @property
    @abstractmethod
    def options(self) -> dict[str, Any]: ...
    @property
    @abstractmethod
    def subtask_type(self) -> str | None: ...
    @property
    @abstractmethod
    def task(self) -> str | None: ...
    @property
    @abstractmethod
    def type(self) -> Any: ...
    @abstractmethod
    def __invert__(self) -> Any: ...
    @abstractmethod
    def __or__(self, other: Any) -> Any: ...
    @abstractmethod
    def clone(
        self, args: tuple[Any, ...] | None = None, kwargs: dict[str, Any] | None = None
    ) -> Any: ...
    @abstractmethod
    def freeze(
        self,
        id: str | None = None,
        group_id: str | None = None,
        chord: Any | None = None,
        root_id: str | None = None,
        group_index: int | None = None,
    ) -> Any: ...
    @abstractmethod
    def link(self, callback: Any) -> Any: ...
    @abstractmethod
    def link_error(self, errback: Any) -> Any: ...
    @abstractmethod
    def set(self, immutable: bool | None = None, **options: Any) -> Any: ...
