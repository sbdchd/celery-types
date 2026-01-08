from collections.abc import Callable, Mapping
from logging import Logger
from typing import Any, NamedTuple

ssl_available: bool
safequote: Callable[..., str]
logger: Logger

class urlparts(NamedTuple):
    scheme: str
    hostname: str | None
    port: int | None
    username: str | None
    password: str | None
    path: str | None
    query: Mapping[str, Any]

def _parse_url(url: str) -> urlparts: ...
def parse_url(url: str) -> dict[str, Any]: ...
def url_to_parts(url: str) -> urlparts: ...
def as_url(
    scheme: str,
    host: str | None = ...,
    port: int | None = ...,
    user: str | None = ...,
    password: str | None = ...,
    path: str | None = ...,
    query: dict[str, Any] | None = ...,
    sanitize: bool = ...,
    mask: str = ...,
) -> str: ...
def sanitize_url(url: str, mask: str = ...) -> str: ...
def maybe_sanitize_url(url: str, mask: str = ...) -> str: ...
def parse_ssl_cert_reqs(query_value: str | None) -> int | None: ...
