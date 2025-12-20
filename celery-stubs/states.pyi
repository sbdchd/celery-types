from typing import Literal

PRECEDENCE: list[str | None]

#: Hash lookup of PRECEDENCE to index
PRECEDENCE_LOOKUP: dict[str | None, int]
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

READY_STATES: frozenset[str]
UNREADY_STATES: frozenset[str]
EXCEPTION_STATES: frozenset[str]
PROPAGATE_STATES: frozenset[str]

ALL_STATES: frozenset[str]

__all__ = [
    "EXCEPTION_STATES",
    "FAILURE",
    "IGNORED",
    "PENDING",
    "PROPAGATE_STATES",
    "READY_STATES",
    "RECEIVED",
    "RETRY",
    "REVOKED",
    "STARTED",
    "SUCCESS",
    "UNREADY_STATES",
    "precedence",
    "state",
]
