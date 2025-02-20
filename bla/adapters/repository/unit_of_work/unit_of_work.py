import logging
from typing import Callable, Optional, Self

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
        exc_type: Optional[type],
        exc_value: Exception,
        traceback: type,
    ) -> None:
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()

        print("oi")
        logger.info(f"exc_type: {exc_type}, exc_value: {exc_value}")
