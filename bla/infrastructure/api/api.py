from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_injector import attach_injector
from injector import Injector

from bla.adapters.repository import SQLiteTasksRepository
from bla.adapters.repository.unit_of_work import UnitOfWork as UnitOfWorkImpl
from bla.adapters.rest.routes import tasks_router
from bla.domain.interfaces.repositories import TasksRepository
from bla.domain.interfaces.unit_of_work import UnitOfWork
from bla.infrastructure.database.database_connection import DatabaseConnection


def create_api(injector: Injector) -> FastAPI:
    api = FastAPI(title="BLA Technical Interview Exercise", version="1.0.0")
    api.include_router(tasks_router, prefix="/api/v1", tags=["tasks"])

    @api.get("/", include_in_schema=False)
    async def redirect_root_to_docs():
        return RedirectResponse("/docs")

    injector.binder.install(DatabaseConnection)
    injector.binder.bind(TasksRepository, to=SQLiteTasksRepository)
    injector.binder.bind(UnitOfWork, to=UnitOfWorkImpl)

    attach_injector(api, injector)

    return api
