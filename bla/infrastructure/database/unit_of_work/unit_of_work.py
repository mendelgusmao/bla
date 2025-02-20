import logging
from typing import Callable, Self

from injector import inject
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class UnitOfWork:
    @inject
    def __init__(self, session_factory: Callable[[], Session]):
        self.session_factory = session_factory

    def __enter__(self) -> Self:
        self.session = self.session_factory()
        return self

    def __exit__(
        self,
        exc_type: type | None,
        exc_value: Exception,
        traceback: type,
    ) -> None:
        print(f"EXC {exc_type} {exc_value} {traceback}")

        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()
