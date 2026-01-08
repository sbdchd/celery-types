from collections.abc import Callable, MutableMapping
from datetime import datetime
from typing import Any

import click
from celery.app.base import Celery
from celery.utils.dispatch.signal import Signal
from kombu.utils.objects import cached_property

class CeleryOption(click.Option): ...

class CeleryCommand(click.Command):
    app: Celery | None
    def __init__(
        self,
        name: str | None,
        context_settings: MutableMapping[str, Any] | None = None,
        callback: Callable[..., Any] | None = None,
        params: list[click.Parameter] | None = None,
        help: str | None = None,
        epilog: str | None = None,
        short_help: str | None = None,
        options_metavar: str | None = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
    ) -> None: ...

class CeleryDaemonCommand(CeleryCommand): ...

class DaemonOption(click.Option):
    def daemon_setting(
        self, ctx: click.Context, opt: CeleryOption, value: Any
    ) -> Any: ...

class CLIContext:
    app: Celery
    OK: cached_property[str]
    ERROR: cached_property[str]

    def __init__(
        self,
        app: Celery,
        no_color: bool,
        workdir: str | None,
        quiet: bool = False,
    ) -> None: ...
    def echo(self, message: str | None = None, **kwargs: Any) -> None: ...
    def error(self, message: str | None = None, **kwargs: Any) -> None: ...
    def pretty(self, n: Any) -> str: ...
    def pretty_dict_ok_error(self, n: dict[str, Any]) -> str: ...
    def pretty_list(self, n: list[Any]) -> str: ...
    def say_chat(
        self, direction: str, title: str, body: str = "", show_body: bool = False
    ) -> None: ...
    def secho(self, message: str | None = None, **kwargs: Any) -> None: ...
    def style(self, message: str | None = None, **kwargs: Any) -> str: ...

class CommaSeparatedList(click.ParamType): ...
class LogLevel(click.ParamType): ...
class ISO8601DateTime(click.ParamType): ...
class ISO8601DateTimeOrFloat(click.ParamType): ...
class JsonArray(click.ParamType): ...
class JsonObject(click.ParamType): ...

COMMA_SEPARATED_LIST: CommaSeparatedList
LOG_LEVEL: LogLevel
ISO8601: ISO8601DateTime
ISO8601_OR_FLOAT: ISO8601DateTimeOrFloat
JSON_ARRAY: JsonArray
JSON_OBJECT: JsonObject
FORMATTER: Any  # pygments Terminal256Formatter
LEXER: Any  # pygments PythonLexer

def handle_preload_options(f: Callable[..., Any]) -> Callable[..., Any]: ...
def maybe_iso8601(dt: datetime | str | None) -> datetime | None: ...
def get_current_app() -> Celery: ...
def mlevel(level: str | int) -> int: ...
def pformat(
    object: Any,
    indent: int = 1,
    width: int = 80,
    depth: int | None = None,
    *,
    compact: bool = False,
    sort_dicts: bool = True,
    underscore_numbers: bool = False,
) -> str: ...

user_preload_options: Signal
