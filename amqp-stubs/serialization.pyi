from decimal import Decimal as Decimal
from typing import Any

from amqp.exceptions import FrameSyntaxError as FrameSyntaxError
from amqp.spec import Basic as Basic

ILLEGAL_TABLE_TYPE: str
ILLEGAL_TABLE_TYPE_WITH_KEY: str
ILLEGAL_TABLE_TYPE_WITH_VALUE: str
PROPERTY_CLASSES: dict[int, type[Any]]

class GenericContent:
    CLASS_ID: int | None
    PROPERTIES: list[tuple[str, str]]

    body_size: int
    body_received: int
    properties: dict[str, Any]
    ready: bool
    frame_method: tuple[int, int] | None
    frame_args: bytes | None

    def __init__(
        self,
        frame_method: tuple[int, int] | None = ...,
        frame_args: bytes | None = ...,
        **props: Any,
    ) -> None: ...
    def inbound_header(self, buf: bytes, offset: int = ...) -> None: ...
    def inbound_body(self, buf: bytes) -> None: ...

def dumps(format: str, values: tuple[Any, ...]) -> bytes: ...
def loads(format: str, buf: bytes, offset: int) -> tuple[Any, ...]: ...
def decode_properties_basic(buf: bytes, offset: int) -> tuple[dict[str, Any], int]: ...
def pstr_t(s: str) -> bytes: ...
def str_to_bytes(s: str) -> bytes: ...
