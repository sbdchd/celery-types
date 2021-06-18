import celery
from celery import shared_task, signature
from celery.canvas import Signature

app = celery.Celery()


@shared_task(name="main.add")
def add(x: int, y: int) -> int:
    return x + y


@app.task(name="main.sub")
def sub(x: int, y: int) -> int:
    return x - y


class HttpNotFound(Exception):
    ...


@app.task(throws=(KeyError, HttpNotFound))
def foo() -> None:
    print("foo")


def test_celery_calling_task() -> None:
    signature("tasks.add", args=(2, 2), countdown=10)

    Signature("tasks.add")

    bar = add(x=10, y=100)
    print(bar)
    add.delay(x=10, y=100)
    add.s(10).delay().get()
    add.s(x=10, y=100)
    add.s(10, 100).apply_async()
    add.s(10, 100).apply()
    add.s(10, 100).delay()

    foo = add.s(10, 10) | add.s(10)
    print(foo)

    sub.chunks([], 10).apply_async()


def test_celery_top_level_exports() -> None:
    celery.Celery
    celery.Signature
    celery.Task
    celery.chain
    celery.chord
    celery.chunks
    celery.current_app
    celery.current_task
    celery.group
    celery.local
    celery.shared_task
    celery.signature
    celery.task
    celery.uuid
    celery.xmap
    celery.xstarmap
