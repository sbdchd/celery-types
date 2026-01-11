from celery.app.base import Celery

__all__ = ("setup_security",)

def setup_security(
    allowed_serializers: list[str] | None = None,
    key: str | None = None,
    key_password: str | None = None,
    cert: str | None = None,
    store: str | None = None,
    digest: str | None = None,
    serializer: str = "json",
    app: Celery | None = None,
) -> None: ...
def disable_untrusted_serializers(
    whitelist: list[str] | None = None,
) -> None: ...
