from collections.abc import Callable, Iterator
from contextlib import contextmanager
from typing import Any, TextIO

__all__ = (
    "blockdetection",
    "cry",
    "humanbytes",
    "mem_rss",
    "memdump",
    "ps",
    "sample",
    "sample_mem",
)

UNITS: tuple[tuple[float, str], ...]

def blockdetection(timeout: float) -> Any: ...
def cry(
    out: TextIO | Callable[[str], None] | None = None,
    sepchr: str = "=",
    seplen: int = 49,
) -> str: ...
def hfloat(f: float, p: int = 5) -> str: ...
def humanbytes(s: float) -> str: ...
def mem_rss() -> float: ...
def memdump(samples: int = 10, file: TextIO | None = None) -> None: ...
def ps() -> Any: ...
def sample(x: int, n: int, k: int = 0) -> list[Any]: ...
@contextmanager
def sample_mem() -> Iterator[Callable[[], str]]: ...
