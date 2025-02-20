from typing import Self

from injector import inject

from bla.application.interfaces.repositories import TasksRepository
from bla.domain.entities import Task
from bla.domain.entities.task import TaskRequest
from bla.domain.interfaces.unit_of_work import UnitOfWork


class CreateTaskUseCase:
    @inject
    def __init__(
        self,
        repository: TasksRepository,
        unit_of_work: UnitOfWork,
    ) -> Self:
        self.repository = repository
        self.unit_of_work = unit_of_work

    def execute(
        self,
        task: TaskRequest,
    ) -> Task:
        with self.unit_of_work as uow:
            task = self.repository.create(uow, task.to_orm())

        return Task.from_orm(task)
