from logging import Logger

import click
from celery.app.base import Celery
from celery.bin.base import CeleryDaemonCommand
from typing_extensions import override

class Autoscale(click.ParamType):
    name: str
    @override
    def convert(
        self,
        value: str | None,
        param: click.Parameter | None,
        ctx: click.Context | None,
    ) -> tuple[int, int] | None: ...

class CeleryBeat(click.ParamType):
    name: str
    @override
    def convert(
        self,
        value: str | None,
        param: click.Parameter | None,
        ctx: click.Context | None,
    ) -> bool: ...

class Hostname(click.types.StringParamType):
    name: str

class WorkersPool(click.Choice):
    name: str
    def __init__(self) -> None: ...

AUTOSCALE: Autoscale
CELERY_BEAT: CeleryBeat
C_FAKEFORK: str | None
HOSTNAME: Hostname
WORKERS_POOL: WorkersPool
logger: Logger

def detach(
    path: str,
    argv: list[str],
    logfile: str | None = None,
    pidfile: str | None = None,
    uid: int | None = None,
    gid: int | None = None,
    umask: int | None = None,
    workdir: str | None = None,
    fake: bool = False,
    app: Celery | None = None,
    executable: str | None = None,
    hostname: str | None = None,
) -> int: ...

worker: CeleryDaemonCommand
