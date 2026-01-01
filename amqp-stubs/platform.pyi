import re

__all__ = ("LINUX_VERSION", "SOL_TCP", "KNOWN_TCP_OPTS")

LINUX_VERSION: tuple[int, int, int]
SOL_TCP: int
KNOWN_TCP_OPTS: set[str]
RE_NUM: re.Pattern[str]
