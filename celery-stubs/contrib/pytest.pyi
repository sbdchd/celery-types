from collections.abc import Generator, Mapping, Sequence
from contextlib import contextmanager
from typing import Any

import pytest
from celery import Celery, Task
from celery.worker import WorkController

NO_WORKER: str | None

def pytest_configure(config: pytest.Config) -> None: ...
@contextmanager
def _create_app(
    enable_logging: bool = False,
    use_trap: bool = False,
    parameters: Mapping[str, Any] | None = None,
    **config: Any,
) -> Generator[Celery[Any], None, None]: ...
@pytest.fixture(scope="session")
def use_celery_app_trap() -> bool: ...
@pytest.fixture(scope="session")
def celery_session_app(
    request: Any,
    celery_config: Mapping[str, Any],
    celery_parameters: Mapping[str, Any],
    celery_enable_logging: bool,
    use_celery_app_trap: bool,
) -> Generator[Celery[Any]]: ...
@pytest.fixture(scope="session")
def celery_session_worker(
    request: pytest.FixtureRequest,
    celery_session_app: Celery[Any],
    celery_includes: Sequence[str],
    celery_class_tasks: str,
    celery_worker_pool: str,
    celery_worker_parameters: Mapping[str, Any],
) -> Generator[WorkController, None, None]: ...
@pytest.fixture(scope="session")
def celery_enable_logging() -> bool: ...
@pytest.fixture(scope="session")
def celery_includes() -> Sequence[str]: ...
@pytest.fixture(scope="session")
def celery_worker_pool() -> str | Any: ...
@pytest.fixture(scope="session")
def celery_config() -> Mapping[str, Any]: ...
@pytest.fixture(scope="session")
def celery_parameters() -> Mapping[str, Any]: ...
@pytest.fixture(scope="session")
def celery_worker_parameters() -> Mapping[str, Any]: ...
@pytest.fixture
def celery_app(
    request: pytest.FixtureRequest,
    celery_config: Mapping[str, Any],
    celery_parameters: Mapping[str, Any],
    celery_enable_logging: bool,
    use_celery_app_trap: bool,
) -> Generator[Celery[Any], None, None]: ...
@pytest.fixture(scope="session")
def celery_class_tasks() -> Sequence[type[Task[Any, Any]]]: ...
@pytest.fixture
def celery_worker(
    request: pytest.FixtureRequest,
    celery_app: Celery[Any],
    celery_includes: Sequence[str],
    celery_worker_pool: str,
    celery_worker_parameters: Mapping[str, Any],
) -> Generator[WorkController, None, None]: ...
@pytest.fixture
def depends_on_current_app(celery_app: Celery[Any]) -> None: ...
