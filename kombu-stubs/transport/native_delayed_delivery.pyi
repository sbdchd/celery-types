from logging import Logger

from kombu.connection import Connection
from kombu.entity import Queue

logger: Logger
MAX_NUMBER_OF_BITS_TO_USE: int
MAX_LEVEL: int
CELERY_DELAYED_DELIVERY_EXCHANGE: str

def level_name(level: int) -> str: ...
def declare_native_delayed_delivery_exchanges_and_queues(
    connection: Connection, queue_type: str
) -> None: ...
def bind_queue_to_native_delayed_delivery_exchange(
    connection: Connection, queue: Queue
) -> None: ...
def calculate_routing_key(countdown: int, routing_key: str) -> str: ...
