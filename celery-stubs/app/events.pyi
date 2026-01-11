from typing import Any

from celery.app.base import Celery

class Events:
    # Class-level configuration
    dispatcher_cls: str
    receiver_cls: str
    state_cls: str

    app: Celery | None

    def __init__(self, app: Celery | None = ...) -> None: ...
    @property
    def Dispatcher(self) -> type[Any]: ...
    @property
    def Receiver(self) -> type[Any]: ...
    @property
    def State(self) -> type[Any]: ...
    def default_dispatcher(
        self,
        hostname: str | None = None,
        enabled: bool = True,
        buffer_while_offline: bool = False,
    ) -> Any: ...
