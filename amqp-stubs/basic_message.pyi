from typing import Any

__all__ = ("Message",)

class Message:
    CLASS_ID: int
    PROPERTIES: list[tuple[str, str]]

    body: bytes | str
    body_size: int
    body_received: int
    channel: Any
    delivery_info: dict[str, Any]
    properties: dict[str, Any]
    ready: bool
    frame_method: tuple[int, int] | None
    frame_args: bytes | None

    content_type: str | None
    content_encoding: str | None
    application_headers: dict[str, Any] | None
    delivery_mode: int | None
    priority: int | None
    correlation_id: str | None
    reply_to: str | None
    expiration: str | None
    message_id: str | None
    timestamp: int | None
    type: str | None
    user_id: str | None
    app_id: str | None
    cluster_id: str | None

    def __init__(
        self,
        body: bytes | str = ...,
        children: Any | None = ...,
        channel: Any | None = ...,
        **properties: Any,
    ) -> None: ...
    @property
    def headers(self) -> dict[str, Any] | None: ...
    @property
    def delivery_tag(self) -> int | None: ...
