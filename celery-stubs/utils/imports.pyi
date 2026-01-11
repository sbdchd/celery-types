from collections.abc import Callable, Iterator
from contextlib import contextmanager
from importlib.metadata import EntryPoints
from types import ModuleType
from typing import Any

__all__ = (
    "NotAPackage",
    "cwd_in_path",
    "find_module",
    "gen_task_name",
    "import_from_cwd",
    "instantiate",
    "module_file",
    "qualname",
    "reload_from_cwd",
    "symbol_by_name",
)

class NotAPackage(Exception): ...

@contextmanager
def cwd_in_path() -> Iterator[None]: ...
def entry_points(**params: Any) -> EntryPoints: ...
def find_module(
    module: str, path: list[str] | None = None, imp: Any | None = None
) -> ModuleType | None: ...
def gen_task_name(app: Any, name: str, module_name: str) -> str: ...
def import_from_cwd(
    module: str,
    imp: Callable[[str], ModuleType] | None = None,
    package: str | None = None,
) -> ModuleType: ...
def instantiate(name: str, *args: Any, **kwargs: Any) -> Any: ...
def load_extension_class_names(namespace: str) -> list[str]: ...
def load_extension_classes(namespace: str) -> list[type[Any]]: ...
def module_file(module: ModuleType) -> str | None: ...
def qualname(obj: Any) -> str: ...
def reload_from_cwd(
    module: ModuleType, reloader: Callable[[ModuleType], ModuleType] | None = None
) -> ModuleType: ...
def symbol_by_name(
    name: str,
    aliases: dict[str, str] | None = None,
    imp: Callable[[str], ModuleType] | None = None,
    package: str | None = None,
    sep: str = ".",
    default: Any = None,
    **kwargs: Any,
) -> Any: ...
