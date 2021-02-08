from typing import Any, MutableMapping

class AttributeDictMixin:
    def __getattr__(self, k: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> None: ...

class ChainMap(MutableMapping[str, Any]): ...  # type: ignore [misc]
class ConfigurationView(ChainMap, AttributeDictMixin): ...  # type: ignore [misc]
