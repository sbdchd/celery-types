from typing import Any

import kombu
from celery.backends.asynchronous import BaseResultConsumer
from celery.backends.base import Backend
from kombu.utils.objects import cached_property
from typing_extensions import override

__all__ = ("BacklogLimitExceeded", "RPCBackend")

class BacklogLimitExceeded(Exception): ...

class RPCBackend(Backend):
    BacklogLimitExceeded: type[BacklogLimitExceeded]
    Consumer: type[kombu.Consumer]
    Exchange: type[kombu.Exchange]
    Producer: type[kombu.Producer]
    Queue: type[kombu.Queue]
    ResultConsumer: type[BaseResultConsumer]

    oid: cached_property[str]

    @property
    def binding(self) -> kombu.Queue: ...
    def __init__(
        self,
        app: Any,
        connection: Any | None = None,
        exchange: str | None = None,
        exchange_type: str | None = None,
        persistent: bool | None = None,
        serializer: str | None = None,
        auto_delete: bool = True,
        **kwargs: Any,
    ) -> None: ...
    def destination_for(self, task_id: str, request: Any) -> tuple[str, str]: ...
    def on_reply_declare(self, task_id: str) -> Any: ...
    def on_result_fulfilled(self, result: Any) -> None: ...
    def on_out_of_band_result(self, task_id: str, message: Any) -> None: ...
    @override
    def get_task_meta(  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
        self, task_id: str, backlog_limit: int = 1000
    ) -> dict[str, Any]: ...
    def poll(
        self, task_id: str, backlog_limit: int = 1000
    ) -> dict[str, Any] | None: ...
    @override
    def reload_group_result(self, task_id: str) -> Any: ...  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
    def revive(self, channel: Any) -> None: ...
