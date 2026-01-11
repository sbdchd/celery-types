from typing import Any

from celery.backends.base import Backend

__all__ = ("by_name", "by_url")

BACKEND_ALIASES: dict[str, str]
UNKNOWN_BACKEND: str

def by_name(
    backend: str | None = None,
    loader: Any | None = None,
    extension_namespace: str = "celery.result_backends",
) -> type[Backend]: ...
def by_url(backend: str | None = None, loader: Any | None = None) -> type[Backend]: ...
