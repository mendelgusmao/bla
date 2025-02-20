from typing import Callable

from injector import Module, provider
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from bla.domain.models import Base

DSN = "sqlite:///:memory:"


class DatabaseConnection(Module):
    def __init__(self):
        engine = create_engine(DSN, echo=True)
        Base.metadata.create_all(engine)
        self.session_maker = sessionmaker(bind=engine, expire_on_commit=False)

    @provider
    def provide_session_factory(self) -> Callable[[], Session]:
        return self.session_maker
