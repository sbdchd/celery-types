from typing import IO, Any

import click
from celery.bin.base import CeleryCommand

UNABLE_TO_LOAD_APP_APP_MISSING: str
UNABLE_TO_LOAD_APP_ERROR_OCCURRED: str
UNABLE_TO_LOAD_APP_MODULE_NOT_FOUND: str
WRONG_APP_OPTION_USAGE_MESSAGE: str

def main() -> int: ...
def previous_show_implementation(self: Any, file: IO[str] | None = None) -> None: ...

celery: click.Group
report: CeleryCommand
