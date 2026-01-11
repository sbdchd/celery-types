# This module requires the optional librabbitmq package
from typing import Any

from kombu.transport.pyamqp import Channel as PyAMQPChannel
from kombu.transport.pyamqp import Connection as PyAMQPConnection
from kombu.transport.pyamqp import Message as PyAMQPMessage
from kombu.transport.pyamqp import Transport as PyAMQPTransport

class Message(PyAMQPMessage): ...
class Channel(PyAMQPChannel): ...

class Connection(PyAMQPConnection):
    Channel: type[Channel]  # pyright: ignore[reportIncompatibleVariableOverride]

class Transport(PyAMQPTransport):
    Connection: type[Connection]  # pyright: ignore[reportIncompatibleVariableOverride]
    default_port: int
    connection_errors: tuple[type[Exception], ...]
    channel_errors: tuple[type[Exception], ...]
    driver_type: str
    driver_name: str
    implements: Any
