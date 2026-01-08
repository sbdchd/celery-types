from typing import Any, NamedTuple

class basic_return_t(NamedTuple):
    reply_code: int
    reply_text: str
    exchange: str
    routing_key: str
    message: Any

class queue_declare_ok_t(NamedTuple):
    queue: str
    message_count: int
    consumer_count: int
