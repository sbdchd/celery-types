from typing import Dict, FrozenSet, List, Optional

from typing_extensions import Literal

PRECEDENCE: List[Optional[str]]

#: Hash lookup of PRECEDENCE to index
PRECEDENCE_LOOKUP: Dict[Optional[str], int]
NONE_PRECEDENCE: int

def precedence(state: object) -> int: ...

class state(str):
    def __gt__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...

PENDING: Literal["PENDING"]
RECEIVED: Literal["RECEIVED"]
STARTED: Literal["STARTED"]
SUCCESS: Literal["SUCCESS"]
FAILURE: Literal["FAILURE"]
REVOKED: Literal["REVOKED"]
REJECTED: Literal["REJECTED"]
RETRY: Literal["RETRY"]
IGNORED: Literal["IGNORED"]

READY_STATES: FrozenSet[str]
UNREADY_STATES: FrozenSet[str]
EXCEPTION_STATES: FrozenSet[str]
PROPAGATE_STATES: FrozenSet[str]

ALL_STATES: FrozenSet[str]

__all__ = [
    "PENDING",
    "RECEIVED",
    "STARTED",
    "SUCCESS",
    "FAILURE",
    "REVOKED",
    "RETRY",
    "IGNORED",
    "READY_STATES",
    "UNREADY_STATES",
    "EXCEPTION_STATES",
    "PROPAGATE_STATES",
    "precedence",
    "state",
]
