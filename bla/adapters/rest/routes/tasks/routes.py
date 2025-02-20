from datetime import datetime
from typing import Annotated, List

from fastapi import APIRouter, Query
from fastapi_injector import Injected

from bla.application.use_cases import CreateTaskUseCase, GetTasksUseCase, GetTaskUseCase
from bla.domain.entities.task import Task, TaskRequest
from bla.domain.queries import PaginationQuery, TasksQuery

DEFAULT_PAGE = 0
DEFAULT_AMOUNT = 10

router = APIRouter()


@router.get(
    "/tasks/{task_id}",
    summary="Retrieves a task",
)
def get_task(
    task_id: int = 0,
    get_task_user_case: GetTaskUseCase = Injected(GetTaskUseCase),
) -> Task:
    return get_task_user_case.execute(task_id)


@router.get(
    "/tasks",
    summary="Retrieves a list of tasks",
)
def list_tasks(
    status: str | None = None,
    due_at: Annotated[datetime | None, Query(alias="dueAt")] = None,
    page: int | None = DEFAULT_PAGE,
    amount: int | None = DEFAULT_AMOUNT,
    get_tasks_user_case: GetTasksUseCase = Injected(GetTasksUseCase),
) -> List[Task]:
    query = TasksQuery(status=status, due_at=due_at)
    pagination = PaginationQuery(page=page, amount=amount)

    return get_tasks_user_case.execute(query, pagination)


@router.post(
    "/tasks",
    summary="Create a new task",
)
def create_tasks(
    task: TaskRequest,
    create_task_use_case: CreateTaskUseCase = Injected(CreateTaskUseCase),
) -> List[Task]:
    return create_task_use_case.execute(task)
