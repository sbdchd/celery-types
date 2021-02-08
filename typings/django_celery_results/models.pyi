from datetime import datetime
from typing import List, Optional, Tuple

from django.db import models
from typing_extensions import TypedDict

from django_celery_results.managers import TaskResultManager

ALL_STATES: List[str]
TASK_STATE_CHOICES: List[Tuple[str, str]]

class TaskResultDict(TypedDict):
    task_id: str
    task_name: str
    task_args: str
    task_kwargs: str
    status: str
    result: str
    date_done: datetime
    traceback: str
    meta: str

class TaskResult(models.Model):
    task_id: models.CharField[str]
    task_name: models.CharField[Optional[str]]
    task_args: models.TextField[Optional[str]]
    task_kwargs: models.TextField[Optional[str]]
    status: models.CharField[Optional[str]]
    content_type: models.CharField[str]
    content_encoding: models.CharField[str]
    result: models.TextField[Optional[str]]
    date_done: models.DateTimeField[datetime]
    traceback: models.TextField[Optional[str]]
    hidden: models.BooleanField[bool]
    meta: models.TextField[Optional[str]]
    objects: TaskResultManager
    def as_dict(self) -> TaskResultDict: ...
