from typing import Any

from celery.loaders.base import BaseLoader
from typing_extensions import override

__all__ = ("DEFAULT_CONFIG_MODULE", "Loader")

DEFAULT_CONFIG_MODULE: str

class Loader(BaseLoader):
    @override
    def read_configuration(  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
        self,
        fail_silently: bool = True,  # type: ignore[override]
    ) -> dict[str, Any]: ...
    def setup_settings(self, settingsdict: dict[str, Any]) -> dict[str, Any]: ...
