from collections.abc import Callable
from typing import TypeAlias

MatcherFunction: TypeAlias = Callable[[str, str], bool]

class MatcherNotInstalled(Exception): ...

class MatcherRegistry:
    MatcherNotInstalled: type[MatcherNotInstalled]
    matcher_pattern_first: list[str]
    _matchers: dict[str, MatcherFunction]
    _default_matcher: MatcherFunction | None

    def __init__(self) -> None: ...
    def register(self, name: str, matcher: MatcherFunction) -> None: ...
    def unregister(self, name: str) -> None: ...
    def _set_default_matcher(self, name: str) -> None: ...
    def match(
        self,
        data: bytes,
        pattern: bytes,
        matcher: str | None = ...,
        matcher_kwargs: dict[str, str] | None = ...,
    ) -> bool: ...

registry: MatcherRegistry

def match(
    data: bytes,
    pattern: bytes,
    matcher: str | None = ...,
    matcher_kwargs: dict[str, str] | None = ...,
) -> bool: ...
def register(name: str, matcher: MatcherFunction) -> None: ...
def unregister(name: str) -> None: ...
def register_glob() -> None: ...
def register_pcre() -> None: ...
