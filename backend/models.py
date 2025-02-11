from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean


class Base(DeclarativeBase):  # New way to declare Base in SQLAlchemy 2.0+
    pass


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)  # Added length & not null
    description = Column(String(500), nullable=True)  # Added length constraint
    completed = Column(Boolean, default=False)
