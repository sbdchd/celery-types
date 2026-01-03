import re

__all__ = ("KNOWN_TCP_OPTS", "LINUX_VERSION", "SOL_TCP")

LINUX_VERSION: tuple[int, int, int]
SOL_TCP: int
KNOWN_TCP_OPTS: set[str]
RE_NUM: re.Pattern[str]
