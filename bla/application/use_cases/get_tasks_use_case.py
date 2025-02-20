from typing import List, Self

from injector import inject

from bla.application.interfaces.repositories import TasksRepository
from bla.domain.entities import Task
from bla.domain.interfaces.unit_of_work import UnitOfWork
from bla.domain.queries import PaginationQuery, TasksQuery


class GetTasksUseCase:
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
        query: TasksQuery,
        pagination: PaginationQuery,
    ) -> List[Task]:
        with self.unit_of_work as uow:
            tasks = self.repository.find_all(uow, query, pagination)

        return [Task.from_orm(t) for t in tasks]
