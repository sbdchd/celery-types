from typing import Any

__all__ = ("asynloop", "synloop")

def asynloop(
    obj: Any,
    connection: Any,
    consumer: Any,
    blueprint: Any,
    hub: Any,
    qos: Any,
    heartbeat: float,
    clock: Any,
    hbrate: float = 2.0,
) -> None: ...
def synloop(
    obj: Any,
    connection: Any,
    consumer: Any,
    blueprint: Any,
    hub: Any,
    qos: Any,
    heartbeat: float,
    clock: Any,
    hbrate: float = 2.0,
    **kwargs: Any,
) -> None: ...
