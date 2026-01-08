import pickle
from collections.abc import Callable
from typing import Any

__all__ = [
    "DupFd",
    "ForkingPickler",
    "dump",
    "recv_handle",
    "recvfds",
    "register",
    "send_handle",
    "sendfds",
]

ForkingPickler: type[pickle.Pickler]

def dump(obj: Any, file: Any, protocol: int | None = ...) -> None: ...
def register(type: type, reduce: Callable[[Any], Any]) -> None: ...
def DupFd(fd: int) -> Any: ...
def sendfds(sock: Any, fds: list[int]) -> None: ...
def recvfds(sock: Any, size: int) -> list[int]: ...
def send_handle(conn: Any, handle: int, destination_pid: int) -> None: ...
def recv_handle(conn: Any) -> int: ...
