from collections.abc import Hashable
from typing import Any

from typing_extensions import override

class EqualityDict(dict[Any, Any]): ...

class HashedSeq(list[Any]):
    __slots__ = "hashvalue"  # noqa: PLC0205  # must match runtime
    hashvalue: int

    def __init__(self, *seq: Any) -> None: ...
    @override
    def __hash__(self) -> int: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleVariableOverride]

def eqhash(o: Any) -> Hashable: ...
