from typing import Any

from celery.security.certificate import Certificate, CertStore
from celery.security.key import PrivateKey

__all__ = ("SecureSerializer", "register_auth")

class SecureSerializer:
    def __init__(
        self,
        key: PrivateKey | None = None,
        cert: Certificate | None = None,
        cert_store: CertStore | None = None,
        digest: str = "sha256",
        serializer: str = "json",
    ) -> None: ...
    def serialize(self, data: Any) -> bytes: ...
    def deserialize(self, data: bytes) -> Any: ...

def register_auth(
    key: str | None = None,
    key_password: str | None = None,
    cert: str | None = None,
    store: str | None = None,
    digest: str = "sha256",
    serializer: str = "json",
) -> SecureSerializer: ...
