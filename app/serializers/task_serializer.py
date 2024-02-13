from pydantic import BaseModel

from typing_extensions import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    priority: Optional[str] = "medium"


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    priority: Optional[str] = "medium"

    class Config:
        orm_mode = True


class TaskList(BaseModel):
    tasks: list[TaskResponse]

    class Config:
        orm_mode = True


class TaskDelete(BaseModel):
    deleted: bool
    message: Optional[str] = None
