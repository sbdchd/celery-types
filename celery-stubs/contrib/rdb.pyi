import socket
import sys
from contextlib import AbstractContextManager
from pdb import Pdb
from types import FrameType, TracebackType
from typing import Any, Literal, TextIO

from typing_extensions import Self, override

__all__ = (
    "CELERY_RDB_HOST",
    "CELERY_RDB_PORT",
    "DEFAULT_PORT",
    "Rdb",
    "debugger",
    "set_trace",
)

DEFAULT_PORT: int = 6899

CELERY_RDB_HOST: str
CELERY_RDB_PORT: int

class Rdb(Pdb, AbstractContextManager[Rdb]):
    me: str = "Remote Debugger"

    def __init__(
        self,
        host: str = ...,
        port: int = ...,
        port_search_limit: int = 100,
        port_skew: int = 0,
        out: TextIO | Any = sys.stdout,
    ) -> None: ...
    def get_avail_port(
        self,
        host: str,
        port: int,
        search_limit: int = 100,
        skew: int = 0,
    ) -> tuple[socket.socket, int]: ...
    def say(self, m: str) -> None: ...
    @override
    def __enter__(self) -> Self: ...
    @override
    def __exit__(
        self,
        typ: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None: ...
    @override
    def do_continue(self, arg: object) -> Literal[1]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    do_cont = do_continue  # type: ignore[assignment]
    do_c = do_continue  # type: ignore[assignment]

    @override
    def do_quit(self, arg: object) -> Literal[1]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    do_exit = do_quit  # type: ignore[assignment]
    do_q = do_quit  # type: ignore[assignment]

    @override
    def set_quit(self) -> None: ...

def debugger() -> Rdb: ...
def set_trace(frame: FrameType | None = None) -> None: ...
