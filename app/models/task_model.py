__all__ = ["Task"]


from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    priority = Column(
        String(length=10),
        CheckConstraint("priority IN ('low', 'medium', 'high')"),
        default="medium",
    )

    user_id = Column(Integer, ForeignKey("users.id"))

    category = relationship("Category", back_populates="tasks")
    user = relationship("User", back_populates="tasks")
