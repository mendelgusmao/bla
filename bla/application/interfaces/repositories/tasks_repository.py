from abc import ABC, abstractmethod
from typing import List

from bla.domain.interfaces.unit_of_work import UnitOfWork
from bla.domain.models import TaskModel
from bla.domain.queries import PaginationQuery, TasksQuery


class TasksRepository(ABC):
    @abstractmethod
    def find_by_id(self, unit_of_work: UnitOfWork, task_id: int) -> TaskModel:
        pass

    @abstractmethod
    def find_all(
        self,
        unit_of_work: UnitOfWork,
        query: TasksQuery,
        pagination: PaginationQuery,
    ) -> List[TaskModel]:
        pass

    @abstractmethod
    def create(self, unit_of_work: UnitOfWork, task: TaskModel) -> TaskModel:
        pass

    @abstractmethod
    def update(self, unit_of_work: UnitOfWork, task: TaskModel) -> TaskModel:
        pass

    @abstractmethod
    def delete(self, unit_of_work: UnitOfWork, task_id: int) -> None:
        pass
