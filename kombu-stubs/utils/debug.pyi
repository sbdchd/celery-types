from logging import Logger
from typing import Any

__all__ = ("Logwrapped", "setup_logging")

class Logwrapped:
    instance: Any
    logger: Logger
    ident: str | None

    def __init__(
        self, instance: Any, logger: Logger | None = ..., ident: str | None = ...
    ) -> None: ...
    def __getattr__(self, key: str) -> Any: ...

def setup_logging(
    loglevel: int | None = ..., loggers: list[str] | None = ...
) -> None: ...
