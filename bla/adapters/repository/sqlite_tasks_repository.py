from injector import inject

from bla.domain.interfaces.repositories import TasksRepository
from bla.domain.interfaces.unit_of_work import UnitOfWork
from bla.domain.models import Task as TaskModel


class SQLiteTasksRepository(TasksRepository):
    @inject
    def get(self, unit_of_work: UnitOfWork, task_id: int) -> TaskModel:
        unit_of_work.session.add(
            TaskModel(
                title="Entregar tarefa agora!",
                status="created",
            )
        )

        session = unit_of_work.session

        return session.query(TaskModel).filter_by(id=task_id).first()
