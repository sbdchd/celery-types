# celery-types [![PyPI](https://img.shields.io/pypi/v/celery-types.svg)](https://pypi.org/project/celery-types/)

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

You'll also need to monkey patch `Task` so generic params can be provided:

```python
from celery.app.task import Task
Task.__class_getitem__ = classmethod(lambda cls, *args, **kwargs: cls) # type: ignore[attr-defined]
```

## dev

### initial setup

```shell
# install poetry (https://python-poetry.org/docs/)
curl -sSL https://install.python-poetry.org | python3 -
# install node
# install yarn
npm install --global yarn

# install node dependencies
yarn
```

### regular development

```shell
poetry config virtualenvs.in-project true
poetry install

# run formatting, linting, and typechecking
s/lint

# build and publish
poetry publish --build
```

## related

- <https://github.com/sbdchd/django-types>
- <https://github.com/sbdchd/djangorestframework-types>
- <https://github.com/sbdchd/mongo-types>
- <https://github.com/sbdchd/msgpack-types>
