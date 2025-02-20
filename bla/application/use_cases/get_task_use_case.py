from typing import Self

from injector import inject

from bla.domain.entities import Task
from bla.domain.interfaces.repositories import TasksRepository
from bla.domain.interfaces.unit_of_work import UnitOfWork


class GetTaskUseCase:
    @inject
    def __init__(
        self,
        repository: TasksRepository,
        unit_of_work: UnitOfWork,
    ) -> Self:
        self.repository = repository
        self.unit_of_work = unit_of_work

    def execute(self, task_id: int) -> Task:
        with self.unit_of_work as uow:
            task = self.repository.get(uow, task_id)

        if not task:
            raise Exception("task não encontrada.")

        return Task.from_orm(task)
