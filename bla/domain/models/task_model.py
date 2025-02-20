from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from .base import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)  # ForeignKey("users.id"),
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_at = Column(DateTime, nullable=True)
    finished_at = Column(DateTime, nullable=True)
