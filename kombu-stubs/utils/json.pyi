import json
from typing import Any, Callable, TypeVar

textual_types: tuple[Any]

class JSONEncoder(json.JSONEncoder): ...  # type: ignore

def dumps(
    s: str,
    _dumps: Callable[..., str],
    cls: JSONEncoder,
    default_kwargs: dict[str, Any],
    **kwargs: Any,
) -> str: ...
def object_hook(o: dict[Any, Any]) -> None: ...
def loads(
    s: str,
    _loads: Callable[[str], Any],
    decode_bytes: bool,
    object_hook: Callable[[dict[Any, Any]], None],
) -> Any: ...

DecoderT = EncoderT = Callable[[Any], Any]
T = TypeVar("T")
EncodedT = TypeVar("EncodedT")

def register_type(
    t: type[T],
    marker: str | None,
    encoder: Callable[[T], EncodedT],
    decoder: Callable[[EncodedT], T],
) -> None: ...
