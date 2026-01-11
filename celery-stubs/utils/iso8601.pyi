import re
from datetime import datetime

__all__ = ("parse_iso8601",)

ISO8601_REGEX: re.Pattern[str]
TIMEZONE_REGEX: re.Pattern[str]

def parse_iso8601(datestring: str) -> datetime: ...
