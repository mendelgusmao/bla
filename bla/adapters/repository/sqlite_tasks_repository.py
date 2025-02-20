from typing import List

from injector import inject

from bla.application.interfaces.repositories import TasksRepository
from bla.domain.interfaces.unit_of_work import UnitOfWork
from bla.domain.models import TaskModel
from bla.domain.queries import PaginationQuery, TasksQuery


class SQLiteTasksRepository(TasksRepository):
    @inject
    def find_by_id(
        self,
        unit_of_work: UnitOfWork,
        task_id: int,
    ) -> TaskModel:
        session = unit_of_work.session

        return session.query(TaskModel).filter_by(id=task_id).one()

    @inject
    def find_all(
        self,
        unit_of_work: UnitOfWork,
        query: TasksQuery,
        pagination: PaginationQuery,
    ) -> List[TaskModel]:
        filter = query.to_dict()

        return (
            unit_of_work.session.query(TaskModel)
            .filter_by(**filter)
            .offset(pagination.page)
            .limit(pagination.amount)
            .all()
        )

    @inject
    def create(
        self,
        unit_of_work: UnitOfWork,
        task: TaskModel,
    ) -> TaskModel:
        unit_of_work.session.add(task)

        return task

    @inject
    def update(
        self,
        unit_of_work: UnitOfWork,
        task: TaskModel,
    ) -> TaskModel:
        self.find_by_id(unit_of_work, task.id)
        unit_of_work.session.add(task)

        return task

    @inject
    def delete(
        self,
        unit_of_work: UnitOfWork,
        task_id: int,
    ) -> None:
        task = self.find_by_id(unit_of_work, task_id)
        unit_of_work.session.delete(task)
