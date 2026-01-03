from kombu.asynchronous.http.base import Headers as Headers
from kombu.asynchronous.http.base import Request as Request
from kombu.asynchronous.http.base import Response as Response
from kombu.asynchronous.http.curl import CurlClient
from kombu.asynchronous.hub import Hub

__all__ = ("Client", "Headers", "Request", "Response")

def Client(hub: Hub | None = ..., **kwargs: int) -> CurlClient: ...
def get_client(hub: Hub | None = ..., **kwargs: int) -> CurlClient: ...
