from datetime import datetime
from enum import StrEnum
from typing import Optional

from pydantic import Field

from .base import Base


class TaskStatus(StrEnum):
    CREATED = "created"
    STARTED = "started"
    DONE = "done"
    ABANDONED = "abandoned"


class Task(Base):
    id: int
    user_id: Optional[int] = Field(alias="userId", default=None)
    title: str
    status: TaskStatus = TaskStatus.CREATED
    created_at: datetime = Field(alias="createdAt")
    due_at: Optional[datetime] = Field(alias="dueAt", default=None)
    finished_at: Optional[datetime] = Field(alias="finishedAt", default=None)
