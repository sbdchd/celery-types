from typing import Any

from kombu.asynchronous.aws.connection import AsyncAWSQueryConnection
from kombu.asynchronous.aws.sqs.queue import AsyncQueue
from typing_extensions import override
from vine import promise

__all__ = ("AsyncSQSConnection",)

class AsyncSQSConnection(AsyncAWSQueryConnection):
    message_system_attribute_names: list[str]
    message_attribute_names: list[str]

    def __init__(
        self,
        sqs_connection: Any,
        debug: int = ...,
        region: str | None = ...,
        message_system_attribute_names: list[str] | None = ...,
        message_attribute_names: list[str] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    @override
    def make_request(  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
        self,
        operation_name: str,
        params: dict[str, Any],
        queue_url: str,
        verb: str,
        callback: Any = ...,
        protocol_params: dict[str, Any] | None = ...,
    ) -> promise: ...
    def create_queue(
        self, queue_name: str, visibility_timeout: int | None = ..., callback: Any = ...
    ) -> promise: ...
    def delete_queue(
        self, queue: AsyncQueue, force_deletion: bool = ..., callback: Any = ...
    ) -> promise: ...
    def get_queue_url(self, queue: str) -> str: ...
    def get_queue_attributes(
        self, queue: AsyncQueue, attribute: str = ..., callback: Any = ...
    ) -> promise: ...
    def set_queue_attribute(
        self, queue: AsyncQueue, attribute: str, value: Any, callback: Any = ...
    ) -> promise: ...
    def receive_message(
        self,
        queue: AsyncQueue,
        queue_url: str,
        number_messages: int = ...,
        visibility_timeout: int | None = ...,
        attributes: list[str] | None = ...,
        wait_time_seconds: int | None = ...,
        callback: Any = ...,
    ) -> promise: ...
    def delete_message(
        self, queue: str | AsyncQueue, receipt_handle: str, callback: Any = ...
    ) -> promise: ...
    def delete_message_batch(
        self, queue: AsyncQueue, messages: list[Any], callback: Any = ...
    ) -> promise: ...
    def delete_message_from_handle(
        self, queue: str | AsyncQueue, receipt_handle: str, callback: Any = ...
    ) -> promise: ...
    def send_message(
        self,
        queue: AsyncQueue,
        message_content: str,
        delay_seconds: int | None = ...,
        callback: Any = ...,
    ) -> promise: ...
    def send_message_batch(
        self,
        queue: AsyncQueue,
        messages: list[tuple[str, str, int]],
        callback: Any = ...,
    ) -> promise: ...
    def change_message_visibility(
        self,
        queue: AsyncQueue,
        receipt_handle: str,
        visibility_timeout: int,
        callback: Any = ...,
    ) -> promise: ...
    def change_message_visibility_batch(
        self, queue: AsyncQueue, messages: list[tuple[Any, int]], callback: Any = ...
    ) -> promise: ...
    def get_all_queues(self, prefix: str = ..., callback: Any = ...) -> promise: ...
    def get_queue(self, queue_name: str, callback: Any = ...) -> promise: ...
    def lookup(self, queue_name: str, callback: Any = ...) -> promise: ...
    def get_dead_letter_source_queues(
        self, queue: AsyncQueue, callback: Any = ...
    ) -> promise: ...
    def add_permission(
        self,
        queue: AsyncQueue,
        label: str,
        aws_account_id: str,
        action_name: str,
        callback: Any = ...,
    ) -> promise: ...
    def remove_permission(
        self, queue: AsyncQueue, label: str, callback: Any = ...
    ) -> promise: ...
