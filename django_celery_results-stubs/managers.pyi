from datetime import timedelta
from typing import Optional, Union
from uuid import UUID

from django.db import models
from django.db.models.query import QuerySet
from django_celery_results.models import GroupResult, TaskResult

class TaskResultManager(models.Manager[TaskResult]):
    def get_task(self, task_id: str) -> TaskResult: ...
    def store_result(
        self,
        content_type: str,
        content_encoding: str,
        task_id: Union[str, UUID],
        result: str,
        status: str,
        traceback: Optional[str] = ...,
        meta: Optional[str] = ...,
        task_name: Optional[str] = ...,
        task_args: Optional[str] = ...,
        task_kwargs: Optional[str] = ...,
        using: Optional[str] = ...,
    ) -> TaskResult: ...
    def get_all_expired(self, expires: timedelta) -> QuerySet[TaskResult]: ...
    def delete_expired(self, expires: timedelta) -> None: ...

class GroupResultManager(models.Manager[GroupResult]):
    def get_group(self, group_id: str) -> GroupResult: ...
    def store_group_result(
        self,
        content_type: str,
        content_encoding: str,
        group_id: str,
        result: Optional[str],
        using: Optional[str] = ...,
    ) -> GroupResult: ...
