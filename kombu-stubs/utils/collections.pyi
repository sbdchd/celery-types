from collections.abc import Hashable
from typing import Any

class EqualityDict(dict[Any, Any]): ...

class HashedSeq(list[Any]):
    __slots__: str
    hashvalue: int

    def __init__(self, *seq: Any) -> None: ...
    def __hash__(self) -> int: ...  # type: ignore[override]

def eqhash(o: Any) -> Hashable: ...
