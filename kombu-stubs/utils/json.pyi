import json
from collections.abc import Callable
from typing import Any, TypeAlias, TypeVar

# These TypeVars are exported by the runtime module, so they must be public
T = TypeVar("T")  # noqa: PYI001
EncodedT = TypeVar("EncodedT")  # noqa: PYI001

textual_types: tuple[type, ...]

class JSONEncoder(json.JSONEncoder): ...

def dumps(
    s: Any,
    _dumps: Callable[..., str] = ...,
    cls: type[json.JSONEncoder] = ...,
    default_kwargs: dict[str, Any] | None = ...,
    **kwargs: Any,
) -> str: ...
def object_hook(o: dict[Any, Any]) -> Any: ...
def loads(
    s: str | bytes | bytearray | memoryview,
    _loads: Callable[[str], Any] = ...,
    decode_bytes: bool = ...,
    object_hook: Callable[[dict[Any, Any]], Any] | None = ...,
) -> Any: ...

EncoderT: TypeAlias = Callable[[Any], Any]
DecoderT: TypeAlias = Callable[[Any], Any]

_T = TypeVar("_T")
_EncodedT = TypeVar("_EncodedT")

def register_type(
    t: type[_T],
    marker: str | None,
    encoder: Callable[[_T], _EncodedT],
    decoder: Callable[[_EncodedT], _T] = ...,
) -> None: ...
