from collections.abc import Callable, Iterable, Sequence
from types import ModuleType
from typing import Any, TypeVar

import kombu
from kombu.utils.functional import LRUCache
from kombu.utils.objects import cached_property as cached_property
from kombu.utils.uuid import uuid as uuid

__all__ = (
    "LOG_LEVELS",
    "cached_property",
    "chunks",
    "gen_task_name",
    "gen_unique_id",
    "get_cls_by_name",
    "get_full_cls_name",
    "import_from_cwd",
    "instantiate",
    "memoize",
    "nodename",
    "nodesplit",
    "noop",
    "uuid",
    "worker_direct",
)

LOG_LEVELS: dict[str, int]
nodenames: ModuleType
_T = TypeVar("_T")

def chunks(it: Iterable[_T], n: int) -> Iterable[Sequence[_T]]: ...
def gen_task_name(app: Any, name: str, module_name: str) -> str: ...
def gen_unique_id() -> str: ...
def get_cls_by_name(
    name: str,
    aliases: dict[str, str] | None = None,
    imp: Any = None,
    package: str | None = None,
    sep: str = ".",
    default: Any = None,
    **kwargs: Any,
) -> Any: ...
def get_full_cls_name(obj: Any) -> str: ...
def import_from_cwd(
    module: str, imp: Any = None, package: str | None = None
) -> Any: ...
def instantiate(name: str, *args: Any, **kwargs: Any) -> Any: ...
def memoize(
    maxsize: int | None = None,
    keyfun: Callable[..., Any] | None = None,
    Cache: type[LRUCache[Any, Any]] = ...,
) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
def nodename(name: str, hostname: str) -> str: ...
def nodesplit(name: str) -> tuple[None, str] | list[str]: ...
def noop(*args: Any, **kwargs: Any) -> None: ...
def worker_direct(hostname: str | kombu.Queue) -> kombu.Queue: ...
