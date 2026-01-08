from typing import Any

__all__ = ("Beat",)

from celery.app.base import Celery
from celery.beat import Service as BeatService

class Beat:
    Service: type[BeatService]
    app: Celery | None

    def __init__(
        self,
        max_interval: int | None = None,
        app: Celery | None = None,
        socket_timeout: int = 30,
        pidfile: str | None = None,
        no_color: bool | None = None,
        loglevel: str = "WARN",
        logfile: str | None = None,
        schedule: str | None = None,
        scheduler: str | None = None,
        scheduler_cls: str | None = None,
        redirect_stdouts: bool | None = None,
        redirect_stdouts_level: str | None = None,
        quiet: bool = False,
        **kwargs: Any,
    ) -> None: ...
    def banner(self, service: BeatService) -> str: ...
    def init_loader(self) -> None: ...
    def install_sync_handler(self, service: BeatService) -> None: ...
    def run(self) -> None: ...
    def set_process_title(self) -> None: ...
    def setup_logging(self, colorize: bool | None = None) -> None: ...
    def start_scheduler(self) -> BeatService: ...
    def startup_info(self, service: BeatService) -> str: ...
