from typing import Any, NamedTuple
from urllib.parse import ParseResult

class urlparts(NamedTuple):
    scheme: str
    hostname: str | None
    port: int | None
    username: str | None
    password: str | None
    path: str
    query: dict[str, Any]

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
def safequote(
    string: str, *, safe: str = ..., encoding: str | None = ..., errors: str | None = ...
) -> str: ...
def parse_ssl_cert_reqs(query_value: str | None) -> int | None: ...
