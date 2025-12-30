import socket
from typing import Any

from kombu.entity import Exchange, Queue
from kombu.utils.functional import memoize

#: Exchange for worker direct queues.
WORKER_DIRECT_EXCHANGE = Exchange("C.dq2")

#: Format for worker direct queue names.
WORKER_DIRECT_QUEUE_FORMAT: str = "{hostname}.dq2"

#: Separator for worker node name and hostname.
NODENAME_SEP: str = "@"

NODENAME_DEFAULT: str = "celery"

gethostname = memoize(1, Cache=dict)(socket.gethostname)

__all__ = (
    "anon_nodename",
    "default_nodename",
    "gethostname",
    "host_format",
    "node_format",
    "nodename",
    "nodesplit",
    "worker_direct",
)

def worker_direct(hostname: str | Queue) -> Queue: ...
def nodename(name: str, hostname: str) -> str: ...
def anon_nodename(hostname: str | None = None, prefix: str = "gen") -> str: ...
def nodesplit(name: str) -> tuple[None, str] | list[str]: ...
def default_nodename(hostname: str) -> str: ...
def node_format(s: str, name: str, **extra: dict[str, Any]) -> str: ...
def host_format(
    s: str,
    host: str | None = None,
    name: str | None = None,
    **extra: dict[str, Any],
) -> str: ...
