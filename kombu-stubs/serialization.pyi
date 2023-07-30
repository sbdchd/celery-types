import pickle as pickle
from collections.abc import Callable, Container, Iterable, Mapping
from typing import Any, NamedTuple

pickle_load = pickle.load

_Encoder = Callable[[Any], str]
_Decoder = Callable[[str], Any]

class codec(NamedTuple):
    content_type: str
    content_encoding: str
    encoder: _Encoder

class SerializerRegistry:
    type_to_name: dict[str, str]
    name_to_type: dict[str, str]
    def __init__(self) -> None: ...
    def register(
        self,
        name: str,
        encoder: _Encoder | None,
        decoder: _Decoder | None,
        content_type: str,
        content_encoding: str = ...,
    ) -> None: ...
    def enable(self, name: str) -> None: ...
    def disable(self, name: str) -> None: ...
    def unregister(self, name: str) -> None: ...
    def dumps(
        self, data: Any, serializer: str | None = ...
    ) -> tuple[str, str, str]: ...
    def loads(
        self,
        data: bytes | str,
        content_type: str,
        content_encoding: str,
        accept: Container[str] | None = ...,
        force: bool = ...,
        _trusted_content: Container[str] = ...,
    ) -> Any: ...

def dumps(data: Any, serializer: str | None = ...) -> tuple[str, str, str]: ...
def loads(
    data: bytes | str,
    content_type: str,
    content_encoding: str,
    accept: Container[str] | None = ...,
    force: bool = ...,
    _trusted_content: Container[str] = ...,
) -> Any: ...
def register(
    name: str,
    encoder: _Encoder | None,
    decoder: _Decoder | None,
    content_type: str,
    content_encoding: str = ...,
) -> None: ...
def unregister(name: str) -> None: ...
def raw_encode(data: Any) -> tuple[str, str, str]: ...
def register_json() -> None: ...
def register_yaml() -> None: ...
def register_pickle() -> None: ...
def register_msgpack() -> None: ...
def enable_insecure_serializers(choices: Container[str] | None = ...) -> None: ...
def disable_insecure_serializers(allowed: Container[str] | None = ...) -> None: ...
def prepare_accept_content(
    content_types: Iterable[str] | None, name_to_type: Mapping[str, str] | None = ...
) -> set[str] | None: ...
