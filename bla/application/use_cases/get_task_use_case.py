from typing import Self

from injector import inject

from bla.application.interfaces.repositories import TasksRepository
from bla.domain.entities import Task
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
            task = self.repository.find_by_id(uow, task_id)

        return Task.from_orm(task)
