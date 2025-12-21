from __future__ import annotations

import errno
import sys
from typing import TYPE_CHECKING, Any, Protocol

import celery
from celery import Celery, shared_task, signature
from celery.app.task import Task
from celery.canvas import Signature, chord
from celery.exceptions import Reject
from celery.result import AsyncResult, allow_join_result, denied_join_result
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from typing_extensions import override

if TYPE_CHECKING:
    from collections.abc import Iterator

    from celery.contrib.django.task import DjangoTask

app = celery.Celery()

logger = get_task_logger(__name__)


@app.task(bind=True)
def add_2(self: Task[Any, Any], x: int, y: int) -> None:
    logger.info(self.request.id)


@shared_task(name="main.add")
def add(x: int, y: int) -> int:
    return x + y


@app.task(name="main.sub")
def sub(x: int, y: int) -> int:
    return x - y


class Table(Protocol):
    def all(self) -> Iterator[dict[str, object]]: ...


class DB(Protocol):
    @property
    def table(self) -> Table: ...


class DatabaseTask(Task[Any, Any]):
    @property
    def db(self) -> DB:
        raise Exception  # noqa: TRY002


@app.task(base=DatabaseTask)
def process_rows(param_1: int) -> None:
    for row in process_rows.db.table.all():
        print(row)


@shared_task(base=DatabaseTask)
def process_rows_2(param_1: int) -> None:
    for row in process_rows_2.db.table.all():
        print(row)


@shared_task(base=DatabaseTask, bind=True)
def process_rows_3(self: DatabaseTask, param_1: int) -> None:
    for row in process_rows_3.db.table.all():
        print(row)


# Here, a typeignore is needed so that when the overload stops working correctly,
# pyright and mypy will report that the typeignore is unnecessary.
@shared_task(base=DatabaseTask, bind=True)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
def process_rows_4(self: int, param_1: int) -> None:
    for row in process_rows_4.db.table.all():
        print(row)


database_app = Celery[DatabaseTask]()


@database_app.task(name="main.process_rows_4")
def process_rows_5(param_1: int) -> None:
    for row in process_rows_5.db.table.all():
        print(row)


@database_app.task(name="main.process_rows_5", bind=True)
def process_rows_6(self: DatabaseTask, param_1: int) -> None:
    for row in process_rows_6.db.table.all():
        print(row)


# Here, a typeignore is needed so that when the overload stops working correctly,
# pyright and mypy will report that the typeignore is unnecessary.
@database_app.task(name="main.process_rows_5", bind=True)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
def process_rows_7(self: int, param_1: int) -> None:
    for row in process_rows_7.db.table.all():
        print(row)


@app.task(bind=True, default_retry_delay=10)
def send_twitter_status(self: Task[Any, Any], oauth: str, tweet: str) -> None:
    try:
        print("fetch stuff")
    except KeyError as exc:
        raise self.retry(exc=exc, countdown=10)
    except ValueError as exc:
        raise Reject(exc, requeue=False)
    except OSError as exc:
        if exc.errno == errno.ENOMEM:
            raise Reject(exc, requeue=False)

        delivery_info = self.request.delivery_info or {}
        if not delivery_info.get("redelivered"):
            msg = "no reason"
            raise Reject(msg, requeue=True)

    self.update_state(state="SUCCESS", meta={"foo": "bar"})


class HttpNotFoundError(Exception): ...


logger = get_task_logger(__name__)


@app.task(bind=True)
def add_5(self: Task[Any, Any], x: int, y: int) -> int:
    old_outs = sys.stdout, sys.stderr
    rlevel = self.app.conf.worker_redirect_stdouts_level
    try:
        self.app.log.redirect_stdouts_to_logger(logger, rlevel)
        print(f"Adding {x} + {y}")
        return x + y
    finally:
        sys.stdout, sys.stderr = old_outs


app.send_task(name="main.add", args=(1, 2))
app.send_task(name="main.add", args=[1, 2])


@app.task(throws=(KeyError, HttpNotFoundError))
def foo() -> None:
    print("foo")


foo.name

app_2 = celery.Celery("worker")

add.chunks(zip(range(100), range(100)), 10).group().skew(start=1, stop=10)()


class MyTask(celery.Task[Any, Any]):
    throws = (ValueError,)

    @override
    def on_failure(
        self,
        exc: Exception,
        task_id: str,
        args: object,
        kwargs: object,
        einfo: object,
    ) -> None:
        print(f"{task_id!r} failed: {exc!r}")

    def foo(self) -> None:
        print("foo")


@app_2.task(base=MyTask)
def add_3(x: int, y: int) -> None:
    raise KeyError


add_3.foo()


def test_celery_register_task() -> None:
    bar = app_2.register_task(MyTask())
    bar.foo()

    baz = app_2.register_task(MyTask)
    baz.foo()


def test_celery_calling_task() -> None:
    signature("tasks.add", args=(2, 2), countdown=10)

    Signature("tasks.add")

    bar = add(x=10, y=100)
    print(bar)
    add.delay(x=10, y=100)
    add.delay(x=10, y=100)
    add.s(10).delay().get()
    add.s(x=10, y=100)
    add.s(10, 100).apply_async()
    add.s(10, 100).apply()
    add.s(10, 100).delay()

    foo = add.s(10, 10) | add.s(10)
    print(foo)

    sub.chunks([], 10).apply_async()

    app.control.broadcast("ping")

    job = celery.group(add.s(5, x) for x in range(10))
    print(job)

    celery.group([add.s(2, 2), add.s(4, 4)])

    celery.group(add.s(1, 1), add.s(1, 2), add.s(1, 3))


def test_celery_signals() -> None:
    app = Celery()

    app.autodiscover_tasks(packages=["foo", "bar"])
    app.autodiscover_tasks(packages=lambda: ["foo", "bar"])

    @app.on_after_configure.connect
    def setup_periodic_tasks(sender: Celery, **kwargs: object) -> None:
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


def test_covariant_assignment() -> None:
    @app.task()
    def foo() -> None:
        pass

    sig: Signature[None] = foo.s()
    result: AsyncResult[None] = sig.apply_async()

    def test_covariance(
        t: Task[[], object], s: Signature[object], r: AsyncResult[object]
    ) -> None:
        pass

    test_covariance(foo, sig, result)


def test_link() -> None:
    @app.task()
    def foo() -> None:
        pass

    @app.task()
    def bar() -> None:
        pass

    @app.task()
    def baz() -> None:
        pass

    foo.apply_async(link=bar.s(), link_error=bar.s())
    foo.apply(link=bar.s(), link_error=bar.s())

    foo.apply_async(link=[bar.s(), baz.s()], link_error=[bar.s(), baz.s()])
    foo.apply(link=[bar.s(), baz.s()], link_error=[bar.s(), baz.s()])

    foo.s().apply_async(link=bar.s(), link_error=bar.s())
    foo.s().apply(link=bar.s(), link_error=bar.s())

    foo.s().apply_async(link=[bar.s(), baz.s()], link_error=[bar.s(), baz.s()])
    foo.s().apply(link=[bar.s(), baz.s()], link_error=[bar.s(), baz.s()])


def run_chord() -> AsyncResult[Any]:
    @app.task()
    def foo() -> None:
        pass

    @app.task()
    def bar() -> None:
        pass

    @app.task()
    def baz() -> None:
        pass

    return chord([foo.s(), bar.s()])(baz.si())


with allow_join_result():
    ...

with denied_join_result():
    ...


def test_celery_top_level_exports() -> None:
    celery.Celery
    celery.Signature[Any]
    celery.Task[Any, Any]
    celery.chain
    celery.chord
    celery.chunks
    celery.current_app
    celery.current_task
    celery.group
    celery.local
    celery.shared_task
    celery.signature
    celery.uuid
    celery.xmap
    celery.xstarmap


def test_djangotask(task: DjangoTask[[int, int], Any]) -> None:
    task.delay_on_commit(1, 2)
    task.apply_async_on_commit((1, 2), countdown=10.0)
