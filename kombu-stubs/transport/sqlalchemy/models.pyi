from typing import Any

from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.schema import Column, MetaData

class_registry: dict[str, Any]
metadata: MetaData
ModelBase: type[Any]

class Queue:
    __table_args__: dict[str, Any]
    __tablename__: str

    id: Column[int]
    name: Column[str]
    messages: RelationshipProperty[Any]

    def __init__(self, name: str) -> None: ...

class Message:
    __table_args__: tuple[Any, ...]
    __tablename__: str
    __mapper_args__: dict[str, Any]

    id: Column[int]
    visible: Column[bool]
    sent_at: Column[Any]
    payload: Column[str]
    version: Column[int]
    queue_id: Column[int]
    queue: Queue

    def __init__(self, payload: str, queue: Queue) -> None: ...
