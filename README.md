# celery-types 
[![PyPI](https://img.shields.io/pypi/v/celery-types.svg)](https://pypi.org/project/celery-types/)
[![Downloads](https://static.pepy.tech/personalized-badge/celery-types?period=month&units=international_system&left_color=black&right_color=orange&left_text=PyPI%20downloads%20per%20month)](https://pepy.tech/project/celery-types)
![PyPI - Types](https://img.shields.io/pypi/types/celery-types)
[![image](https://img.shields.io/pypi/pyversions/celery-types.svg)](https://pypi.python.org/pypi/celery-types)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


Type stubs for celery related projects:

- [`celery`](https://github.com/celery/celery)
- [`django-celery-results`](https://github.com/celery/django-celery-results)
- [`amqp`](http://github.com/celery/py-amqp)
- [`kombu`](https://github.com/celery/kombu)
- [`billiard`](https://github.com/celery/billiard)
- [`vine`](https://github.com/celery/vine)
- [`ephem`](https://github.com/brandon-rhodes/pyephem)

## install

```shell
pip install celery-types
```

You'll also need to monkey patch the classes from the example below (you can delete anything you don't intend to use) so generic params can be provided:

```python
from celery import Celery, Signature
from celery.app.task import Task
from celery.contrib.abortable import AbortableAsyncResult, AbortableTask
from celery.contrib.django.task import DjangoTask
from celery.local import class_property
from celery.result import AsyncResult
from celery.utils.objects import FallbackContext

classes = [
    Celery,
    Task,
    DjangoTask,
    AbortableTask,
    AsyncResult,
    AbortableAsyncResult,
    Signature,
    FallbackContext,
    class_property,
]

for cls in classes:
    setattr(  # noqa: B010
        cls,
        "__class_getitem__",
        classmethod(lambda cls, *args, **kwargs: cls),
    )
```

## dev

### initial setup

```shell
# install uv (https://docs.astral.sh/uv/)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### regular development

```shell
uv sync
```
```shell
# run formatting, linting, and typechecking
s/lint
```
or
```shell
uv run ruff check --fix
uv run ruff format
uv run basedpyright typings tests
uv run mypy tests
```
```shell
# build and publish
uv build && uv publish
```

### pre-commit

The project uses [pre-commit](https://pre-commit.com/) for code quality checks:

```shell
# install pre-commit hooks
uv run prek install

# run all checks manually
uv run prek run --all-files
```

### tooling

- [ruff](https://docs.astral.sh/ruff/) — formatting and linting
- [basedpyright](https://docs.basedpyright.com/) — type checking
- [mypy](https://mypy.readthedocs.io/) — type checking

## related

- <https://github.com/sbdchd/django-types>
- <https://github.com/sbdchd/djangorestframework-types>
- <https://github.com/sbdchd/mongo-types>
- <https://github.com/sbdchd/msgpack-types>
