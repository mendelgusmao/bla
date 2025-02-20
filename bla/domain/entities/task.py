from datetime import datetime
from enum import StrEnum

from pydantic import Field

from bla.domain.models import TaskModel

from .base import Base


class TaskStatus(StrEnum):
    CREATED = "created"
    STARTED = "started"
    DONE = "done"
    ABANDONED = "abandoned"


class BaseTask(Base):
    user_id: int | None = Field(alias="userId", default=None)
    title: str
    status: TaskStatus = TaskStatus.CREATED
    due_at: datetime | None = Field(alias="dueAt", default=None)
    finished_at: datetime | None = Field(alias="finishedAt", default=None)


class Task(BaseTask):
    id: int
    created_at: datetime = Field(alias="createdAt")


class TaskRequest(BaseTask):
    def to_orm(self):
        return TaskModel(**self.dict())
