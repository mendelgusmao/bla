from typing import Callable

import injector
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from bla.domain.models import Base

DATABASE_URL = "sqlite:///:memory:"


class DatabaseConnection(injector.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        engine = create_engine(DATABASE_URL, echo=True)
        self.session_maker = sessionmaker(bind=engine, expire_on_commit=False)
        Base.metadata.create_all(engine)

    @injector.provider
    def provide_session_factory(self) -> Callable[[], Session]:
        return self.session_maker
