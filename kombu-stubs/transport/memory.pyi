from typing import Any

from kombu.transport.virtual import Transport as VirtualTransport

class Transport(VirtualTransport):
    default_port: int | None
    driver_type: str
    driver_name: str

class Channel:
    connection: Any
    def __init__(self, connection: Any, **kwargs: Any) -> None: ...
