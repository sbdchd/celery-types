from typing import Any

from typing_extensions import override

class SASL:
    @property
    def mechanism(self) -> bytes | None: ...
    def start(self, connection: Any) -> bytes | None: ...

class PLAIN(SASL):
    mechanism: bytes  # pyright: ignore[reportIncompatibleMethodOverride]
    username: str
    password: str

    def __init__(self, username: str, password: str) -> None: ...
    @override
    def start(self, connection: Any) -> bytes: ...

class AMQPLAIN(SASL):
    mechanism: bytes  # pyright: ignore[reportIncompatibleMethodOverride]
    username: str
    password: str

    def __init__(self, username: str, password: str) -> None: ...
    @override
    def start(self, connection: Any) -> bytes: ...

class EXTERNAL(SASL):
    mechanism: bytes  # pyright: ignore[reportIncompatibleMethodOverride]

    @override
    def start(self, connection: Any) -> bytes: ...

class RAW(SASL):
    mechanism: bytes | None  # pyright: ignore[reportIncompatibleMethodOverride]
    response: bytes | None

    def __init__(self, mechanism: bytes | None, response: bytes | None) -> None: ...
    @override
    def start(self, connection: Any) -> bytes | None: ...

class GSSAPI(SASL):
    mechanism: bytes | None  # pyright: ignore[reportIncompatibleMethodOverride]
    client_name: str | None
    service: bytes
    rdns: bool
    fail_soft: bool

    def __init__(
        self,
        client_name: str | None = ...,
        service: bytes = ...,
        rdns: bool = ...,
        fail_soft: bool = ...,
    ) -> None: ...
    @override
    def start(self) -> bytes | None: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
