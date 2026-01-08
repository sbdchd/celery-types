from abc import ABCMeta
from collections import UserList
from collections.abc import Callable, Sequence
from signal import Signals
from typing import Any, TypeAlias

from typing_extensions import override

__all__ = ("Cluster", "Node")

class Cluster(UserList[Node], metaclass=ABCMeta):
    name: str
    nodes: list[Node]

    def __init__(
        self,
        nodes: list[str],
        cmd: str | None = None,
        env: dict[str, str] | None = None,
        on_stopping_preamble: Callable[..., Any] | None = None,
        on_send_signal: Callable[..., Any] | None = None,
        on_still_waiting_for: Callable[..., Any] | None = None,
        on_still_waiting_progress: Callable[..., Any] | None = None,
        on_still_waiting_end: Callable[..., Any] | None = None,
        on_node_start: Callable[..., Any] | None = None,
        on_node_restart: Callable[..., Any] | None = None,
        on_node_shutdown_ok: Callable[..., Any] | None = None,
        on_node_status: Callable[..., Any] | None = None,
        on_node_signal: Callable[..., Any] | None = None,
        on_node_signal_dead: Callable[..., Any] | None = None,
        on_node_down: Callable[..., Any] | None = None,
        on_child_spawn: Callable[..., Any] | None = None,
        on_child_signalled: Callable[..., Any] | None = None,
        on_child_failure: Callable[..., Any] | None = None,
    ) -> None: ...
    def start(self) -> None: ...
    def stop(
        self,
        retry: int | None = None,
        callback: Callable[..., Any] | None = None,
        sig: Signals = ...,
    ) -> None: ...
    def stopwait(
        self,
        retry: int = 2,
        callback: Callable[..., Any] | None = None,
        sig: Signals = ...,
    ) -> None: ...
    def restart(self, sig: Signals = ...) -> None: ...
    def kill(self) -> None: ...
    @property
    @override
    def data(self) -> list[Node]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleVariableOverride]  # override UserList.data
    def find(self, name: str) -> Node | None: ...
    def getpids(self, on_down: Callable[..., Any] | None = None) -> dict[str, int]: ...
    def send_all(self, sig: Signals) -> None: ...
    def shutdown_nodes(
        self,
        nodes: Sequence[Node],
        sig: Signals = ...,
        retry: int | None = None,
    ) -> None: ...
    def start_node(self, node: Node) -> int: ...

class Node:
    name: str
    cmd: str | None
    append: str | None
    options: dict[str, Any]
    extra_args: Sequence[str]
    pid: int | None

    def __init__(
        self,
        name: str,
        cmd: str | None = None,
        append: str | None = None,
        options: dict[str, Any] | None = None,
        extra_args: Sequence[str] | None = None,
    ) -> None: ...
    def alive(self) -> bool: ...
    def send(
        self, sig: int, on_error: Callable[[Exception], Any] | None = None
    ) -> bool: ...
    def start(self, env: dict[str, str] | None = None, **kwargs: Any) -> int: ...
    @classmethod
    def from_kwargs(cls, name: str, **kwargs: Any) -> Node: ...
    def getopt(self, option: str) -> str | None: ...
    def handle_process_exit(
        self,
        retcode: int,
        on_signalled: Callable[[int], Any] | None = None,
        on_failure: Callable[[int], Any] | None = None,
    ) -> None: ...
    def prepare_argv(self, argv: list[str], path: str) -> list[str]: ...
    @property
    def argv_with_executable(self) -> list[str]: ...
    @property
    def executable(self) -> str: ...
    @property
    def logfile(self) -> str | None: ...
    @property
    def pidfile(self) -> str | None: ...

# Type alias for use inside MultiParser where the class attribute shadows the module-level class
_Node: TypeAlias = Node

class MultiParser:
    Node: type  # type[Node] at runtime
    cmd: str
    append: str
    prefix: str
    suffix: str
    range_prefix: str

    def __init__(
        self,
        cmd: str = "celery worker",
        append: str = "",
        prefix: str = "",
        suffix: str = "",
        range_prefix: str = "celery",
    ) -> None: ...
    def parse(self, p: list[str]) -> tuple[list[_Node], list[str]]: ...

class NamespacedOptionParser:
    args: list[str]
    options: dict[str, dict[str, Any]]
    values: list[str]
    passthrough: str

    def __init__(self, args: list[str]) -> None: ...
    def add_option(
        self, name: str, value: str, short: bool = False, ns: str | None = None
    ) -> None: ...
    def optmerge(
        self, ns: str, defaults: dict[str, Any] | None = None
    ) -> dict[str, Any]: ...
    def parse(self) -> tuple[dict[str, dict[str, Any]], list[str]]: ...
    def process_long_opt(self, arg: str, value: str | None = None) -> None: ...
    def process_short_opt(self, arg: str, value: str | None = None) -> None: ...
