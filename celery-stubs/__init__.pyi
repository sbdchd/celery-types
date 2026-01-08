from types import ModuleType
from typing import Any, NamedTuple

from celery import execute as execute
from celery import local as local
from celery import messaging as messaging
from celery._state import current_app as current_app
from celery._state import current_task as current_task
from celery.app import bugreport as bugreport
from celery.app import shared_task
from celery.app.base import Celery
from celery.app.task import Task
from celery.canvas import (
    Signature,
    chain,
    chord,
    chunks,
    group,
    signature,
    xmap,
    xstarmap,
)
from celery.canvas import maybe_signature as maybe_signature
from celery.canvas import signature as subtask
from celery.utils import uuid

# These are lazy module proxies at runtime
log: ModuleType
registry: ModuleType

class version_info_t(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: str

VERSION: version_info_t
version_info: version_info_t
VERSION_BANNER: str
SERIES: str
__version__: str
__author__: str
__contact__: str
__homepage__: str
__docformat__: str

def _find_option_with_arg(
    argv: list[str], short_opts: str | None = ..., long_opts: list[str] | None = ...
) -> str | None: ...
def maybe_patch_concurrency(
    argv: list[str] | None = ...,
    short_opts: str | None = ...,
    long_opts: list[str] | None = ...,
    patches: dict[str, Any] | None = ...,
) -> None: ...

# Note: These are lazy module proxies at runtime
# log, execute, registry, messaging are module-level lazy proxies

__all__ = (
    "SERIES",
    "VERSION",
    "VERSION_BANNER",
    "Celery",
    "Signature",
    "Task",
    "__author__",
    "__contact__",
    "__docformat__",
    "__homepage__",
    "__version__",
    "_find_option_with_arg",
    "bugreport",
    "chain",
    "chord",
    "chunks",
    "current_app",
    "current_task",
    "execute",
    "group",
    "local",
    "log",
    "maybe_patch_concurrency",
    "maybe_signature",
    "messaging",
    "registry",
    "shared_task",
    "signature",
    "subtask",
    "uuid",
    "version_info",
    "version_info_t",
    "xmap",
    "xstarmap",
)
