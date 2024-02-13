__all__ = ['Images']

from sqlalchemy import Column, String, Integer

from app.core.database import Base


class Images(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(63), unique=True, index=True)

