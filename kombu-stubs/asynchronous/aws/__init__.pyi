from typing import Any

from kombu.asynchronous.aws.sqs.connection import AsyncSQSConnection

def connect_sqs(
    aws_access_key_id: str | None = ...,
    aws_secret_access_key: str | None = ...,
    **kwargs: Any,
) -> AsyncSQSConnection: ...
