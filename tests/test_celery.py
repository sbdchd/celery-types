from __future__ import annotations

from typing import Any

import celery
from celery import Celery, shared_task, signature
from celery.canvas import Signature
from celery.schedules import crontab

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


def test_celery_signals() -> None:
    app = Celery()

    @app.on_after_configure.connect
    def setup_periodic_tasks(sender: Any, **kwargs: Any) -> None:
        # Calls test('hello') every 10 seconds.
        sender.add_periodic_task(10.0, test.s("hello"), name="add every 10")

        # Calls test('world') every 30 seconds
        sender.add_periodic_task(30.0, test.s("world"), expires=10)

        # Executes every Monday morning at 7:30 a.m.
        sender.add_periodic_task(
            crontab(hour=7, minute=30, day_of_week=1),
            test.s("Happy Mondays!"),
        )

    @app.task()
    def test(arg: object) -> None:
        print(arg)

    @app.task()
    def add(x: int, y: int) -> None:
        z = x + y
        print(z)

    add.delay(1, 2)


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
