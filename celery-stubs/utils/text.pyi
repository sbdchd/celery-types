from collections.abc import Callable, Iterable
from functools import partial
from re import Pattern
from typing import Any

__all__ = (
    "abbr",
    "abbrtask",
    "dedent",
    "dedent_initial",
    "ensure_newlines",
    "ensure_sep",
    "fill_paragraphs",
    "indent",
    "join",
    "pluralize",
    "pretty",
    "simple_format",
    "str_to_list",
    "truncate",
)

def abbr(S: str, max: int, ellipsis: str = "...") -> str: ...
def abbrtask(S: str, max: int) -> str: ...
def dedent(s: str, sep: str = "\n") -> str: ...
def dedent_initial(s: str, n: int = 4) -> str: ...
def ensure_sep(sep: str, s: str, n: int = 2) -> str: ...

ensure_newlines: partial[str]

def fill_paragraphs(s: str, width: int, sep: str = "\n") -> str: ...
def indent(t: str, indent: int = 0, sep: str = "\n") -> str: ...
def join(l: Iterable[str], sep: str = "\n") -> str: ...
def pluralize(n: int, text: str, suffix: str = "s") -> str: ...
def pretty(
    value: Any, width: int = 80, nl_width: int = 80, sep: str = "\n", **kw: Any
) -> str: ...
def simple_format(
    s: str,
    keys: dict[str, str | Callable[..., Any]],
    pattern: Pattern[str] = ...,
    expand: str = ...,
) -> str: ...
def str_to_list(s: str) -> list[str]: ...
def truncate(s: str, maxlen: int = 128, suffix: str = "...") -> str: ...
