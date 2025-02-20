from abc import ABC, abstractmethod

from bla.domain.entities.task import Task


class TasksRepository(ABC):
    @abstractmethod
    def get(self, task_id: int) -> Task:
        pass
