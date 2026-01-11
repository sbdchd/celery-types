from celery.loaders.base import BaseLoader

__all__ = ("get_loader_cls",)

def get_loader_cls(loader: str) -> type[BaseLoader]: ...
