from collections.abc import Callable, Iterable

__all__ = (
    "compress",
    "decompress",
    "encoders",
    "get_decoder",
    "get_encoder",
    "register",
)

def register(
    encoder: Callable[[bytes], bytes],
    decoder: Callable[[bytes], bytes],
    content_type: str,
    aliases: Iterable[str] | None = ...,
) -> None: ...
def encoders() -> list[str]: ...
def get_encoder(t: str) -> Callable[[bytes], bytes]: ...
def get_decoder(t: str) -> Callable[[bytes], bytes]: ...
def compress(body: bytes | str, content_type: str) -> tuple[bytes, str]: ...
def decompress(body: bytes, content_type: str) -> bytes: ...
