from logging import Logger
from typing import Any

__all__ = ("setup_logging", "Logwrapped")

class Logwrapped:
    obj: Any
    logger: Logger
    ident: str

    def __init__(
        self, obj: Any, logger: Logger | None = ..., ident: str | None = ...
    ) -> None: ...
    def __getattr__(self, key: str) -> Any: ...

def setup_logging(
    loglevel: int | None = ..., loggers: list[str] | None = ...
) -> None: ...
