from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_injector import attach_injector
from injector import Injector

from bla.adapters.repository import SQLiteTasksRepository
from bla.adapters.rest.routes import tasks_router
from bla.application.interfaces.repositories import TasksRepository
from bla.domain.interfaces.unit_of_work import UnitOfWork as IUnitOfWork
from bla.infrastructure.database import DatabaseConnection
from bla.infrastructure.database.unit_of_work import UnitOfWork


def create_api() -> FastAPI:
    api = FastAPI(title="BLA Technical Interview Exercise", version="1.0.0")
    api.include_router(tasks_router, prefix="/api/v1", tags=["tasks"])

    @api.get("/", include_in_schema=False)
    async def redirect_root_to_docs():
        return RedirectResponse("/docs")

    injector = Injector()
    injector.binder.install(DatabaseConnection)
    injector.binder.bind(TasksRepository, to=SQLiteTasksRepository)
    injector.binder.bind(IUnitOfWork, to=UnitOfWork)

    attach_injector(api, injector)

    return api
