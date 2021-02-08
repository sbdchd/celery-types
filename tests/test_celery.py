import celery
from celery import shared_task


@shared_task(name="main.add")
def add(x: int, y: int) -> int:
    return x + y


def test_celery_calling_task() -> None:

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
