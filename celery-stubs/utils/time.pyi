from typing import Optional

class ffwd: ...

def get_exponential_backoff_interval(
    factor: int,
    retries: int,
    maximum: int,
    full_jitter: Optional[bool],
) -> int: ...
