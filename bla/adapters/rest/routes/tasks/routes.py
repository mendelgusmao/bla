from fastapi import APIRouter
from fastapi_injector import Injected

from bla.application.use_cases import GetTaskUseCase
from bla.domain.entities.task import Task

router = APIRouter()


@router.get(
    "/tasks/{task_id}",
    summary="Retrieves a task",
)
async def get_task(
    get_task_user_case: GetTaskUseCase = Injected(GetTaskUseCase),
    task_id: int = 0,
) -> Task:
    return get_task_user_case.execute(task_id)
