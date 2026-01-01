from collections.abc import Hashable
from typing import Any

class EqualityDict(dict[Any, Any]): ...

class HashedSeq(list[Any]):
    hashvalue: int

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __hash__(self) -> int: ...  # type: ignore[override]

def eqhash(o: Any) -> Hashable: ...
