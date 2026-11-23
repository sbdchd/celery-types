from __future__ import annotations

import errno
import sys
from collections.abc import Callable, Hashable, Mapping
from threading import Lock
from typing import TYPE_CHECKING, Any, ParamSpec, Protocol, TypeVar
from weakref import ReferenceType

import celery
from celery import Celery, shared_task, signature
from celery.app.task import Task
from celery.backends.base import Backend
from celery.beat import BeatPidbox, Service
from celery.canvas import Signature, chord
from celery.contrib.django.task import DjangoTask
from celery.exceptions import Reject
from celery.fixups.django import DjangoFixup, DjangoWorkerFixup
from celery.result import (
    AsyncResult,
    EagerResult,
    GroupResult,
    ResultBase,
    allow_join_result,
    denied_join_result,
    result_from_tuple,
)
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from celery.worker.request import Request
from typing_extensions import assert_type, override

if TYPE_CHECKING:
    from collections.abc import Iterator
    from weakref import WeakMethod

    from celery.contrib.abortable import AbortableTask
    from celery.utils.dispatch import Signal

P = ParamSpec("P")
R = TypeVar("R")
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


def test_app_finalized(celery_app: Celery, *, finalized: bool) -> None:
    assert_type(celery_app.finalized, bool)
    celery_app.finalized = finalized
    assert_type(celery_app.finalized, bool)


def test_app_finalized_rejects_non_boolean(celery_app: Celery) -> None:
    # Expected error: the writable lifecycle flag is boolean, not arbitrary data.
    # Unused-ignore checks catch a regression that widens its type.
    celery_app.finalized = "yes"  # type: ignore[assignment]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[invalid-assignment]


def test_task_send_event(task: Task[P, R]) -> None:
    assert_type(task.send_event("task-progress"), None)
    assert_type(
        task.send_event(
            "task-progress", retry=False, retry_policy={"max_retries": 1}, progress=50
        ),
        None,
    )


def test_task_send_event_override() -> None:
    class MonitoredTask(Task[Any, Any]):
        @override
        def send_event(
            self,
            type_: str,
            retry: bool = True,
            retry_policy: Mapping[str, int] | None = None,
            **fields: Any,
        ) -> None:
            super().send_event(type_, retry=retry, retry_policy=retry_policy, **fields)

    assert_type(MonitoredTask().send_event("task-progress"), None)


def test_task_constructor_signature(func: Callable[P, R]) -> None:
    """
    The constructor form of the task creation decorator passes the function
    signature through to the newly created task.
    """
    task_from_constructor = app.task(func)
    assert_type(task_from_constructor, Task[P, R])


def test_task_decorator_signature(func: Callable[P, R]) -> None:
    """
    The task creation decorator passes the function signature through to the
    newly created task.
    """

    @app.task(max_retries=1)
    def signature_passthrough(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)

    assert_type(signature_passthrough, Task[P, R])


def test_bound_task_decorator_signature(func: Callable[P, R]) -> None:
    """
    The bound task creation decorator creates a new task with a function
    signature that does not include the first `self` parameter.
    """

    @app.task(bind=True)
    def signature_passthrough(
        self: Task[Any, Any], *args: P.args, **kwargs: P.kwargs
    ) -> R:
        return func(*args, **kwargs)

    assert_type(signature_passthrough, Task[P, R])


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
    assert_type(process_rows, DatabaseTask)

    for row in process_rows.db.table.all():
        print(row)


@shared_task(base=DatabaseTask)
def process_rows_2(param_1: int) -> None:
    assert_type(process_rows_2, DatabaseTask)

    for row in process_rows_2.db.table.all():
        print(row)


@shared_task(base=DatabaseTask, bind=True)
def process_rows_3(self: DatabaseTask, param_1: int) -> None:
    assert_type(process_rows_3, DatabaseTask)

    for row in process_rows_3.db.table.all():
        print(row)


# Here, a typeignore is needed so that when the overload stops working correctly,
# pyright and mypy will report that the typeignore is unnecessary.
@shared_task(base=DatabaseTask, bind=True)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]
def process_rows_4(self: int, param_1: int) -> None:
    assert_type(process_rows_4, DatabaseTask)

    for row in process_rows_4.db.table.all():
        print(row)


database_app = Celery[DatabaseTask]()


@database_app.task(name="main.process_rows_5")
def process_rows_5(param_1: DatabaseTask) -> None:
    assert_type(process_rows_5, DatabaseTask)
    for row in process_rows_5.db.table.all():
        print(row)


@database_app.task(name="main.process_rows_6", bind=True)
def process_rows_6(self: DatabaseTask, param_1: int) -> None:
    assert_type(process_rows_6, DatabaseTask)

    for row in process_rows_6.db.table.all():
        print(row)


# Here, a typeignore is needed so that when the overload stops working correctly,
# pyright and mypy will report that the typeignore is unnecessary.
@database_app.task(name="main.process_rows_7", bind=True)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]
def process_rows_7(self: int, param_1: int) -> None:
    assert_type(process_rows_7, DatabaseTask)

    for row in process_rows_7.db.table.all():
        print(row)


# Here, a typeignore is needed so that when the overload stops working correctly,
# pyright and mypy will report that the typeignore is unnecessary.
@database_app.task(name="main.process_rows_8", bind=True, base=Task[..., None])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]
def binded_task_8_fail(self: int, param_1: int) -> None:
    pass


@database_app.task(name="main.process_rows_8", bind=True, base=Task[[int], None])
def binded_task_8_ok(self: Task[[int], None], param_1: int) -> None:
    assert_type(binded_task_8_ok, Task[[int], None])


@app.task(bind=True, default_retry_delay=10)
def send_twitter_status(self: Task[[str, str], Any], oauth: str, tweet: str) -> None:
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


assert_type(foo.name, str)

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


def test_task_request_class() -> None:
    class MyRequest(Request):
        pass

    class CustomRequestTask(Task[Any, Any]):
        Request = MyRequest

    assert_type(Task[Any, Any].Request, str | type[Request])
    CustomRequestTask()


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


def test_signature_args_are_writable(sig: Signature[R]) -> None:
    assert_type(sig.args, tuple[Any, ...])
    sig.args = (1, "value")
    sig.args = ()
    assert_type(sig.delay(), AsyncResult[R])


def test_signature_kwargs_are_writable(sig: Signature[R]) -> None:
    assert_type(sig.kwargs, dict[str, Any])
    sig.kwargs = {"value": 1}
    sig.kwargs = {}
    assert_type(sig.delay(), AsyncResult[R])


def test_signature_options_are_writable(sig: Signature[R]) -> None:
    assert_type(sig.options, dict[str, Any])
    sig.options = {"countdown": 1, "label": "example"}
    sig.options = {}
    assert_type(sig.delay(), AsyncResult[R])


def test_signature_argument_assignments_reject_invalid_types(
    sig: Signature[int],
) -> None:
    # Expected type errors: args is a tuple; kwargs and options are dictionaries.
    # If invalid values start passing, unused-ignore checks flag these markers.
    sig.args = 42  # type: ignore[assignment]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[invalid-assignment]
    sig.kwargs = 42  # type: ignore[assignment]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[invalid-assignment]
    sig.options = 42  # type: ignore[assignment]  # pyright: ignore[reportAttributeAccessIssue]  # ty: ignore[invalid-assignment]


def test_signature_set_accepts_custom_options(sig: Signature[R]) -> None:
    assert_type(sig.set(label="example"), Signature[R])
    assert_type(
        sig.set(countdown=1, label="example", custom_metadata={"enabled": True}),
        Signature[R],
    )
    assert_type(sig.set(True, label="example"), Signature[R])


def test_signature_set_checks_known_option_types(sig: Signature[int]) -> None:
    # Custom options must not weaken the types of known options such as countdown.
    # This call must fail; unused-ignore checks flag it if it starts passing.
    sig.set(countdown="soon", label="example")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]


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
    celery.Celery[Task[Any, Any]]
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


def test_djangotask_base_decorator_signature(func: Callable[P, R]) -> None:
    """
    `base=DjangoTask` keeps the function signature on the new task, unlike an
    arbitrary `base=` which can only name the bare base type.
    """

    @shared_task(base=DjangoTask)
    def shared_passthrough(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)

    @app.task(base=DjangoTask)
    def app_passthrough(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)

    assert_type(shared_passthrough, DjangoTask[P, R])
    assert_type(app_passthrough, DjangoTask[P, R])


@shared_task(base=DjangoTask)
def add_on_commit(x: int, y: int) -> int:
    return x + y


def test_djangotask_base_methods() -> None:
    assert_type(add_on_commit.delay_on_commit(1, 2), AsyncResult[int])
    assert_type(
        add_on_commit.apply_async_on_commit((1, 2), countdown=10.0), AsyncResult[int]
    )


def test_djangotask_base_bound_decorator_signature(func: Callable[P, R]) -> None:
    @shared_task(base=DjangoTask, bind=True)
    def shared_passthrough(
        self: DjangoTask[Any, Any], *args: P.args, **kwargs: P.kwargs
    ) -> R:
        return func(*args, **kwargs)

    @app.task(base=DjangoTask, bind=True)
    def app_passthrough(
        self: DjangoTask[Any, Any], *args: P.args, **kwargs: P.kwargs
    ) -> R:
        return func(*args, **kwargs)

    assert_type(shared_passthrough, DjangoTask[P, R])
    assert_type(app_passthrough, DjangoTask[P, R])


django_app = Celery[DjangoTask[Any, Any]]()


def test_djangotask_app_constructor_signature(func: Callable[P, R]) -> None:
    task_from_constructor = django_app.task(func)
    assert_type(task_from_constructor, DjangoTask[P, R])


def test_djangotask_app_decorator_signature(func: Callable[P, R]) -> None:
    @django_app.task(max_retries=1)
    def signature_passthrough(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)

    assert_type(signature_passthrough, DjangoTask[P, R])


def test_djangotask_app_bound_decorator_signature(func: Callable[P, R]) -> None:
    @django_app.task(bind=True)
    def signature_passthrough(
        self: DjangoTask[Any, Any], *args: P.args, **kwargs: P.kwargs
    ) -> R:
        return func(*args, **kwargs)

    assert_type(signature_passthrough, DjangoTask[P, R])


@django_app.task
def add_on_commit_2(x: int, y: int) -> int:
    return x + y


def test_djangotask_app_methods() -> None:
    assert_type(add_on_commit_2.delay_on_commit(1, 2), AsyncResult[int])
    assert_type(
        add_on_commit_2.apply_async_on_commit((1, 2), countdown=10.0), AsyncResult[int]
    )


def test_push_request(task: Task[[int, int], None]) -> None:
    # push_request builds a `Context` from its fields, not the task's arguments.
    task.push_request(retries=3)
    task.push_request({"id": "abc"}, retries=1)
    task.pop_request()


def test_beat_service_remote_control() -> None:
    # Service takes the beat remote-control options added in celery 5.7,
    # and BeatPidbox is the mailbox node that answers `celery inspect ping`
    # for beat.
    service = Service(app, remote_control=True, hostname="beat@host")
    assert_type(service.remote_control, bool)
    assert_type(service.hostname, str | None)
    assert_type(service.schedule_filename, str)
    pidbox = BeatPidbox(service)
    assert_type(pidbox.service, Service)
    assert_type(pidbox.app, Celery)
    assert_type(pidbox.hostname, str)
    assert_type(pidbox.max_tick_age, float)
    assert_type(pidbox.tick_age(), float | None)
    assert_type(pidbox.is_stale(), bool)
    assert_type(pidbox.fanout_support(), tuple[bool, Any])


def test_abortabletask(task: AbortableTask[[], None]) -> None:
    task.is_aborted()


@app.task(bind=True)
def add_6(self: Task[Any, Any], x: int, y: int) -> None:
    # `Context.children` holds the `AsyncResult`s of any subtasks started by
    # this task (populated via `Task.add_trail`), not their string ids.
    assert_type(self.request.children, list[AsyncResult[Any]])
    for child in self.request.children:
        assert_type(child, AsyncResult[Any])


def test_async_result_as_list(result: AsyncResult[None]) -> None:
    assert_type(result.as_list(), list[str])


def test_async_result_children(result: AsyncResult[R]) -> None:
    assert_type(
        result.children,
        list[AsyncResult[Any] | GroupResult | tuple[object, ...] | list[object]] | None,
    )
    for child in result.children or []:
        # Narrow away serialized metadata before using the result-object API.
        if isinstance(child, (AsyncResult, GroupResult)):
            assert_type(child.id, str | None)
            assert_type(child.ready(), bool)


def test_async_result_state_and_status(result: AsyncResult[R]) -> None:
    assert_type(result.state, str)
    assert_type(result.status, str)
    assert_type(result.state == "REVOKED", bool)
    assert_type(result.status == "PROGRESS", bool)


def test_eager_result_state_and_status(result: EagerResult[R]) -> None:
    assert_type(result.state, str)
    assert_type(result.status, str)
    assert_type(result.state == "REVOKED", bool)
    assert_type(result.status == "PROGRESS", bool)


def test_async_result_traceback(result: AsyncResult[R]) -> None:
    traceback = result.traceback
    assert_type(traceback, str | None)
    if traceback is not None:
        assert_type(traceback.splitlines(), list[str])


def test_eager_result_traceback(result: EagerResult[R]) -> None:
    traceback = result.traceback
    assert_type(traceback, str | None)
    if traceback is not None:
        assert_type(traceback.splitlines(), list[str])


def test_async_result_reduce_args(result: AsyncResult[R]) -> None:
    assert_type(
        result.__reduce_args__(), tuple[str, Backend, None, None, ResultBase | None]
    )
    assert_type(result.__copy__(), AsyncResult[R])


def test_eager_result_reduce_args(result: EagerResult[R]) -> None:
    # Failed eager tasks serialize their captured exception as the result payload.
    # Older versions omit the final task-name argument.
    assert_type(
        result.__reduce_args__(),
        tuple[str, R | BaseException, str, str | None]
        | tuple[str, R | BaseException, str, str | None, str | None],
    )
    assert_type(result.__copy__(), EagerResult[R])


def test_async_result_transport_tuple(result: AsyncResult[R]) -> None:
    data = result.as_tuple()
    header, children = data
    task_id, parent = header
    assert_type(task_id, str)
    assert_type(children, None)
    assert_type(result_from_tuple(data), AsyncResult[Any])
    if parent is not None:
        restored_parent: ResultBase = result_from_tuple(parent)
        assert_type(restored_parent.parent, ResultBase | None)


def test_group_result_transport_tuple(group: GroupResult, leaf: AsyncResult[R]) -> None:
    data = group.as_tuple()
    header, children = data
    group_id, _parent = header
    assert_type(group_id, str | None)
    assert_type(result_from_tuple(data), GroupResult)
    children.append(leaf.as_tuple())
    for child in children:
        assert_type(result_from_tuple(child), AsyncResult[Any] | GroupResult)


def test_result_from_tuple_preserves_result_objects(
    result: AsyncResult[R], eager: EagerResult[R], group: GroupResult, base: ResultBase
) -> None:
    assert_type(result_from_tuple(result), AsyncResult[R])
    assert_type(result_from_tuple(eager), EagerResult[R])
    assert_type(result_from_tuple(group), GroupResult)
    assert_type(result_from_tuple(base), ResultBase)


def test_result_from_tuple_accepts_dynamic_data(
    data: tuple[object, ...] | list[object], result: AsyncResult[R]
) -> None:
    assert_type(result_from_tuple(data), AsyncResult[Any] | GroupResult)
    for child in result.children or []:
        assert_type(result_from_tuple(child), AsyncResult[Any] | GroupResult)


def test_result_from_tuple_recognizes_tuple_kinds(result: AsyncResult[R]) -> None:
    assert_type(result_from_tuple(("leaf-id", None)), AsyncResult[Any])
    assert_type(result_from_tuple(("empty-group-id", [])), GroupResult)
    assert_type(result_from_tuple((None, [])), GroupResult)
    children = [result.as_tuple()]
    assert_type(result_from_tuple((("group-id", None), children)), GroupResult)


def test_result_from_tuple_rejects_scalar_inputs() -> None:
    # Expected type errors: only result objects or tuple/list records are valid.
    # Unused-ignore checks catch a regression that starts accepting scalars.
    result_from_tuple("not-a-record")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]  # ty: ignore[no-matching-overload]
    result_from_tuple(None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]  # ty: ignore[no-matching-overload]


def test_django_fixup(fixup: DjangoFixup) -> None:
    assert_type(fixup.install(), DjangoFixup)
    assert_type(fixup.autodiscover_tasks(), list[str])
    assert_type(fixup.worker_fixup, DjangoWorkerFixup)
    fixup.worker_fixup = DjangoWorkerFixup(fixup.app)


def test_django_worker_fixup(worker_fixup: DjangoWorkerFixup) -> None:
    assert_type(worker_fixup.install(), DjangoWorkerFixup)
    assert_type(worker_fixup.db_reuse_max, int | None)
    worker_fixup.validate_models()
    worker_fixup.close_database()
    worker_fixup.close_cache()


def test_signal_dispatch_ids(
    signal: Signal, receiver: Callable[P, R], custom_uid: Hashable
) -> None:
    dispatch_ids: tuple[Hashable | None, ...] = (
        "receiver",
        42,
        ("receiver", 42),
        None,
        custom_uid,
    )
    for dispatch_uid in dispatch_ids:
        assert_type(signal.connect(receiver, dispatch_uid=dispatch_uid), Callable[P, R])
        assert_type(signal.connect(dispatch_uid=dispatch_uid)(receiver), Callable[P, R])
        assert_type(signal.disconnect(receiver, dispatch_uid=dispatch_uid), bool)

    assert_type(signal.connect(receiver), Callable[P, R])
    assert_type(signal.connect()(receiver), Callable[P, R])
    assert_type(signal.disconnect(receiver), bool)


def test_signal_dispatch_ids_reject_unhashable_values(
    signal: Signal, receiver: Callable[..., object]
) -> None:
    # Expected errors in mypy/pyright: dispatch IDs must be hashable, not lists/dicts.
    # ty currently misses these errors; no ty ignores are needed.
    # Unused-ignore checks flag a regression if the other checkers accept them.
    signal.connect(receiver, dispatch_uid=[1])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
    signal.connect(dispatch_uid={"id": 1})  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
    signal.disconnect(receiver, dispatch_uid=[1])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]


def test_signal_lock(signal: Signal) -> None:
    lock = signal.lock
    assert_type(lock, Lock)
    acquired = lock.acquire(blocking=False)
    assert_type(acquired, bool)
    if acquired:
        lock.release()
    with lock:
        assert_type(lock.locked(), bool)


def test_signal_receiver_entries(signal: Signal) -> None:
    assert_type(
        signal.receivers,
        list[
            tuple[
                tuple[Hashable, Hashable],
                Callable[..., Any] | ReferenceType[Callable[..., Any]],
            ]
        ],
    )


def test_signal_receiver_storage_types(
    signal: Signal,
    receiver: Callable[..., int],
    weak_receiver: ReferenceType[Callable[..., int]],
    bound_receiver: WeakMethod[Callable[..., str]],
) -> None:
    # Check the internal storage shapes, not a replacement for connect().
    signal.receivers = [
        ((1, 2), receiver),
        ((("dispatch", 1), "sender"), weak_receiver),
        ((b"dispatch", b"sender"), bound_receiver),
    ]
