from typing import Any, ClassVar, Literal

from celery.app.task import Task as BaseTask
from docutils import nodes
from sphinx.domains.python import PyFunction
from sphinx.ext.autodoc import Documenter, FunctionDocumenter
from typing_extensions import override

class TaskDocumenter(FunctionDocumenter):
    objtype: ClassVar[str]
    member_order: ClassVar[int]

    @override
    @classmethod
    def can_document_member(
        cls: type[Documenter],
        member: Any,
        membername: str,
        isattr: bool,
        parent: Any,
    ) -> bool: ...
    @override
    def format_args(self) -> str: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def document_members(self, all_members: bool = False) -> None: ...
    @override
    def check_module(self) -> bool: ...

class TaskDirective(PyFunction):
    @override
    def get_signature_prefix(self, sig: str) -> list[nodes.Node]: ...

def autodoc_skip_member_handler(
    app: Any,
    what: object,
    name: object,
    obj: BaseTask[Any, Any],
    skip: bool,
    options: object,
) -> Literal[False] | None: ...
def setup(app: Any) -> dict[Literal["parallel_read_safe"], Literal[True]]: ...
